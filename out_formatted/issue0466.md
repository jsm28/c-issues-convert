## Issue 0466: scope of a `for` loop control declaration

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Martin Sebor  
Date: 2014-09-19  
Reference document: [N1865](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1865.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The scope of a `for` loop control declaration in C is different from that in
C\+\+. In particluar, while in C the declaration establishes its own scope in
which the scope of the body of the `for` statement is nested, in C\+\+ the two
are one and the same. The practical implication of this difference is that while
in C a declaration in the body can hide the `for` loop declaration, in C\+\+
such a re-declaration would be ill-formed. The following example demonstrates
the difference:

```c
        static inline int f (void) {
            for (int i = 0; ; ) {
                long i = 1;   // valid C, invalid C++
                // ...
                return i;     // (perhaps unexpectedly) returns 1 in C
            }
        }
```

During a discussion of this difference on the mailing list (starting with post
C22WG14.13355), it was noted that the re-declaration could lead to subtle bugs.

The incompatibility between rules used by the two languages also makes writing
headers intended to be used by both C and C\+\+ that contain inline functions
more prone to error than necessary.

In addition, it was noted (by Larry Jones in SC22WG14.13359) that the intent was
for C99, where the ability to declare a `for` loop control variable was first
added, to follow the C\+\+ rules, but that it had been missed that the C\+\+
rules ultimately adopted by ISO/IEC 14882:1998 changed from those of The
Annotated C\+\+ Reference Manual that was initially used to craft the C rules.

### Suggested Technical Corrigendum

The author recognizes that changing the C rules could render some existing
programs invalid. However, it is likely that such programs are broken/buggy and
thus a breaking change would result in correcting such latent bugs.

Therefore, the proposed corrigendum suggests to align the C rules with those of
C\+\+ by adding a new paragraph to section **6.2.1 Scopes of identifiers** as
follows.

> <ins>Names declared in *clause-1* of the `for` statement are local to the `for`
> statement and shall not be redeclared in a subsequent condition of that
> statement nor in the outermost block of the controlled statement.</ins>

Note: the text of the paragraph is aligned with the corresponding paragraph 4 of
section **3.3.3 Block scope** of ISO/IEC 14882:2014 (and section **3.3.2 Block
scope** of ISO/IEC 14882:1998).

---

Comment from WG14 on 2015-10-29:

Oct 2014 meeting

### Committee Discussion

The committee accepted this as a DR because there was an intent to not be
gratuitously different than C\+\+, and yet this small drift occurred.

### Proposed Committee Response

> This small and unintended difference between the two languages is known and some
> of its uses were discussed. It also turns out that some C\+\+ compilers also
> know and allow this construct with a warning. Overall, the committee concludes
> that this is not an area we wish to change.
