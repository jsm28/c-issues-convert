## Issue 0476: volatile semantics for lvalues

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Martin Sebor  
Date: 2015-08-26  
Reference document: [N1956](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1956.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C23  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The following sections discuss the C semantics of the `volatile` keyword and
show that they neither support existing practice nor, we believe, reflect the
intent of the committee when they were crafted. The Suggested Technical
Corrigendum then details changes to the C specification required to bring it
into harmony with both, as well as with C\+\+.

#### Motivation For Volatile

The use case that motivated the introduction of the `volatile` keyword into C
was a variant of the following snippet copied from early UNIX sources \[1]:

```c
    #define KL 0177560

    struct { char lobyte, hibyte; };
    struct { int ks, kb, ps, pb; };

    getchar() {
        register rc;
        ...
        while (KL->ks.lobyte >= 0);
        rc = KL->kb & 0177;
        ...
        return rc;
    }
```

The desired effect of the `while` loop in the `getchar()` function is to iterate
until the most significant (sign) bit of the keyboard status register mapped to
an address in memory represented by the `KL` macro (the address of the
memory-mapped `KBD_STAT` I/O register on the PDP-11) has become non-zero,
indicating that a key has been pressed, and then return the character value
extracted from the low 7 bits corresponding to the pressed key. In order for the
function to behave as expected, the compiler must emit an instruction to read a
value from the I/O register on each iteration of the loop. In particular, the
compiler must avoid caching the read value in a CPU register and substituting it
in subsequent accesses.

On the other hand, in situations where the memory location doesn't correspond to
a special memory-mapped register, it's more efficient to avoid reading the value
from memory if it happens to already have been read into a CPU register, and
instead use the value cached in the CPU register.

The problem is that without some sort of notation (in K\&R C there was none)
there would be no way for a compiler to distinguish between these two cases. The
following paragraph quoted from *The C Programming Language, Second Edition*, by
Kernighan and Ritchie, explains the solution that was introduced into standard C
to deal with this problem: the `volatile` keyword.

> The purpose of `volatile` is to force an implementation to suppress optimization
> that could otherwise occur. For example, for a machine with memory-mapped
> input/output, a pointer to a device register might be declared as a pointer to
> `volatile`, in order to prevent the compiler from removing apparently redundant
> references through the pointer.

Using the `volatile` keyword, it should then be possible to rewrite the loop in
the snippet above as follows:

```c
    while (*(volatile int*)&KL->ks.lobyte >= 0);
```

or equivalently:

```c
    volatile int *lobyte = &KL->ks.lobyte;
    while (*lobyte >= 0);
```

and prevent the compiler from caching the value of the keyboard status register,
thus guaranteeing that the register will be read once in each iteration.

The difference between the two forms of the rewritten loop is of historical
interest: Early C compilers are said to have recognized the first pattern
(without the `volatile` keyword) where the address used to access the register
was a constant, and avoided the undesirable optimization for such accesses
\[11]. However, they did not have the same ability when the access was through
pointer variable in which the address had been stored, especially not when the
use of such a variable was far removed from the last assignment to it. The
`volatile` keyword was intended to allow both forms of the loop to work as
expected.

The use case exemplified by the loop above has since become idiomatic and is
being extensively relied on in today's software even beyond reading I/O
registers.

As a representative example, consider the Linux kernel which relies on
`volatile` in its implementation of synchronization primitives such as spin
locks, or for performance counters. The variables that are operated on by these
primitives are typically declared to be of unqualified (i.e., non-volatile)
scalar types and allocated in ordinary memory. In serial code, for maximum
efficiency, each such variable is read and written just like any other variable,
with its value cached in a CPU register as compiler optimizations permit. At
well-defined points in the code where such a variable may be accessed by more
than one CPU at a time, the caching must be prevented and the variable must be
accessed using the special volatile semantics. To achieve that, the kernel
defines two macros: `READ_ONCE`, and `WRITE_ONCE`, in whose terms the primitives
are implemented. Each of the macros prevents the compiler optimization by
casting the address of its argument to a `volatile T*` and accessing the
variable via an lvalue of the `volatile`-qualified type `T` (where `T` is one of
the standard scalar types). Other primitives gurantee memory synchronization and
visibility but those are orthogonal to the subject of this paper. See \[3].

Similar examples can be found in other system or embedded programs as well as in
many other pre-C11 and pre-C\+\+11 code bases that don't rely on the Atomic
types and operations newly inroduced in those standards. They are often cited in
programming books \[4] and in online articles \[5, 6, 7, 8].

#### The Trouble With Volatile

In light of the motivation for the keyword and the wide-spread practice of
relying on its expected effect it might then come as a surprise that the C
standard lacks the necessary guarantees to support this popular idiom. In the
text of the C standard, volatile semantics are specified to apply to objects
explicitly declared with the qualifier. Quoting from §5.1.2.3, Program
execution, p2:

> Accessing a volatile object, modifying an object, ... are all *side effects*,
> which are changes in the state of the execution environment.

and p6:

> Accesses to volatile objects are evaluated strictly according to the rules of
> the abstract machine.

Note in particular that the text refers to <u>volatile objects</u>, which are
defined as regions of storage storing the representation of their values.
Objects are distinct from expressions used to designate and access them. Such
expressions are referred to as *lvalues*, and may but don't need to mention the
name of the accessed object. However, since the words in the paragraphs above
don't mention lvalues the special volatile semantics don't apply to such
accessess. As a result, since the expression `*(volatile int*)&KL->ks.lobyte` is
not an object but an lvalue of type `volatile int` that designates an object of
an otherwise unknown/unspecified type (the `KL` pointer doesn't point at an
object in the C sense), the volatile semantics do not apply to it. Consequently,
and due to §6.8.5, Iteration statements, p6

> An iteration statement whose controlling expression is not a constant
> expression, that ... does not access volatile objects ... may be assumed ... to
> terminate.

the controlling expression of the `while` loop is not required to be evaluated
with the special volatile semantics, allowing a C compiler to read the value of
the keyboard status register just once, and to return its value from the
function even if it's zero. (No known compiler has been observed to take
advantage of this permission.) This would obviously cause the `getchar` function
to behave in an unexpected way.

Although the problem with the C specification of volatile isn't well known, it
isn't new. It was pointed out in the past, for example in *The trouble with
volatile* \[9], Jonathan Corbet quotes Linus Torvalds, the author and maintainer
of the Linux kernel, as saying:

> Also, more importantly, "`volatile`" is on the wrong <u>part</u> of the whole
> system. In C, it's "data" that is volatile, but that is insane. Data isn't
> volatile — <u>accesses</u> are volatile. So it may make sense to say "make this
> particular <u>access</u> be careful", but not "make all accesses to this data
> use some random strategy".

#### Volatile In C\+\+

This problem is unique to the C standard. Unlike C, the text in the C\+\+
standard avoids referring to volatile objects and instead refers to volatile
*glvalues*. (A *glvalue* is a C\+\+ generalization of the C concept of
*lvalue*.) The C\+\+ text that corresponds to the quote from §5.1.2.3 Program
execution, p2 of C11 above, in §1.9 Program execution, p12, reads:

> Accessing an object designated by a volatile *glvalue*, modifying an object, ...
> are all side effects, which are changes in the state of the execution
> environment.

It might be tempting to chalk up this differenc to a deliberate or accidental
diveregence of the C\+\+ guarantees from C. But the C\+\+ standard contains an
informative note in §7.1.6.1, The *cv-qualifiers*, p7, making it clear that:

> In general, the semantics of volatile are intended to be the same in C\+\+ as
> they are in C.

This note which appears in the latest revision of C\+\+ from 2014 dates back to
the first revision of the standard from 1998\.

#### Intended Semantics

Besides the evidence above that the words in the C standard do not reflect
existing practice, there is also indication beyond the informative note in the
C\+\+ standard that the words most likely do not reflect the original intent of
the committee at the time they were crafted.

The C99 Rationale \[10], in §6.7.3 makes it clear that the committee's intent
when introducing `volatile` was to specify semantics that apply to accesses to
non-volatile objects via volatile-qualified lvalues and not just to accesses to
objects explicitly declared with the qualifier:

> The C89 Committee added to C two type qualifiers, `const` and `volatile`; ....
> Individually and in combination they specify the assumptions a compiler can and
> must make when accessing an object through an lvalue.
>
> .... `volatile` and `restrict` are inventions of the Committee; and both follow
> the syntactic model of `const`.

(Note: The syntactic model of `const` is to apply constness to accesses through
lvalues, regardless of whether or not the object being accessed has been
declared with a const-qualified type.)

The same section then further clarifies that:

> If it is necessary to access a non-`volatile` object using `volatile` semantics,
> the technique is to cast the address of the object to the appropriate
> pointer-to-qualified type, then dereference that pointer.

### Suggested Technical Corrigendum

The suggested technical corrigendum that follows brings the volatile
specification into alignment with existing practice, with their original intent,
and also with the C\+\+ specification.

In §5.1.2.3, Program execution, p2:

> Accessing a<u>n object through the use of an lvalue of volatile-qualified
> type</u>~~volatile object~~, modifying a file, or calling a function that does
> any of those operations are all side effects...

In §5.1.2.3, Program execution, p4:

> An actual implementation need not evaluate part of an expression if it can
> deduce that its value is not used and that no needed side effects are produced
> (including any caused by calling a function or accessing a<u>n object through
> the use of an lvalue of volatile-qualified type</u>~~volatile object~~).

In §5.1.2.3, Program execution, p6, bullet 1:

> Accesses to <u>objects through the use of lvalues of volatile-qualified
> types</u>~~volatile objects~~ are evaluated strictly according to the rules of
> the abstract machine.

In §6.7.3, Type qualifiers, p7:

> What constitutes an access to an object <u>through the use of an lvalue
> of</u>~~that has~~ volatile-qualified type is implementation-defined.

In §6.8.5, Iteration statements, p6:

> An iteration statement whose controlling expression is not a constant
> expression,<sup>156\)</sup> that performs no input/output operations, does not
> access <u>objects through the use of lvalues of volatile-qualified types</u>
> ~~volatile objects~~, ... may be assumed by the implementation to terminate.

In §J.3.10, Qualifiers, p1:

> What constitutes an access to an object <u>through the use of an lvalue
> of</u>~~that has~~ volatile-qualified type (6.7.3).

In §L.2.1, p1:

> out-of-bounds store
>
> an (attempted) access (3.1) that, at run time, for a given computational state,
> would modify (or, for an ~~object declared~~<u>lvalue of</u>
> volatile<u>-qualified type</u>, fetch) one or more bytes that lie outside the
> bounds permitted by this Standard.

### References

1. [`/usr/src/stand/pdp11/iload/console.c`](http://minnie.tuhs.org/cgi-bin/utree.pl?file=SysIII/usr/src/stand/pdp11/iload/console.c), AT\&T UNIX System III, 1982
2. [The C Programming Language, Second Edition](https://hassanolity.files.wordpress.com/2013/11/the_c_programming_language_2.pdf), Brian W. Kernighan, Dennis M. Ritchie
3. ISO/IEC SC22/WG21 document [N4444](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2015/n4444.html): Linux-Kernel Memory Model, Paul E. McKenney
4. [§8.4. Const and volatile](http://publications.gbdirect.co.uk/c_book/chapter8/const_and_volatile.html), The C Book, Second Edition, Mike Banahan and Declan Brady, GBdirect
5. [Introduction to the volatile keyword](http://www.embedded.com/electronics-blogs/beginner-s-corner/4023801/Introduction-to-the-Volatile-Keyword) an embedded.com article by Nigel Jones, July 2, 2001
6. [Why does volatile exist?](http://stackoverflow.com/questions/72552/why-does-volatile-exist), a stackoverflow.com article, September 16, 2008
7. [Why is volatile needed in c?](http://stackoverflow.com/questions/246127/why-is-volatile-needed-in-c), a stackoverflow.com article, October 29, 2008
8. [volatile (computer programming)](https://en.wikipedia.org/wiki/Volatile_%28computer_programming%29), a Wikipedia article
9. [The trouble with volatile](https://lwn.net/Articles/233479), an LWN article, Jonathan Corbet, May 9 2007
10. [Rationale for International Standard — Programming Languages — C](https://www.open-std.org/jtc1/sc22/wg14/www/C99RationaleV5.10.pdf), Revision 5.10, April 2003
11. [A question on volatile accesses](https://groups.google.com/forum/#!msg/comp.std.c/tHvQhiKFtD4/zfIgJhbkCXcJ) — A response to comp.std.c question by Doug Gwyn, November 1990

---

Comment from WG14 on 2018-10-18:

Oct 2015 meeting

### Committee Discussion

* The premise of this DR is essentially that the original specification of `volatile` did not accurately reflect the intent at the time of its formulation and that ongoing practice has in fact implemented the intent. On the basis that the intent was clearly established and that practice corroborates it, the committee accepted this as a defect and moreover concluded that it is in substantial agreement.
* Although asked, the committee did not spend any time answering the question as to why such a defect had never before been reported. All implementors represented on the committee were polled and all confirmed that indeed, the intent, not the standard, is implemented. In addition to the linux experience documented in the paper, at least two committee members described discussions with systems engineers where this difference between the standard vs the implementation was discussed because the systems engineers clearly depended on the implementation of actual intent. The sense was that this was simply a well known discrepency.
* Specifically, the intent is reflected in the implementations of the gcc, Intel, clang, sparc, and IBM compilers. Although far from a complete enumeration of C compilers, these were broad enough to accept that all known compilers that the committee could speak to that are used for systems implementation in fact implement the intent, not the standard.
* The committee also believes that C\+\+ “got this (nearly) right” and that there will likely be a liaison issue on this topic.
* The committee feels that the changes proposed to 5.1.2.3p6 bullet 1 are the “heart of the matter”. There was a suggestion that editorially, it might be worthwhile to define a new term *volatile access* at that point and use it consistently in the other parts of the standard rather than as proposed in the suggested technical corrigendum. This suggestion and other comments can also be found in [(SC22WG14.13870) N1956 volatile semantics](https://www.open-std.org/jtc1/sc22/wg14/13870). This rephrasing of the proposed changes could eliminate potential confusion when introduced elsewhere.
* The author was asked to revise his wordings through soliciting input either directly from committee members or indirectly through the use of the WG14 reflector and to formulate and submit a new paper on this topic.

Apr 2016 meeting

### Committee Discussion

> Further correspondence with the author led to a small paper containing a revised
> Suggested Technical Corrigendum incorporating the suggestion from the last
> meeting. The following proposed changes were considered appropriate.
>
> Change §5.1.2.3p2 from:
>
> > Accessing a volatile object, modifying an object, modifying a file, or calling a
> > function that does any of those operations are all side effects ...
>
> to:
>
> > An access to an object through the use of an lvalue of volatile-qualified type
> > is a *volatile access*. A volatile access to an object, modifying a file, or
> > calling a function that does any of those operations are all side effects ...
>
> Change §5.1.2.3p4 from:
>
> > An actual implementation need not evaluate part of an expression if it can
> > deduce that its value is not used and that no needed side effects are produced
> > (including any caused by calling a function or accessing a volatile object.
>
> to:
>
> > An actual implementation need not evaluate part of an expression if it can
> > deduce that its value is not used and that no needed side effects are produced
> > (including any caused by calling a function or through volatile access to an
> > object.
>
> Change §5.1.2.3p6 bullet 1 from:
>
> > Accesses to volatile objects are evaluated strictly according to the rules of
> > the abstract machine.
>
> to:
>
> > Volatile accesses to objects are evaluated strictly according to the rules of
> > the abstract machine.
>
> There was a suggestion that *volatile access* be reconciled with the definition
> of *lvalue* in §6.3.2.1 and that further wording is solicited.

Apr 2017 meeting

### Committee Discussion

> The committee agreed to adopt the wording worked out in prior meetings, and to
> leave the definition of *lvalue* unchanged at this time.

### Proposed Change

Change §5.1.2.3p2 from:

> Accessing a volatile object, modifying an object, modifying a file, or calling a
> function that does any of those operations are all side effects ...

to:

> An access to an object through the use of an lvalue of volatile-qualified type
> is a *volatile access*. A volatile access to an object, modifying a file, or
> calling a function that does any of those operations are all side effects ...

Change §5.1.2.3p4 from:

> An actual implementation need not evaluate part of an expression if it can
> deduce that its value is not used and that no needed side effects are produced
> (including any caused by calling a function or accessing a volatile object.

to:

> An actual implementation need not evaluate part of an expression if it can
> deduce that its value is not used and that no needed side effects are produced
> (including any caused by calling a function or through volatile access to an
> object.

Change §5.1.2.3p6 bullet 1 from:

> Accesses to volatile objects are evaluated strictly according to the rules of
> the abstract machine.

to:

> Volatile accesses to objects are evaluated strictly according to the rules of
> the abstract machine.
