# C11 / C17: issue log

**This issue log has been automatically converted from the original issue lists and some formatting may not have been preserved.**

|Issue|Summary|Status|
|-|-|-|
|[0400](log_c11c17.md#issue0400)|`realloc` with size zero problems|Fixed in C17|
|[0401](log_c11c17.md#issue0401)|"happens before" cannot be cyclic|Fixed in C17|
|[0402](log_c11c17.md#issue0402)|memory model coherence is not aligned with C\+\+11|Fixed in C17|
|[0403](log_c11c17.md#issue0403)|`malloc()` and `free()` in the memory model|Fixed in C17|
|[0404](log_c11c17.md#issue0404)|joke fragment remains in a footnote|Fixed in C17|
|[0405](log_c11c17.md#issue0405)|mutex specification not aligned with C\+\+11 on total order|Fixed in C17|
|[0406](log_c11c17.md#issue0406)|Visible sequences of side effects are redundant|Fixed in C17|
|[0407](log_c11c17.md#issue0407)|SC fences do not restrict modification order enough|Fixed in C17|
|[0408](log_c11c17.md#issue0408)|Should locks provide intra-thread synchronization|Closed|
|[0409](log_c11c17.md#issue0409)|`f(inf)` is `inf` being a range error|Closed|
|[0410](log_c11c17.md#issue0410)|`ilogb` inconsistent with `lrint`, `lround`|Fixed in C17|
|[0411](log_c11c17.md#issue0411)|Predefined macro values|Fixed in C11 TC1|
|[0412](log_c11c17.md#issue0412)|`#elif`|Fixed in C17|
|[0413](log_c11c17.md#issue0413)|initialization|Fixed in C17|
|[0414](log_c11c17.md#issue0414)|Typos in 6.27 Threads `<threads.h>`|Fixed in C17|
|[0415](log_c11c17.md#issue0415)|Missing divide by zero entry in Annex J.2|Fixed in C17|
|[0416](log_c11c17.md#issue0416)|`tss_t` destruction unspecified|Fixed in C17|
|[0417](log_c11c17.md#issue0417)|Annex J not updated with necessary `aligned_alloc` entries|Fixed in C17|
|[0418](log_c11c17.md#issue0418)|`fmod(0.,Nan)` and `fmod(Nan, infinity)`|Closed|
|[0419](log_c11c17.md#issue0419)|What the heck is a "generic function"?|Fixed in C17|
|[0420](log_c11c17.md#issue0420)|syntax error in specification of for-statement|Closed|
|[0421](log_c11c17.md#issue0421)|initialization of `atomic_flag`|Closed|
|[0422](log_c11c17.md#issue0422)|initialization of atomic types|Closed|
|[0423](log_c11c17.md#issue0423)|Defect Report relative to n1570: underspecification for qualified rvalues|Fixed in C17|
|[0424](log_c11c17.md#issue0424)|underspecification of `tss_t`|Fixed in C17|
|[0425](log_c11c17.md#issue0425)|no specification for the access to variables with temporary lifetime|Closed|
|[0426](log_c11c17.md#issue0426)|G.5.1: `-yv` and `-x/v` are ambiguous|Fixed in C17|
|[0427](log_c11c17.md#issue0427)|Function Parameter and Return Value Assignments|Closed|
|[0428](log_c11c17.md#issue0428)|runtime-constraint issue with sprintf family of routines in Annex K|Fixed in C17|
|[0429](log_c11c17.md#issue0429)|Should `gets_s` discard next input line when `(s == NULL)` ?|Fixed in C17|
|[0430](log_c11c17.md#issue0430)|`getenv_s`, `maxsize` should be allowed to be zero|Fixed in C17|
|[0431](log_c11c17.md#issue0431)|`atomic_compare_exchange`: What does it mean to say two structs compare equal?|Fixed in C17|
|[0432](log_c11c17.md#issue0432)|Is `0.0` required to be a representable value?|Closed|
|[0433](log_c11c17.md#issue0433)|Issue with constraints for wide character function arguments involving **RSIZE\_MAX**|Fixed in C17|
|[0434](log_c11c17.md#issue0434)|Missing constraint w.r.t. Atomic|Fixed in C17|
|[0435](log_c11c17.md#issue0435)|Missing constraint w.r.t. Imaginary|Closed|
|[0436](log_c11c17.md#issue0436)|Request for interpretation of C11 6.8.5#6|Fixed in C17|
|[0437](log_c11c17.md#issue0437)|`clock` overflow problems|Fixed in C17|
|[0438](log_c11c17.md#issue0438)|`ungetc / ungetwc` and file position after discarding push back problems|Fixed in C17|
|[0439](log_c11c17.md#issue0439)|Issues with the definition of “full expression”|Fixed in C17|
|[0440](log_c11c17.md#issue0440)|Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 1|Closed|
|[0441](log_c11c17.md#issue0441)|Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 2|Fixed in C17|
|[0442](log_c11c17.md#issue0442)|Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 3|Closed|
|[0443](log_c11c17.md#issue0443)|Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 4|Closed|
|[0444](log_c11c17.md#issue0444)|Issues with alignment in C11, part 1|Fixed in C17|
|[0445](log_c11c17.md#issue0445)|Issues with alignment in C11, part 2|Fixed in C17|
|[0446](log_c11c17.md#issue0446)|Use byte instead of character for memcmp, memcpy|Closed|
|[0447](log_c11c17.md#issue0447)|Boolean from complex|Fixed in C17|
|[0448](log_c11c17.md#issue0448)|What are the semantics of a **\# non-directive**?|Fixed in C17|
|[0449](log_c11c17.md#issue0449)|What is the value of TSS\_DTOR\_ITERATIONS for implementations with no maximum?|Closed|
|[0450](log_c11c17.md#issue0450)|`tmpnam_s` clears `s[0]` when `maxsize > RSIZE_MAX`|Fixed in C17|
|[0451](log_c11c17.md#issue0451)|Instability of uninitialized automatic variables|Closed|
|[0452](log_c11c17.md#issue0452)|Effective Type in Loop Invariant|Fixed in C17|
|[0453](log_c11c17.md#issue0453)|Atomic flag type and operations|Fixed in C17|
|[0454](log_c11c17.md#issue0454)|ATOMIC\_VAR\_INIT (issues 3 and 4\)|Closed|
|[0455](log_c11c17.md#issue0455)|ATOMIC\_VAR\_INIT issue 5|Closed|
|[0456](log_c11c17.md#issue0456)|Compile time definition of `UINT`*`N`*`_C(`*`value`*`)`|Closed|
|[0457](log_c11c17.md#issue0457)|The `ctime_s` function in Annex K defined incorrectly|Fixed in C17|
|[0458](log_c11c17.md#issue0458)|ATOMIC\_XXX\_LOCK\_FREE macros not constant expressions|Fixed in C17|
|[0459](log_c11c17.md#issue0459)|atomic\_load missing const qualifier|Fixed in C17|
|[0460](log_c11c17.md#issue0460)|`aligned_alloc` underspecified|Fixed in C17|
|[0461](log_c11c17.md#issue0461)|problems with references to objects in signal handlers|Closed|
|[0462](log_c11c17.md#issue0462)|Clarifying objects accessed in signal handlers|Fixed in C17|
|[0463](log_c11c17.md#issue0463)|Left-shifting into the sign bit|Closed|
|[0464](log_c11c17.md#issue0464)|Clarifying the Behavior of the `#line` Directive|Fixed in C17|
|[0465](log_c11c17.md#issue0465)|Fixing an inconsistency in `atomic_is_lock_free`|Fixed in C17|
|[0466](log_c11c17.md#issue0466)|scope of a `for` loop control declaration|Closed|
|[0467](log_c11c17.md#issue0467)|maximum representable finite description vs math|Closed|
|[0468](log_c11c17.md#issue0468)|`strncpy_s` clobbers buffer past `null`|Fixed in C17|
|[0469](log_c11c17.md#issue0469)|lock ownership vs. thread termination|Closed|
|[0470](log_c11c17.md#issue0470)|mtx\_trylock should be allowed to fail spuriously|Fixed in C17|
|[0471](log_c11c17.md#issue0471)|Complex math functions cacosh and ctanh|Fixed in C17|
|[0472](log_c11c17.md#issue0472)|Introduction to complex arithmetic in 7.3.1p3 wrong due to CMPLX|Fixed in C17|
|[0473](log_c11c17.md#issue0473)|"A range error occurs if x is too large." is misleading|Fixed in C17|
|[0474](log_c11c17.md#issue0474)|NOTE 1 Clarification for `atomic_compare_exchange`|Closed|
|[0475](log_c11c17.md#issue0475)|Misleading Atomic library references to atomic types|Fixed in C17|
|[0476](log_c11c17.md#issue0476)|volatile semantics for lvalues|Fixed in C23|
|[0477](log_c11c17.md#issue0477)|`nan` should take a string argument|Fixed in C17|
|[0478](log_c11c17.md#issue0478)|valid uses of the `main` function|Closed|
|[0479](log_c11c17.md#issue0479)|unclear specification of `mtx_trylock` on non-recursive muteness|Closed|
|[0480](log_c11c17.md#issue0480)|`cnd_wait` and `cnd_timewait` should allow spurious wake-ups|Fixed in C17|
|[0481](log_c11c17.md#issue0481)|Controlling expression of `_Generic` primary expression|Fixed in C17|
|[0482](log_c11c17.md#issue0482)|Macro invocation split over many files|Closed|
|[0483](log_c11c17.md#issue0483)|`__LINE__` and `__FILE__` in macro replacement list|Closed|
|[0484](log_c11c17.md#issue0484)|invalid characters in `strcoll()`|Closed|
|[0485](log_c11c17.md#issue0485)|Problem with the specification of `ATOMIC_VAR_INIT`|Fixed in C17|
|[0486](log_c11c17.md#issue0486)|Inconsistent specification for arithmetic on atomic objects|Closed|
|[0487](log_c11c17.md#issue0487)|`timespec` vs. `tm`|Fixed in C17|
|[0488](log_c11c17.md#issue0488)|`c16rtomb()` on wide characters encoded as multiple `char16_t`|Fixed in C23|
|[0489](log_c11c17.md#issue0489)|Integer Constant Expression|Closed|
|[0490](log_c11c17.md#issue0490)|Unwritten Assumptions About if-then|Closed|
|[0491](log_c11c17.md#issue0491)|Concern with Keywords that Match Reserved Identifiers|Fixed in C17|
|[0492](log_c11c17.md#issue0492)|Named Child struct-union with no Member|Closed|
|[0493](log_c11c17.md#issue0493)|Mutex Initialization Underspecified|Closed|
|[0494](log_c11c17.md#issue0494)|Part 1: Alignment specifier expression evaluation|Fixed in C23|
|[0495](log_c11c17.md#issue0495)|Part 2: Atomic specifier expression evaluation|Closed|
|[0496](log_c11c17.md#issue0496)|`offsetof` questions|Fixed in C23|
|[0497](log_c11c17.md#issue0497)|"white-space character" defined in two places|Fixed in C23|
|[0498](log_c11c17.md#issue0498)|`mblen`, `mbtowc`, and `wctomb` thread-safety|Closed|
|[0499](log_c11c17.md#issue0499)|Anonymous structure in union behavior|Fixed in C23|
|[0500](log_c11c17.md#issue0500)|Ambiguous specification for **FLT\_EVAL\_METHOD**|Fixed in C23|
|[0501](log_c11c17.md#issue0501)|Can **DECIMAL\_DIG** be larger than necessary?|Fixed in C23|
|[0502](log_c11c17.md#issue0502)|Flexible array member in an anonymous struct|Closed|
|[0503](log_c11c17.md#issue0503)|Hexadecimal floating-point and `strtod`|Closed|

---

<div id="issue0400">

## Issue 0400: `realloc` with size zero problems

Authors: Austin Group, Nick Stoughton (US)  
Date: 2011-10-24  
Reference document: [N1559](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1559.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

There are at least three existing `realloc` behaviors when `NULL` is returned;
the differences only occur for a size of 0 (for non-zero size, all three
implementations set `errno` to `ENOMEM` when returning `NULL`, even though that
is not required by C99).

> **AIX**
>
> > `realloc(NULL,0)` always returns NULL, errno is EINVAL  
> > `realloc(ptr,0)` always returns NULL, ptr freed, errno is EINVAL
>
> **BSD**
>
> > `realloc(NULL,0)` only gives NULL on alloc failure, errno is ENOMEM  
> > `realloc(ptr,0)` only gives NULL on alloc failure, ptr unchanged, errno is
> > ENOMEM
>
> **glibc**
>
> > `realloc(NULL,0)` only gives NULL on alloc failure, errno is ENOMEM  
> > `realloc(ptr,0)` always returns NULL, ptr freed, errno unchanged

The Austin Group raised this matter with WG14 during earlier meetings (most
notably during the London 2011 meeting). The direction from WG14 has led to The
Austin Group aligning the POSIX text more closely to that in C99 and C1x as a
part of TC1.

The behavior now required in POSIX is that implemented by **BSD** above.
However, C99 has a loophole in implementation-defined behavior that still
appears to permit AIX and glibc behaviors. The C1x draft carries the same
wording loophole, so the planned course of action is to raise a defect against
C1x once it completes standardization, where the outcome of that defect will
either be that C1x tightens the wording to eliminate the loophole or relaxes the
wording to align with existing practice. Therefore, the behavior of errno in
Issue 8 should be deferred until after any C1x defect has been resolved.

> If the size of the space requested is zero, the behavior is
> implementation-defined: either a null pointer is returned, or the behavior is as
> if the size were some nonzero value, except that the returned pointer shall not
> be used to access an object.

An implementation should not be allowed to define the behavior of returning a
null pointer as a successful reallocation; if a null pointer is returned, then
the orignal pointer has not been freed.

### Suggested Change

At 7.22.3, para 1, change:

> If the size of the space requested is zero, the behavior is
> implementation-defined: either a null pointer is returned, or the behavior is as
> if the size were some nonzero value, except that the returned pointer shall not
> be used to access an object.

to

> If the size of the space requested is zero, the behavior is
> implementation-defined: either a null pointer is returned <ins>and errno set to
> indicate the error</ins>, or the behavior is as if the size were some nonzero
> value, except that the returned pointer shall not be used to access an object.

Add a footnote to this sentence stating:

> <ins>**Note** Memory allocated by these functions should be freed via a call to
> `free`, and not by means of a `realoc(p, 0)`.</ins>

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee Discussion

> * It was pointed out that the AIX behavior was not correct according to Rajan, in fact the behavior is that `errno` is not set.
> * This change came out of a defect report on C99

Feb 2012 meeting

### Committee Discussion

> * The current C Rationale needs to be edited.

### Proposed Technical Corrigendum

> In subsection 7.22.3 paragraph 1, change
>
> > If the size of the space requested is zero, the behavior is
> > implementation-defined: either a null pointer is returned, ...
>
> to
>
> > If the size of the space requested is zero, the behavior is
> > implementation-defined: either a null pointer is returned to indicate an error,
> > ...
>
> In subsection 7.22.3.5 (The `realloc` function), change the final sentence of
> paragraph 3 from
>
> > If memory for the new object cannot be allocated, the old object is not
> > deallocated and its value is unchanged.
>
> to
>
> > If `size` is non-zero and memory for the new object is not allocated, the old
> > object is not deallocated. If `size` is zero and memory for the new object is
> > not allocated, it is implementation-defined whether the old object is
> > deallocated. If the old object is not deallocated, its value shall be unchanged.
>
> In subsection 7.22.3.5 (The `realloc` function), change paragraph 4 from
>
> > The `realloc` function returns a pointer to the new object (which may have the
> > same value as a pointer to the old object), or a null pointer if the new object
> > could not be allocated.
>
> to
>
> > The `realloc` function returns a pointer to the new object (which may have the
> > same value as a pointer to the old object), or a null pointer if the new object
> > has not been allocated.
>
> Add to subsection 7.31.12 a new paragraph (paragraph 2):
>
> > Invoking `realloc` with a size argument equal to zero is an obsolescent feature.


</div>


---

---

<div id="issue0401">

## Issue 0401: "happens before" cannot be cyclic

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C\+\+11 forbids "happens before" from being cyclic, but this change has not made
its way into C11. In order to fix this, the following sentence (taken from C\+\+
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf),
1.10p12) should be added to 5.1.2.4p18:

> The implementation shall ensure that no program execution demonstrates a cycle
> in the "happens before" relation.  
>
> NOTE: This cycle would otherwise be possible only through the use of consume
> operations.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee Discussion

> * Seems as if C\+\+ made this change at the last minute and WG 14 had already voted a document for ballot.
> * There seems to be consensus to make a change along this line.

Feb 2012 meeting

### Proposed Technical Corrigendum

> Add to 5.1.2.4p18:
>
> > The implementation shall ensure that no program execution demonstrates a cycle
> > in the "happens before" relation.  
> >
> > NOTE: This cycle would otherwise be possible only through the use of consume
> > operations.


</div>


---

---

<div id="issue0402">

## Issue 0402: memory model coherence is not aligned with C\+\+11

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0406](log_c11c17.md#issue0406)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The memory model described in
[N1569](https://www.open-std.org/jtc1/sc22/wg14/prot/n1569.pdf) matches an older
version of the C\+\+0x memory model, one that allowed executions that were not
intended by the designers. The recommandation is to match the C\+\+11 text by
removing the sentence starting 'Furthermore' in 5.1.2.4p22, and including the
following paragraphs in section 5.1.2.4 (Taken from C\+\+
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf),
1.10p15 through 18):

> If an operation `A` that modifies an atomic object `M` happens before an
> operation `B` that modifies `M` , then `A` shall be earlier than `B` in the
> modification order of `M` .
>
> *NOTE:* The requirement above is known as write-write coherence.
>
> If a value computation `A` of an atomic object `M` happens before a value
> computation `B` of `M` , and `A` takes its value from a side effect `X` on `M`,
> then the value computed by `B` shall either be the value stored by `X` or the
> value stored by a side effect `Y` on `M`, where `Y` follows `X` in the
> modification order of `M`.
>
> *NOTE:* The requirement above is known as read-read coherence.
>
> If a value computation `A` of an atomic object `M` happens before an operation
> `B` on `M`, then `A` shall take its value from a side effect `X` on `M`, where
> `X` precedes `B` in the modification order of `M`.
>
> *NOTE:* The requirement above is known as read-write coherence.
>
> If a side effect `X` on an atomic object `M` happens before a value computation
> `B` of `M`, then the evaluation `B` shall take its value from `X` or from a side
> effect `Y` that follows `X` in the modification order of `M`.
>
> *NOTE:* The requirement above is known as write-read coherence.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee Discussion

> * The consensus was that this is an oversight, and should be changed as recommended.

Feb 2012 meeting

### Proposed Technical Corrigendum

> In 5.1.2.4 Paragraph 22 starting at the third sentence, add:
>
> > If an operation `A` that modifies an atomic object `M` happens before an
> > operation `B` that modifies `M` , then `A` shall be earlier than `B` in the
> > modification order of `M` .
> >
> > *NOTE:* The requirement above is known as write-write coherence.
> >
> > If a value computation `A` of an atomic object `M` happens before a value
> > computation `B` of `M` , and `A` takes its value from a side effect `X` on `M`,
> > then the value computed by `B` shall either be the value stored by `X` or the
> > value stored by a side effect `Y` on `M`, where `Y` follows `X` in the
> > modification order of `M`.
> >
> > *NOTE:* The requirement above is known as read-read coherence.
> >
> > If a value computation `A` of an atomic object `M` happens before an operation
> > `B` on `M`, then `A` shall take its value from a side effect `X` on `M`, where
> > `X` precedes `B` in the modification order of `M`.
> >
> > *NOTE:* The requirement above is known as read-write coherence.
> >
> > If a side effect `X` on an atomic object `M` happens before a value computation
> > `B` of `M`, then the evaluation `B` shall take its value from `X` or from a side
> > effect `Y` that follows `X` in the modification order of `M`.
> >
> > *NOTE:* The requirement above is known as write-read coherence.


</div>


---

---

<div id="issue0403">

## Issue 0403: `malloc()` and `free()` in the memory model

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The synchronisation afforded to malloc and free is missing some vital ordering,
and as the definition stands it makes little sense and creates cycles in happens
before. C\+\+11 includes a total order over the allocation and deallocation
calls, which fixes the problem and seems to give a sensible semantics. From
18.6.1.4p1 in
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf):

> Calls to these functions that allocate or deallocate a particular unit of
> storage shall occur in a single total order, and each such deallocation call
> shall happen before the next allocation (if any) in this order.

Unfortunately, there is a typo here. Happens before edges are not transitively
closed in to the happens before relation, but the edges here are meant to be.
Instead the sentence above should create a synchronises with edge. In light of
this, we suggest removing the last two sentences from 7.22.3p2 and replacing
them with:

> Calls to these functions that allocate or deallocate a particular region of
> memory shall occur in a single total order, and each such deallocation call
> shall synchronise with the next allocation (if any) in this order.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee discussion

> * The consensus was that this is an oversight, and should be changed along the lines that are recommended.

Feb 2012 meeting

### Proposed Technical Corrigendum

> Replace last two sentences in 7.22.3 paragraph 2 with:
>
> > Calls to these functions that allocate or deallocate a particular region of
> > memory shall occur in a single total order, and each such deallocation call
> > shall synchronize with the next allocation (if any) in this order.


</div>


---

---

<div id="issue0404">

## Issue 0404: joke fragment remains in a footnote

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 seems to have inherited part of a joke from C\+\+, which ought to be removed
or made whole and annotated as such. Originally, C\+\+0x had the footnotes:

> "Atomic objects are neither active nor radioactive" and "Among other
> implications, atomic variables shall not decay".

The first is pretty clearly a joke, but it's not obvious that the second doesn't
have some technical meaning, and that is the one that remains in C11 in
7.17.3p13.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee discussion

> * It is not clear that rewording will make the footnote useful.

Feb 2012

### Proposed Technical Corrigendum

> In 7.17.3 Paragraph 13, remove footnote 256\.


</div>


---

---

<div id="issue0405">

## Issue 0405: mutex specification not aligned with C\+\+11 on total order

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The C11 specification of mutexes is missing the total order over all the calls
on a particular mutex. This is present in C\+\+11. The following is from
30.4.1.2p5 in
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf):

> For purposes of determining the existence of a data race, these behave as atomic
> operations (1.10). The lock and unlock operations on a single mutex shall appear
> to occur in a single total order. \[ Note: this can be viewed as the
> modification order (1.10) of the mutex. — end note \]

The synchronisation in 7.26.4 is defined in terms of some order over these
calls, even though none is specified, for instance 7.26.4.4p2 reads:

> Prior calls to mtx\_unlock on the same mutex shall synchronize with this
> operation.

This seems like simple omission. We suggest adding a new paragraph to 7.26.4
that matches C\+\+11:

> For purposes of determining the existence of a data race, mutex calls behave as
> atomic operations. The lock and unlock operations on a single mutex shall appear
> to occur in a single total order.
>
> *NOTE:* This can be viewed as the modification order of the mutex.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee discussion

> * The quoted text was added to C\+\+11 after WG 14 voted out the FDIS in London.
> * The consensus was that this is probably an oversight, and should be changed along the lines that are recommended above.

Feb 2012 meeting

### Committee Discussion

> * The wording in the proposed wording is not correct, should read "shall occur" rather than "shall appear to occur."
> * No consensus reached on the words, Clark Nelson took action item to furnish words for the next meeting.

Oct 2012 meeting

### Committee Discussion

Add the following as 7.26.4 p1 and p2:

> For purposes of determining the existence of a data race, lock and unlock
> operations behave as atomic operations. All lock and unlock operations on a
> particular mutex occur in some particular total order.
>
> *NOTE:* This total order can be viewed as the modification order of the mutex.

Apr 2013 meeting

### Committee Discussion

Accept wording from Oct 2012 as proposed technical corrigendum

### Proposed Technical Corrigendum

Add the following as 7.26.4 p1 and p2:

> For purposes of determining the existence of a data race, lock and unlock
> operations behave as atomic operations. All lock and unlock operations on a
> particular mutex occur in some particular total order.
>
> *NOTE:* This total order can be viewed as the modification order of the mutex.


</div>


---

---

<div id="issue0406">

## Issue 0406: Visible sequences of side effects are redundant

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0402](log_c11c17.md#issue0402)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

It has been mathematically proved that a simplification can be made to the
memory model as it is specified in the final draft of the C\+\+11 standard.
Essentially, the restriction defining *visible sequence of side effects* (vsse)
is redundant and can be removed with no ill effects. The main motivation for
doing this is that the current restriction is misleading. 5.1.2.4p22 defines
vsse's:

> The visible sequence of side effects on an atomic object `M`, with respect to a
> value computation `B` of `M`, is a maximal contiguous sub-sequence of side
> effects in the modification order of `M`, where the first side effect is visible
> with respect to `B`, and for every subsequent side effect, it is not the case
> that `B` happens before it. The value of an atomic object `M`, as determined by
> evaluation B, shall be the value stored by some operation in the visible
> sequence of `M` with respect to `B`.

The wording of this paragraph makes it seem as if the vsse identifies the writes
that an atomic read is allowed to read from, but this is not the case. There can
be writes in the vsse that cannot be read due to the coherence requirements (to
be included in C, 1.10p15 through 1.10p18 in C\+\+
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf)).
Consequently this is even more confusing than it at first appears.

Also propose changing 5.1.2.4p22 to the following:

> The value of an atomic object `M`, as determined by evaluation `B`, shall be the
> value stored by some side effect `A` that modifies `M`, where `B` does not
> happen before `A`.

With a note to remind the reader of the coherence requirements:

> *NOTE:* The set of side effects that a given evaluation might take its value
> from is also restricted by the rest of the rules described here, and in
> particular, by the coherence requirements below

If the committee is concerned about allowing a differing text from C\+\+11, then
a note could be added to assure the reader:

> *NOTE:* Although the rules for multi-threaded executions differ here from those
> of C\+\+11, the executions they allow are precisely the same. Visible sequences
> of side effects are a redundant restriction.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee Discussion

> * The changes seem reasonable, there is a concern about having C and C\+\+ differ.
> * Should be contingent on [Defect 402](log_c11c17.md#issue0402).

Feb 2012 meeting

### Committee Discussion

> * There was no work done on this defect between meetings.
> * Seems more complicated than thought at the last meeting.
> * It is not clear if WG 21 has considered these changes.
> * Clark Nelson took an action item to liaise with WG 21\.

Oct 2012 meeting

### Committee Discussion

> This item has become WG21 Core issue 1466

Apr 2013 meeting

### Committee Discussion

> There has been no discussion or action from WG21.

Oct 2013 meeting

### Committee Discussion

These changes have been proposed for the C\+\+ working draft:

* For C 5.1.2.4 paragraph 2, the following C\+\+ discussion is relevant:
  > Change 1.10 paragraph 14 as follows:
  >
  > > <del>The *visible sequence of side effects* on an atomic object *M*, with
  > > respect to a value computation *B* of *M*, is a maximal contiguous sub-sequence
  > > of side effects in the modification order of M, where the first side effect is
  > > visible with respect to *B*, and for every side effect, it is not the case that
  > > *B* happens before it.</del> The value of an atomic object *M*, as determined by
  > > evaluation *B*, shall be the value stored by some <del>operation in the visible
  > > sequence of *M* with respect to *B*</del> <ins>side effect *A* that modifies
  > > *M*, where *B* does not happen before *A*</ins>. \[*Note:* <del>It can be shown
  > > that the visible sequence of side effects of a value computation is unique
  > > given</del> <ins>The set of side effects that a given evaluation might take its
  > > value from is also restricted by the rest of the rules described here, and in
  > > particular, by</ins> the coherence requirements below. —*end note*\]
* For C 5.1.2.4 paragraph 24, the following C\+\+ discussion is relevant:
  > 1.10p20 should be changed as follows:
  >
  > > \[ *Note:* The <del>visible sequence of side effects</del> <ins>value observed
  > > by a load of an atomic</ins> depends on the "happens before" relation, which
  > > depends on the values observed by loads of atomics<del>, which we are
  > > restricting here</del>. The intended reading is that there must exist an
  > > association of atomic loads with modifications they observe that, together with
  > > suitably chosen modification orders and the "happens before" relation derived as
  > > described above, satisfy the resulting constraints as imposed here. —*end note*
  > > \]
* For C 5.1.2.4 paragraph 27, the following C\+\+ discussion is relevant:
  > I think 1.10p22 should be changed as follows:
  >
  > > \[ *Note:* Compiler transformations that introduce assignments to a potentially
  > > shared memory location that would not be modified by the abstract machine are
  > > generally precluded by this standard, since such an assignment might overwrite
  > > another assignment by a different thread in cases in which an abstract machine
  > > execution would not have encountered a data race. This includes implementations
  > > of data member assignment that overwrite adjacent members in separate memory
  > > locations. Reordering of atomic loads in cases in which the atomics in question
  > > may alias is also generally precluded, since this may violate the <del>"visible
  > > sequence"</del><ins>coherence</ins> rules. —*end note* \]
* For C 7.17.3 paragraph 6, the following C\+\+ discussion is relevant:
  > I believe the 29.3p3 wording should change as follows:
  >
  > + the result of the last modification *A* of *M* that precedes *B* in *S*, if it exists, or
  > + if *A* exists, the result of some modification of *M* <del>in the visible sequence of side effects with respect to *B*</del> that is not `memory_order_seq_cst` and that does not happen before *A*, or
  > + if *A* does not exist, the result of some modification of *M* <del>in the visible sequence of side effects with respect to *B*</del> that is not `memory_order_seq_cst`.

Apr 2014 meeting

### Committee Discussion

> WG21 liaison has been asked to ascertain status of this w.r.t. C\+\+14 and to
> provide a suggested TC.

Oct 2014 meeting

### Committee Discussion

> A paper [N1856](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1856.htm) was
> provided that discusses the drift between the two Standards and a first cut at
> some possible wording changes, as follows. It was not, however, discussed, but
> does provide insight as to the necessary direction for a resolution to this DR.

1. Change 5.1.2.4 paragraph 22 as follows:

   > <del>The *visible sequence of side effects* on an atomic object *M*, with
   > respect to a value computation *B* of *M*, is a maximal contiguous sub-sequence
   > of side effects in the modification order of M, where the first side effect is
   > visible with respect to *B*, and for every side effect, it is not the case that
   > *B* happens before it.</del> The value of an atomic object *M*, as determined by
   > evaluation *B*, shall be the value stored by some <del>operation in the visible
   > sequence of *M* with respect to *B*</del> <ins>side effect *A* that modifies
   > *M*, where *B* does not happen before *A*</ins>. \[*Note:* <del>It can be shown
   > that the visible sequence of side effects of a value computation is unique
   > given</del> <ins>The set of side effects that a given evaluation might take its
   > value from is also restricted by the rest of the rules described here, and in
   > particular, by</ins> the coherence requirements below. —*end note*\]
2. Change 5.1.2.4 paragraph 24 as follows:

   > \[*Note:* The <del>visible sequence of side effects</del> <ins>value observed by
   > a load of an atomic</ins> depends on the “happens before” relation, which
   > depends on the values observed by loads of atomics<del>, which we are
   > restricting here</del>. The intended reading is that there must exist an
   > association of atomic loads with modifications they observe that, together with
   > suitably chosen modification orders and the “happens before” relation derived as
   > described above, satisfy the resulting constraints as imposed here. —*end
   > note*\]
3. Change 5.1.2.4 paragraph 27 as follows:

   > \[*Note:* Compiler transformations that introduce assignments to a potentially
   > shared memory location that would not be modified by the abstract machine are
   > generally precluded by this standard, since such an assignment might overwrite
   > another assignment by a different thread in cases in which an abstract machine
   > execution would not have encountered a data race. This includes implementations
   > of data member assignment that overwrite adjacent members in separate memory
   > locations. Reordering of atomic loads in cases in which the atomics in question
   > may alias is also generally precluded, since this may violate the <del>“visible
   > sequence”</del> <ins>coherence</ins> rules. —*end note*\]
4. Change 7.17.3 paragraph 6 as follows:

   > There shall be a single total order *S* on all `memory_order_seq_cst`
   > operations, consistent with the “happens before” order and modification orders
   > for all affected locations, such that each `memory_order_seq_cst` operation *B*
   > that loads a value from an atomic object *M* observes one of the following
   > values:
   >
   > * the result of the last modification *A* of *M* that precedes *B* in *S*, if it
   >   exists, or
   > * if *A* exists, the result of some modification of *M* <del>in the visible
   >   sequence of side effects with respect to *B*</del> that is not
   >   `memory_order_seq_cst` and that does not happen before *A*, or
   > * if *A* does not exist, the result of some modification of *M* <del>in the
   >   visible sequence of side effects with respect to *B*</del> that is not
   >   `memory_order_seq_cst`.
   >
   > \[*Note:*...

Apr 2015 meeting

### Committee Discussion

> The provided words were accepted, with slight editorial changes, as the Proposed
> Technical Corrigendum.

### Proposed Technical Corrigendum

Change 5.1.2.4 paragraph 22 from:

> The *visible sequence of side effects* on an atomic object *M*, with respect to
> a value computation *B* of *M*, is a maximal contiguous sub-sequence of side
> effects in the modification order of M, where the first side effect is visible
> with respect to *B*, and for every subsequent side effect, it is not the case
> that *B* happens before it. The value of an atomic object *M*, as determined by
> evaluation *B*, shall be the value stored by some operation in the visible
> sequence of *M* with respect to *B*.

to:

> The value of an atomic object *M*, as determined by evaluation *B*, shall be the
> value stored by some side effect *A* that modifies *M*, where *B* does not
> happen before *A*.

After 5.1.2.4 paragraph 22 add:

> **Note** The set of side effects from which a given evaluation might take its
> value is also restricted by the rest of the rules described here, and in
> particular, by the coherence requirements below.

Change 5.1.2.4 paragraph 24 from:

> **Note 11:** The visible sequence of side effects depends on the “happens
> before” relation, which in turn depends on the values observed by loads of
> atomics, which we are restricting here. The intended reading is that there must
> exist an association of atomic loads with modifications they observe that,
> together with suitably chosen modification orders and the “happens before”
> relation derived as described above, satisfy the resulting constraints as
> imposed here.

to

> **Note 11:** The value observed by a load of an atomic depends on the “happens
> before” relation, which in turn depends on the values observed by loads of
> atomics. The intended reading is that there must exist an association of atomic
> loads with modifications they observe that, together with suitably chosen
> modification orders and the “happens before” relation derived as described
> above, satisfy the resulting constraints as imposed here.

Change 5.1.2.4 paragraph 27 from:

> **Note 13:** Compiler transformations that introduce assignments to a
> potentially shared memory location that would not be modified by the abstract
> machine are generally precluded by this standard, since such an assignment might
> overwrite another assignment by a different thread in cases in which an abstract
> machine execution would not have encountered a data race. This includes
> implementations of data member assignment that overwrite adjacent members in
> separate memory locations. Reordering of atomic loads in cases in which the
> atomics in question may alias is also generally precluded, since this may
> violate the “visible sequence” rules.

to

> **Note 13:** Compiler transformations that introduce assignments to a
> potentially shared memory location that would not be modified by the abstract
> machine are generally precluded by this standard, since such an assignment might
> overwrite another assignment by a different thread in cases in which an abstract
> machine execution would not have encountered a data race. This includes
> implementations of data member assignment that overwrite adjacent members in
> separate memory locations. Reordering of atomic loads in cases in which the
> atomics in question may alias is also generally precluded, since this may
> violate the coherence requirements.

Change 7.17.3 paragraph 6 from:

> There shall be a single total order *S* on all `memory_order_seq_cst`
> operations, consistent with the “happens before” order and modification orders
> for all affected locations, such that each `memory_order_seq_cst` operation *B*
> that loads a value from an atomic object *M* observes one of the following
> values:
>
> * the result of the last modification *A* of *M* that precedes *B* in *S*, if it
>   exists, or
> * if *A* exists, the result of some modification of *M* in the visible sequence of
>   side effects with respect to *B* that is not `memory_order_seq_cst` and that
>   does not happen before *A*, or
> * if *A* does not exist, the result of some modification of *M* in the visible
>   sequence of side effects with respect to *B* that is not `memory_order_seq_cst`.

to:

> There shall be a single total order *S* on all `memory_order_seq_cst`
> operations, consistent with the “happens before” order and modification orders
> for all affected locations, such that each `memory_order_seq_cst` operation *B*
> that loads a value from an atomic object *M* observes one of the following
> values:
>
> * the result of the last modification *A* of *M* that precedes *B* in *S*, if it
>   exists, or
> * if *A* exists, the result of some modification of *M* that is not
>   `memory_order_seq_cst` and that does not happen before *A*, or
> * if *A* does not exist, the result of some modification of *M* that is not
>   `memory_order_seq_cst`.


</div>


---

---

<div id="issue0407">

## Issue 0407: SC fences do not restrict modification order enough

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 seems to omit the restriction imposed in C\+\+11 in 29.3p7 (from
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf)):

> For atomic operations `A` and `B` on an atomic object `M`, if there are
> `memory_order_seq_cst fences X` and `Y` such that `A`is sequenced before `X`,
> `Y` is sequenced before `B`, and `X` precedes `Y` in `S`, then `B` occurs later
> than `A` in the modification order of `M`.

Furthermore, it seems that both C11 and C\+\+11 are missing the following two
derivatives of this rule:

> For atomic modifications `A` and `B` of an atomic object `M`, if there is a
> `memory_order_seq_cst fence X` such that `A` is sequenced before `X`, and `X`
> precedes `B` in `S`, then `B` occurs later than `A` in the modification order of
> `M`.
>
> For atomic modifications `A` and `B` of an atomic object `M`, if there is a
> `memory_order_seq_cst` fence `Y` such that `Y` is sequenced before `B`, and `A`
> precedes `Y` in `S`, then `B` occurs later than `A` in the modification order of
> `M`.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee Discussion

> * The changes are difficult to fully understand \- a diagram might help.
> * A paper for the next meeting would help the Committee make progress on this.
> * Some concern about having C and C\+\+ differ.

Feb 2012 meeting

### Committee Discussion

> * No work was done on this defect between meetings, so no additional information has been provided.
> * There seems to be two issues here, and this should possibility be two defect reports rather than one.
> * No known liaison has taken place with WG 21 on this issue.
> * The proposed words are inappropriate for C, still need words that work for C.
> * There seems to be editorial issues with the proposed words for C\+\+ as well.
> * There is consensus to adopt something along the lines of the first proposed change, with wording that is consistent with C.
> * WG 14 needs to stay in step with WG 21\.
> * Clark Nelson took an action item to liaise with WG 21\.

Oct 2012 meeting

### Committee Discussion

> * This item has also become WG21 Library Issue 2130\.
> * Rajan presented a diagram and argued that we should adopt the first part and that the second two parts were redundant.
> * After 7.17.3 paragraph 11 add the following:
>
>   > For atomic operations `A` and `B` on an atomic object `M`, if there are
>   > `memory_order_seq_cst fences X` and `Y` such that `A` is sequenced before `X`,
>   > `Y` is sequenced before `B`, and `X` precedes `Y` in `S`, then `B` occurs later
>   > than `A` in the modification order of `M`.

Oct 2013 meeting

### Committee Discussion

* The corresponding words in proposed working draft for C\+\+ have changed, and the proposal above is no longer appropriate.
* The corresponding paragraph reference for C is still 7.13.3 paragraph 11\.
* The following change has been applied to the C\+\+ working draft:
  > Change 29.3 \[atomics.order\] paragraph 7 as indicated: *\[Drafting note: Note
  > that the wording change intentionally does also replace the term atomic
  > operation by atomic modification\]*
  >
  > -7- <del>For atomic operations *A* and *B* on an atomic object *M*, if there are
  > `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*,
  > *Y* is sequenced before *B*, and *X* precedes *Y* in *S*, then *B* occurs later
  > than *A* in the modification order of *M*.</del> <ins>For atomic modifications
  > *A* and *B* of an atomic object *M*, *B* occurs later than *A* in the
  > modification order of *M* if:</ins>
  >
  > + <ins>there is a `memory_order_seq_cst` fence *X* such that *A* is sequenced before *X*, and *X* precedes *B* in *S*, or</ins>
  > + <ins>there is a `memory_order_seq_cst` fence *Y* such that *Y* is sequenced before *B*, and *A* precedes *Y* in *S*, or</ins>
  > + <ins>there are `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*, *Y* is sequenced before *B*, and *X* precedes *Y* in *S*.</ins>

Apr 2014 meeting

### Committee Discussion

> WG21 liaison has been asked to ascertain status of this w.r.t. C\+\+14 and to
> provide a suggested TC.

Oct 2014 meeting

### Committee Discussion

> A paper [N1856](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1856.htm) was
> provided that discusses the drift between the two Standards and a first cut at
> some possible wording changes, as follows. It was not, however, discussed, but
> does provide insight as to the necessary direction for a resolution to this DR.

1. *\[Drafting note: The project editor is kindly asked to consider to replace in
   1.10 \[intro.multithread\] p17 the phrase "before an operation B on M" by
   "before a modification B of M".\]*
2. Change 7.17.3 paragraph 11 as indicated: *\[Drafting note: Note that the wording
   change intentionally does also replace the term atomic operation by atomic
   modification\]*

   <del>For atomic operations *A* and *B* on an atomic object *M*, if there are
   `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*,
   *Y* is sequenced before *B*, and *X* precedes *Y* in *S*, then *B* occurs later
   than *A* in the modification order of *M*.</del> <ins>For atomic modifications
   *A* and *B* of an atomic object *M*, *B* occurs later than *A* in the
   modification order of *M* if:</ins>

   * <ins>there is a `memory_order_seq_cst` fence *X* such that *A* is sequenced before *X*, and *X* precedes *B* in *S*, or</ins>
   * <ins>there is a `memory_order_seq_cst` fence *Y* such that *Y* is sequenced before *B*, and *A* precedes *Y* in *S*, or</ins>
   * <ins>there are `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*, *Y* is sequenced before *B*, and *X* precedes *Y* in *S*.</ins>

   \[ *Note*: `memory_order_seq_cst` ensures sequential consistency only for a
   program that is free of data races and uses exclusively `memory_order_seq_cst`
   operations. Any use of weaker ordering will invalidate this guarantee unless
   extreme care is used. In particular, `memory_order_seq_cst` fences ensure a
   total order only for the fences themselves. Fences cannot, in general, be used
   to restore sequential consistency for atomic operations with weaker ordering
   specifications. —*end note* \]

Apr 2015 meeting

### Committee Discussion

> The provided words were adopted as the Proposed Technical Corrigendum. The
> project editor is asked to review and replace the phrase "before an operation
> *B* on *M*" by "before a modification *B* of *M*".

### Proposed Technical Corrigendum

Change 7.17.3 paragraph 11 from:

> For atomic operations *A* and *B* on an atomic object *M*, if there are
> `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*,
> *Y* is sequenced before *B*, and *X* precedes *Y* in *S*, then *B* occurs later
> than *A* in the modification order of *M*.

to:

> For atomic modifications *A* and *B* of an atomic object *M*, *B* occurs later
> than *A* in the modification order of *M* if:
>
> * there is a `memory_order_seq_cst` fence *X* such that *A* is sequenced before *X*, and *X* precedes *B* in *S*, or
> * there is a `memory_order_seq_cst` fence *Y* such that *Y* is sequenced before *B*, and *A* precedes *Y* in *S*, or
> * there are `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*, *Y* is sequenced before *B*, and *X* precedes *Y* in *S*.


</div>


---

---

<div id="issue0408">

## Issue 0408: Should locks provide intra-thread synchronization

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Most of the C\+\+ standard, synchronisation is used exclusively inter-thread, so
in particular, synchronisation can't be used to avoid undefined behavior arising
from conflicting un-sequenced memory accesses, e.g.:

> ```c
> (x = 1)==(x = 2)
> ```

Firstly, C does not define this sort of thing as undefined behavior. Is this
intentional? Secondly in C\+\+ locks can currently be used to fix up such
programs and avoid undefined behavior, e.g.:

> ```c
> (lock; x = 1; unlock; x)==(lock; x = 2; unlock; x)
> ```

The reason not to allow this sort of synchronisation in general is, because it
disallows some single threaded compiler optimisations. Is intra-thread locking
intended to be defined and usable?

### Suggested Technical Corrigendum

---

Comment from WG14 on 2013-04-26:

Oct 2011 meeting

### Committee Discussion

> * The changes seem reasonable, but without actual text no position can be formed.
> * A paper for the next meeting is probably the best way to make progress.

Feb 2012 meeting

### Committee Discussion

> * Blaine Garst and the submitter worked on this between meetings, they believe this is not a problem.
> * Convener prefers this remain OPEN for now, there could be additional text as discussed in Oct.
> * C11 does define the semantics of a lock within a single thread.

Oct 2012 meeting

### Proposed Committee Response

> * The expression `(x = 1)==(x = 2)` has undefined behavior in C11.
> * The happens-before relationship imposed by `(lock(), x = 1, unlock())` does not constrain the possible interwoven order of evaluation of `(lock(), x = 2, unlock())` .


</div>


---

---

<div id="issue0409">

## Issue 0409: `f(inf)` is `inf` being a range error

Authors: WG 14, Fred J. Tydeman (USA)  
Date: 2012-01-11  
Reference document: [N1593](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1593.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Several of the functions in `<math.h>` that compute infinity for `f(infinity)`
have the phrase (or something similar):

> A range error occurs if the magnitude of x is too large.

Since infinity is 'too large', one might conclude that `f(infinity)` is a range
error for those functions.

However, 7.12.1#5 has:

> A floating result overflows if the magnitude of the mathematical result is
> finite but so large that the mathematical result cannot be represented without
> extraordinary roundoff error ...

The key word being 'finite'. So, one could conclude f(infinity) being infinity
is not overflow (and therefore, not a range error).

To me, this appears to be a contradiction. I have encountered both kinds of
implementations; some treat this case as a range error, and others that do not.

For both LIA and IEEE-754, f(infinity) being infinity is not considered an
error.

### Suggested Change

1. 7.12.5.4 The cosh functions

   Change to: A range error occurs if the magnitude of finite x is too large.
2. 7.12.5.5 The sinh functions

   Change to: A range error occurs if the magnitude of finite x is too large.
3. 7.12.6.1 The exp functions

   Change to: A range error occurs if the magnitude of finite x is too large.
4. 7.12.6.2 The exp2 functions

   Change to: A range error occurs if the magnitude of finite x is too large.
5. 7.12.6.3 The expm1 functions

   Change to: A range error occurs if the magnitude of finite x is too large.
6. 7.12.6.6 The ldexp functions

   Change to: A range error may occur for finite arguments.
7. 7.12.6.13 The scalbn and scalbln functions

   Change to: A range error may occur for finite arguments.
8. 7.12.7.3 The hypot functions

   Change to: A range error may occur for finite arguments.
9. 7.12.7.4 The pow functions

   Change to: A range error may occur for finite arguments.
10. 7.12.8.2 The erfc functions

    Change to: A range error occurs if finite x is too large.
11. 7.12.8.3 The lgamma functions

    Change to: A range error occurs if finite x is too large.
12. 7.12.8.4 The tgamma functions

    Change to: A range error occurs if the magnitude of finite x is too large and
    may occur if the magnitude of x is too small.
13. 7.12.12.1 The fdim functions

    Change to: A range error may occur for finite arguments.
14. 7.12.13.1 The fma functions

    Change to: A range error may occur for finite arguments.

---

Comment from WG14 on 2016-10-21:

Feb 2012 meeting

### Committee Discussion

> * The committee rejected the Suggested Change in the main body of this defect report.
> * The committee considered the following, but rejected it (as just being a restatement of 7.12.1 paragraphs 4 and 5).
>   > If the result overflows, a range error shall occur.
> * A question arose as to why these range error cases are listed in the individual functions (instead of just being covered by the blanket 7.12.1 paragraphs 4, 5, and 6\)
>
>   7.12.1 paragraph 1 has the answer:
>
>   > The behavior of each of the functions in \<math.h\> is specified for all
>   > representable values of its input arguments, except where stated otherwise.
> * Several other approaches were discussed, without any consensus reached
>   1. Add a footnote to 7.12.1 paragraph 5, first sentence:
>      > In an implementation that supports infinities, a range error may happen for
>      > functions that map an infinity argument into an exact infinity or exact zero
>      > result.
>   2. Add to end of 7.12.1 paragraph 4:
>      > Recommended practice
>      >
>      > In an implementation that supports infinities, a range error should not happen
>      > for functions that map an infinity argument into an exact infinity or exact zero
>      > result.
>   3. Add to 7.12.1 paragraph 4:
>      > An implementation may define additional range errors, provided that such errors
>      > are consistent with the mathematical definition of the function.

Oct 2012 meeting

### Committee Discussion

> * Fred wrote a paper [N1629](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1629.htm) discussing "Fixing a contradiction" and "Taking care of infinity".
> * The definition of range error, however, in 7.12.1 paragraph 4 indicates infinity is excluded (since it has a representation), and as such no change is required.

Oct 2015 meeting

### Committee Discussion

> Fred presented another paper
> [N1979](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1979.htm) noting an
> error in the October 2012 committee response, and after discussion, the proposed
> clarification was adopted, and is as follows

### Proposed Committee Response

The definition of range error in 7.12.1 paragraph 4 excludes infinity.

For example, `exp(+infinity)` is `+infinity`. Since the input `+infinity` is
representable, then the output `+infinity` is representable in an object of the
specified type. By, 7.12.1 paragraph 4, a range error has not happened. Also, by
7.12.1 paragraph 5, since the result is not finite, overflow has not happened.


</div>


---

---

<div id="issue0410">

## Issue 0410: `ilogb` inconsistent with `lrint`, `lround`

Authors: WG 14, Fred J. Tydeman (USA)  
Date: 2012-01-11  
Reference document: [N1595](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1595.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

For the case of converting a large finite value to an integer value, lrint and
lround have one set of requirements, while ilogb has another set. This is
inconsistent.

Both 7.12.9.5 The lrint and llrint functions and 7.12.9.7 The lround and llround
functions have:

> If the rounded value is outside the range of the return type, the numeric result
> is unspecified and a domain error or range error may occur.

While 7.12.6.5 The ilogb functions has:

> If the correct value is outside the range of the return type, the numeric result
> is unspecified.

I believe that the following changes to C11 should be done.

1. 7.12.6.5 The ilogb functions:

   Change to: If the correct value is outside the range of the return type, the
   numeric result is unspecified and a domain error or range error may occur.

---

Comment from WG14 on 2017-11-03:

Feb 2012 meeting

> ### Committee discussion
>
> > * Some believe the rationale presented as a reason for doing this is not a valid rationale for the change.
>
> ### Proposed Technical Corrigendum
>
> > In 7.12.6.5 paragraph 2, change the last sentence to:
> >
> > > If the correct value is outside the range of the return type, the numeric result
> > > is unspecified and a domain error or range error may occur.


</div>


---

---

<div id="issue0411">

## Issue 0411: Predefined macro values

Authors: Project Editor, Project Editor (Larry Jones)  
Date: 2012-01-18  
Status: Fixed  
Fixed in: C11 TC1  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The actual values for the predefined macros `__STDC_VERSION__` and
`__STDC_LIB_EXT1__` should be specified.

### Suggested Technical Corrigendum

Change the relevant list entry in 6.10.8.1 to:

> `__STDC_VERSION__` The integer constant `201112L`.

Change the relevant list entry in 6.10.8.3 to:

> `__STDC_LIB_EXT1__` The integer constant `201112L`.

---

Comment from WG14 on 2012-02-17:

Feb 2012 meeting

> ### Committee Discussion
>
> > * The committee asked the Convener to look into making this an errata if possible.
>
> ### Proposed Technical Corrigendum
>
> Change 6.10.8.1 from:
>
> > `__STDC_VERSION__` The integer constant`201ymmL`.<sup>178\)</sup>
>
> to:
>
> > `__STDC_VERSION__` The integer constant `201112L`.<sup>178\)</sup>
>
> Change 6.10.8.3 from:
>
> > `__STDC_LIB_EXT1__` The integer constant`201ymmL`, intended to indicate support
> > for the extensions defined in annex K (Bounds-checking
> > interfaces).<sup>179\)</sup>
>
> to:
>
> > `__STDC_LIB_EXT1__` The integer constant `201112L`, intended to indicate support
> > for the extensions defined in annex K (Bounds-checking
> > interfaces).<sup>179\)</sup>


</div>


---

---

<div id="issue0412">

## Issue 0412: `#elif`

Authors: Project Editor (Larry Jones), Edward Diener (comp.std.c)  
Date: 2012-01-18  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

It appears that `#elif` is not entirely equivalent to `#else`, `#if`, and
`#endif`.

Consider the code:

> ```c
> #if 1
> ...
> #else
> #if this is not a valid expression
> ...
> #endif
> #endif
> ```

This is well-defined. Since the controlling expression of the `#if` evaluates to
true, the `#else` group is skipped and thus the nested `#if` is only processed
through the directive name (6.10.1p6).

However, if this is recast using `#elif`:

> ```c
> #if 1
> ...
> #elif this is not a valid expression
> ...
> #endif
> ```

the `#elif` is not part of a group that is skipped and thus must be processed
completely, including evaluating the controlling condition (even though the
resulting value is of no interest).

I do not believe this was the committee's intent.

### Suggested Technical Corrigendum

In 6.10.1p6, change:

> Only the first group whose control condition evaluates to true (nonzero) is
> processed.

to:

> Only the first group whose control condition evaluates to true (nonzero) is
> processed; any following groups are skipped and their controlling directives are
> processed as if they were in a group that is skipped.

---

Comment from WG14 on 2017-11-03:

Feb 2012 meeting

### Proposed Technical Corrigendum

In 6.10.1p6, change:

> Only the first group whose control condition evaluates to true (nonzero) is
> processed.

to:

> Only the first group whose control condition evaluates to true (nonzero) is
> processed; any following groups are skipped and their controlling directives are
> processed as if they were in a group that is skipped.


</div>


---

---

<div id="issue0413">

## Issue 0413: initialization

Authors: WG14, Willem Wakker  
Date: 2012-01-27  
Reference document: [N1601](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1601.htm)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0253](log_c99.md#issue0253)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Consider the following code:

> ```c
> typedef struct {
> int k;
> int l;
> int a[2];
> } T;
>
> typedef struct {
> int i;
> T t;
> } S;
>
> T x = {.l = 43, .k = 42, .a[1] = 19, .a[0] = 18 };
>
> void f(void)
> {
> S l = { 1, .t = x, .t.l = 41, .t.a[1] = 17};
> }
> ```

The question is: what is now the value of `l.t.k`? Is it 42 (due to the
initialization of `.t = x`) or is it 0 (due to the fact that `.t.l` starts an
incomplete initialization of `.t`?

The relevant clause from the standard is 6.7.9 clause 19:

> 19 The initialization shall occur in initializer list order, each initializer
> provided for a particular subobject overriding any previously listed initializer
> for the same subobject;<sup>151</sup>) all subobjects that are not initialized
> explicitly shall be initialized implicitly the same as objects that have static
> storage duration.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2014-10-31:

Feb 2012 Meeting

### Committee Discussion

> * It was noted that this is basically similar to [dr\_253](log_c99.md#issue0253).
> * The following was proposed, but there was no consensus for adoption.
>   > The initialization shall occur in initializer list order, each initializer
>   > provided for a particular subobject overriding any previously listed initializer
>   > for the same subobject <sup>151\)</sup>. Subsequently, all subobjects that are
>   > not initialized explicitly previously shall be initialized implicitly the same
>   > as objects that have static storage duration.

Oct 2012 meeting

### Committee Discussion

> * The original author intended the result to be 42 by the following reasoning:
> * 6.7.9 paragraphs 17-18 specify that each designator list affects only the smallest subobject to which the designator list refers. As a result, the second clause of paragraph 19 occurs once for the greater object as a whole, filling in only those parts of the whole object that were never initialized explicitly.
> * **gcc** and some IBM compilers give the result as 0, although it is not believed that there is code dependent on this interpretation.
> * David Keaton proposed [N1659](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1659.pdf).
> * This, however, does not clarify the interpreted conflict of paragraph 19 "subobjects that are not initialized explicitly \[shall be set to zero\]" applied "recursively to subaggregates" (paragraph 20).
> * Adding the example is a desired outcome.

Apr 2013 meeting

### Committee Discussion

> There was no work performed on this DR.
>
> Although both GCC and six compilers from IBM provide the unintended answer, it
> is believed to be such a rarely used feature that it is not depended upon to a
> great degree, and the compiler venders are willing to change their behavior
> appropriately.

Oct 2013 meeting

### Committee Discussion

> There has been considerable discussion and several proposals ( N1659, N1749) to
> clarify the standard to no avail. Upon reflection, and consultation with the
> author, we believe that the proper course of action is twofold. First, simply
> answer the question asked as the committee believes that the standard already
> specifies correctly. To add clarification to the standard we will also add the
> examples from N1659 that leads to this answer.

### Proposed Committee Response

The proper answer to the question raised according to the standard is that the
value of l.t.k is 42, because implicit initialization does not override explicit
initialization. We will also provide a non-normative example to further clarify
the intent.

### Proposed Technical Corrigendum

Add the following example to 6.7.9:

```c
    typedef struct {
        int k;
        int l;
        int a[2];
    } T;

    typedef struct {
        int i;
        T t;
    } S;

    T x = {.l = 43, .k = 42, .a[1] = 19, .a[0] = 18 };

    void f(void)
    {
        S l = { 1, .t = x, .t.l = 41, .t.a[1] = 17};
    }
```

The value of l.t.k is 42, because implicit initialization does not override
explicit initialization.


</div>


---

---

<div id="issue0414">

## Issue 0414: Typos in 6.27 Threads `<threads.h>`

Authors: WG14, Tom Plum  
Date: 2012-03-20  
Reference document: [N1614](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1614.htm)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0469](log_c11c17.md#issue0469), [0493](log_c11c17.md#issue0493)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

In 7.26.1 paragraph 5

> The enumeration constants are
>
> > ```c
> > mtx_plain
> > ```
>
> which is passed to `mtx_init` to create a mutex object that supports neither
> timeout nor test and return;

the "test and return" is referring to `try_lock`, `try_lock` is not optional,
therefore the "test and return" should be removed.   

In 7.26.4.2 paragraph 2

> The `mtx_init` function creates a mutex object with properties indicated by
> `type`,   
> which must have one of the six values:  
> `mtx_plain` for a simple non-recursive mutex,  
> `mtx_timed` for a non-recursive mutex that supports timeout,  
> `mtx_plain | mtx_recursive` for a simple recursive mutex, or   
> `mtx_timed | mtx_recursive` for a recursive mutex that supports timeout.

There are not **six** values listed, "six" should be changed to "these".

### Suggested Technical Corrigendum

Change 7.26.1 paragraph 5 to

> The enumeration constants are
>
> > ```c
> > mtx_plain
> > ```
>
> which is passed to `mtx_init` to create a mutex object that does not support
> timeout;

Change 7.26.4.2 paragraph 2 to

> The `mtx_init` function creates a mutex object with properties indicated by
> `type`,   
> which must have one of these values:

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Committee Discussion

Adopt the Suggested Technical Corregendum as proposed.

### Proposed Technical Corrigendum

Change 7.26.1 paragraph 5 to

> The enumeration constants are
>
> > ```c
> > mtx_plain
> > ```
>
> which is passed to `mtx_init` to create a mutex object that does not support
> timeout;

Change 7.26.4.2 paragraph 2 to

> The `mtx_init` function creates a mutex object with properties indicated by
> `type`,   
> which must have one of the these values:


</div>


---

---

<div id="issue0415">

## Issue 0415: Missing divide by zero entry in Annex J.2

Authors: WG14, Seacord (PL22.11)  
Date: 2012-06-02  
Reference document: [N1617](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1617.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The undefined behavior defined in paragraph 6 of 6.5.5 is missing in J.2 and
should be added.

### Suggested Technical Corrigendum

Add a bullet with the following text to J.2 after bullet 45

> If the quotient `a/b` is not representable, the behavior of both `a/b` and `a%b`
> is undefined (6.5.5).

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Committee Discussion

Adopt the Suggested Technical Corregendum as proposed.

### Proposed Technical Corrigendum

Add a bullet with the following text to J.2 after bullet 45

> If the quotient `a/b` is not representable, the behavior of both `a/b` and `a%b`
> is undefined (6.5.5).


</div>


---

---

<div id="issue0416">

## Issue 0416: `tss_t` destruction unspecified

Authors: WG14, Owen Shepherd  
Date: 2012-08-12  
Reference document: [N1627](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1627.htm)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0424](log_c11c17.md#issue0424), [0469](log_c11c17.md#issue0469)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The standard does not specify if or when destructors for thread specific data
keys (created with the `tss_create` function) are invoked.

This proposal suggests to align the behavior with that specified by POSIX for
`pthread_key_t`. This behavior is hoped to both match the intention of the
standard, and be possible to implement on other systems (it is noted that a
pthreads implementation exists for Windows, for example, while the behavior of
POSIX and Windows thread local storage implementations differ greatly)

### Suggested Technical Corrigendum

After 7.26.5.1p2, add

> Returning from `func` shall have the same behaviour as invoking `thrd_exit` with
> the returned value

Change 7.26.5.5 parts 2 and 3 from

> The `thrd_exit` function terminates execution of the calling thread and sets its
> result code to `res`.
>
> The program shall terminate normally after the last thread has been terminated.
> The behavior shall be as if the program called the exit function with the
> status EXIT\_SUCCESS at thread termination time.

to

> For every thread specific storage key which was created with a non-NULL
> destructor and for which the value is non-NULL, `thrd_exit` shall set the value
> associated with the key to NULL and then invoke the destructor with its previous
> value. The order in which destructors are invoked is unspecified.
>
> If after this process there remain keys with both non-NULL destructors and
> values, the implementation shall repeat this process up to `TSS_DTOR_ITERATIONS`
> times.
>
> If `thrd_exit` is not being invoked in the last thread in the process, then the
> implementation shall terminate execution of the calling thread and set its
> result code to `res`. Otherwise, the implementation shall behave as
> if `exit(EXIT_SUCCESS)` was invoked.

(This change provides application writers guarantees about the identity of the
thread executing functions registered with `atexit`)

After 7.26.6.1p2, add

> The value NULL shall be associated with the newly created key in all existing
> threads. Upon thread creation, the value associated with all keys shall be
> initialized to NULL
>
> Note that destructors associated thread specific storage are not invoked at
> process exit.

To 7.26.6.2p2, append

> If `tss_delete` is called while another thread is executing destructors, whether
> this will affect the number of invocations of the destructor associated
> with `key` on that thread is unspecified. If the thread from which `tss_delete`
> is invoked is executing destructors, then no further invocations of the
> destructor associated with `key` will occur on said thread.
>
> Calling `tss_delete` will not result in the invocation of any destructors.

After 7.26.6.4p2, add

> This action will not invoke the destructor associated with the key on the value
> being replaced.

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Committee Discussion

> * This paper was discussed in conjunction with [DR424](log_c11c17.md#issue0424) which covers one additional related issue.
> * The key observation is that these papers are about the deliberate underspecification of threads, since that allows the greatest opportunity for implementation on a variety of operating systems.
> * Pete Becker, an implementor of the C11 threads library, was asked about these papers and replied in SC22/WG14 message 12813\.
> * Based on that response the committee is concerned that there could be subtleties in adopting the Proposed Technical Corrigendum and that, as such, these changes are substantial enough to warrant a proposal and to not be considered a defect.

Apr 2013 meeting

### Committee Discussion

> * A revised paper [N1687](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1687.pdf) was submitted, although not in the recommended html format.
> * The suggested technical corrigendum would specify new instances of undefined behavior as well as new requirements on implementations.
> * The committee expressed concern that some of the new requirements may be onerous or impossible to provide above the native platform implementation.

Oct 2013 meeting

### Committee Discussion

> After several papers
> [N1750,](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1750.htm)
> [N1751,](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1751.htm) revisions,
> and much discussion, the committee has agreed on the following as the
> resolution.

### Proposed Technical Corrigendum

After 7.26.5.1 paragraph 2, add

> Returning from `func` shall have the same behavior as invoking `thrd_exit` with
> the value returned from `func`.

Change 7.26.5.5, replace paragraph 2 with:

> For every thread-specific storage key which was created with a non-null
> destructor and for which the value is non-null, `thrd_exit` shall set the value
> associated with the key to `NULL` and then invoke the destructor with its
> previous value. The order in which destructors are invoked is unspecified.
>
> If after this process there remain keys with both non-null destructors and
> values, the implementation shall repeat this process up to `TSS_DTOR_ITERATIONS`
> times.
>
> Following this, the `thrd_exit` function terminates execution of the calling
> thread and sets its result code to `res`.

After 7.26.6.1 paragraph 2, add the following new paragraphs:

> The value `NULL` shall be associated with the newly created key in all existing
> threads. Upon thread creation, the value associated with all keys shall be
> initialized to `NULL`.
>
> Destructors associated with thread-specific storage are not invoked at program
> termination.
>
> A call to `tss_create` from within a destructor results in undefined behavior.

In 7.26.6.2 paragraph 2, add the following new second sentence:

> A call to `tss_delete` function results in undefined behavior if the call to
> `tss_create` which set `key` completed after the thread commenced executing
> destructors.

After 7.26.6.2 paragraph 2, add the following new paragraphs:

> If `tss_delete` is called while another thread is executing destructors, whether
> this will affect the number of invocations of the destructor associated with
> `key` on that thread is unspecified.
>
> Calling `tss_delete` will not result in the invocation of any destructors.

In 7.26.6.3 paragraph 2, add the following new second sentence:

> A call to `tss_get` function results in undefined behavior if the call to
> `tss_create` which set `key` completed after the thread commenced executing
> destructors.

In 7.26.6.4 paragraph 2, add the following new second sentence:

> A call to `tss_set` function results in undefined behavior if the call to
> `tss_create` which set `key` completed after the thread commenced executing
> destructors.

After 7.26.6.4 paragraph 2, add the following new paragraph:

> This action will not invoke the destructor associated with the key on the value
> being replaced.


</div>


---

---

<div id="issue0417">

## Issue 0417: Annex J not updated with necessary `aligned_alloc` entries

Authors: WG14, John Benito  
Date: 2012-10-22  
Reference document: [N1628](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1628.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The following unspecified behaviors are incomplete in Annex J.1,
`aligned_alloc()` is missing in both entries.

> — The order and contiguity of storage allocated by successive calls to the
> `calloc`, `malloc`, and `realloc` functions (7.22.3).   
>
> — The amount of storage allocated by a successful call to the `calloc`,
> `malloc`, or `realloc` function when 0 bytes was requested (7.22.3).

The following undefined behavior bullet is incomplete in Annex J.2,
`aligned_alloc()` is missing.

> — A non-null pointer returned by a call to the `calloc`, `malloc`, or `realloc`
> function with a zero requested size is used to access an object (7.22.3).

The following implementation-defined behavior bullet is incomplete in Annex
J.3.12, `aligned_alloc()` is missing.

> — Whether the `calloc`, `malloc`, and `realloc` functions return a null pointer
> or a pointer to an allocated object when the size requested is zero (7.22.3).

### Suggested Technical Corrigendum

Change bullet 42 of J.1 to:

> — The order and contiguity of storage allocated by successive calls to the
> `calloc`, `malloc`, `realloc`, and `aligned_alloc` functions (7.22.3).

Change bullet 43 of J.1 to:

> — The amount of storage allocated by a successful call to the `calloc`,
> `malloc`, `realloc`, or `aligned_alloc` function when 0 bytes was requested
> (7.22.3).

Change bullet 166 of J.2 to

> — A non-null pointer returned by a call to the `calloc`, `malloc`, `realloc`, or
> `aligned_alloc` function with a zero requested size is used to access an object
> (7.22.3).

Change bullet 37 of J.3.12 to

> — Whether the `calloc`, `malloc`, `realloc` and `aligned_alloc` functions return
> a null pointer or a pointer to an allocated object when the size requested is
> zero (7.22.3).

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Committee Discussion

Adopt as proposed the Suggested Technical Corrigendum.

### Proposed Technical Corrigendum

Change bullet 42 of J.1 to:

> — The order and contiguity of storage allocated by successive calls to the
> `calloc`, `malloc`, `realloc`, and `aligned_alloc` functions (7.22.3).

Change bullet 43 of J.1 to:

> — The amount of storage allocated by a successful call to the `calloc`,
> `malloc`, `realloc`, or `aligned_alloc` function when 0 bytes was requested
> (7.22.3).

Change bullet 166 of J.2 to

> — A non-null pointer returned by a call to the `calloc`, `malloc`, `realloc`, or
> `aligned_alloc` function with a zero requested size is used to access an object
> (7.22.3).

Change bullet 37 of J.3.12 to

> — Whether the `calloc`, `malloc`, `realloc` and `aligned_alloc` functions return
> a null pointer or a pointer to an allocated object when the size requested is
> zero (7.22.3).


</div>


---

---

<div id="issue0418">

## Issue 0418: `fmod(0.,Nan)` and `fmod(Nan, infinity)`

Authors: WG14, Fred J. Tydeman (USA)  
Date: 2012-09-13  
Reference document: [N1633](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1633.htm)   
 **Related:** [N1497](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1497.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

First question. When Annex F is in effect, what should the value of fmod(0.,NaN)
be? The two choices are 0\. or NaN.

Annex F.10.7.1 The fmod functions has:

> * fmod(\+/-0, y) returns \+/-0 for y not zero.
> * fmod(x, y) returns a NaN and raises the “invalid” floating-point exception for x infinite or y zero (and neither is a NaN).

So, that first bullet item says fmod(0.,NaN) is 0\.

Elsewhere in that annex (F.10 Mathematics, paragraph 11), we have:

> Functions with a NaN argument return a NaN result and raise no floating-point
> exception, except where stated otherwise.

That says that fmod(0.,NaN) is NaN.

One idea is to explicitly add words about a NaN to the first bullet item in
F.10.7.1, such as:

> * fmod(\+/-0, y) returns \+/-0 for y not zero nor NaN.

However, if F.10#11 covers NaN arguments before any other arguments are
considered, then words about NaN could be removed from the second case in
F.10.7.1, such as:

> * fmod(x, y) returns a NaN and raises the “invalid” floating-point exception for x infinite or y zero.

I believe that takes us back to before N1497 was done.

Second question: what should fmod(NaN,infinity) be? Must it be the same NaN
argument, or may it be any NaN?

Annex F.10.7.1 The fmod functions has:

> * fmod(x, \+/-infinity) returns x for x not infinite.

Which says fmod(NaN,infinity) must be the same NaN argument.

But, if F.10#11 covers this NaN argument, then this case is just some NaN.

It appears that the third bullet should either be left alone or changed to:

> * fmod(x, \+/-infinity) returns x for finite x.

Some other functions that discuss NaN arguments in Annex F are: frexp, ilogb,
modf, hypot, pow, fmax, fmin, and fma. Of those, only hypot, pow, fmax, and fmin
have exceptions on NaN in implies NaN out.

---

Comment from WG14 on 2013-04-26:

Oct 2012 meeting

### Committee Discussion

> * Given that, unless stated otherwise, if the argument is a NaN, the result is a NaN, and there is no floating point exception.
> * The parenthetical comment **might** be causing confusion, and removing it seems to make it more confusing.
> * Adding more explicit wording is possible but seems unnecessary.

### Proposed Committee Response

The consensus was to do nothing and the author agrees.


</div>


---

---

<div id="issue0419">

## Issue 0419: What the heck is a "generic function"?

Authors: WG14, Douglas Walls  
Date: 2012-09-16  
Reference document: [N1635](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1635.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

What the heck is a "generic function", and what are the sections of the standard
covering how a user (or implementor) can write a stardard conforming program
defining a "type generic function"?

I was trying to reconcile the rules in 7.1.4 Use of library functions allowing
an implementation to define a function as a macro, and the user suppressing the
macro by enclosing the name of the function in parentheses. But, I don't see how
to make a function declaration, where a parameter can be any atomic type.

I've convinced myself, generic functions will take compiler magic. There is no
way to declare them using C standard conforming code. Just like the type generic
macros of \<tgmath.h\> in C99.

Somehow I missed this. I remember all the discussion of adding atomic operation
to operators like \+\= but somehow I missed the fact we were again adding in
function specifications that cannot be implemented using standard C. I thought
we were adding type generic macros. Sigh ...

I've been told that the discussion included talk about a proposal to recast them
as generic macros, but that never happened so we ended up with generic functions
through the back door without much explication.

### Suggested Technical Corrigendum

Redefine the atomic type generic functions as type generic macros. Define the
underlying functions to which the type generic macros expand.

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Proposed Technical Corrigendum

7.17.1 add a new paragraph after paragraph 5:

> It is unspecified whether any generic function declared in `stdatomic.h` is a
> macro or an identifier declared with external linkage. If a macro definition is
> suppressed in order to access an actual function, or a program defines an
> external identifier with the name of a generic function, the behavior is
> undefined.

J.2 add:

> The macro definition of a generic function is suppressed in order to access an
> actual function (7.17.1)


</div>


---

---

<div id="issue0420">

## Issue 0420: syntax error in specification of for-statement

Authors: WG14, Jens Gustedt  
Date: 2012-10-08  
Reference document: [N1647](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1647.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The standard lists two different forms for the `for`-statement in 6.8.5p1:

```c
for ( expression[opt] ; expression[opt] ; expression[opt] ) statement
for ( declaration expression[opt] ; expression[opt] ) statement
```

whereas later in 6.8.5.3 these two forms are subsumed in a third form by:

```c
for ( clause-1 ; expression-2 ; expression-3 ) statement
```

Obviously the second form above is a typo and doesn't fit within this third
form, the semantic that is given in 6.8.5.3 and to common practice in existing
compilers.

### Suggested Technical Corrigendum

Replace the second form in 6.8.5p1 and A.2.3 by the intended one:

```c
for ( declaration expression[opt] ; expression[opt] ; expression[opt] ) statement
```

---

Comment from WG14 on 2013-04-26:

Oct 2012 meeting

### Proposed Committee Response

> The second form of for-statement is not a typo. The syntax for "declaration", in
> 6.7 paragraph 1, includes an optional init-declarator-list and a trailing
> semicolon.


</div>


---

---

<div id="issue0421">

## Issue 0421: initialization of `atomic_flag`

Authors: WG14, Jens Gustedt  
Date: 2012-10-08  
Reference document: [N1648](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1648.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 expresses the intention to have `atomic_flag` as a primitive that should
allow to emulate all other atomic types and operations, *7.17.8 p3* in a note
says:

> The remaining types can be emulated with `atomic_flag`, though with less than
> ideal properties.

With the current semantic for the initialization of `atomic_flag` this goal
cannot be achieved.

### Details

This is a very good concept as far as I can see, but I have one problem to
achieve this, initialization. The phrasing for atomic types in general and for
`atomic_flag` are different. For `atomic_flag` we have:

> An atomic\_flag that is not explicitly initialized with `ATOMIC_FLAG_INIT` is
> initially in an indeterminate state.

The problem is how to emulate an atomic type with `atomic_flag` during
initialization. Say we emulate with something like

```c
struct atomic_int_struct {
  atomic_flag cat;
  int val;
};
```

Then the `ATOMIC_VAR_INIT` macro could simply look like:

```c
#define ATOMIC_VAR_INIT(V) { .cat = ATOMIC_FLAG_INIT, .val = (V), }
```

But if I’d have a variable of `atomic_int_struct` with static storage duration

```c
struct atomic_int_struct v;
```

is supposed to do the right thing, namely to guarantee that `v` has a valid
state at startup, so it should contain a `0` for `.val`, and `.cat` must be in a
determinate state. Since all atomic operations should work without problems on
`v`, the state of `.cat` can’t be anything else than “clear”.

Now looking into the possible implementations of `atomic_flag` in assembler I
didn’t yet meet a processor where the “clear” state would not be naturally
represented by an all `0` value. So I guess in any reasonable implementation we
would just have

```c
#define ATOMIC_FLAG_INIT { 0 }
```

(or some equivalent formulation.)

If this is so, why `ATOMIC_FLAG_INIT` at all? Why not phrasing the same as for
the other atomic types

### Suggested Technical Corrigendum

Eliminate the mention of `ATOMIC_FLAG_INIT` in 7.17.1p3, B.16 and the index.

Proposed change for the initialization of `atomic_flag`, 7.17.8p4:

<ins>The default initializer `{ 0 }` may be used to initialize an `atomic_flag`
to the clear state. An `atomic_flag` object with automatic storage duration that
is not explicitly initialized using `{ 0 }` is initially in an indeterminate
state; *however, the default (zero) initialization for objects with static or
thread-local storage duration initializes an `atomic_flag` to the clear state.*   
EXAMPLE</ins>

<ins>`atomic_flag guard = { 0 };`</ins>

If the committee would want to keep the macro `ATOMIC_FLAG_INIT` arround, a
partial alternative to the above text would be to modify the text in 7.17.1

<ins>`ATOMIC_FLAG_INIT`</ins>

<ins>which expands to a default initializer (`{ 0 }` or equivalent) for an
object of type `atomic_flag`.</ins>

---

Comment from WG14 on 2014-04-11:

Oct 2012 meeting

### Committee Discussion

> * The standard deliberately does not specify values for the clear and set states of `atomic_flag` objects in order to support the widest possible set of architectures.
> * The change suggested could be viewed as a proposal, but should be submitted as such, and since C11 shares the same memory model as C\+\+11 a corresponding proposal should be submitted to WG21 as well.

Apr 2013 meeting

### Proposed Committee Response

The standard deliberately does not specify values for the clear and set states
of atomic\_flag objects in order to support the widest possible set of
architectures. As such, the committee does not believe that this is a defect.


</div>


---

---

<div id="issue0422">

## Issue 0422: initialization of atomic types

Authors: WG14, Jens Gustedt  
Date: 2012-10-08  
Reference document: [N1649](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1649.htm)  
Status: Closed  
Cross-references: [0454](log_c11c17.md#issue0454)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The current version of the standard doesn't specify to which value an atomic
object should be initialized if it is initialized by default.

> An atomic object with automatic storage duration that is not explicitly
> initialized using `ATOMIC_VAR_INIT` is initially in an indeterminate state;
> however, the default (zero) initialization for objects with static or
> thread-local storage duration is guaranteed to produce a valid state.

The mentioned valid state (in contrast to the indeterminate state mentioned
before) is thus a determinate state, but the value that is stored is not
mentioned explicitly. In the introduced language of the standard it is no
definition of a "determinate state". It could be an "implementation-defined
value", just an "unspecified value" or a default (zero) initialization.
Everything suggests the later, that this would be the same value as for
initializing a variable of the underlying base type by `{ 0 }`. But I think it
would have helped to make that explicit.

### Suggested Technical Corrigendum

Proposed change for the initialization of atomic objects, 7.17.2.1p2:

<ins>An atomic object with automatic storage duration that is not explicitly
initialized using `ATOMIC_VAR_INIT` is initially in an indeterminate state;
however, the default (zero) initialization for objects with static or
thread-local storage duration is guaranteed to produce a valid state that
corresponds to the value of a zero initialized object of the unqualified base
type.   
EXAMPLE All three of the following objects initially have an observable value of
`0`.</ins>

<ins>`_Atomic(unsigned) A = { 0 };`  
`_Atomic(unsigned) B = ATOMIC_VAR_INIT(0u);`  
`static _Atomic(unsigned) C;`</ins>

---

Comment from WG14 on 2014-04-11:

Oct 2012 meeting

### Committee Discussion

> * `ATOMIC_VAR_INIT` is required to initialize an atomic object to a known value.
> * The default value for an atomic object is defined to be valid but is unspecified.
> * The committee does not see this as a defect.
> * N1649 proposes that the default value be specified to be the same as the non-atomic type’s default value.
> * Such a proposal should be submitted as such and may also need to be submitted to and addressed by WG21 (C\+\+) as well.

Apr 2013 meeting

### Proposed Committee Response

`ATOMIC_VAR_INIT` is required to initialize an atomic object to a known value.
This value is defined to be valid but is unspecified in order to support the
widest possible set of architectures. This is not a defect.


</div>


---

---

<div id="issue0423">

## Issue 0423: Defect Report relative to n1570: underspecification for qualified rvalues

Authors: WG14, Jens Gustedt  
Date: 2012-10-08  
Reference document: [N1650](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1650.htm)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0427](log_c11c17.md#issue0427), [0431](log_c11c17.md#issue0431)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The dealing of rvalues with qualified types is largely underspecified in all
versions of the C standard. This didn't surface as a problem until C11, since
until then the type of an expression was not observable but only its value.

With C11 now a problem arises for type generic primary expressions; with
`_Generic` type qualifications of values have become observable.

The standard in any of its versions has not much to say when it comes to
qualified types for rvalues. They definitively do exist, since the cast operator
(6.5.4p2) explicitly specifies that the type could be qualified. That section on
casts also has the only indication that relates to rvalues. There is a footnote
(thus not normative) that says

> 89\) A cast does not yield an lvalue. Thus, a cast to a qualified type has the
> same effect as a cast to the unqualified version of the type.

That could mean two things:

1. the effective type of the resulting rvalue is unqualified
2. all operators that will accept the rvalue as an operand will act all the same whether the type is qualified or not

doing some tests I have found that clang and gcc disagree on this point. (gcc
doesn't have `_Generic`, yet, but other builtins to observe types)

clang seems to implement 1., gcc 2\. They agree for lvalues like this

```c
_Generic((double const){ 0 },
         default: 0,
         double const: 1)
```

both evaluate it to `1`.

They disagree on the outcome for rvalues

```c
_Generic((double const)0,
         default: 0,
         double const: 1)
```

clang gives `0`, gcc gives `1`.

(for gcc all with caution that it doesn't have `_Generic` yet, but that this was
obtained using an emulation of it by means of other gcc builtins)

So that situation can easily lead to simple programs that have a behavior that
depends on an undocumented choice and thus observe *unspecified behavior*.

### Discussion

#### Importance of observability of qualifiers

This is not a defect of the `_Generic` construct itself. The intention is
clearly to distinguish all types (with the exception of VM types) that are not
compatible, thus to allow to distinguish all 8 different forms of qualifications
of a type (resp. 16 for pointer types) that can be obtained from the qualifiers
`_Atomic`, `const`, `volatile` (and `restrict`).

For type generic expressions that are intended to operate on lvalues, such
distinction can be crucial for any of the four qualifiers:

* For `const` or `volatile` qualified lvalues there might be situations where application code might want to use an unqualified compound literal in place of the controlling expression.
* For `_Atomic` qualified lvalues there might be situations where application code might want to select a different function than for expressions with same base type but without such a qualifier.
* `restrict` (or not) qualified pointers may enable an application to select different algorithms or functions (e.g `memcopy` versus `memmove`).

#### Lvalue conversion of the controlling expression of the generic selection is not a solution

Up to now, the conversions of 6.3.2.1 do not apply to primary expressions but
only to operators. E.g in the following

```c
double A[5];
double (*B)[5] = &A;
double (*C)[5] = &(A);
```

`B` and `C` should be initialized to the same value, the address of `A`. If in
`(A)` the primary expression `()` would enforce a decay of the array to a
pointer (and thus to an rvalue) the initialization expression for `C` would be a
constraint violation.

So it seems obvious that the conversions in 6.3.2 ("Other Operands") are not
intended to be applied to primary expressions.

Also the conversions in 6.3.2 are not consistent with respect to qualifiers. The
only conversion that explicitly drops qualifiers is lvalue conversion
(6.3.2.1p2). Array to pointer conversion (6.3.2.1p3) doesn't change qualifiers
on the base type. Pointer conversion then, in 6.3.2.3, may add qualifiers to the
base type when converting.

#### Origin

Two different constructs can be at the origin of a qualification of an rvalue:

* casts, but only for scalar types
* function evaluation, resulting in any type but an array or function type.

Both constructs explicitly allow for qualifiers to be applied to the type. In
particular 6.7.6.3p15 emphasizes (and constrains) the return type of function
specifications to have compatible types, thus indicating that the qualification
of the return type bares a semantic meaning.

#### Operations

If we suppose that any rvalue expression carries its qualification further,
other operations (e.g unary or binary `+`) could or could not result in
qualified rvalues. The conversion rules in 6.3 and in particular the usual
arithmetic conversions in 6.3.1.8 that allow to determine a common real type
don't specify rules to deal with qualifiers.

It seems that a lot of compilers already warn on such "superfluous"
qualifications, but in view of type generic primary expression it is not clear
that such warnings are still adequate.

#### Comparison to C\+\+

C\+\+ had to resolve this problem since its beginnings, because the feature of
function overloading together with references of rvalues had made rvalue types
and their qualifications observable.

Interestingly, to solve the problem the C\+\+ refers to the C standard, claiming
that C would drop all qualifiers for rvalue expressions that have scalar base
type. It does this without refering to a particular text in the C standard, and
in fact it can't since there doesn't seem to be such text.

The actual solution in C\+\+ is thus that all rvalue expressions of non-scalar
types are `const`-qualified and that those of scalar types are unqualified. In
view that scalar types are exactly those types that are allowed to have cast
operators that qualify the type, all of this looks like a useless additional
complication of the issue.

### Suggested Technical Corrigendum

There doesn't seem to be an easy solution to this defect, and the proposed
solutions (as below or even differently) probably will need some discussion and
investigations about their implications on existing code before a consensus
could be reached.

#### Proposal 1: Require the implementation to specify its choice

This is (to my opinion) the worst solution, because the potential different code
paths that an application code could take are numerous. There are 4 different
qualifiers to handle and code that would have to rely on enumerating all
combinations of different generic choices can quickly become a maintenance
nightmare.

Also, implementations that chose to keep qualifiers on rvalues would have to
decide (and document) by their own what the rules would be when operators are
applied to such qualified rvalues.

#### Proposal 2: Keep all qualifiers on types of rvalue expressions

For this solution in should be then elaborated how operators handle qualifiers.
A natural way would be to accumulate qualifiers from operands with different
qualifiers.

An important issue with this approach is the rapidly increasing number of cases,
in particular 16 for pointer types. To keep the number of cases low when
programming with type generic expressions we would need a *generic* tool for the
following:

How to drop qualifiers for type generic expressions? Or alternatively add all
qualifiers?

For arithmetic types with base type other than `_Bool`, `char`, or `short`
something like the following would be useful:

```c
+(X)                                 // if unary plus drops all qualifiers
(X) + (int const volatile _Atomic)0  // if qualifiers accumulate
```

This strategy wouldn't work for the narrow types, because the are promoted to
`signed` or `unsigned`.

#### Proposal 3: Require the implementation to provide a feature test macro

This solution would already be a bit better than the previous one, since
applications that compose type generic macros could select between two (or
several) implementations. But the main problems (complexity and
underspecification of operations) would remain.

#### Proposal 4: Drop all qualifiers from the controlling expression of the generic selection

This is not an ideal solution, since it would remove a lot of expressiveness
from the generic selection construct. Lvalues could no be distinguished for
their qualifiers:

```c
void f(double*);
#define F(X) _Generic((X), double: f)(&(X))

double const A = 42;
F(A);
```

Here dropping the qualifiers of `A` would result in a choice of `f` and in the
evaluation of `f(&A)`. In case that `f` modifies its argument object (which we
can't know) this would lead to undefined behavior.

Not dropping the qualifiers would lead to a compile time constraint violation,
because none of the types in the type generic expression matches. So here an
implementation would be forced to issue a diagnostic, whereas if qualifiers are
dropped the diagnostic is not mandatory.

#### Proposal 5: Drop all qualifiers of rvalues

This solution seems the one that is chosen by clang. It is probably the easiest
to specify. As mentioned above it has the disadvantage that the two very similar
expressions `(int const){0}` and `(int const)0` have different types.

Some clarification should be added to the standard, though.

<ins>6.5.1.1, modify as follows:  
EXAMPLE The `cbrt` type-generic macro could be implemented as follows. Here the
prefix operator `+` in the selection expression ensures that lvalue conversion
on arithmetic types is performed such that e.g lvalues of type `float const`
select `cbrtf` and not the default `cbrt`.</ins>

```c
#define cbrt(X) _Generic(+(X), \
long double: cbrtl,            \
default: cbrt,                 \
float: cbrtf                   \
)(X)
```

<ins>6.5.2.2, add after p1: The type of a function call is the return type of
the function without any qualifiers.</ins>

<ins>6.5.4, add after p2: The type of a cast expression of a qualified scalar
type is the scalar type without any qualifiers.</ins>

<ins>6.7.63, change p15, first sentence: For two function types to be
compatible, the unqualified versions of both return types shall be
compatible.</ins>

**C11:** When introduced like this, this will invalidate some valid C11
programs, since some type generic expression might behave differently. The
faster such corrigendum is adopted the less likely it is that such programs
exist.

#### Proposal 6: Add a `const` qualifier to all types for rvalues

Analogous as in the case above it has the disadvantage that the two very similar
expressions `(int){0}` and `(int)0` have different types.

This is my favorite solution, since it also "repairs" another issue that I am
unconfortable with: the problem of array decay in objects with temporary
lifetime:

```c
  struct T { double a[4]; } A;
  struct T f(void) { return (struct T){ 0 }; }
  double g0(double* x) { return *x; }
  ...
  g0(f().a);
```

Here `f()` is an rvalue that results in an object of temporary lifetime `struct
T` and then `f().a` decays to a `double*`. Semantically a better solution would
be that it decays to a `double const*` since a modification of the value is not
allowed (undefined behavior). Already with C99 it would be clearer to declare
`g1` as:

```c
  double g1(double const* x) { return *x; }
```

If `f()` would be of type `struct T const`, `f().a` would decay to a `double
const*`. Then a call of `g0` would be a constraint violation and `g1` would have
to be used.

The necessary changes to the standard would be something like:

<ins>6.5.1.1, modify as follows:  
EXAMPLE The `cbrt` type-generic macro could be implemented as follows. Here the
prefix operator `+` in the selection expression ensures that lvalue conversion
on arithmetic types is performed such that e.g lvalues of type `float` select
`cbrtf` and not the default `cbrt`.</ins>

```c
#define cbrt(X) _Generic(+(X), \
long double const: cbrtl,      \
default: cbrt,                 \
float const: cbrtf             \
)(X)
```

<ins>6.5.2.2, add after p1: The type of a function call is the `const`-qualified
return type of the function without any other qualifiers.</ins>

<ins>6.5.4, add after p2: The type of a cast expression of a qualified scalar
type is the `const`-qualified scalar type without any other qualifiers.</ins>

The third addedum would be the same as in the previous case:

<ins>6.7.63, change p15, first sentence: For two function types to be
compatible, the unqualified versions of both return types shall be
compatible.</ins>

**C11:** When introduced like this, this will invalidate some valid C11
programs, since some type generic expression might behave differently. The
faster such corrigendum is adopted the less likely it is that such programs
exist.

**C99:** When introduced like this, this will invalidate some valid C99 programs
that pass rvalue pointers as presented above to function parameters that are not
`const`-qualified but where the called function then never modifies the object
of temporary lifetime behind the pointer. Unless for very old legacy functions
(from before the introduction of `const` to the language) such interfaces should
be able to use the "correct" `const`-qualification, or they could be overloaded
with a type generic interface that takes care of that issue.

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Committee Discussion

> * This paper is new enough that a thorough examination of its contents has not been made. It is not clear whether it is a DR or a proposal.
> * If implementers do not know what to do, it is a defect.
> * Handling of the atomic type qualifier may be the most likely defect, if there is one.

Apr 2013 meeting

### Committee Discussion

* The intent of the Standard is most clearly reflected in the author's Proposal 5\.
* Clark Nelson provided an in-depth analysis of Proposal 5\.
* The suggested changes to 6.5.1.1 are unnecessary. The controlling expression of a generic selection was very carefully *not* added to the list of contexts in which lvalue conversion is not done and type qualification is discarded; see 6.3.2.1p2. As such, the controlling expression of a generic selection can not have qualified type. It was thought that a note to that effect might be useful in 6.5.1.1p3.
* The suggested addition to 6.5.4 is useful, but a better change would be to change 6.5.4p5 to:
  > Preceding an expression by a parenthesized type name converts the value of the
  > expression to <ins>the unqualified version</ins> of the named type. This
  > construction is called a cast. A cast that specifies no conversion has no effect
  > on the type or value of an expression.

  Also, footnote 104 should be reduced to just its first sentence.
* The suggested changes to 6.5.2.2 and 6.7.63p15 are desirable, but a simpler change would be to remove any qualifier from the declared return type of a function. So, in 6.7.6.3p5, change to:
  > and the type specified for *ident* in the declaration "`T D`" is
  > "*derived-declarator-type-list T*", then the type specified for *ident* is
  > "*derived-declarator-type-list* function returning <ins>the unqualified version
  > of</ins> *T*".
* Atomic types may or may not be subject to distinct generic selection and this needs to be resolved.

Oct 2013 meeting

### Committee Discussion

* The committee notes that in reflector email 13037 (2013-08-13) that the issue w.r.t. atomics applies to casts, and also needs addressing. The standard was thought to be clear that during conversion to non-atomic type that any implementation size differences are resolved to the non-atomic value, and such conversions would be expected for casts. Such does not seem to be the case, however.
* Further refinement of when and where and how to express the treatment of lvalues and non-lvalues has been made. Specifically, the controlling expression of a generic selection "was very carefully not added" to the list of cases where lvalue conversion is not done.
* Specifically, change 6.5.4.p5 to:
  > Preceding an expression by a parenthesized type name converts the value of the
  > expression to the unqualified version of the named type. This construction is
  > called a cast. A cast that specifies no conversion has no effect on the type or
  > value of an expression. (and delete footnote 104\)
* Also, change 6.7.63 paragraph 5:
  > . . . then the type specified for ident is "derived-declaration-type-list
  > function returning the unqualified version of T".
* A paper has been solicited to resolve the atomic issues that would argue that type generic selection should apply distinctly to atomic types, as seems to be the direction sought by the submitter.

Apr 2014 meeting

### Committee Discussion

* The proposed resolution found in [N1803](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1803.htm) was withdrawn.
* A paper has been solicited to provide a technical corrigendum. It should reflect that the first sentence of footnote 104, "A cast does not yield an lvalue" should be kept.

Apr 2015 meeting

### Committee Discussion

> The paper [N1863](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1863.pdf)
> was provided and its Suggested Technical Suggestion was adopted.

### Proposed Technical Corrigendum

Change 6.5.4.p5 from

> Preceding an expression by a parenthesized type name converts the value of the
> expression to the named type. This construction is called a
> *cast*<sup>104</sup>. A cast that specifies no conversion has no effect on the
> type or value of an expression.
>
> 104\) A cast does not yield an lvalue. Thus, a cast to a qualified type has the
> same effect as a cast to the unqualified version of that type.

to

> Preceding an expression by a parenthesized type name converts the value of the
> expression to the unqualified version of the named type. This construction is
> called a *cast*<sup>104</sup>. A cast that specifies no conversion has no effect
> on the type or value of an expression.
>
> 104\) A cast does not yield an lvalue.

Change 6.7.6.3 p5 from

> ... then the type specified for *ident* is *“derived-declarator-type-list
> function returning T”*.

to

> ... then the type specified for *ident* is *“derived-declarator-type-list
> function returning the unqualified version of T”*.


</div>


---

---

<div id="issue0424">

## Issue 0424: underspecification of `tss_t`

Authors: WG14, Jens Gustedt  
Date: 2012-10-08  
Reference document: [N1651](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1651.htm)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0416](log_c11c17.md#issue0416)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Section 7.26.6 “Thread-specific storage functions” of C11 is severely
underspecified since it uses terms that are not introduced (so far) in the
context of C. This is really a pity, since POSIX also has `pthread_key_t` that
is completely feature equivalent and for which the specification is much more
complete.

Jacob Navia had observed that at several occasions in `comp.std.c` but it seems
that he had not got enough attention such that this had made it in a defect
report.

> The `tss_create` function creates a thread-specific storage pointer with
> destructor `dtor`, which may be null.

The main problem is that it is nowhere explained/defined

* what a destructor should be,
* when such a destructor should be called,
* in which thread context this constructor is executed
* what happens when new destructors are added while others are executed
* what the meaning of the value of `TSS_DTOR_ITERATIONS` would be.

### Suggested Technical Corrigendum

I think several paragraphs should be added after the one above:

> The effect is that for each thread that has the thread specific storage
> corresponding to `key` set to a value `x` that is not null, the destructor
> function `*dtor` is called with `dtor(x)` before the thread exits.
>
> This call to `dtor` is executed in the context of the same thread; it is
> sequenced after the `return` statement or the call to `thrd_exit` that
> terminates the thread and before any return from `thrd_join` of a waiter for
> this same thread. If there are several thread specific storages for the same
> thread their destructor functions are called in an unspecific order but with a
> sequence point between each of these function calls.
>
> If a destructor function for `key` issues calls to `tss_set`, `tss_get` or
> `tss_delete` with the same `key` the behavior is undefined.  
> `tss_set` can be used to set the value of a thread specific storage for a
> different key `key2` that had not been set before or that has been processed
> with a call to the corresponding destructor.

By that the set of thread specific storages for a given thread may change during
the execution of the corresponding destructors.

> If after processing all tss that are active at the `return` of the thread
> function or at the end of `thrd_exit` there are still tss that are active the
> procedure of calling destructors is iterated. An implementation may bind the
> maximum number such of supplementary iterations by `TSS_DTOR_ITERATIONS`.

A second problem is that there are two functionalities that are easily mixed up
and which interrelationship should be clarified: the destructor that is called
(let us suppose this) at exit of a thread, and `tss_delete` that deletes a
thread specific storage for all running threads. I think something like the
following should be added in 7.26.6.2 after para 2:

> The deletion of `key` will not change the observable behavior of any of the
> active threads. If `tss_delete` is called for `key` and there is a thread that
> has a non-null value for `key` that has passed a terminating `return` statement
> or call to `thrd_exit` but not yet finished the processing of all its tss
> destructors, the behavior is undefined.

---

Comment from WG14 on 2014-10-31:

Oct 2012 meeting

### Committee Discussion

> These issues are covered under [DR 416](log_c11c17.md#issue0416). See discussion there.

Apr 2013 meeting

### Committee Discussion

> In addition to [DR 416](log_c11c17.md#issue0416) this report suggests defining as undefined
> behavior the interaction of `thrd_exit` and `tss_delete`.

Oct 2013 meeting

### Proposed Committee Response

> The issues raised herein have been considered in conjunction with [DR
> 416](log_c11c17.md#issue0416) and are jointly resolved in that DR's Proposed Technical
> Corrigendum.


</div>


---

---

<div id="issue0425">

## Issue 0425: no specification for the access to variables with temporary lifetime

Authors: WG14, Jens Gustedt  
Date: 2012-10-08  
Reference document: [N1653](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1653.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Section 6.2.4 in p4 and p5 requires implementation defined behavior for
accessing objects with thread local or automatic storage from different threads
than where they are defined. No such mention is done for objects with *temporary
lifetime* in p8. Can they be accessed by other threads? Is this property handled
similar to the property for automatic storage duration? Or should this simply be
forbidden?

### Suggested Technical Corrigendum

Add to the end of 6.2.4 p8:

> The result of attempting to indirectly access an object with temporary lifetime
> from a thread other than the one with which the object is associated is
> implementation-defined.

Add to 7.26.1p3:

> ```c
> __STDC_THREAD_TEMPORARY_VISIBLE__
> ```
>
> which expands to 1 if objects of temporary lifetime are visible to other threads
> and to 0 otherwise.

---

Comment from WG14 on 2013-10-03:

Oct 2012 meeting

### Proposed Committee Response

> Objects with *temporary lifetime* are defined in 6.2.4 paragraph 8 to be those
> with automatic storage duration, and so inter-thread access is implementation
> defined. No change needed.


</div>


---

---

<div id="issue0426">

## Issue 0426: G.5.1: `-yv` and `-x/v` are ambiguous

Authors: WG 14, Fred J. Tydeman  
Date: 2013-01-07  
Reference document: [N1670](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1670.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The tables in G.5.1 have the mathematical formulas -yv and -x/v. I believe that
they are ambiguous as they could have two meanings:

* (-y)/v and (-x)/v
* -(y/v) and -(x/v)

I believe it matters for at least these cases:

1. The two operands are different NaNs, negate flips the sign of a NaN, and the result of \* and / depends upon the sign and value of the NaN.
2. The result is a NaN from non-NaN operands, negate does not flip the sign of a NaN, while both \* and / set the sign of the result as the XOR of the signs of the operands.
3. All operands are non-NaN, the result is inexact and non-NaN, and a rounding that is not symmetric about zero is in effect.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* The committee sees the mathematical formulae as unambiguous since the regroupings presented in the paper are mathematically equivalent, and should not be construed as C expressions. As such, there was considerable skepticism expressed that this was indeed a defect.
* The author promised to provide a supplemental paper that would substantiate his concern about this as a defect.

Oct 2013 meeting

### Committee Discussion

* [N1738](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1738.htm) clarifies a typo in the original document.
* A very long discussion ensued, starting with the fact that C11 notation was used in the clarifying example rather than mathematical notation.
* The concerns raised about `NaNs` were deemed moot by the fact that multiply and divide are not required by either C11 or IEEE-754 to honor the sign of `NaNs`.
* The intended mathematical result seems obvious to most on the committee, and the arguments about mathematical notations were not persuasive.
* The third case, however, has modest merit if one considers an implementation that transcribes the provided notation into C11 directly, in which case when asymmetric rounding mode is selected an incorrect result will be formed if negation is applied after the division (or multiplication). More exactly, in the third case, all operands are non-Nan, the result is inexact and non-NaN, and a rounding that is not symmetric about zero is in effect.
* As such, the committee, with great reluctance, narrowly formed a consensus for change, and is concerned that this issue is almost certainly not significant enough to warrant the effort already expended, let alone further discussion, lest the entire matter be returned with no changes proposed as a Record of Response.

### Proposed Technical Corrigendum

> In the table in G.5.1 #2, change
>
> > -yv
>
> to
>
> > (-y)v
>
> in three places.
>
> In the table in G.5.1 #3, change
>
> > -x/v
>
> to
>
> > (-x)/v
>
> in two places.


</div>


---

---

<div id="issue0427">

## Issue 0427: Function Parameter and Return Value Assignments

Authors: WG 14, Shao Miller \<sha0.miller@gmail.com\>  
Date: 2013-01-24  
Reference document: [N1671](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1671.htm)  
Status: Closed  
Cross-references: [0423](log_c11c17.md#issue0423), [0454](log_c11c17.md#issue0454)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The wording for the the assignments of function arguments to function parameters
and for the assignment of a `return` statement's expression to the value of the
function call can potentially be confused.

6.5.2.2p2:

> If the expression that denotes the called function has a type that includes a
> prototype, the number of arguments shall agree with the number of parameters.
> Each argument shall have a type such that its value may be assigned to an object
> with the unqualified version of the type of its corresponding parameter.

The appearance of "may be assigned" can lead to the question (#1) of whether or
not the constraints and semantics under both 6.5.16 and 6.5.16.1 might apply.
The **Forward references** indicate 6.5.16.1, so this question might be
unwarranted.

The appearance of "unqualified version of the type of its corresponding
parameter" does not match 6.9.1p10, which doesn't use "unqualified" (see below).

6.5.16p2:

> An assignment operator shall have a modifiable lvalue as its left operand.

If 6.5.2.2p2's mention of "assigned" implies this constraint as a secondary
constraint, it is not clear which "modifiable lvalue" or even "lvalue" would
ever satisfy the constraint. The "modifiable lvalue" does not appear to be the
parameter, because:

* the mention of "unqualified version" suggests a theoretical object, while the parameter might be `const`-qualified, or
* the parameter might have an unqualified structure or union type having at least one `const`-qualified member (possibly via recursion)

6.7.3p4:

> The properties associated with qualified types are meaningful only for
> expressions that are lvalues.132)
>
> 132\) The implementation may place a const object that is not volatile in a
> read-only region of storage. Moreover, the implementation need not allocate
> storage for such an object if its address is never used.

This can suggest that 6.5.2.2p2's "an object with the unqualified version of the
type" implies an lvalue, but (question #2) is it a modifiable lvalue? Question
#3: If the type is a structure or union type with a `const`-qualified member
(possibly via recursion), are the members considered to be unqualified, too? If
so, this is an important difference from pointer types where the referenced type
(or its referenced type, recursively) would not be considered unqualified. Also
worth consideration would be an array object (which is not qualified) having
elements matching such a structure or union type (possibly via recursion).

The return type of a function might be `const`-qualified, or might be a
structure or union type having such a member (possibly via recursion). Question
#4: Should the return type of a function be adjusted to be an unqualified
version of the type? Such an adjustment might have implications for type
compatibility and composite type and might be better off left alone. (`const` is
being used for illustrative purposes, but all type qualifiers can equally be
considerations.)

6.8.6.4p3:

> If a return statement with an expression is executed, the value of the
> expression is returned to the caller as the value of the function call
> expression. If the expression has a type different from the return type of the
> function in which it appears, the value is converted as if by assignment to an
> object having the return type of the function.160)
>
> 160\) The return statement is not an assignment. The overlap restriction of
> subclause 6.5.16.1 does not apply to the case of function return. The
> representation of floating-point values may have wider range or precision than
> implied by the type; a cast may be used to remove this extra range and
> precision.

If the return type of a function is `const`-qualified, or is a structure or
union type having such a member (possibly via recursion), then "as if by
assignment" works for 6.5.16.1, but the constraint of 6.5.16p2 requires a
"modifiable lvalue".

The footnote reminds us that a `return` statement with an expression is not an
assignment, but it is not clear that only 6.5.16.1 applies for the "as if by
assignment" case.

6.9.1p10:

> On entry to the function, the size expressions of each variably modified
> parameter are evaluated and the value of each argument expression is converted
> to the type of the corresponding parameter as if by assignment. (Array
> expressions and function designators as arguments were converted to pointers
> before the call.)

6.9.1p11:

> After all parameters have been assigned, the compound statement that constitutes
> the body of the function definition is executed.

A `const`-qualified lvalue cannot normally be assigned-to. An lvalue for an
object having a structure or union type containing a `const`-qualified member
(possible via recursion) cannot normally be assigned-to.

6.9.1p10 doesn't match the use of "unqualified" in 6.5.2.2p2 (see above).

### Suggested Technical Corrigendum

**Sun c99** and **GCC** disagree on the `return` statement's semantics.

Change 6.5.2.2p2 to:

> If the expression that denotes the called function has a type that includes a
> prototype, the number of arguments shall agree with the number of parameters.
> Each argument shall be such that it satifies the constraints of simple
> assignment when considering the argument to be the right operand and considering
> the left operand to have the unqualified version of the type of the
> corresponding parameter.

(Loosely establishes an example for "as if by simple assignment".)

Change 6.8.6.4p3 to:

> If a return statement with an expression is executed, the value of the
> expression is returned to the caller as the value of the function call
> expression. If the expression has a type different from the return type of the
> function in which it appears, the value is converted as if by simple assignment
> to an object having the unqualified version of the return type of the
> function.160)

Change 6.9.1p10 to:

> On entry to the function, the size expressions of each variably modified
> parameter are evaluated in an unspecified order, the value of each argument
> expression is converted to the unqualified version of the type of the
> corresponding parameter as if by simple assignment, then each converted value
> becomes the initial value for the corresponding parameter. (Array expressions
> and function designators as arguments were converted to pointers before the
> call.)

Change 6.9.1p11 to:

> After all parameters have initial values, the compound statement that
> constitutes the body of the function definition is executed.

Add bullet to J.1

> \- The order in which the size expressions of variably modified parameters are
> evaluated upon function entry (6.9.1).

---

Comment from WG14 on 2016-10-21:

Apr 2013 meeting

### Committee Discussion

* No one on the committee understood the problem that this paper was trying to discuss.
* In particular, the actual difference in behavior referenced between Sun c99 and GCC is not elaborated upon.
* The committee will solicit further input from the author.

Oct 2013 meeting

* As a result of further correspondence with the author, a proposed resolution was made on the WG14 reflector in message 13024 and refined in 13035\.
* The defect is that the initial values of parameters to function calls are specified in the standard in terms of assignment instead of initialization, such that `const` and aggregates containing `const` would be excluded since they cannot be the subject of assignments!
* A Suggested Technical Corrigendum was composed, and follows. It is not yet a Proposed Technical Corrigendum due to the following unresolved discussion points.
* In 6.5.2.2p2 change:

  If the expression that denotes the called function has a type that includes a
  prototype, the number of arguments shall agree with the number of parameters.
  Each argument shall have a type such that its value may be assigned to an object
  with the unqualified version of the type of its corresponding parameter.

  to

  If the expression that denotes the called function has a type that includes a
  prototype, the number of arguments shall agree with the number of parameters.
  Each argument shall have a type such that its value may be used to initialize an
  object having the type of its corresponding parameter.

  In 6.5.2.2p4 change

  An argument may be an expression of any complete object type. In preparing for
  the call to a function, the arguments are evaluated, and each parameter is
  assigned to the value of the corresponding argument.

  to

  An argument may be an expression of any complete object type. In preparing for
  the call to a function, the arguments are evaluated, and each parameter is
  initialized to the value of the corresponding argument.
* It is not clear yet whether there are issues around conversions with respect to this change since this is actual practice that we are intending to simply reflect and to not introduce new constraints.
* This change might be augmented by a new example along the lines of, say, 6.5.16.1 example 3\.

Apr 2014 meeting

### Committee Discussion

> The issue of conversion has to do with whether there are differing promotions
> and type conversions that would apply when constructing an argument list that
> would not occur if these expressions were used as initializers in a declaration.

Oct 2014 meeting

### Committee Discussion

> The committee concluded after a discussion that there were no promotion or type
> conversion issues raised by the proposed wording above, and that the following
> should be adopted as a Proposed Technical Corrigendum.

### Proposed Technical Corrigendum (superceded)

In 6.5.2.2p2 change:

> If the expression that denotes the called function has a type that includes a
> prototype, the number of arguments shall agree with the number of parameters.
> Each argument shall have a type such that its value may be assigned to an object
> with the unqualified version of the type of its corresponding parameter.

to

> If the expression that denotes the called function has a type that includes a
> prototype, the number of arguments shall agree with the number of parameters.
> Each argument shall have a type such that its value may be used to initialize an
> object having the type of its corresponding parameter.

In 6.5.2.2p4 change

> An argument may be an expression of any complete object type. In preparing for
> the call to a function, the arguments are evaluated, and each parameter is
> assigned the value of the corresponding argument.

to

> An argument may be an expression of any complete object type. In preparing for
> the call to a function, the arguments are evaluated, and each parameter is
> initialized to the value of the corresponding argument.

Apr 2015 meeting

### Committee Discussion

> The goal of preserving conversions as if by assignment is fulfilled by the
> definition of initialization found in **6.7.9 Initialization** paragraph 11\.
> Another instance of assignment that should be changed was found in **6.9.1
> Function Definitions** paragraph 11\.
>
> It was noted that implicit conversion is described only in terms of assignment
> (6.5.16.1). There was broad agreement that committee members and implementors
> are unconfused by the intent of the standard here despite the inconsistencies.
> It was also noted that initialization is distinct from assignment and, in the
> case of non-lock free atomic implications, this requires operational differences
> and as such that it is worth further consideration. As such, the following
> should be regarded as a possible direction.
>
> In 6.5.2.2p2 change:
>
> > If the expression that denotes the called function has a type that includes a
> > prototype, the number of arguments shall agree with the number of parameters.
> > Each argument shall have a type such that its value may be assigned to an object
> > with the unqualified version of the type of its corresponding parameter.
>
> to
>
> > If the expression that denotes the called function has a type that includes a
> > prototype, the number of arguments shall agree with the number of parameters.
> > Each argument shall have a type such that its value may be used to initialize an
> > object having the type of its corresponding parameter.
>
> In 6.5.2.2p4 change
>
> > An argument may be an expression of any complete object type. In preparing for
> > the call to a function, the arguments are evaluated, and each parameter is
> > assigned the value of the corresponding argument.
>
> to
>
> > An argument may be an expression of any complete object type. In preparing for
> > the call to a function, the arguments are evaluated, and each parameter is
> > initialized to the value of the corresponding argument.
>
> In 6.9.1 paragraph 11 change:
>
> > After all parameters have been assigned,
>
> to
>
> > After all parameters have been initialized,

Oct 2015 meeting

### Committee Discussion

* The committee no longer believes that any of the issues raised in this report warrant changes to the standard.
* The difference in behavior on return value semantics cited in gcc has been resolved by a bug fix to gcc
* Qualifiers on the return type of a function are superfluous since by resolution to [DR 423](log_c11c17.md#issue0423) the committee affirms that qualifiers are dropped as part of the evaluation of expressions including function calls.
* The committee does agree that the use of “assignment” to describe the initialization of function parameters can be misleading, but that in fact there is not an implementation that has ever been misled. Careful reading of the Standard notes that initialization is described fundamentally “as if by assignment”, and that it would take a comprehensive review and edit of the Standard to possibly achieve a more consistent treatment of the topics. There is a danger of circularity that must be avoided as well.

### Proposed Committee Response

> The committee believes that the primary issue of return value semantics was a
> consequence of a mistake in the implementation of `gcc` which has been
> rectified, and that further the treatment of qualifiers has been clarified in
> the Proposed Technical Corrigendum of [DR 423](log_c11c17.md#issue0423). The treatment of
> initialization in the Standard is clear enough that no errors have been observed
> in implementations, and as such further clarification is unwarranted at this
> time.


</div>


---

---

<div id="issue0428">

## Issue 0428: runtime-constraint issue with sprintf family of routines in Annex K

Authors: WG 14, Douglas Walls  
Date: 2013-02-11  
Reference document: [N1672](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1672.htm)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0433](log_c11c17.md#issue0433)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

snprintf\_s  (Annex K.3.5.3.5)  

In the "Runtime-constraints" section, K.3.5.3.5p2 first sentence it says:  

"Neither s nor format shall be a null pointer. n shall neither equal  
zero nor be greater than RSIZE\_MAX."  

So,

```c
    if (n == 0 || n > RSIZE_MAX)
        /* runtime constraints violation */
```

This is clear. However the next paragraph K.3.5.3.5p3, says this about "s":  

"If there is a runtime-constraint violation, then if s is not a null  
pointer and n is greater than zero and less than RSIZE\_MAX, then the  
snprintf\_s function sets s\[0\] to the null character."  

So, it takes action when (n \< RSIZE\_MAX)

```c
        if (s != NULL && n > 0 && n < RSIZE_MAX)
            s[0] = '\0';
```

Question here is, what if n equals RSIZE\_MAX? Should we still reset  
s\[0\]?  

If I were to say this looks like a typo, would WG14 agree with me?  

That is the text of K.3.5.3.5p3 should be:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  snprintf\_s function sets s\[0\] to the null character.  
    
This issue applies to all the sprintf family of routines in Annex K

### Suggested Technical Corrigendum

snprintf\_s  
Replace K.3.5.3.5p3 with:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  snprintf\_s function sets s\[0\] to the null character.  

sprintf\_s  
Replace K.3.5.3.6p3 with:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  sprintf\_s function sets s\[0\] to the null character.  

vsnprintf\_s  
Replace K.3.5.3.12p3 with:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  vsnprintf\_s function sets s\[0\] to the null character.  

vsprintf\_s  
Replace K.3.5.3.13p3 with:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  vsprintf\_s function sets s\[0\] to the null character.

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* The committee agrees with the assessment and the suggested changes.
* There are, however, other places where similar changes are needed.

Oct 2013 meeting

### Committee Discussion

* Further investigation confirmed that there were several other functions that also need similar corrections to their runtime constraints. All of these additional functions also need additional corrections as specified in [DR433,](log_c11c17.md#issue0433) and the full resolution of both this defect and the additional issue will be found in the Proposed Technical Corrigendum of [DR433.](log_c11c17.md#issue0433)
* That list is:
  + K.3.9.1.3 The snwprintf\_s function
  + K.3.9.1.4 The swprintf\_s function
  + K.3.9.1.8 The vsnwprintf\_s function
  + K.3.9.1.9 The vswprintf\_s function
  + K.3.9.3.2.1 The mbsrtowcs\_s function
  + K.3.9.3.2.2 The wcsrtombs\_s function
* It is noted that with these changes that K.3.5.1.2 `tmpname_s` will have wording inconsistent with respect to these modifications.
* Consistent wording would be, in K.3.5.1.2p2 replace "less than or equal to RSIZE\_MAX" with "not greater than RSIZE\_MAX".
* As such, the committee continues to accept unchanged the Proposed Technical Corrigendum as partial fulfillment of this defect, and that full resolution of the other similar defects will be found in [DR433.](log_c11c17.md#issue0433)

### Proposed Technical Corrigendum

snprintf\_s  
Replace K.3.5.3.5p3 with:  

If there is a runtime-constraint violation, then if s is not a null   pointer
and n is greater than zero and not greater than RSIZE\_MAX, then the  
snprintf\_s function sets s\[0\] to the null character.

sprintf\_s  
Replace K.3.5.3.6p3 with:  

If there is a runtime-constraint violation, then if s is not a null pointer and
n is greater than zero and not greater than RSIZE\_MAX, then the sprintf\_s
function sets s\[0\] to the null character.

vsnprintf\_s  
Replace K.3.5.3.12p3 with:  

If there is a runtime-constraint violation, then if s is not a null pointer and
n is greater than zero and not greater than RSIZE\_MAX, then the   vsnprintf\_s
function sets s\[0\] to the null character.

vsprintf\_s  
Replace K.3.5.3.13p3 with:  

If there is a runtime-constraint violation, then if s is not a null   pointer
and n is greater than zero and not greater than RSIZE\_MAX, then the  
vsprintf\_s function sets s\[0\] to the null character.


</div>


---

---

<div id="issue0429">

## Issue 0429: Should `gets_s` discard next input line when `(s == NULL)` ?

Authors: WG 14, Douglas Walls  
Date: 2013-02-11  
Reference document: [N1673](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1673.htm) [N1748](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1748.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

gets\_s Annex K.3.5.4.1p2 says:  

"If there is a runtime-constraint violation, s\[0\] is set to the null  
character, and characters are read and discarded from stdin until a  
new-line character is read, or end-of-file or a read error occurs."  

The runtime-constraint violation here can be caused by a null "s"  
pointer.  Should we discard the next input line even if `(s == NULL)` ?  

The way it is written, it looks like the answer is yes.  However it is  
not clear to us that that was the intent.  Note also that s\[0\] cannot be  
set to the null character when `s==NULL`.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* The issue is found in Annex K.3.5.4.1p3, not p2.
* The Microsoft implementation appears to treat this as a runtime-constraint violation.
* The Dikumware implementation leaves this behavior unspecified.

Oct 2013 meeting

### Committee Discussion

* Given that footnote 404 already provides guidance on this issue, the author and the committee agree that the answer to the question posed is indeed yes.
* The other issue with respect to `s[0]` cannot be set to the null character when `s==NULL` has been determined to be resolved by the following changes.

### Proposed Technical Corrigendum

In Annex K.3.5.4.1, replace paragraph 3 with the following:

> If there is a runtime-constraint violation, characters are read and discarded
> from `stdin` until a new-line character is read, or end-of-file or a read error
> occurs, and if `s` is not a null pointer `s[0]` is set to the null character.


</div>


---

---

<div id="issue0430">

## Issue 0430: `getenv_s`, `maxsize` should be allowed to be zero

Authors: WG 14, Douglas Walls  
Date: 2013-02-11  
Reference document: [N1674](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1674.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

getenv\_s, Annex K.3.6.2.1p2 under Runtime-constraints says:  

  **name** shall not be a null pointer. **maxsize** shall neither equal zero nor
be greater than  
  **RSIZE\_MAX**. If **maxsize** is not equal to zero, then **value** shall not
be a null pointer.  

Question here is, if maxsize really cannot be 0\.  If it cannot be  
zero, why does the 2nd sentence mention the condition that `(maxsize != 0)`?  

If maxsize can be 0, it would allow the value to be a null pointer  
which allows what is described in 6.6.2.1 of TR24731 (N1173) cleanly:  

  The **getenv\_s** function can also be used to get the size needed to  
  represent the result. This allows the programmer to first call  
  **getenv\_s** to get the size, then allocate a buffer to hold the result,  
  and then call **getenv\_s** again to actually obtain the result."  

if maxsize can be zero, then I think we would get the length of string thusly:

```c
    getenv_s(&len, NULL, 0, "HOME");
```

However, since maxsize cannot be 0 which also requires value not to be  
a null pointer, we would need to do something like this:

```c
    getenv_s(&len, something, 1, "HOME");
```

AFAICT, getnenv\_s as specified in C11 exactly matches what was in TR24731
(N1172).  
What is in TR24731 (N1172) does not coincide with what is in the rational  
for TR24731 (N1173).  The wording in TR24731 (N1172) (and by extension  
C11) is awkward and it certainly looks like an update intended to correspond to  
the rational for TR24731 (N1173) was either misapplied or not applied.

### Suggested Technical Corrigendum

Replace Annex K.3.6.2.1p2 second sentence with:  

**maxsize** shall not be greater than **RSIZE\_MAX**.  

K.3.6.2.1p2 would then read thusly:  

**name** shall not be a null pointer.  **maxsize** shall not be greater than  
**RSIZE\_MAX**.  If **maxsize** is not equal to zero, then **value** shall not
be a null pointer.

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* The proposed change seems appropriate and is consistent with the existing rationale.
* The committee notes that some implementations may need to change to avoid treating a value of zero for **maxsize** as a constraint violation.

### Proposed Technical Corrigendum

Replace Annex K.3.6.2.1p2 second sentence with:  

**maxsize** shall not be greater than **RSIZE\_MAX**.  

K.3.6.2.1p2 would then read thusly:  

**name** shall not be a null pointer.  **maxsize** shall not be greater than  
**RSIZE\_MAX**.  If **maxsize** is not equal to zero, then **value** shall not
be a null pointer.


</div>


---

---

<div id="issue0431">

## Issue 0431: `atomic_compare_exchange`: What does it mean to say two structs compare equal?

Authors: WG14, Douglas Walls  
Date: 2013-02-21  
Reference document: [N1675](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1675.htm)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0423](log_c11c17.md#issue0423), [0474](log_c11c17.md#issue0474)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

7.17.7.4 The atomic\_compare\_exchange generic functions  

7.17.7.4p2 Description  

  Atomically, compares the value pointed to by **object** for equality with  
  that in **expected**, and if true, replaces the value pointed to by **object**  
  with **desired**, and if false, updates the value in expected with the  
  value pointed to by **object**.  

When **object** is an atomic struct type and **expected** is the corresponding  
non-atomic struct type.  What does it mean to compare two struct types  
as equal?  

Where does the C standard define what it means for two objects of struct  
type to be equal?  

7.17.7.4 NOTE 1 gives an example using memcmp on how the test for  
equality might be defined.  But that is non-normative.  

But the padding bytes in a struct have unspecified values (6.2.6.1p6)  

7.24.4.1 The memcmp function, footnote 310 reminds us that the contents  
of padding in a struct is indeterminate.  

Even integers can have padding bits, whose values are unspecified (6.2.6.2p1)  

A similar issue probably occurs for Atomic union types.

### Suggested Technical Corrigendum

Either define equality of objects of struct type, add a restriction disallowing  
use of atomic structs as arguments for the atomic\_compare\_exchange generic
functions,  
or note that atomic\_compare\_exchange generic functions for objects of atomic  
struct type results in undefined behavior.

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* There is no sentiment to define equality for structs.
* 7.17.6 lists atomic types required to have the same size and alignment as the corresponding direct type. Other atomic types may have differing size and alignment as per 6.2.5p27.
* 6.5.2.3p5 states that any access to an atomic struct or union member is undefined behavior and as such so would atomic\_compare\_exchange since it requires access.

Oct 2013 meeting

### Committee Discussion

* There are several points that need addressing.
* The original intention of the atomics design was to allow `memcmp` and `memcpy` (with suitable synchronization) be a common implementation for all \_Atomic objects.
* This practice, however, would lead to undefined behavior for implementations that have padding bits for integer representations.
* For implementations that choose larger representations for some \_Atomic types, there would need to be at least one larger type specific implementation of `atomic_compare_exchange` compared to what might be possible to implement in common for all types. This seems to imply that an implementation must supply something akin to a type generic implementation of `atomic_compare_exchange`. Type generic macros as applied to \_Atomic is the subject of [DR423.](log_c11c17.md#issue0423)
* A proposal to address these issues has been solicited.

Apr 2014 meeting

### Committee Discussion

* The proposed resolution from [N1803](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1803.htm) was withdrawn since there are implementations choosing to represent atomic non-lock-free types with extra state and hence a larger size.
* Structure compare will result in undefined behavior.
* A new paper to address this DR has been solicited

Oct 2014 meeting

### Committee Discussion

> As requested, the paper
> [N1864](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1864.htm) was written
> and provided. From our C\+\+ liaison, however, it was learned that corresponding
> behavior is well defined and is in use. Further investigation revealed that
> `atomic_compare_exchange` in C\+\+ is and has been explicitly defined to be that
> of bit comparison. C11 defines it as value comparison.
>
> It was noted that bit comparison for atomic bool would not give the expected
> answer if differing non-zero "true" values were compared. It was also noted that
> bit comparison exposes padding bits, whereas lock bits would be required to be
> discarded, leading to code that might work on one implementation of an
> architecture but fail on another.
>
> A new paper was solicited.

Apr 2015 meeting

### Committee Discussion

> The paper [N1906](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1906.htm)
> was provided and discussed and its Proposed Technical Corrigendum was adopted.
> This resolution clarifies that

### Proposed Committee Response

> `atomic_compare_exchange` is now aligned with C\+\+11 as operating on bit
> representations. Where these representations are unpadded integer or structure
> values, the operation is well defined. The type `bool` is padded in many
> implementations.

### Proposed Technical Corrigendum

In 7.17.7.4p2 replace

> Atomically, compares the value pointed to by **object** for equality with that
> in **expected**, and if true, replaces the value pointed to by **object** with
> **desired**, and if false, updates the value in **expected** with the value
> pointed to by **object**

with:

> Atomically, compares the contents of the memory pointed to by **object** for
> equality with that in **expected**, and if true, replaces the contents of the
> memory pointed to by **object** with **desired**, and if false, updates the
> value in **expected** with the value pointed to by **object**.


</div>


---

---

<div id="issue0432">

## Issue 0432: Is `0.0` required to be a representable value?

Authors: WG 14, Fred J. Tydeman (USA)  
Date: 2013-03-07  
Reference document: [N1677](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1677.htm)  
Status: Closed  
Cross-references: [0467](log_c11c17.md#issue0467)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

There are many places in C11 that assume a floating-point zero value, e.g., 0.0,
is representable.

* 6.3.1.7 Real and complex #1 has:
  > When a value of real type is converted to a complex type, the real part of the
  > complex result value is determined by the rules of conversion to the
  > corresponding real type and the imaginary part of the complex result value is a
  > positive zero or an unsigned zero.
* 6.7.9 Initialization, #10 (second bullet) has (for static and thread storage initialzation):
  > if it has arithmetic type, it is initialized to (positive or unsigned) zero;
* 7.22.1.3 The strtod, strtof, and strtold functions, #10 has:
  > If no conversion could be performed, zero is returned.
* 7.29.4.1.1 The wcstod, wcstof, and wcstold functions, #10 has:
  > If no conversion could be performed, zero is returned.
* Annex F and Annex G, being based upon IEEE-754, require signed floating-point zeros.

There are many places in C11 that allow for a representable floating-point zero
value.

* 5.2.4.2.2 Characteristics of floating types \<float.h\> #4 has:
  > An implementation may give zero and values that are not floating-point numbers
  > (such as infinities and NaNs) a sign or may leave them unsigned.
* 7.3.3 Branch cuts, #1 and #2 talk about signed zeros.
* 7.6 Floating-point environment \<fenv.h\>, #6, lists **FE\_DIVBYZERO** (divide-by-zero) as a possible floating-point exception. And, 7.12.1 Treatment of error conditions gives more details.
* 7.12 Mathematics \<math.h\> #6 says that zero, subnormal, normal, NaN, and infinite are mutually exclusive kinds of floating-point values. And 7.12.3.1 The fpclassify macro uses those classification macros.
* 7.12.3.2 The isfinite macro, #2 says that zero is a finite value.
* 7.12.3.5 The isnormal macro, #2 says that zero is not a normal value.
* 7.12.\*; many of the math functions (atan2, frexp, ilogb, log, log10, log2, logb, pow, lgamma, tgamma, fmod, remainder, remquo, copysign) mention zero as special cases.

The C Rationale in its discussion of 5.2.4.2.2 has:

> Note that the floating-point model adopted permits all common representations,
> including sign-magnitude and two's-complement, but precludes a logarithmic
> implementation.
>
> The C89 Committee also endeavored to accommodate the IEEE 754 floating-point
> standard by not adopting any constraints on floating-point which were contrary
> to that standard.

However, if one carefully reads 5.2.4.2.2 Characteristics of floating types
\<float.h\>, #2 and #3, one finds that zero is not required to be representable.
As I read those paragraphs, normalized floating-point numbers are the only
things required to be contained in floating types. Subnormal floating-point
numbers, unnormalized floating-point numbers, infinities, and NaNs are
additional (optional) things that may be contained in floating types. Zero is
not mentioned explicitly.

So, it appears that some parts of C11 require that floating-point zeros be
representable, while other parts do not require that they be representable.

I think that the first sentance in 5.2.4.2.2 #3 should be changed to:

> Floating types shall be able to represent normalized floating-point numbers
> (f<sub>1</sub> \> 0 if x !\= 0\) and (positive or unsigned) zero. In addition,
> floating types may be able to contain other kinds of floating-point numbers,
> such as negative zero and subnormal ...

---

Comment from WG14 on 2018-10-18:

Apr 2013 meeting

### Committee Discussion

* The committee agrees that the standard is missing an explicit requirement for floating point zero.
* There is no need for the clause **if x !\= 0**.

### Proposed Change

The first sentance in 5.2.4.2.2 #3 should be changed to:

> Floating types shall be able to represent normalized floating-point numbers
> (f<sub>1</sub> \> 0\) and (positive or unsigned) zero. In addition, floating
> types may be able to contain other kinds of floating-point numbers, such as
> negative zero and subnormal ...

Apr 2017 meeting

### Committee Discussion

This is a necessary but not sufficient change to address the problem, and as
such, it was considered more dangerous to have than to have not, and was
reopened. Combining this PTC with that of [**<ins>DR 467</ins>**](log_c11c17.md#issue0467)
should resolve the issue completely.

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that this proposed change and that from [CR 467](log_c11c17.md#issue0467) be
> combined in a new paper to completely resolve this issue.


</div>


---

---

<div id="issue0433">

## Issue 0433: Issue with constraints for wide character function arguments involving **RSIZE\_MAX**

Authors: WG 14, Douglas Walls  
Date: 2013-03-12  
Reference document: [N1683](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1683.htm) [N1771](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1771.htm)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0428](log_c11c17.md#issue0428)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

**K.3.7.2.2 The strncat\_s function**  
The **strncat\_s()** has a constraint that neither **s1max** nor **n** shall be
greater than **RSIZE\_MAX.**  
Both s1max and n are defined as representing a number of char sized characters.  

**K.3.9.2.1.2 The wcsncpy\_s function**  
The same constraint is given for the function the **wcsncat\_s()** function,
i.e. that neither **s1max** nor **n** shall be greater than **RSIZE\_MAX**.  For
**wcsncat\_s(), s1max** and **n** are defined as representing a number of
**wchar\_t** sized characters.  On most implementations the size of a wide
characters is many times the size of a char.  On Solaris it is 4 time the size.   

**K.3.4 Integer types \<stdint.h\>** is defined as follows  
1 The header **\<stdint.h\>** defines a macro.  
2 The macro is  

      **RSIZE\_MAX**  

which expands to a value 386\) of type **size\_t**. Functions that have
parameters of type **rsize\_t** consider it a runtime-constraint violation if
the values of those parameters are greater than **RSIZE\_MAX**.  

386\) The macro **RSIZE\_MAX** need not expand to a constant expression.  

**Recommended practice**  

3 Extremely large object sizes are frequently a sign that an object's size was
calculated incorrectly. For example, negative numbers appear as very large
positive numbers when converted to an unsigned type like size\_t. Also, some
implementations do not support objects as large as the maximum value that can be
represented by type size\_t.  

4 For those reasons, it is sometimes beneficial to restrict the range of object
sizes to detect programming errors. For implementations targeting machines with
large address spaces, it is recommended that **RSIZE\_MAX** be defined as the
smaller of the size of the largest object supported or **(SIZE\_MAX \>\> 1\)**,
even if this limit is smaller than the size of some legitimate, but very large,
objects. Implementations targeting machines with small address spaces may wish
to define **RSIZE\_MAX** as **SIZE\_MAX**, which means that there is no object
size that is considered a runtime-constraint violation.

---

The recommended practice implies **RSIZE\_MAX** represents maximum object sizes.  

Footnote 386\) implies an implementation can adjust what **RSIZE\_MAX** expands
to depending upon the context in which it is being used.  But what I don't
understand is how, the user can take advantage of **RSIZE\_MAX** to check the
values of n and s1max prior to calling the function **wcsncpy\_s** in order to
avoid violating the runtime constraint error.  There is no context in which the
implementation can expand **RSIZE\_MAX** to the value they need.  

Example:

```c
  if ((s1max <= RSIZE_MAX) & (n <= RSIZE_MAX))
     error = wcsncpy_s (s1, s1max, s2 n);  // Assume no other runtime constraints
     if (error != 0) {
        // Since RSIZE_MAX is not a constant expression
        // Can this ever occur due to s1max or n being greater than RSIZE_MAX?
     }
  }
```

Is a conforming implementation allowed  to return a non-zero value for
**wcsncpy\_s()** in the example above?  

N1147 the Rationale for TR24731 explains implementations might wish to adjust
the value of **RSIZE\_MAX** dynamically, and gives several scenarios for doing
so. None of which seem germane to the questions raised here.

---

So what is the purpose of providing the macro **RSIZE\_MAX**?  
If the purpose is to limit all buffer sizes to **RSIZE\_MAX**, it's use in
constraints for wide character functions appear to be malformed.  

The definitions of **wcsncpy\_s()** and **strncat\_s()** have constraints that
treat their arguments that represent character counts as if those counts
represent the size of an object that can be tested against **RSIZE\_MAX** in the
same way.  But those character counts represent characters of very different
sizes.  And thus very different object sizes.  Maybe the constraint error for
**wcsncpy\_s()** arguments **smax1** and **n** should be rewritten as something
like:  

  Neither **(s1max \* sizeof(wchar\_t))** nor **(n \* sizeof(wchar\_t))** shall
be greater than **RSIZE\_MAX**.  

Other functions where max argument represent the number of  
wchar\_t or multi-byte characters and may need similar changes  
include:  

**mbstowcs\_s  
wcstombs\_s  
snwprintf\_s  
swprintf\_s  
swscanf\_s  
vsnwprintf\_s  
vswprintf\_s  
wcscpy\_s  
wcsncpy\_s  
wmemcpy\_s  
wmemmove\_s  
wcscat\_s  
wcstok\_s  
wcrtomb\_s  
mbsrtowcs\_s  
wcsrtombs\_s**

### Suggested Technical Corrigendum

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* RSIZE\_MAX is intended to be the maximum size, in bytes, permitted by an implementation for an object.
* The constraints for wide character functions appear to be incorrect.
* For example, K.3.9.2.1.2p8 second sentence should read something like "Neither s1max\*sizeof(wchar\_t) nor n\*sizeof(wchar\_t) shall be greater than RSIZE\_MAX."

Oct 2013 meeting

### Committee Discussion

* The list of functions cited was not entirely correct, and upon further review the Suggested Technical Corrigendum from [N1771](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1771.htm) were adopted.
* These changes also address, where noted, the defect reported in [DR428.](log_c11c17.md#issue0428)

Apr 2014 meeting

### Committee Discussion

> A "nor nor" typo in the Suggested Technical Corrigendum for K.3.9.3.2.2p12 was
> noticed and corrected in the Proposed Technical Corrigendum below.

### Proposed Technical Corrigendum

K.3.6.5.1 The mbstowcs\_s function  

In K.3.6.5.1p2, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.6.5.1p3, replace "less than RSIZE\_MAX" with "not greater than
RSIZE\_MAX/sizeof(wchar\_t)".  

K.3.6.5.2 The wcstombs\_s function  

In K.3.6.5.2p2, replace "then neither len nor dstmax shall be greater than
RSIZE\_MAX" with  
"then neither len shall be greater than RSIZE\_MAX/sizeof(wchar\_t) nor dstmax
shall be greater than RSIZE\_MAX".  
In K.3.6.5.2p3, replace "less than RSIZE\_MAX" with "not greater than
RSIZE\_MAX".  

K.3.9.1.3 The snwprintf\_s function  

In K.3.9.1.3p2, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.1.3p3, replace "less than RSIZE\_MAX" with "not greater than
RSIZE\_MAX/sizeof(wchar\_t)".  See DR 428  

K.3.9.1.4 The swprintf\_s function  

In K.3.9.1.4p2, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.1.4p3, replace "less than RSIZE\_MAX" with "not greater than
RSIZE\_MAX/sizeof(wchar\_t)".  See DR 428  

K.3.9.1.8 The vsnwprintf\_s function  

In K.3.9.1.8p2, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.1.8p3, replace "less than RSIZE\_MAX" with "not greater than
RSIZE\_MAX/sizeof(wchar\_t)".  See DR 428  

K.3.9.1.9 The vswprintf\_s function  

In K.3.9.1.9p2, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.1.9p3, replace "less than RSIZE\_MAX" with "not greater than
RSIZE\_MAX/sizeof(wchar\_t)".  See DR 428  

K.3.9.2.1.1 The wcscpy\_s function  

In K.3.9.2.1.1p2, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.2.1.1p3, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  

K.3.9.2.1.2 The wcsncpy\_s function  

In K.3.9.2.1.2p8, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.2.1.2p9, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  

K.3.9.2.1.3 The wmemcpy\_s function  

In K.3.9.2.1.3p15, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.2.1.3p16, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  

K.3.9.2.1.4 The wmemmove\_s function  

In K.3.9.2.1.4p20, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.2.1.4p21, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  

K.3.9.2.2.1 The wcscat\_s function  

In K.3.9.2.2.1p3, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.2.2.1p4, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  

K.3.9.2.2.2 The wcsncat\_s function  

In K.3.9.2.2.2p10, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.2.2.2p11, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  

K.3.9.2.3.1 The wcstok\_s function  

In K.3.9.2.3.1p2, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  

K.3.9.3.2.1 The mbsrtowcs\_s function  

In K.3.9.3.2.1p3, replace "RSIZE\_MAX" with "RSIZE\_MAX/sizeof(wchar\_t)".  
In K.3.9.3.2.1p4, replace "less than RSIZE\_MAX" with "not greater than
RSIZE\_MAX/sizeof(wchar\_t)".  See DR 428

K.3.9.3.2.2 The wcsrtombs\_s function  

In K.3.9.3.2.2p12, replace "then neither len nor dstmax shall be greater than
RSIZE\_MAX" with  
"then neither len shall be greater than RSIZE\_MAX/sizeof(whcar\_t) nor dstmax
shall be greater than RSIZE\_MAX".  
In K.3.9.3.2.2p13, replace "less than RSIZE\_MAX" with "not greater than
RSIZE\_MAX".


</div>


---

---

<div id="issue0434">

## Issue 0434: Missing constraint w.r.t. Atomic

Authors: WG 14, Fred J. Tydeman (USA)  
Date: 2012-10-26  
Reference document: N1660 [N1660](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1660.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

6.7.2.4 Atomic type specifiers, has in paragraph 2:

> Atomic type specifiers shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).

But, 6.7.3 Type qualifiers, has no similar constraint with respect to \_Atomic.

Also, 7.17.6 Atomic integer types, has no similar constraint. Aside: The only
constraints I see in the library are in \<float.h\> and \<limits.h\>, so it is
not clear if this case should be a constraint.

### Suggested Technical Corrigendum

Add to 6.7.3 Type qualifiers, a new paragraph after paragraph 3,

> Atomic type qualifiers shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).

Add to 7.16.6 Atomic integer types, a new paragraph before paragraph 1:

> Constraints
>
> Atomic type names shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

* The committee agrees to the first additional constraint.
* The second constraint is not required due to 7.17 paragraph 2\.

### Proposed Technical Corrigendum

Add to 6.7.3 Type qualifiers, a new paragraph after paragraph 3,

> Atomic type qualifiers shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).


</div>


---

---

<div id="issue0435">

## Issue 0435: Missing constraint w.r.t. Imaginary

Authors: WG 14, Fred J. Tydeman (USA)  
Date: 2012-10-26  
Reference document: [N1661](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1661.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

> The type specifier \_Complex shall not be used if the implementation does not
> support complex types (see 6.10.8.3).

But, G.2 Types, has no similar constraint with respect to \_Imaginary.

### Suggested Technical Corrigendum

Add to G.2 Types, a new sentence in paragraph 1:

> The \_Imaginary type specifier shall not be used if the implementation does not
> support imaginary types (see 6.10.8.3).

---

Comment from WG14 on 2014-10-31:

Oct 2013 meeting

### Committee Discussion

> This is not actually a defect.

### Proposed Committee Response

> Annex G requires `_Imaginary` be supported, so there is no need to cite a
> requirement for when it is not supported.


</div>


---

---

<div id="issue0436">

## Issue 0436: Request for interpretation of C11 6.8.5#6

Authors: WG 14, Willem Wakker (NL)  
Date: 2013-05-08  
Reference document: [N1713](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1713.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

C11, section 6.8.5 paragraph 6 reads:

> An iteration statement whose controlling expression is not a constant
> expression,156) that performs no input/output operations, does not access
> volatile objects, and performs no synchronization or atomic operations in its
> body, controlling expression, or (in the case of a for statement) its
> expression-3, may be assumed by the implementation to terminate.157)

Question: to what does the *that* refers back to: to the *controlling
expression* or to the *constant expression*?

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

> This is indeed an ambiguity, and after considering various proposals, the
> following was approved.

Apr 2014 meeting

### Committee Discussion

> The committee noted a typo in the Suggested Technical Corrigendum where "its
> expression \*157" was intended to be "its expression-3 \*157", and so has been
> corrected below.

### Proposed Technical Corrigendum

Replace 6.8.5 paragraph 6 with:

> An iteration statement may be assumed by the implementation to terminate if its
> controlling expression is not a constant expression \*156), and none of the
> following operations are performed in its body, controlling expression or (in
> the case of a for statement) its expression-3 \*157):
>
> * input/output operations
> * accessing a volatile object
> * synchronization or atomic operations.


</div>


---

---

<div id="issue0437">

## Issue 0437: `clock` overflow problems

Authors: Austin Group, Nick Stoughton (US)  
Date: 2013-06-19  
Reference document: [N1719](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1719.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 (and C99 before it) state for **clock()** that

> If the processor time used is not available or its value cannot be represented,
> the function returns the value (clock\_t)(-1).

(C11 7.27.2.1 p3). Footnote 319 also states

> In order to measure the time spent in a program, the clock function should be
> called at the start of the program and its return value subtracted from the
> value returned by subsequent calls.

The normative requirement implies that if more processor time has passed than
can be fit into a variable of type **clock\_t** the function must fail and
return **(clock\_t)-1**.

However, existing implementations almost exclusively ignore this requirement and
if more ticks pass than can fit into a **clock\_t** the implementation simply
truncates the value and return the lowermost bits of the actual value. In
programming environments where clock\_t is a 32-bit integer type and
CLOCKS\_PER\_SEC is one million (a very common implementation), clock() will
start misreporting in less than 36 minutes of processor time for signed
clock\_t, or 72 minutes for unsigned clock\_t.

*Question 1:* Are such implementations conforming? If not, should the standard
be altered in any way to permit this *de-facto* standard implementation?

*Question 2:* Should the standard define some limit macros for clock\_t
(effectively defining new values in limits.h for CLOCK\_MAX, the minimum maximum
value for a clock\_t)?

*Question 3:* If the value is truncated and clock\_t is a signed type, the
recommended application usage n footnote 319 (subtracting clock\_t values to
measure intervals) can cause the application to invoke undefined behavior via
integer overflow. In particular, if the initial call to clock() returned A \> 0
(by virtue of some processor time having been consumed before the start of
main() or the point of first measurement), and a subsequent call returned
B\=INT\_MIN just after overflow, then the recommended practice of computing B-A
invokes undefined behavior. Should there be any warning of this included in the
footnote?

### Suggested Change

Given that the vast majority of surveyed implementations appear to have
implemented clock with a simple incrementing counter with no check for overflow,
the requirement for **clock()** to return **(clock\_t)-1** when the number of
clock ticks cannot be represented in a variable of type clock\_t should be
relaxed:

At 7.27.2.1 paragraph 3, change:

> If the processor time used is not available or its value cannot be represented,
> the function returns the value (clock\_t)(-1).

to:

> If the processor time used is not available, the function returns the value
> (clock\_t)-1.

(thus leaving the behavior on overflow unspecified). Change footnote 319 to:

> In order to measure the time spent in a program, the clock function should be
> called at the start of the program and its return value subtracted from the
> value returned by subsequent calls. Note, however, that such a subtraction may
> result in undefined behavior if clock\_t is an unsigned integer type.

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

* This issue is tied to Austin Group Defect #686.
* The committee feels that the core issue regards required behavior under the condition that overflow occurs in the implementations choice for the representation of `clock_t`.
* It is noted that many and possibly most implementations have chosen an integer `clock_t` size that overflows early and often.
* The standard does seem to require that the overflow condition is detected and that the corresponding return value shall be that of failure `(clock_t)-1`.
* Such detection runs counter to the desired behavior of the clock counter as being that of highest implementation efficiency, and to subsequent uses across durations that do not exhibit overflow after the first occurrence.
* The suggested technical corrigendum does not appear to discuss or address this core issue and warrants further discussion. The following suggestion for the footnote is offered:
  > Implementations commonly use an integer `clock_t` type that can overflow in as
  > little as 36 minutes. All uses of `clock()` to measure a duration of time must
  > address the issue of possible overflow.

Apr 2014 meeting

### Committee Discussion

> The author will be solicited for a revised technical corrigendum.

Oct 2014 meeting

### Committee Discussion

> There was no paper submitted on this topic, and the committee will again solicit
> the Austin Group for direction.

Apr 2015 meeting

### Committee Discussion

> The paper [N1895](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1895.htm)
> was provided and discussed. The general sentiment in the committee is that
> `clock_t` is underspecified and that this function should be deprecated and
> replaced in a revision to the standard with something that uses, perhaps,
> `struct timespec`. In particular, no implementations are known to implement the
> `-1` return value on overflow.
>
> The committee reviewed the following words and approved them as the Proposed
> Technical Corrigendum.

### Proposed Committee Response

> To question 1, such programs are not conforming and, no, the standard should not
> be altered to accept this behavior.
>
> To question 2, no, this is not the direction.
>
> To question 3, the committee does not agree that this invokes undefined
> behavior. The value returned under such conditions is unspecified.

### Proposed Technical Corrigendum

In 7.27.2.1p3 change:

> If the processor time used is not available or its value cannot be represented,
> the function returns the value `(clock_t)(-1)`<sup>319</sup>. ...
>
> 319\) In order to measure the time spent in a program, the `clock` function
> should be called at the start of the program and its return value subtracted
> from the value returned by subsequent calls.

to

> If the processor time used is not available, the function returns the value
> `(clock_t)(-1)`. If the value cannot be represented, the function returns an
> unspecified value<sup>319</sup>. ...
>
> 319\) This may be due to overflow of the `clock_t` type.


</div>


---

---

<div id="issue0438">

## Issue 0438: `ungetc / ungetwc` and file position after discarding push back problems

Authors: Austin Group, Nick Stoughton (US)  
Date: 2013-06-19  
Reference document: [N1720](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1720.htm), [Austin Group Defect #701](http://austingroupbugs.net/view.php?id=701)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 (and C99 before it) state for both **ungetc()** and **ungetwc()** that

> A successful intervening call (with the stream pointed to by stream) to a file
> positioning function (fseek, fsetpos, or rewind) discards any pushed-back
> characters for the stream. ... The value of the file position indicator for the
> stream after reading or discarding all pushed-back characters shall be the same
> as it was before the characters were pushed back.

(7.21.7.10 p2 \& p5, with similar at 7.29.3.10 p2 \& p5). The "or discarding"
phrasing in p5 makes no sense: all of the listed functions which discard the
push back also \_set\_ the file position. The file position will end up as
whatever the function sets it to, not "the same as it was before the characters
were pushed back".

### Suggested Change

Change

> The value of the file position indicator for the stream after reading or
> discarding all pushed-back characters shall be the same as it was before the
> characters were pushed back.

to

> The value of the file position indicator for the stream after all pushed-back
> characters have been read shall be the same as it was before the characters were
> pushed back.

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

* This issue arises because of the different architectures of a buffered stream which can hold pushed back characters, and that of the underlying filesystem which honors seek independent of the buffering.
* The committee sentiment is that the suggested changes are nearly correct and have requested that the project editor suggest better wording, subject to further discussion.

Apr 2014 meeting

### Committee Discussion

> The Standard is correct as written because the intent is that the specified file
> position indicator is an intermediate state inside the file positioning function
> after the pushed-back characters are discarded but before the actual seek. That
> gives you a reliable file position from which to do the seek. It's not intended
> that the file positioning function doesn't set the file position indicator.

### Proposed Technical Corrigendum

Add a footnote to 7.21.7.10 paragraph 5, second sentence:

> Note that a file positioning function may further modify the file position
> indicator after discarding any pushed-back characters.

Add a footnote to 7.29.3.10 paragraph 5, second sentence:

> Note that a file positioning function may further modify the file position
> indicator after discarding any pushed-back wide characters.


</div>


---

---

<div id="issue0439">

## Issue 0439: Issues with the definition of “full expression”

Authors: WG 14, Clark Nelson  
Date: 2013-07-16  
Reference document: [N1729](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1729.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

I have discovered several issues in 6.8p4, which defines “full expression” and
points out the major implications for an expression that is a full expression.
In this paper I present the issues, along with my recommendations. For the
issues for which it makes sense, I will later submit defect reports.

Here is the text of 6.8p4, with clause numbering added for convenience of
reference:

> 1. A *full expression* is an expression that is not part of another expression or of a declarator.
> 2. Each of the following is a full expression:
>    1. an initializer that is not part of a compound literal;
>    2. the expression in an expression statement;
>    3. the controlling expression of a selection statement (if or switch);
>    4. the controlling expression of a while or do statement;
>    5. each of the (optional) expressions of a for statement;
>    6. the (optional) expression in a return statement.
> 3. There is a sequence point between the evaluation of a full expression and the evaluation of the next full expression to be evaluated.

And here are the issues.

A. The phrase “not part of another expression or of a declarator” (sentence 1\)
is rather difficult to understand. It *probably* means: not part of another
expression, nor part of a declarator. (But DeMorgan's law is hard on the brain.)

I believe this could be fixed as a simple editorial issue.

B. The status of an initializer expression depends on whether the context is a
declaration or a compound literal (clause 2.1). That would seem to imply
different sequencing guarantees in those contexts. As it turns out, it does, but
the implication is quite subtle. Consider 6.7.9p23:

> The evaluations of the initialization list expressions are indeterminately
> sequenced with respect to one another and thus the order in which any side
> effects occur is unspecified.

And consider this example:

```c
#include <stdio.h>



#define ONE_INIT        '0' + i++ % 3

#define INITIALIZERS    [2] = ONE_INIT, [1] = ONE_INIT, [0] = ONE_INIT



int main()

{

        int i = 0;

        char x[4] = { INITIALIZERS }; // case 1

        puts(x);

        puts((char [4]){ INITIALIZERS }); // case 2

        puts((char [4]){ INITIALIZERS } + i % 2); // case 3

}
```

In every use of the `INITIALIZERS` macro, the variable `i` is incremented three
times. In cases 1 and 2, there is no undefined behavior, because the increments
are in expressions that are indeterminately sequenced with respect to one
another, not unsequenced. There is no guarantee in what order the evaluations
are done, so there is no guarantee in what order they will appear, but the
initial values are guaranteed to be `'0'`, `'1'` and `'2'`.

(It's not perfectly clear whether that guarantee was provided by C99, which
instead said:

> The order in which any side effects occur among the initialization list
> expressions is unspecified.

In any event, as a data point, that guarantee was not honored by GCC until
release 4.6, in 2011.)

On the other hand, because case 3 contains an unsequenced evaluation of `i` in
the same full expression, it has undefined behavior.

Considering the number of hours it took me to finally reach this conclusion, I
thought it would be worthwhile to bring it to the full committee to make sure
everyone understands and agrees with it. If so, an addition to the rationale
might be in order.

C. Consider 6.7.6p3 (emphasis added):

> A *full declarator* is a declarator that is not part of another declarator.
> **The end of a full declarator is a sequence point.** …

Also 6.2.4p8:

> A non-lvalue expression with structure or union type, where the structure or
> union contains a member with array type (including, recursively, members of all
> contained structures and unions) refers to an object with automatic storage
> duration and *temporary lifetime*.<sup>36\)</sup> Its lifetime begins when the
> expression is evaluated and its initial value is the value of the expression.
> Its lifetime ends **when the evaluation of the containing full expression or
> full declarator ends**. Any attempt to modify an object with temporary lifetime
> results in undefined behavior.

It is clear from these passages that the sequence of evaluations includes not
only full expressions, but also full declarators – whatever sense it makes to
talk about “evaluating” a full declarator. But sentence 3 does not acknowledge
that reality.

My inclination is to adopt a bit of terminology from Ada, and start talking
about the “elaboration” of a declarator, which, for a variably modified type,
involves the run-time evaluation of array sizes, and then to re-draft sentence 3
and the other paragraphs cited here, to make it clear that sequence points
separate elaborations of full declarators as well as evaluations of full
expressions. In any event, I think there's a problem in sentence 3 that needs to
be fixed.

D. Expressions in abstract declarators are not mentioned at all (compare to
sentence 1). The logical inference is that such an expression is not a full
expression by itself, but part of the containing full expression. But there are
cases where there is no containing full expression. For example:

```c
typedef _Atomic(int (*)[rand()]) T;

_Alignas(int [rand()]) int i;
```

In these examples, not only is there no containing full expression, there isn't
even any containing full declarator, because these expressions appear in the
declaration specifiers, not the declarator.

Probably the simplest approach here would be to disallow variably modified types
with `_Atomic` and `_Alignas`, at least until the next revision of the standard.

E. The list of full expression contexts (sentence 2\) is not logically complete.
According to the definition (sentence 1), an expression appearing in a
constant-expression context is (often) a full expression. Of course there are no
sequencing implications relevant for constant expressions, but it's not clear
that makes it important for a constant expression not to be counted as a full
expression. In any event, it's not clear how the list normatively interacts with
the definition.

I think we should consider moving the list into a note, so it's clear that the
definition is, well, definitive. The note could also point out that sequencing
is irrelevant to constant expressions.

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

* These are subtle issues upon which the committee wishes to continue discussing.
* The committee is seeking concurrence with the project editor that Point A may be viewed as editorial.
* To Point B the committee is in agreement that there is a "guarantee" of the distinct values `0`, `1`, and `2`, and that this is not new to C11. The committee requires further discussion as to whether and how these subtleties could be expressed in a non-normative fashion, such as "in the rationale", "in a footnote", or simply as an example.
* To Point C the committee agrees that some change is needed and has solicited a suggested resolution from the author. The fact that VLAs can have several dimensions and hence several expressions gave pause to all.
* To Point D the committee agrees that this has been left undefined and deserves a committee response but no normative or other change.
* To Point E, the committee agreed that the list of full expressions named in 6.8 paragraph 4 second sentence should likely be regarded as non-normative rather than allowing it to appear exhaustive. To achieve this, the list could be transformed into a note or footnote.

Apr 2014 meeting

### Committee Discussion

> The committee solicits the author for any suggested technical corrigenda.

Oct 2014 meeting

### Committee Discussion

> There was no paper submitted on this topic, and the committee will again solicit
> the author for suggested technical corrigenda.

Apr 2015 meeting

### Committee Discussion

> There was no paper submitted on this topic, and the committee has solicited the
> author for suggested technical corrigenda.

Oct 2015 meeting

### Committee Discussion

* The paper [N1965](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1965.htm) was submitted and discussed.
* From that, the editorial suggestion from Part A was incorporated into Part C which was approved by the committee as a normative element in the following Proposed Technical Corrigendum, and Part E was approved as a non-normative footnote.
* The Part D section had already met with some some skepticism from the committee and was mostly provided as an idea to consider. Discussion revealed that there are some implementations of VLA that would be broken by this change, and so the committee preferred to not try to address this issue from this DR at this time. Another new paper on this point would be welcomed by the committee.
* The sequencing issues raise in Part B are subtle and the Standard potentially confusing, but there is no reported evidence that this is causing any issues in practice. The new paper offered no Suggested Technical Corrigendum in this area, and the committee did not request further elaboration of what might be needed in this area, and so was content to accept just the changes resolving issues A, C, and E in the following Proposed Technical Corrigendum.

### Proposed Technical Corrigendum

Change 6.2.4p8 sentence 3 from:

> Its lifetime ends when the evaluation of the containing full expression or full
> declarator ends.

to:

> Its lifetime ends when the evaluation of the containing full expression ends.

Delete 6.7.6p3 sentence 2:

> The end of a full declarator is a sequence point.

Change 6.8p4 from:

> A *full expression* is an expression that is not part of another expression, or
> of a declarator. Each of the following is a full expression: an initializer that
> is not part of a compound literal; the expression in an expression statement;
> the controlling expression of a selection statement (`if` or `switch)`; the
> controlling expression of a `while` or `do` statement; each of the (optional)
> expressions of a `for` statement; the (optional) expression in a `return`
> statement. There is a sequence point between the evaluation of a full expression
> and the evaluation of the next full expression to be evaluated.

to:

> A *full expression* is an expression that is not part of another expression, nor
> part of a declarator or abstract declarator. There is also an implicit full
> expression in which the non-constant size expressions for a variably modified
> type are evaluated; within that full expression, the evaluation of different
> size expressions are unsequenced with respect to one another. There is a
> sequence point between the evaluation of a full expression and the evaluation of
> the next full expression to be evaluated.

Add after 6.8p4:

> NOTE: Each of the following is a full expression:
>
> * a full declarator for a variably modified type;
> * an initializer that is not part of a compound literal;
> * the expression in an expression statement;
> * the controlling expression of a selection statement (`if` or `switch)`;
> * the controlling expression of a `while` or `do` statement;
> * each of the (optional) expressions of a `for` statement;
> * the (optional) expression in a `return` statement.
>
> While a constant expression satisfies the definition of a full expression,
> evaluating it does not depend on nor produce any side effects, so the sequencing
> implications of being a full expression are not relevant to a constant
> expression.

Delete the Annex C bullet:

* The end of a full declarator; declarators (6.7.6);

Change the Annex C bullet from:

* Between the evaluation of a full expression and the next full expression to be evaluated. The following are full expressions: an initializer that is not part of a compound literal; the expression in an expression statement; the controlling expression of a selection statement (`if` or `switch)`; the controlling expression of a `while` or `do` statement; each of the (optional) expressions of a `for` statement; the (optional) expression in a `return` statement.

to:

Between the evaluation of a full expression and the next full expression to be evaluated. The following are full expressions: a full declarator for a variably modified type; an initializer that is not part of a compound literal; the expression in an expression statement; the controlling expression of a selection statement (`if` or `switch)`; the controlling expression of a `while` or `do` statement; each of the (optional) expressions of a `for` statement; the (optional) expression in a `return` statement.


</div>


---

---

<div id="issue0440">

## Issue 0440: Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 1

Authors: WG 14, Joseph Myers  
Date: 2013-07-21  
Reference document: [N1730](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1730.pdf)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 1: Choice of long double in Annex F

Annex F provides various choices for the long double type (which may or may not
be an IEC 60559 type), but no method is provided for an application to determine
which choice has been made.

If a macro is provided to say whether the type is an IEC 60559 type, all the
other properties can be determined from the existing \<float.h\> macros. So, a
sufficient fix would be:

> In 5.2.4.2.2, insert a new paragraph after paragraph 10: Whether a type matches
> an IEC 60559 type is characterized by the implementation-defined values of
> FLT\_IS\_IEC\_60559, DBL\_IS\_IEC\_60559, and LDBL\_IS\_IEC\_60559:
>
> * 0 type does not match an IEC 60559 format
> * 1 type's values and operations are those of an IEC 60559 basic, interchange or extended type

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

> Committee discussion led to a proposed committee response.

Apr 2014 meeting

> Correspondence with the author led the committee to augment the proposed
> committee response.

### Proposed Committee Response

> To do as suggested, distinguish whether `float`, `double`, and `long double` are
> IEC or not, requires the addition of new macros, which is a feature, which is
> not allowed by the mechanism of defect reports.
>
> The defect originator notes that the underlying issue that needs consideration
> in any further comprehensive publication of the Standard is that all
> implementation defined behaviors need to be strictly called out in the Standard,
> and moreover that they be done so in a manner that is accessible to a client of
> the implementation to allow proper choice of algorithms. It has been asserted
> that leaving implementation defined behaviors formally undefined in the Standard
> has led to significant and unnecessary divergences in implementations.


</div>


---

---

<div id="issue0441">

## Issue 0441: Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 2

Authors: WG 14, Joseph Myers  
Date: 2013-07-21  
Reference document: [N1730](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1730.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 2: Definition of FLT\_ROUNDS

The C11 definition of FLT\_ROUNDS is inadequate in that it refers to
floating-point addition but does not say addition of what type. If long double
is not an IEC 60559 type, it may not fully support all rounding modes even
though they are supported by other types. (This is an actual issue with real
implementations using non-IEC 60559 types for long double.) A suitable fix would
be:

> In 5.2.4.2.2#8, insert "for type float" after "floating-point addition". At the
> end of F.2#1, insert "The value of FLT\_ROUNDS applies to all IEC 60559 types
> supported by the implementation, but may not apply to non-IEC 60559 types.".

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

> The committee adopted a Proposed Committee Response that has been substantially
> revised.

Oct 2014 meeting

### Committee Discussion

> The Proposed Committee Response was revised for accuracy and more detailed
> information, and is provided below.

**Proposed Committee Response (obsolete)**

> The committee regards the existing definition of `FLT_ROUNDS` as intended to
> apply to types `float`, `double` and `long double`. However, if all three types
> cannot support the same set of rounding modes, the implementation needs to set
> `FLT_ROUNDS` to -1 meaning indeterminable.
>
> As has been pointed out, in Annex F, only the types float and double need be IEC
> 60559 types. If long double is not an IEC 60559 type (for example, a pair of
> doubles), it may not support the same set of rounding modes as float and double.
> In this case, having `FLT_ROUNDS` apply to float and double (but not long
> double) would result in a value of 0, 1, 2, or 3 and would provide new and
> useful information to the programmer.
>
> However, this behavioral change could also break existing programs, and as such
> the committee prefers to leave as is for this revision of the Standard.

Apr 2015 meeting

### Committee Discussion

> The Proposed Committee Response was revised yet again based on the input that
> since FLT\_ROUNDS in existing practice is universally coded as 1, the proposed
> changes won’t affect existing practice.

### Proposed Committee Response

> The implementation of `long double`, for example, may significantly differ from
> IEC floating types and may not support the same choices as would otherwise be
> possible for `FLT_ROUNDS`. All known implementations define `FLT_ROUNDS` as the
> value `1` (round to nearest). and as such exempting non-IEC `long double`
> behavior allows the potential for implementations to provide the full range of
> possible values for IEC floating types.

### Proposed Technical Corrigendum

At the end of F.2#1, insert

> The value of FLT\_ROUNDS applies to all IEC 60559 types supported by the
> implementation, but need not apply to non-IEC 60559 types.


</div>


---

---

<div id="issue0442">

## Issue 0442: Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 3

Authors: WG 14, Joseph Myers  
Date: 2013-07-21  
Reference document: [N1730](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1730.pdf)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 3: Floating-point exceptions and 6.5#5

C11 6.5#5 says "If an exceptional condition occurs during the evaluation of an
expression (that is, if the result is not mathematically defined or not in the
range of representable values for its type), the behavior is undefined.". When
the Annex F bindings are in effect, it must be intended that floating-point
exceptions do not produce such undefined behavior (instead, behavior such as
evaluating to a NaN must be defined). But no normative text actually says that.

A suitable fix would be:

> Append to 6.5#5: For implementations defining \_\_STDC\_IEC\_559\_\_, this does
> not apply to exceptional conditions where the behavior (such as raising a
> floating-point exception and returning a NaN) is defined by Annex F, directly or
> by reference to IEC 60559\.

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

### Committee Discussion

* The following words were discussed extensively and thought appropriate as appropriate for inclusion in F.3, rather than a new F.4:
  > If an exceptional condition occurs during the evaluation of an expression (that
  > is, if the result is not mathematically defined or not in the range of
  > representable values for its type), and the behaviour is not defined in this
  > annex or by reference to IEC 60559, 6.5p5 applies and the behaviour is
  > undefined.
* The committee also suggested adding an example or footnote suggesting that this would apply to a non-IEC 60550 `long double`.

Apr 2014 meeting

### Committee Discussion

> Further correspondence with the author and excerpted in
> [N1804](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1804.htm) has
> identified the core issue as being a simple misunderstanding of the
> applicability of normative annexes to the standard.

### Proposed Committee Response

> WG14 treats normative annexes such as Annex F as if they were linear extensions
> of the standard itself. When Annex F is requested via definition of
> `__STDC_IEC_559__` then 6.5#5 is superseded and floating point exceptions become
> well defined.


</div>


---

---

<div id="issue0443">

## Issue 0443: Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 4

Authors: WG 14, Joseph Myers  
Date: 2013-07-21  
Reference document: [N1730](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1730.pdf)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 4: Floating-point state not being an object

The description of the floating-point environment in C11 fails to make
sufficiently clear what is or is not an object (C11 footnote 205 is not
normative, and so cannot be used to that effect); it uses terms such as "system
variable" without saying what that is. Simply moving that footnote to normative
text would fix this issue:

> Move the contents of footnote 205 (C11 subclause 7.6) to the end of 5.1.2.3#2.

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

### Committee Discussion

* The committee agrees that the floating point environment is not an object and must be stated in normative terms instead of in non-normative footnote 205\.
* The environment may be modified more than once in an expression without inducing undefined behavior, this is just "how it works".
* The floating-point environment is described in the standard using an otherwise undefined term "system variable" having 7.6p2 thread storage duration, implying that it is an object, and so this is perhaps the actual manifestation of the defect that requires correction.
* The floating-point environment is technically an actor, not an object, having a model of its behavior defined purely by messages as its internal "piece of state" is not directly visible. In this case the messages are the macros and functions, as are the electronic signals from the floating-point computational units to consult and honor the desired floating point modal behaviors, and the electronic signals that record "auxiliary information" in the model for floating point exceptions.
* In any case, the floating point environment implementation is not described by the abstract C machine, only its operations.
* The committee prefers that this be cleared up in 7.6, by moving the second sentence and possibly the first sentence into normative text.

Apr 2014 meeting

### Committee Discussion

> The committee discusses this issue further and could not see an actual defect:
> there are no misinterpretations stated or implied.

### Proposed Committee Response

> Since operations on the floating point environment are well defined there is no
> need to normatively define anything further about its implementation. The
> footnote adds clarity and should remain as is.


</div>


---

---

<div id="issue0444">

## Issue 0444: Issues with alignment in C11, part 1

Authors: WG 14, Joseph Myers  
Date: 2013-07-23  
Reference document: [N1731](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1731.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

There are various deficiencies in the C11 text about alignment requirements.

Issue 1: Existence of over-aligned types

6.2.8#3 defines the concept of an over-aligned type, with a footnote saying
"Every over-aligned type is, or contains, a structure or union type with a
member to which an extended alignment has been applied.". But there is no way in
the syntax to apply such an alignment to a member. \_Alignas appears in the
syntax for alignment-specifier, which in turn appears in that for
declaration-specifiers (6.7#1). But structure and union members instead use
struct-declaration which uses specifier-qualifier-list which doesn't include a
case for alignment-specifier at all. So for the reference to over-aligned types,
and the reference in 6.7.5#6 to the "declared object or member", to be
meaningful, something needs adding to the syntax for struct-declaration. (Note
that specifier-qualifier-list is also used in the syntax for type-name, and it
seems less likely that a type-name was intended to be able to include
alignment-specifiers.)

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

> * The desired and intended syntax is indeed missing.
> * Whereas one could achieve the desired effect by placing the directive on the aggregate itself and controlling it by the maximum alignment of each of its members, this is far from the intended goal, and we do consider this a defect.
> * We solicit a suggested technical corrigendum from the author.
> * Modifying the definition of type name will require considerable thought.
> * Applying the directive beyond aggregate members, such as a simple scalar declaration, is not well defined, and brings in the various storage durations and how or whether all or any are supported.

Apr 2014 meeting

### Committee Discussion

* The author provided the following technical corrigendum as input to [N1804](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1804.htm):   
   6.7.2.1#1: Move the definition of specifier-qualifier-list to 6.7.7#1. Insert a new definition in 6.7.2.1#1:
  > specifier-qualifier-alignment-list:
  >
  > type-specifier specifier-qualifier-alignment-list\_opt  
  > type-qualifier specifier-qualifier-alignment-list\_opt  
  > alignment-specifier specifier-qualifier-alignment-list\_opt

  Change the use of specifier-qualifier-list in the syntax for struct-declaration
  to specifier-qualifier-alignment-list.

  6.7.2#2:

  > Change "and in the specifier-qualifier list in each struct declaration and type
  > name" to ", in the specifier-qualifier-alignment list in each struct declaration
  > and in the specifier-qualifier list in each type name".

  6.7.3#5:

  > Change "specifier-qualifier-list" to "specifier-qualifier-list,
  > specifier-qualifier-alignment-list or declaration-specifiers" (twice).

  (That the wording about duplicate qualifiers and qualifiers used with \_Atomic doesn't deal with declaration-specifiers, the syntax production relevant to normal declarations, is a pre-existing problem noticed in the course of preparing this wording.)

  (I believe all the semantics and constraints required for alignment specifiers
  on members are in place, including 6.2.7#1 dealing with cross-translation-unit
  type compatibility and references to bit-fields and members in 6.7.5.)
* The committee agrees with this as the proper direction and will solicit further review from implementors.

Oct 2014 meeting

### Committee Discussion

> There still has not been adequate review of these changes. The Project Editor
> and others have been asked to examine these changes closely prior to our next
> meeting.

Apr 2015 meeting

### Committee Discussion

> The suggested syntax provided by the author has been adopted on a trial basis in
> at least one implementation. It does not, however, provide for compound
> literals.
>
> A simpler syntax change was discussed, to wit
>
> > *specifier-qualifier-list*:
> >
> > > *type-specifier specifier-qualifier-list<sub>opt</sub>*
> > >
> > > *type-qualifier specifier-qualifier-list<sub>opt</sub>*
> > >
> > > <ins>*alignment-specifier specifier-qualifier-list<sub>opt</sub>*</ins>
>
> where *specifier-qualifier-list* is used in the grammar in only two productions:
> *struct-declaration* (which relates to the primary purpose of this DR), and
> *type-name*, which is used only in the definitions of these constructs:
>
> * generic association (generic selection)
> * compound literal
> * `sizeof` expression
> * `_Alignof` expression
> * cast expression
> * atomic type specifier
> * alignment specifier
>
> A constraint could be added to 6.7.7 *type-name* after paragraph 1 disallowing
> the use of *alignment-specifier* in a *type-name* except in the case of
> *compound literal* which was deemed useful by the committee. The following
> principles were elucidated:
>
> * `_Alignas` needs to be applied wherever objects are laid out in memory. On modern architectures page and cache line alignment of data structures is increasingly critical for performance.
> * Alignment is incorporated into the type system for structure (and union) members, but otherwise is not considered part of the type.
>
> In 6.7.3p5, there are two references to *specifier-qualifier-list*, which should
> also reference declaration specifiers.
>
> In 6.7.5 paragraphs 2 and 4, there are occurrences of the phrase “alignment
> attribute” which should instead read “alignment specifier”

Oct 2015 meeting

### Committee Discussion

> The committee did not discuss the direction from the last meeting in any
> substantial manner. It has solicited a paper from the author of the direction
> expressing these ideas as a Suggested Technical Corrigendum.

Apr 2016 meeting

### Committee Discussion

> A new paper [N2028](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2028.htm)
> was submitted that embodied the direction above and the committee accepted it.

Oct 2016 meeting

### Committee Discussion

> It was noted that C\+\+ allows one additional production for
> *alignment-specifier* between `struct` and *tag*.
>
> The paper [N2028](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2028.htm)
> was presented which had an alternate suggestion for a resolution, but the
> committee preferred the following.

**Proposed Technical Correigendum**

Change 6.7.2.1p1 from

> *specifier-qualifier-list*:
>
> > *type-specifier specifier-qualifier-list<sub>opt</sub>*
> >
> > *type-qualifier specifier-qualifier-list<sub>opt</sub>*

to

> *specifier-qualifier-list*:
>
> > *type-specifier specifier-qualifier-list<sub>opt</sub>*
> >
> > *type-qualifier specifier-qualifier-list<sub>opt</sub>*
> >
> > *alignment-specifier specifier-qualifier-list<sub>opt</sub>*

Change 6.7.5p2 from

> An alignment attribute shall not be specified in a declaration of a typedef, or
> a bit-field, or a function, or a parameter, or an object declared with the
> `register` storage-class specifier.

to

> An alignment specifier shall appear only in the declaration specifiers of a
> declaration, or in the specifier-qualifier list of a member declaration, or in
> the type name of a compound literal. An alignment specifier shall not be used in
> conjunction with either of the storage-class specifiers `typedef` or `register`,
> nor in a declaration of a function or bit-field.

Change 6.7.3p5 from

> If the same qualifier appears more than once in the same
> *specifier-qualifier-list*, either directly or via one or more `typedef`s, the
> behavior is the same as if it appeared only once. If other qualifiers appear
> along with the `_Atomic` qualifier in a *specifier-qualifier-list*, the
> resulting type is the so-qualified atomic type.

to

> If the same qualifier appears more than once in the same
> *specifier-qualifier-list* or as *declaration-specifiers*, either directly or
> via one or more `typedef`s, the behavior is the same as if it appeared only
> once. If other qualifiers appear along with the `_Atomic` qualifier the
> resulting type is the so-qualified atomic type.

Change 6.7.5p4 from

> The combined effect of all alignment attributes in a declaration shall not...

to

> The combined effect of all alignment specifiers in a declaration shall not...


</div>


---

---

<div id="issue0445">

## Issue 0445: Issues with alignment in C11, part 2

Authors: WG 14, Joseph Myers  
Date: 2013-07-23  
Reference document: [N1731](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1731.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

There are various deficiencies in the C11 text about alignment requirements.

Issue 2: Contexts in which alignments are supported

6.2.8#2 defines "fundamental alignment": "A fundamental alignment is represented
by an alignment less than or equal to the greatest alignment supported by the
implementation in all contexts, which is equal to \_Alignof (max\_align\_t)."

6.2.8#3 defines "extended alignment": "An extended alignment is represented by
an alignment greater than \_Alignof (max\_align\_t). It is
implementation-defined whether any extended alignments are supported and the
contexts in which they are supported. A type having an extended alignment
requirement is an over-aligned type."

6.2.8#4 defines "valid alignment", saying "Alignments are represented as values
of the type size\_t. Valid alignments include only those values returned by an
\_Alignof expression for fundamental types, plus an additional
implementation-defined set of values, which may be empty. Every valid alignment
value shall be a nonnegative integral power of two.".

max\_align\_t is specified in 7.19#2 as "an object type whose alignment is as
great as is supported by the implementation in all contexts".

The memory management functions in 7.22.3 are defined to return a pointer
"suitably aligned so that it may be assigned to a pointer to any type of object
with a fundamental alignment requirement and then used to access such an object
or an array of such objects in the space allocated". In the case of
aligned\_alloc, there may be a stricter requirement given by the alignment
passed to the function, but the alignment passed to the function can't result in
memory any less-aligned than a fundamental alignment requirement. The alignment
requirement still applies even if the size is too small for any object requiring
the given alignment (see the response to C90 DR#075).

There are various problems with the above:

* The term "fundamental type" is not defined in C11.
* There is also no definition of what a "context" is in which an alignment might or might not be supported. In common implementation practice, separate contexts might be by the storage duration of the object (static, thread, automatic, allocated, with the last referring to the alignments guaranteed by calloc, malloc and realloc).
* A "valid alignment" may not be a "fundamental alignment". Thus, whatever interpretation is adopted for "fundamental type", nothing in the standard requires the alignment of a "fundamental type" to be a "fundamental alignment". For example, say "long double" is a "fundamental type"; it would seem nonsensical if declaring "long double" objects (in any context) failed to work, but nothing seems to require malloc to return objects sufficiently aligned for long double.
* Given these gaps in the definition, nothing in the normative text appears to imply footnote 57 "Every over-aligned type is, or contains, a structure or union type with a member to which an extended alignment has been applied.", although no doubt it reflects the intent.
* If "fundamental type" is interpreted to mean "basic type", that is not sufficient to resolve these lacunae. For example, if

  ```c
  struct s { long double ld; }
  ```

  has an alignment requirement bigger than long double, it should still be
  possible to allocate memory for it with malloc, and the same applies to any
  typedef from a standard header that might also have a bigger alignment
  requirement than any basic type.

The following principles seem natural for any fix for this issue:

* C99 referred to "any type of object" in the alignment requirements for calloc, malloc and realloc. As a matter of compatibility, this means that any type that could be constructed within C99 (including one using types from standard headers) should have an alignment required by C11 to be supported in all contexts, and the same applies to types from C extensions originally specified as extensions to C99. Most of the following principles follow to a greater or lesser extent from this compatibility principle.
* All basic types have alignments supported in all contexts.
* All enumerated types have alignments supported in all contexts.
* All pointer types have alignments supported in all contexts (even if the type pointed to does not).
* All types from standard headers specified as complete object types in the definitions of those headers have alignments supported in all contexts. (This includes both types specified as typedefs and types specified as structs or unions with a given tag.)
* If a type has an alignment supported in all contexts, so do arrays of that type, qualified versions of that type, and atomic versions of that type.
* If all the members of a structure or union have types with alignments supported in all contexts, and none of them use an \_Alignas specifier specifying an alignment bigger than supported in all contexts, then that structure or union has an alignment supported in all contexts.
* Where C extensions such as TS 18661-2 and 18661-3 are proposed that define new types, or existing such extensions such as TR 18037 are revised and updated for C11, care should be taken that the new types are covered under the above, whether through being basic types or through being defined in standard headers. (If SIMD vector types, as mentioned at [http://www.open-std.org/pipermail/cplex/2013-June/000010.html](https://www.open-std.org/pipermail/cplex/2013-June/000010.html), were to end up in any such extension, it would probably be appropriate to define them in a way that does \*not\* require calloc, malloc and realloc to return memory suitably aligned for them; such types often require alignments bigger than needed for any other type, so imposing such requirements on memory allocation functions would result in undue inefficiency.)

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

* It is indeed the case that 6.2.8p3 "fundamental type" is not defined. The intention is that it be "basic type", such that "fundamental alignment" is well defined, and yet this is not the case, and "fundamental alignment" also needs a definition. It is likely that the definition of fundamental type can be made editorially, but that when and where fundamental alignment is required is substantive.
* It is also the case that 6.2.8p3 "contexts" is not defined. It is intended to mean the full set of storage durations. Perhaps we should say "storage duration contexts".
* It is also the case that "valid alignment" may not be a "fundamental alignment".
* It was the case in C99 that `malloc` was required to return memory appropriate for "any type", and this should not be lost in the new wording regarding types that are not over-aligned. All other C99 behaviors must also be preserved as he describes as guidance.
* All types declared without the \_Alignas directive are intended to have fundamental alignment, which must be tied somehow to basic type. A consequence is that the only manner in which one can produce an over-aligned type is through \_Alignas. `malloc` has been defined in terms of fundamental alignment, yet we do not anywhere strongly state that, say, `int` has such fundamental alignment.
* These are several interwoven definitions and missing definitions that need a comprehensive review for adequate correction. We solicit the author for a suggested technical corrigendum. A copy of the audio discussion can be provided.

Apr 2014 meeting

### Committee Discussion

* The author provided input to [N1804](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1804.htm) as a proposed technical corrigendum:
* Change 6.2.8#2 to:
  > A fundamental alignment is a valid alignment less than or equal to `_Alignof
  > (max_align_t)`. Fundamental alignments shall be supported by the implementation
  > for objects of all storage durations. The alignment requirements of the
  > following types shall be fundamental alignments:
  >
  > + all atomic, qualified or unqualified basic types;
  > + all atomic, qualified or unqualified enumerated types;
  > + all atomic, qualified or unqualified pointer types;
  > + all array types whose element type has a fundamental alignment requirement;
  > + all types specified in clause 7 as complete object types;
  > + all structure or union types all of whose elements have types with fundamental alignment requirements and none of whose elements have an alignment specifier specifying an alignment that is not a fundamental alignment.

  In 6.2.8#3, change "the contexts in" to "the storage durations of objects for
  which".

  In 6.2.8#4, change "those values returned by an \_Alignof expression for
  fundamental types" to "fundamental alignments".

  (Note that the above admits the possibility that e.g. 1 and 4 are fundamental
  alignments, but 2 isn't, in which case it can't be an extended alignment either.
  If we want to ensure that 2 isn't a valid alignment at all in that case, rather
  than possibly having valid alignments that are neither fundamental nor extended,
  also change "additional implementation-defined set of values" to "additional
  implementation-defined set of extended alignments" in 6.2.8#4.) In 6.7.5#3,
  change "in the context in which it appears" to "for an object of the storage
  duration, if any, being declared". Add a new constraint at the end of 6.7.5#3:
  "An object shall not be declared with an over-aligned type with an extended
  alignment requirement not supported by the implementation for an object of that
  storage duration.".

  (This deals with the point that if an over-aligned struct is defined, then
  objects with that type may be supported with some storage durations but not
  others, so it is the declaration of an object with that type that can violate a
  constraint rather than the declaration of the struct.)

  In 7.19#2, change "whose alignment is as great as is supported by the
  implementation in all contexts" to "whose alignment is the greatest fundamental
  alignment".

  (I'm trying to avoid an undesirable implication that if an alignment of e.g. 1MB
  is supported in all contexts \- and it's quite plausible that an implementation
  can support more or less arbitrary alignments \- then max\_align\_t must have
  such an alignment and so such an alignment must count as fundamental and so
  malloc must return memory suitable aligned for it.)
* This is a difficult area and further study is required.

Oct 2014 meeting

### Committee Discussion

> The proposed changes have raised no concerns and so the committee has agreed to
> use them as the following Proposed Technical Corrigendum.

### Proposed Technical Corrigendum

Change 6.2.8#2 to:

> A fundamental alignment is a valid alignment less than or equal to `_Alignof
> (max_align_t)`. Fundamental alignments shall be supported by the implementation
> for objects of all storage durations. The alignment requirements of the
> following types shall be fundamental alignments:
>
> * all atomic, qualified or unqualified basic types;
> * all atomic, qualified or unqualified enumerated types;
> * all atomic, qualified or unqualified pointer types;
> * all array types whose element type has a fundamental alignment requirement;
> * all types specified in clause 7 as complete object types;
> * all structure or union types all of whose elements have types with fundamental alignment requirements and none of whose elements have an alignment specifier specifying an alignment that is not a fundamental alignment.

In 6.2.8#3, change

> "the contexts in"

to

> "the storage durations of objects for which".

In 6.2.8#4, change

> "those values returned by an \_Alignof expression for fundamental types"

to

> "fundamental alignments".

In 6.7.5#3, change

> "in the context in which it appears"

to

> "for an object of the storage duration, if any, being declared".

Add a new constraint at the end of 6.7.5#3:

> "An object shall not be declared with an over-aligned type with an extended
> alignment requirement not supported by the implementation for an object of that
> storage duration.".

In 7.19#2, change

> "whose alignment is as great as is supported by the implementation in all
> contexts"

to

> "whose alignment is the greatest fundamental alignment".


</div>


---

---

<div id="issue0446">

## Issue 0446: Use byte instead of character for memcmp, memcpy

Authors: WG 14, Blaine Garst  
Date: 2013-07-31  
Reference document: [N1736](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1736.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

It has been noted that the descriptions for 7.24.2.1 `memcpy`, 7.24.2.2
`memmove` and 7.24.4.1 `memcmp` are written using the term *character* which is
inconsistent with their design as *memory* functions. Moreover, if one then
reads 3.7.2 as allowing character to mean multibyte character, it is thought
that confusion could arise as to whether the number of multibyte characters
should be supplied rather than the number of bytes.

Although it is clear by 7.24.1 *String function conventions* paragraph 3

> For all functions in this sub clause, each character shall be interpreted as if
> it had the type `unsigned char`

that the number of bytes to be used corresponds to the size of a `unsigned
char`, one has to reference 6.2.6 *Representation of types* to learn that
`unsigned char` is in fact a single byte (consisting of `CHAR_BIT` bits).

It would be simpler and more to the point if the three memory functions describe
their count parameter `n` in terms of bytes.

### Suggested Technical Corrigendum

**memcpy**

Change 7.24.2.1 p 2 first sentence from

> The `memcpy` function copies `n` <ins>characters</ins> from the object pointed
> to by `s2` into the object pointed to by `s1`.

to

> The `memcpy` function copies `n` <ins>bytes</ins> from the object pointed to by
> `s2` into the object pointed to by `s1`.

**memmove**

Change 7.24.2.2 p 2 from

> The `memmove` function copies `n` <ins>characters</ins> from the object pointed
> to by `s2` into the object pointed to by `s1`. Copying takes place as if the `n`
> <ins>characters</ins> from the object pointed to by `s2` are first copied into a
> temporary array of `n` <ins>characters</ins> that does not overlap the objects
> pointed to by `s1` and `s2`, and then the `n` <ins>characters</ins> from the
> temporary array are copied into the object pointed to by `s1`.

to

> The `memmove` function copies `n` <ins>bytes</ins> from the object pointed to by
> `s2` into the object pointed to by `s1`. Copying takes place as if the `n`
> <ins>bytes</ins> from the object pointed to by `s2` are first copied into a
> temporary array of `n` <ins>bytes</ins> that does not overlap the objects
> pointed to by `s1` and `s2`, and then the `n` <ins>bytes</ins> from the
> temporary array are copied into the object pointed to by `s1`.

**memcmp**

Change 7.24.4.1 p 2 from

> The `memcmp` function compares the first `n` <ins>characters</ins> of the object
> pointed to by `s1` to the first `n` <ins>characters</ins> of the object pointed
> to by `s2`.

to

> The `memcmp` function compares the first `n` <ins>bytes</ins> of the object
> pointed to by `s1` to the first `n` <ins>bytes</ins> of the object pointed to by
> `s2`.

---

Comment from WG14 on 2014-10-31:

Oct 2013 meeting

### Proposed Committee Response

> After reviewing the original motivation and suggestion for change, it was noted
> by the project editor that "character" is used in several distinct contexts, and
> that it would be inappropriate to simply improve one area without a
> comprehensive review of all uses such that the existing consistency of uses of
> character be replaced in a consistent new manner, as yet undetermined. As it
> stands, although careful reading is strictly required, it is correct and as such
> this is not a defect.


</div>


---

---

<div id="issue0447">

## Issue 0447: Boolean from complex

Authors: WG 14, Fred J. Tydeman  
Date: 2013-08-20  
Reference document: [N1739,](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1739.htm) [DR 285](log_c99.md#issue0285)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0285](log_c99.md#issue0285)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

What is the value of: `_Bool b = 0.0 + 3.0*I;`

I believe that there is a contradiction between **6.3.1.2 Boolean type** and
**6.3.1.7 Real and complex** in that one requires that the value to be 1 and the
other requires the value to be 0\.

> **6.3.1.2 Boolean type**
>
> 1 When any scalar value is converted to **\_Bool**, the result is 0 if the value
> compares equal to 0; otherwise, the result is 1\.
>
> **6.3.1.7 Real and complex**
>
> 2 When a value of complex type is converted to a real type, the imaginary part
> of the complex value is discarded and the value of the real part is converted
> according to the conversion rules for the corresponding real type.

DR 285 against C99 had a similar issue on conversion from imaginary to boolean.
That resulted in:

> **G.4.2 Real and imaginary**
>
> 1 When a value of imaginary type is converted to a real type other than
> **\_Bool**,376) the result is a positive zero.
>
> 376\) See 6.3.1.2.

### Suggested Technical Corrigendum

I believe that **6.3.1.7 Real and complex**, paragraph 2 should be changed to:

> 2 When a value of complex type is converted to a real type other than
> **\_Bool**(footnote), the imaginary part of the complex value is discarded and
> the value of the real part is converted according to the conversion rules for
> the corresponding real type.
>
> (footnote) See 6.3.1.2.

---

Comment from WG14 on 2017-11-03:

### Committee Discussion

> The committee agrees.

### Proposed Technical Corrigendum

Change 6.3.1.7, paragraph 2 to:

> When a value of complex type is converted to a real type other than
> **\_Bool**(footnote), the imaginary part of the complex value is discarded and
> the value of the real part is converted according to the conversion rules for
> the corresponding real type.
>
> (footnote) See 6.3.1.2.


</div>


---

---

<div id="issue0448">

## Issue 0448: What are the semantics of a **\# non-directive**?

Authors: WG 14, Fred J. Tydeman  
Date: 2013-08-20  
Reference document: [N1740,](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1740.htm) [DR 231](log_c99.md#issue0231), [DR 250](log_c99.md#issue0250)  
Status: Fixed  
Fixed in: C17  
Cross-references: [0231](log_c99.md#issue0231), [0250](log_c99.md#issue0250)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

What is a **directive name**? What are the semantics of a **\# non-directive**?

In particular, what should happen for a translation unit with these four lines:

> ```c
> # non-directive
> # "Long string"
> # 'Many characters are implementation defined'
> # 1234
> ```

The syntax in **6.10 Preprocessing directives** has in group-part:

> \# non-directive

The C standard section 6.10, paragraph 3 has:

> A non-directive shall not begin with any of the directive names appearing in the
> syntax.

I find that confusing as **directive name** is only used in the C standard in
6.10 paragraphs 3 and 4 (without any definition). So, what is a **directive
name**?

Assuming **directive name** is one of:

* if
* ifdef
* ifndef
* elif
* else
* endif
* include
* define
* undef
* line
* error
* pragma

then my four line program contains lines that are

> \# non-directive

so should be valid. However, almost every C compiler I have tried considers them
errors that end translation. I did find at least one C compiler that ignored
them (treated them as comments). I did find at least one C compiler that
considered them errors even inside of:

> ```c
> #if 0
> #endif
> ```

where they should have been ignored.

I believe that gcc treats

> ```c
> # 1234
> ```

the same as:

> ```c
> # line 1234
> ```

I see no semantics for non-directive. So, what is supposed to happen with them?
Is it implicitly undefined?

Since preprocessing directives (which includes non-directive) are deleted at the
end of translation phase 4, these non-directives could act as comments.

DRs 231 and 250 appear to contradict each other on what happens with a
non-directive and neither refers to the other.

[DR 231](log_c99.md#issue0231) Says that text-line and non-directive are not
implementation defined. They are placeholders in the phases of translation and
are subject to normal processing in subsequent phases of translation. And that
words were supposed to be added to the Rationale.

[DR 250](log_c99.md#issue0250) Says that non-directive is a preprocessing directive. And,
it added that as a footnote in 6.10.3#11

Neither DR added normative words.

In answering this, we should consider what happens with mis-spellings, such as:

* #endf
* #deifine

Should **\# non-directive** be a comment (and ignored)? Implementation defined?
An error that ends translation (like #error)? Undefined behaviour?

### Suggested Technical Corrigendum

Since I do not know what should happen, I have none. But, if we decide on
undefined behaviour, I would like that as explicit words.

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

> There is intentional vagueness in this area such that implementations have and
> exhibit unspecified and useful additional behaviors. This has been a source of
> historical confusion and should be addressed.

Oct 2014 meeting

### Committee Discussion

> A small change was identified and made in the Proposed Technical Corrigendum.

### Proposed Technical Corrigendum

Add new paragraph 6.10 paragraph 9:

> The execution of a non-directive preprocessing directive results in undefined
> behavior.

Add to Annex J.2:

> The execution of a non-directive preprocessing directive (6.10)


</div>


---

---

<div id="issue0449">

## Issue 0449: What is the value of TSS\_DTOR\_ITERATIONS for implementations with no maximum?

Authors: WG 14, Douglas Walls  
Date: 2013-08-24  
Reference document: [N1744](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1744.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

### Suggested Technical Corrigendum

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

### Committee Discussion

* The committee notes that existing practice in all cases has provided a small integer value for this definition.
* Allowing no restrictions is likely to break existing practice.

Apr 2014 meeting

### Committee Discussion

> The question posed should be answered.

### Proposed Committee Response

> The standard intentionally does not define a value of `TSS_DTOR_ITERATIONS` for
> implementations with no maximum.
>
> The `TSS_DTOR_ITERATIONS` macro is used to limit recursion at thread
> termination. The issue is that existing practice allows the creation of new
> `tss` bindings during the destructor call, and one destructor might reincarnate
> the original, thus forming an infinite recursive destructor loop. This loop may
> appear non-deterministically and is difficult to detect. The purpose of
> `TSS_DTOR_ITERATIONS` is as a bound to such recursion.
>
> It is possible monitor the recursion depth with careful defensive programming
> and in those cases the value of `TSS_DTOR_ITERATIONS` is useful as that bound.


</div>


---

---

<div id="issue0450">

## Issue 0450: `tmpnam_s` clears `s[0]` when `maxsize > RSIZE_MAX`

Authors: WG 14, Martin Sebor  
Date: 2013-09-02  
Reference document: [N1752](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1752.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

> The majority of bounds checking functions are specified to set the first element
> of the destination buffer, `s[0]`, to the NUL character when a constraint
> violation occurs and the `s` pointer is non-null and the size of the buffer is
> greater than zero and less than or equal to `SIZE_MAX`.
>
> However, the `tmpnam_s` function sets `s[0]` to NUL even when `maxsize` is
> greater than `RSIZE_MAX`, making its behavior on constraint violation
> inconsistent with the rest.

#### Suggested Technical Corrigendum:

> Change paragraph 8 in the Returns section of tmpnam\_s to read:
>
> * If no suitable string can be generated, or if there is a runtime-constraint violation and `s` is not null and `maxsize` is greater than zero and not greater than `RSIZE_MAX`, the `tmpnam_s` function sets `s[0]` to the null character and returns a nonzero value.

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

> The committee agrees with the issue, and requests that the suggested technical
> corrigendum be broken into more parts for both clarity and consistency.

Apr 2014 meeting

### Committee Discussion

> The committee did not receive revised words and will again solicit them from the
> author.

Oct 2014 meeting

### Committee Discussion

> The paper [N1873](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1873.htm)
> was provided and discussed, and after several revisions the following proposal
> were approved.

### Proposed Technical Corrigendum

Change K.3.5.1.2 paragraph 8 (the Returns section of `tmpnam_s`) from:

> If no suitable string can be generated, or if there is a runtime-constraint
> violation, the `tmpnam_s` function writes a null character to `s[0]` (only if
> `s` is not null and `maxsize` is greater than zero) and returns a nonzero value.

to:

> If no suitable string can be generated, or if there is a runtime-constraint
> violation, the `tmpnam_s` function:
>
> * if `s` is not null and `maxsize` is both greater than zero and not greater than `RSIZE_MAX`, writes a null character to `s[0]`
> * returns a nonzero value.


</div>


---

---

<div id="issue0451">

## Issue 0451: Instability of uninitialized automatic variables

Authors: WG 14, Freek Wiedijk and Robbert Krebbers (Radboud University Nijmegen, The Netherlands)  
Date: 2013-08-30  
Reference document: [N1747](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1747.htm)  
Status: Closed  
Cross-references: [0260](log_c99.md#issue0260)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The standard is unclear about the following questions:

1. Can an uninitialized variable with automatic storage duration (of a type that does not have trap values, whose address has been taken so 6.3.2.1p2 does not apply, and which is not volatile) change its value without direct action of the program?
2. If the answer to question 1 is "yes", then how far can this kind of "instability" propagate?
3. If "unstable" values can propagate through function arguments into a called function, can calling a C standard library function exhibit undefined behavior because of this?

Specifically, consider:

```c
unsigned char x[1]; /* intentionally uninitialized */
printf("%d\n", x[0]);
printf("%d\n", x[0]);
```

Does the standard allow an implementation to let this code print two different
values? And if so, if we insert either of the following three statements

```c
x[0] = x[0];
x[0] += 0;
x[0] *= 0;
```

between the declaration and the `printf` statements, is this behavior still
allowed? Or alternatively, can these `printf` statements exhibit undefined
behavior instead of having to print a reasonable number.

#### Motivation and discussion

The standard is unclear about these questions.

On the one hand the committee response to [Defect Report #260](log_c99.md#issue0260)
strongly suggests that the committee decided that the standard implies the
answer to question 1 to be "yes". (Although Defect Report #260 applies to the
C99 standard and hence has been superseded by the C11 standard, no modification
to the standard text was deemed necessary at the time, and all relevant text in
the C11 standard is identical to that in the C99 standard.) The relevant quote
from the committee response to Defect Report #260 is:

> In the case of an indeterminate value \[...\] the actual bit-pattern may change
> without direct action of the program.

A subtlety is that Defect Report #260 talks about bit-patterns and not about
values, but for variables of type `unsigned char` there is a one-to-one
correspondence between bit-patterns and values.

Another argument in favor of "instability" of indeterminate values is that
values can "become indeterminate" (e.g. 5.1.2.3p5, 6.2.4p2, and 6.2.4p6). In
these cases the value of an object may also change without an explicit store
(and can keep changing?)

On the other hand, 6.7.9p10 states that the kind of uninitialized variables that
we are discussing get an indeterminate value. From 3.19.2 it follows that if a
type has no trap values, then indeterminate and unspecified values are the same.
And in 3.19.3, it is stated explicitly that an unspecified value is *chosen*.
Which implies that the value \- after having been chosen \- cannot change
anymore.

Another argument against "instability" is that 6.8p3 states that "the values are
stored in the objects (including *storing* an indeterminate value in objects
without an initializer) each time the declaration is reached in the order of
execution", and that 6.2.4p2 states that "An object \[...\] retains its
last-*stored* value throughout its lifetime." The only way that one could read
this in light of Defect Report #260 is if "retaining an indeterminate value" is
read as meaning that the indeterminateness of the value is retained, without the
value having a *specific* value.

It seems attractive to make a distinction between *indeterminate* values that
are allowed to change without direct action of the program in the way that
Defect Report #260 interpreted the standard, and *unspecified* values that do
not have this property. However the current text of 3.19.2 does not allow for
this interpretation. Also, probably some instances of "indeterminate" and
"unspecified" would need to be changed for such an interpretation to make sense.
(For example in 6.2.6.1p6 "the bytes of the object representation that
correspond to any padding bytes take unspecified values." should probably become
"... take indeterminate values.")

The reason for question 3 is that *if* the kind of "instability" that questions
1 and 2 ask for is allowed to propagate maximally, then it becomes impossible to
implement `printf` in C itself. When converting an indeterminate value to a
string of output characters, the value can *keep* changing underneath, and the
code cannot protect itself against this.

On the other hand, if library functions exhibit undefined behavior on these
kinds of "unstable" uninitialized values, then an `fwrite` of a struct with
uninitialized padding bytes would also give undefined behavior. The fact that
one wants to be able to copy uninitialized padding bytes in structs using
`memcpy` without undefined behavior is the reason that using the value of an
uninitialized object is not undefined behavior. This seems to suggest that an
`fwrite` of a struct with uninitialized padding bytes should *not* exhibit
undefined behavior.

### Possible Resolutions

We see three reasonable sets of answers to these questions:

#### Resolution (a)

1. no
2. not applicable
3. not applicable

##### Advantage

Easy to repair the unclarity in the standard. Just add text that explicitly
states that indeterminate values cannot change without direct action from the
program. This will prevent people from invoking the response to Defect Report
#260 from then on.

##### Disadvantage

Restricts the kind of optimizations compilers are allowed to perform.

#### Resolution (b)

1. yes
2. any operation performed on indeterminate values will have an indeterminate value as its result
3. no

Specifically, "unstable" values will also propagate through function calls.
Also, after

```c
x[0] *= 0;
```

the value of `x[0]` *still* will be "unstable" and hence still can be any byte,
and will not necessary be `0`.

##### Advantage

Gives compilers more freedom to perform optimizations.

Is Defect Report #260-compliant (i.e., "the committee did not change its mind").

##### Disadvantage

Needs more modifications to the text of the standard. It will then be necessary
to make an explicit distinction between "indeterminate non-trap value" and
"unspecified value".

#### Resolution (c)

1. yes
2. any operation performed on indeterminate values will have an indeterminate value as its result
3. yes, library functions will exhibit undefined behavior when used on indeterminate values (probably functions like `memcpy` and maybe `fwrite` should be immune from this)

##### Advantage

Restricts program behaviors least, giving compilers even more freedom.

##### Disadvantage

Needs even more modification to the text of the standard.

Needs a decision on what library functions will *not* have undefined behavior
when working on indeterminate values.

This is certainly not compatible with the current version of the standard, as no
undefined behavior of this kind related to library functions is described there.

### Suggested Technical Corrigendum

##### For resolution (a)

In 6.2.4p2, change "An object exists, has a constant address, and retains its
last-stored value throughout its lifetime." to "An object exists and has a
constant address throughout its lifetime. The value of an object is retained,
including the object representation, until some other value is stored into it,
or until the moment when the value becomes indeterminate (at which moment it is
replaced with an indeterminate value, and after which that value is retained
again)."

##### For resolution (b)

In 3.19.2 change "either an unspecified value or a trap representation" to
"either an unspecified value or a trap representation, which can change
arbitrarily without direct action from the program".

In 6.2.4p2, change "An object exists, has a constant address, and retains its
last-stored value throughout its lifetime." to "An object exists, has a constant
address, and retains its last-stored value (provided this value is not
indeterminate), throughout its lifetime."

At the end of 6.5p1 add "If at least one of the operands of an operator is
indeterminate, the result of the operator is also indeterminate."

Some instances of "indeterminate" and "unspecified" (to be determined) should be
replaced by respectively "unspecified" and "indeterminate". See for example the
instance in 6.2.6.1p6 mentioned earlier.

##### For resolution (c)

The changes for resolution (b), and also:

In 7.1.4p1 add: "If a function is called with an indeterminate value, the
behavior is undefined."

In a selection (to be determined) of functions from the library, add text that
counters this general statement added to 7.1.4p1.

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

### Committee Discussion

* The committee asserts that the answer to the first question is "yes", an uninitialized value under the conditions described can appear to change its value.
* Since question 2 is applicable, the answer is that any operation performed on indeterminate values will have an indeterminate value as its result.
* The answer to the applicable question 3 is that indeed library functions will exhibit undefined behavior when used on indeterminate values.
* The committee notes that the problem applies to all types that do not have trap representations as per the implementation.
* Strong sentiment formed, in part based on prior experience in developing Annex L, that a new category of "wobbly" value is needed. The underlying issue is that modern compilers track value propagation, and uninitialized values synthesized for an initial use of an object may be discarded as inconsequential prior to synthesizing a different value for a subsequent use. To require otherwise defeats important compiler optimizations. All uses of "wobbly" values might be deemed undefined behavior.
* The principle of Resolution C is desired.
* This requires careful thought.

Apr 2014 meeting

### Committee Discussion

> The author provided
> [N1793](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1793.pdf) and an
> accompanying presentation
> [N1818](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1818.pdf) in which his
> position changed to believing that "wobbly" values are not actually defined by
> the standard, and after discussion agreed that the following committee response
> would be an acceptable resolution.

### Proposed Committee Response

* The answer to question 1 is "yes", an uninitialized value under the conditions described can appear to change its value.
* The answer to question 2 is that any operation performed on indeterminate values will have an indeterminate value as a result.
* The answer to question 3 is that library functions will exhibit undefined behavior when used on indeterminate values.
* These answers are appropriate for all types that do not have trap representations.
* This viewpoint reaffirms the C99 DR260 position.
* The committee agrees that this area would benefit from a new definition of something akin to a "wobbly" value and that this should be considered in any subsequent revision of this standard.
* The committee also notes that padding bytes within structures are possibly a distinct form of "wobbly" representation.


</div>


---

---

<div id="issue0452">

## Issue 0452: Effective Type in Loop Invariant

Authors: WG 14, Shao Miller  
Date: 2013-09-29  
Reference document: [N1762](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1762.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The definition for "effective type" does not appear to apply to non-lvalue
expressions. This can cause a behavioural difference, in loops.

6.5p6:

> The effective type of an object for an access to its stored value is the
> declared type of the object, if any.87) If a value is stored into an object
> having no declared type through an lvalue having a type that is not a character
> type, then the type of the lvalue becomes the effective type of the object for
> that access and for subsequent accesses that do not modify the stored value. If
> a value is copied into an object having no declared type using memcpy or
> memmove, or is copied as an array of character type, then the effective type of
> the modified object for that access and for subsequent accesses that do not
> modify the value is the effective type of the object from which the value is
> copied, if it has one. For all other accesses to an object having no declared
> type, the effective type of the object is simply the type of the lvalue used for
> the access.

Given the following code:

> union u1 {  
>     int x;  
>     long y;  
>   };  
>
> int func1(void) {  
>     union u1 o1 \= { 42 };  
>
>     return (0, o1).x;  
>   }

The `o1` sub-expression in the `return` statement's expression accesses the
stored union value of the object. The comma operator's result has that value,
but it is not an lvalue and so "effective type" does not appear to apply. While
the access to `o1` involves an access to a stored value, the membership operator
can be said to access an object whose value is available, but perhaps not
exactly "stored." `o1.x` is an lvalue, but `(0, o1).x` is not.

6.5.2.3p3:

> A postfix expression followed by the . operator and an identifier designates a
> member of a structure or union object. The value is that of the named member,95)
> and is an lvalue if the first expression is an lvalue. If the first expression
> has qualified type, the result has the so-qualified version of the type of the
> designated member.

6.5p7:

> An object shall have its stored value accessed only by an lvalue expression that
> has one of the following types:88)
>
> * a type compatible with the effective type of the object,
> * a qualified version of a type compatible with the effective type of the object,
> * a type that is the signed or unsigned type corresponding to the effective type of the object,
> * a type that is the signed or unsigned type corresponding to a qualified version of the effective type of the object,
> * an aggregate or union type that includes one of the aforementioned types among its members (including, recursively, a member of a subaggregate or contained union), or
> * a character type.

Given:

> union u2 {  
>     int x;  
>     long y;  
>     char ca\[2\];  
>   };  
>
> int func2(void) {  
>     union u2 o2 \= { 42 };  
>
>     return (0, o2).x;  
>   }

We have a similar situation, even though `(0, o2)` yields an object with
temporary lifetime. (Side question: Should the expression `(0, o2).ca == o2.ca`
yield zero, non-zero, or should it be implementation-defined?)

Suppose we have a portable strategy to determine whether or not the object
representations of `int` and `long` are the same. If they are and if we have the
following code:

> union u3 {  
>     int x;  
>     long y;  
>   };  
>
> long func3(void) {  
>     union u3 o3;  
>
>     o3.x \= 42;  
>     return (0, o3).y;  
>   }

Are we violating the effective type rules? We might expect type-punning to be
relevant here and the membership operator to be accessing a member value of a
union value.

If the answer is yes, then does the Standard define the effective type of the
non-lvalue expression `0, o3` ?

If the answer is no, then this can cause the loss of an optimization opportunity
in the following code:

> struct s4 {  
>     int x;  
>     float f;  
>   };  
>
> void func4(long \* lp, struct s4 \* s4p) {  
>     int c;  
>
>     for (c \= 0; c \< (0, \*s4p).i; \+\+c)  
>       --\*lp;  
>   }

We do not expect `*lp` to alias into `*s4p`, so we might optimize this loop such
that `(0, *s4p).i` is only computed once. If, in another translation unit, it
turned out that these did alias, the optimization would normally be justified
based on a violation of the effective type rules. If there isn't a violation
because of the non-lvalue nature of the comma operator's expression, then the
optimization would not appear to be justified.

### Suggested Technical Corrigendum

None.

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

> The committee did not have adequate time to consider these issues and intends
> that these issues be further refined through consultation with the author.

Apr 2014 meeting

### Committee Discussion

> Further input was not received from the author and will again be solicited.

Oct 2014 meeting

### Committee Discussion

> Discussion with the author clarified these issues, and the paper
> [N1888](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1888.htm) was
> discussed. From that, we extract the following example
>
> > ```c
> > union u2 {
> >     int x;
> >     long y;
> >     char ca[2];
> > };
> >
> > int func2(void) {
> >     union u2 o2 = { .ca = "a" };
> > ```
>
> and question, what is the result of `(0,o2).ca == o2.ca`?
>
> Given that the comma operator doesn't yield an lvalue (6.5.17), and from 6.2.4p8
> such a non-lvalue expression is stated to have automatic storage duration, this
> seems to require that the answer is false, even though this defeats compiler
> optimizations.
>
> The effective type rule 6.5.p6 also does not seem to apply to objects with
> temporary lifetime, and has undesirable consequences.
>
> The direction the committee would like to go is something like:
>
> In 6.2.4p8, append
>
> > An object with temporary lifetime behaves as if it had the declared type of its
> > value. Such an object is known as a *temporary object*. A temporary object need
> > not have a unique address.
>
> Apr 2015 meeting
>
> ### Committee Discussion
>
> > The following words were drafted and approved by the committee as the Proposed
> > Technical Corrigendum.
>
> ### Proposed Committee Response
>
> > To the question "Should the expression `(O, o2).ca == o2.ca` yield zero,
> > non-zero, or should it be implementation defined?" the answer is "implementation
> > defined".
> >
> > With the following changes, the effective type of `O, o3` is defined.
>
> ### Proposed Technical Corrigendum
>
> In 6.2.4p8, append
>
> > An object with temporary lifetime behaves as if it were declared with the type
> > of its value for the purposes of effective type. Such an object need not have a
> > unique address.
> >
> > (add forward reference to 6.5p6 to this section)


</div>


---

---

<div id="issue0453">

## Issue 0453: Atomic flag type and operations

Authors: WG14, Fred J. Tydeman (USA)  
Date: 2013-10-22  
Reference document: [N1776](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1776.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

It appears to me that there is a wording problem in 7.17.8.\*

> 7.17.8 Atomic flag type and operations  
> #1: The **atomic\_flag** type provides the classic test-and-set functionality.
> It has two states, set and clear.
>
> 7.17.8.1 The atomic\_flag\_test\_and\_set functions  
> #2: Atomically sets the value pointed to by **object** to true.
>
> #3: Atomically, the value of the object immediately before the effects.
>
> 7.17.8.2 The atomic\_flag\_clear functions  
> #2: Atomically sets the value pointed to by **object** to false.

An issue is states (set, clear) versus values (true, false).

Does an atomic\_flag structure have both states (set, clear) and values (true,
false)? Can it have all four combinations?

Another issue is 'set' is used both as a verb and a noun.

Another issue is: While the test is atomic, and the set is atomic, it is not
clear that both test and set are part of the same atomic operation.

I have been told that the same issues exists in the C\+\+ standard (29.7
\[atomics.flag\]).

There was discussion of these topics on the WG14 reflector (around messages
13067 to 13073\)

One person in the discussion would like the value zero (from default static
initialization) to be the clear state. They also mentioned DR 421\.

Based upon the email discussion, the intent was that flags logically have
exactly two states: "set" and "clear". The test\_and\_set operation returns true
if it was "set", and false if it was "clear". Test\_and\_set sets the state to
"set", and the clear operations set the state to "clear". The value zero need
not be the "clear" state.

### Suggested Technical Corrigendum

Replace

> 7.17.8.1 The atomic\_flag\_test\_and\_set functions  
> #2: Atomically sets the value pointed to by **object** to true.
>
> #3: Atomically, the value of the object immediately before the effects.
>
> 7.17.8.2 The atomic\_flag\_clear functions  
> #2: Atomically sets the value pointed to by **object** to false.

with:

> 7.17.8.1 The atomic\_flag\_test\_and\_set functions  
> #2: Tests the state of the flag pointed to by **object** and then sets the flag,
> as a single atomic operation.
>
> #3: Returns true if the flag was set when tested or false otherwise.
>
> 7.17.8.2 The atomic\_flag\_clear functions  
> #2: Atomically clears the flag pointed to by **object**.

Add to the rationale in the section on atomic flag:

> The atomic flag type is defined in terms of states, not values, as the value
> zero (false) need not be the "clear" state. The committee knows of one
> implementation where zero is the "set" state.

---

Comment from WG14 on 2017-11-03:

Apr 2014 meeting

### Committee Discussion

* The committee agrees that the use of *true* and *false* are inaccurate.
* The committee does not feel that the proposed words are a sufficient resolution, however, and has solicited a new paper to resolve the issue.

Oct 2014 meeting

### Committee Discussion

> The paper [N1853](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1853.htm)
> was provided and discussed, revised, discussed further, and a further paper was
> solicited. In particular, the committee did not like "converted to a \_Bool"
> because it implies some unspecified arithmetic conversion.

Apr 2015 meeting

### Committee Discussion

> The paper [N1908](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1908.pdf)
> was provided and discussed. "Clears" the flag was vaguely troubling and a new
> approach was offered:
>
> > In 7.17.8.1p2, change:
> >
> > Atomically sets the value pointed to by `object` to true.
> >
> > to:
> >
> > Atomically places the atomic flag pointed to by `object` in the set state and
> > returns the value corresponding to the immediately preceding state.
> >
> > In 7.17.8.1p3, change:
> >
> > Atomically, the value of the object immediately before the effects.
> >
> > to:
> >
> > The `atomic_flag_test_and_set` functions return the value that corresponds to
> > the state of the atomic flag immediately before the effects. The return value
> > true corresponds to the set state and the return value false corresponds to the
> > clear state.
> >
> > In 7.17.8.2p2, change:
> >
> > Atomically sets the value pointed to by `object` to false.
> >
> > to:
> >
> > Atomically places the atomic flag pointed to by `object` into the clear state.

Oct 2015 meeting

### Committee Discussion

> The direction developed late at the last meeting is adopted as the Proposed
> Technical Corrigendum.

### Proposed Technical Corrigendum

In 7.17.8.1p2, change:

> Atomically sets the value pointed to by `object` to true.

to:

> Atomically places the atomic flag pointed to by `object` in the set state and
> returns the value corresponding to the immediately preceding state.

In 7.17.8.1p3, change:

> Atomically, the value of the object immediately before the effects.

to:

> The `atomic_flag_test_and_set` functions return the value that corresponds to
> the state of the atomic flag immediately before the effects. The return value
> true corresponds to the set state and the return value false corresponds to the
> clear state.

In 7.17.8.2p2, change:

> Atomically sets the value pointed to by `object` to false.

to:

> Atomically places the atomic flag pointed to by `object` into the clear state.


</div>


---

---

<div id="issue0454">

## Issue 0454: ATOMIC\_VAR\_INIT (issues 3 and 4\)

Authors: WG14, Fred J. Tydeman (USA)  
Date: 2013-10-22  
Reference document: [N1777](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1777.htm)  
Status: Closed  
Cross-references: [0422](log_c11c17.md#issue0422), [0427](log_c11c17.md#issue0427)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

I see several issues with **ATOMIC\_VAR\_INIT**. They could be turned into one
combined defect report, or separate defects, or folded into DR 422\.

Consider the following code:

```c
#include <stdatomic.h>
int main(void){
 atomic_int guide1 = ATOMIC_VAR_INIT(42); /* known value(42); WHAT STATE? */
 atomic_int guide2;        /* indeterminate value; indeterminate state */
 atomic_int guide3 = 42;   /* known value(42); indeterminate state */
static atomic_int guide4;  /* known value(0); valid state */
static atomic_int guide5 = 42; /* known value(42); valid state */
 atomic_int guide6;
 atomic_init(&guide6, 42); /* known value(42); initialized state */
 return 0;
}
```

What is the status of the additional state carried for guide1?

* Implicitly undefined
* Indeterminate
* Valid
* Initialized
* Something else

Is the state of guide1 the same as what guide6 has? If yes, does
"initialization-compatible" mean do the same thing as if atomic\_init() of the
same object with the same value?

* (Issue 3 from N1777)

  **ATOMIC\_VAR\_INIT** is not usable in assignment to an atomic object.

  I see no difference between:

  ```c
  atomic_int guide = ATOMIC_VAR_INIT(42);
  ```

  and

  ```c
  atomic_int guide;
  guide = ATOMIC_VAR_INIT(42);
  ```

  I would hope that initialization (which looks like an assignment in a
  declaration) and a simple assignment would be equivalent and
  **ATOMIC\_VAR\_INIT** could be used in either context.
* (Issue 4 from N1777)

  What should happen if **ATOMIC\_VAR\_INIT**(value) is used in context other than initializing an atomic object of the same type as the value?

  Should it be undefined behaviour? A constraint violation? Just the value
  **value** converted to the type of the object?

  ```c
  atomic_float f = ATOMIC_VAR_INIT(42); /* type mis-match */

  int nonAtomic = ATOMIC_VAR_INIT(42); /* non-atomic object */

  if( ATOMIC_VAR_INIT(42) ){...};
  guide1 = 1729 + ATOMIC_VAR_INIT(42) * 3;

  void func( atomic_int ai ); /* function parm/arg */
  func( ATOMIC_VAR_INIT(42) ); /* DR 427 is now making this
                               initialization (not assigment) */
  ```

  DR 427 is changing how a function parameter is getting its value from the actual
  argument from assignment to initialization (to get around const). Would this
  initialization be a valid context for **ATOMIC\_VAR\_INIT**?

### Suggested Technical Corrigendum

* In the first sentence of 7.17.2.1#2, after

  > suitable for initializing

  add the words

  > or assigning to
* Add to 7.17.2.1 as a constraint or a new paragraph between 3 and 4:

  > If **ATOMIC\_VAR\_INIT** is used in a context other than initialization \[or
  > assignment\] of an atomic object of a compatible type of the value, the
  > behaviour is undefined.

---

Comment from WG14 on 2015-04-17:

Apr 2014

### Proposed Committee Response

> The **ATOMIC\_VAR\_INIT** macro prepares an atomic value that includes any extra
> state necessary for a non-lock-free type. Initialization, by definition, ignores
> all previous state. Assignment must honor the extra state that would indicate
> another atomic operation in progress; such an assignment takes the non-atomic
> corresponding value resulting from removing all qualifiers including atomic from
> the value expression, and will manipulate the extra state held in the object to
> assure proper atomic assignment semantics. **ATOMIC\_VAR\_INIT** produces a
> value appropriate for initialization because it will have any necessary extra
> state, whereas a value suitable for assignment is the non-qualified version of
> the assignment expression.
>
> All uses of **ATOMIC\_VAR\_INIT** other than for initialization result in
> implicitly undefined behavior.


</div>


---

---

<div id="issue0455">

## Issue 0455: ATOMIC\_VAR\_INIT issue 5

Authors: WG14, Fred J. Tydeman (USA)  
Date: 2013-10-22  
Reference document: [N1777](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1777.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

I see several issues with **ATOMIC\_VAR\_INIT**. They could be turned into one
combined defect report, or separate defects, or folded into DR 422\.

Consider the following code:

```c
#include <stdatomic.h>
int main(void){
 atomic_int guide1 = ATOMIC_VAR_INIT(42); /* known value(42); WHAT STATE? */
 atomic_int guide2;        /* indeterminate value; indeterminate state */
 atomic_int guide3 = 42;   /* known value(42); indeterminate state */
static atomic_int guide4;  /* known value(0); valid state */
static atomic_int guide5 = 42; /* known value(42); valid state */
 atomic_int guide6;
 atomic_init(&guide6, 42); /* known value(42); initialized state */
 return 0;
}
```

What is the status of the additional state carried for guide1?

* Implicitly undefined
* Indeterminate
* Valid
* Initialized
* Something else

Is the state of guide1 the same as what guide6 has? If yes, does
"initialization-compatible" mean do the same thing as if atomic\_init() of the
same object with the same value?

* (Issue 5 from N1777)

  Zero initialization of static atomic objects in C requires more than in C\+\+.

  I have been told that C's 7.17.2.1#2:

  > ...; however, the default (zero) initialization for objects with static or
  > thread-local storage duration is guaranteed to produce a valid state.

  is not in C\+\+. If true and assuming that the two languages should be the
  "same" here, should this be deleted from C? Added to C\+\+?

  DR 422 is somewhat related to this issue.

### Suggested Technical Corrigendum

* No suggestion on the requirements mis-match between C and C\+\+.

---

Comment from WG14 on 2015-10-29:

Apr 2014 meeting

### Committee Discussion

* The 7.17.2.1#2 words should not be deleted.
* Interoperability with C\+\+ atomics must be done by macros that use C\+\+'s declarative syntax for atomic variables. As such there is no direct compatibility issue as is asserted.

Oct 2014 meeting

### Committee Discussion

> There were was no substantiative further discussion.

### Proposed Committee Response

> Interoperability with C\+\+ atomics must be done by macros that use C\+\+'s
> declarative syntax for atomic variables. As such there is no direct
> compatibility issue as is asserted, and 7.17.2.1#2 shall remain.


</div>


---

---

<div id="issue0456">

## Issue 0456: Compile time definition of `UINT`*`N`*`_C(`*`value`*`)`

Authors: WG14, Rajan Bhakta  
Date: 2014-03-05  
Reference document: [N1798](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1798.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

With reference to ISO/IEC WG14 N1569, subclause 7.20.4.1: The macro
`UINT`*`N`*`_C(`*`value`*`)` shall expand to an integer constant expression
corresponding to the type `uint_least`*`N`*`_t`.

7.20.4 p1 imposes a stricter requirement on the form of the expansion; it must
be an integer constant (for which paragraph 2 points to 6.4.4.1).

The type described in 7.20.4 p3 for the result of the expansion has an
interesting property; we observe this for `uint_least16_t` without reference to
the `UINT16_C` macro by using `u'\0'` in a context where it will be first
promoted as part of the usual arithmetic conversions:

```c
#include <assert.h>

#if u'\0' - 1 < 0
  // Types: #if (uint_least16_t) - (signed int) < (signed int)
  // Due to 6.10.1 p4, near the reference to footnote 167,
  // after applying the integer promotions as part of 6.3.1.8 p1
  // to the operands of the subtraction, the expression becomes:
  // Types: #if (unsigned int) - (signed int) < (signed int)
  // Following 6.3.1.8 p1 through to the last point gives:
  // Types: #if (unsigned int) - (unsigned int) < (signed int)
  // Result: false
# error Expected large unsigned value.
#endif

int main(void) {
  // Types: assert((uint_least16_t) - (signed int) < (signed int))
  // Assuming that signed int can represent all values of uint_least16_t,
  // after applying the integer promotions as part of 6.3.1.8 p1
  // to the operands of the subtraction, the expression becomes:
  // Types: assert((signed int) - (signed int) < (signed int))
  // Result: true
  assert(u'\0' - 1 < 0);
  return 0;
}
```

The code presented should neither fail to compile nor abort when executed (for
example) on a system using two's complement and 8, 16 and 32 bits (respectively)
for `char`, `short` and `int` with no padding bits.

Consider the case for N \= 8 or 16 on systems with `INT_MAX` as \+2147483647,
`UCHAR_MAX` as 255 and `USHRT_MAX` as 65535: it is unclear how a macro can be
formed such that it expands to an integer constant that has the promoted signed
int type in phase 7 of translation and also the promoted `unsigned int` type in
phase 4 of translation without special (non-standard) support from the compiler.

Even if the requirement for an integer constant is relaxed to only require an
integer constant expression, the case for N \= 8 on systems with `INT_MAX` as
\+32767 and `UCHAR_MAX` as 255 remains a problem without the use of casts (since
`uint_least16_t`, for which we can form a literal, has different promotion
behaviour from `uint_least8_t`).

Implementations seen:

1. `#define UINT8_C(c) c ## U`
2. `#define UINT8_C(c) c`

DR 209 seemed to try to address the issue of needing special compiler support in
order to define the macros for integer constants; however, the problem seems to
remain.

### Suggested Technical Corrigendum

1. Add in suffixes for char and short literals.
2. Remove the `UINT{8,16}_C` macros from the standard.

---

Comment from WG14 on 2015-10-29:

Apr 2014 meeting

### Committee Discussion

* The committee believes that DR209 is still appropriate in that "compiler magic" must be used for the implementation of these macros.
* As such, both proposed resolutions were found inappropriate.

Oct 2014 meeting

### Proposed Committee Response

> The committee believes that DR209 is still appropriate in that "compiler magic"
> must be used for the implementation of these macros. The committee does not
> consider this a defect.
>
> As such, both proposed resolutions were found inappropriate.


</div>


---

---

<div id="issue0457">

## Issue 0457: The `ctime_s` function in Annex K defined incorrectly

Authors: WG14, David Keaton (suggested by Jens Gustedt)  
Date: 2014-03-13  
Reference document: [N1802](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1802.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The `ctime_s` function in Annex K was defined analogously to `ctime`, and some
of the text from the definition of `ctime` was copied and modified slightly.

K.3.8.2.2p4 states that `ctime_s` is equivalent to the following.

> ```c
> asctime_s(s, maxsize, localtime_s(timer))
> ```

In this case, the text from the original `ctime` definition was not quite
modified enough.  The `localtime_s` function takes two arguments and the above
code only supplies one.

### Suggested Technical Corrigendum

In K.3.8.2.2p4, replace

> ```c
> asctime_s(s, maxsize, localtime_s(timer))
> ```

with the following.

> ```c
> asctime_s(s, maxsize, localtime_s(timer, &(struct tm){ 0 }))
> ```

---

Comment from WG14 on 2017-11-03:

Apr 2014 meeting

### Proposed Technical Corrigendum

In K.3.8.2.2p4, replace

> ```c
> asctime_s(s, maxsize, localtime_s(timer))
> ```

with the following.

> ```c
> asctime_s(s, maxsize, localtime_s(timer, &(struct tm){ 0 }))
> ```


</div>


---

---

<div id="issue0458">

## Issue 0458: ATOMIC\_XXX\_LOCK\_FREE macros not constant expressions

Authors: WG14, [Martin Sebor](mailto:msebor@gmail.com)  
Date: 2014-03-18  
Reference document: [N1806](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1806.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Section **7.17.1 Introduction** (to section **7.17 Atomics** `<stdatomic.h>`)
specifies that the `<stdatomic.h>` header define a number of macros having the
form `ATOMIC_XXX_LOCK_FREE` that indicate the lock-free property of the
corresponding atomic types. No further description of the macros is provided
here.

Section **7.17.5 Lock-free property**, then goes on to specify that the atomic
lock-free macros (presumably the same ones as those listed in 7.17.1) expand to
one of three values: 0, 1, or 2\.

Neither of the two sections above, nor any other in the standard, specifies
whether or not the macros are required to expand to constant expressions usable
in preprocessor `#if` directives. This is in contrast to some other standard
macros such as those defined in `<limits.h>` which are typically so specified
using language such as:

> The values given below shall be replaced by constant expressions suitable for
> use in `#if` preprocessing directives.

As discussed in the thread starting with SC22WG14.13216, the only purpose for
the existence of the `ATOMIC_XXX_LOCK_FREE` macros is to be able to write more
efficient code by relying on their use in preprocessor `#if` conditionals. Thus,
the absence of the requirement that they expand to constant expressions makes
the macros unsuitable for that purpose.

### Suggested Technical Corrigendum

In section 7.17.1, modify paragraph 3 as indicated below:

> ...which <ins>expand to constant expressions suitable for use in `#if`
> preprocessing directives and which</ins> indicate the lock-free property of the
> corresponding atomic types (both signed and unsigned); and

---

Comment from WG14 on 2017-11-03:

Apr 2014 meeting

### Proposed Technical Corrigendum

In section 7.17.1 paragraph 3 change:

> ...which indicate the lock-free property of the corresponding atomic types (both
> signed and unsigned); and

to

> ...which expand to constant expressions suitable for use in `#if` preprocessing
> directives and which indicate the lock-free property of the corresponding atomic
> types (both signed and unsigned); and


</div>


---

---

<div id="issue0459">

## Issue 0459: atomic\_load missing const qualifier

Authors: WG14, [Martin Sebor](mailto:msebor@gmail.com)  
Date: 2014-03-22  
Reference document: [N1807](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1807.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The synopsis of the `atomic_load` pair of generic functions specified in
7.17.7.2 shows that they accept pointers to a `volatile`\- (bot not `const`-)
qualified type:

> ```c
>           #include <stdatomic.h>
>
>           C atomic_load(volatile A *object);
>           C atomic_load_explicit(volatile A *object,
>                                  memory_order order);
> ```

The absence of the `const` qualifier implies that the functions cannot be called
with an argument of type `const` *`A`*`*` since there is no such conversion.

However, since neither function modifies its argument, there is no need to
prevent it from being called with an argument of type `const` *`A`*`*`. And, in
fact, the latest draft C\+\+ standard as of this writing,
[N3936](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3936.pdf
"Working Draft, Standard for Programming Language C++"), does provide an
overload of each function that takes a `const volatile` pointer.

### Suggested Technical Corrigendum

In section 7.17.7.2, paragraph 1, **Synopsis**, modify the declarations of the
`atomic_load` pair of generic functions as indicated below:

> `#include <stdatomic.h>`  
>     
>           *`C`* `atomic_load(`<ins>`const`</ins> `volatile` *`A`* `*object);`  
>           *`C`* `atomic_load_explicit(`<ins>`const`</ins> `volatile` *`A`* `*object,`  
>                                  `memory_order order);`

---

Comment from WG14 on 2017-11-03:

Apr 2014 meeting

### Proposed Technical Corrigendum

In section 7.17.7.2, paragraph 1, **Synopsis**, modify the declarations of the
`atomic_load` pair of generic functions from:

> ```c
>           #include <stdatomic.h>
>
>           C atomic_load(volatile A *object);
>           C atomic_load_explicit(volatile A *object,
>                                  memory_order order);
> ```

to:

> ```c
>           #include <stdatomic.h>
>
>           C atomic_load(const volatile A *object);
>           C atomic_load_explicit(const volatile A *object,
>                                  memory_order order);
> ```


</div>


---

---

<div id="issue0460">

## Issue 0460: `aligned_alloc` underspecified

Authors: WG14, [Martin Sebor](mailto:msebor@gmail.com)  
Date: 2014-03-22  
Reference document: [N1808](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1808.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The `aligned_alloc` function specifies the following constraints on its
arguments, `alignment` and `size`:

> The value of `alignment` shall be a valid alignment supported by the
> implementation and the value of `size` shall be an integral multiple of
> alignment.

Therefore, the behavior of the function is undefined when either constraint is
violated.

According to section 6.2.8, paragraph 1, the greatest alignment a conforming
implementation is required to support (known as *fundamental alignment*) is
`_Alignof(max_align_t)`. Furthermore, according to paragraph 2 of the same
section, whether alignments greater than the fundamental alignment (known as
*extended alignments*) are supported and in what contexts is
implementation-defined.

The standard specifies no mechanism by which programs could determine whether an
extended alignment is supported by an implementation, or whether the
`aligned_alloc` function is among the contexts where an extended alignment is
supported.

As a result, there is no way for strictly conforming programs to use the
`aligned_alloc` function with an `alignment` argument greater than the result of
`_Alignof(max_align_t)`. Since the `malloc` function returns objects that meet
the same alignment requirement, this restriction makes `aligned_alloc` useless
in portable programs.

This restriction is unnecessary since it's possible, and in fact nearly trivial
given access to the internal details of the memory allocator, to implement an
efficient `aligned_function` that fails when its arguments don't meet the
specified requirements.

As a data point, the POSIX Advanced Realtime function
[`posix_memalign`](http://pubs.opengroup.org/onlinepubs/9699919799/functions/posix_memalign.html),
as well as the historical BSD `memalign` function, are both required to return a
null pointer when either of their arguments don't meet the specified
requirements (in addition to setting `errno` to `EINVAL`.

### Suggested Technical Corrigendum

The proposed corrigendum below changes the standard to require `aligned_alloc`
to fail by returning a null pointer when either of its constraints is violated.

In section 7.22.3.1, modify paragraph 2 as indicated below:

> The `aligned_alloc` function allocates space for an object whose alignment is
> specified by `alignment`, whose size is specified by `size`, and whose value is
> indeterminate. <del>T</del><ins>If t</ins>he value of `alignment` <del>shall
> be</del> <ins>is not</ins> a valid alignment supported by the implementation
> <del>and</del><ins>or</ins> the value of `size` <del>shall be</del><ins>is
> not</ins> an integral multiple of `alignment` <ins>the function shall fail by
> returning a null pointer</ins>.

In addition, in section **J.2 Undefined behavior**, remove the following bullet:

> <del>— The alignment requested of the aligned\_alloc function is not valid or
> not supported by the implementation, or the size requested is not an integral
> multiple of the alignment (7.22.3.1).</del>

If the proposal above isn't acceptable, then an alternative solution to consider
that would allow `aligned_alloc` to be used even in strictly conforming programs
is to add a new function to determine whether a given alignment is supported by
an implementation. For example:

> ```c
> _Bool alignment_is_valid (size_t alignment);
> ```
>
> **Returns**
>
> The `alignment_is_valid` function returns non-zero if the value specified by
> `alignment` is a valid alignment argument to the `aligned_alloc` function, and
> zero otherwise.

---

Comment from WG14 on 2017-11-03:

Apr 2014 meeting

### Committee Discussion

> The committee agrees that the first proposal in the suggested technical
> corrigendum should be adopted.

Oct 2016 meeting

### Committee Discussion

* The paper [N2072](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2072.htm) was presented which made the point that non-integral multiples of `alignment` are useful for allocating on, say, page size boundaries.
* The behavior on a value of zero has been left to the implementation to either support or reject, and this flexibility must be preserved.
* After discussion, the Suggested Technical Corrigendum from [(SC22WG14.14473) updated DR460 wording based on N2072](https://www.open-std.org/jtc1/sc22/wg14/14473) was adopted.

### Proposed Technical Corrigendum

In section 7.22.3.1, change paragraph 2 from:

> The `aligned_alloc` function allocates space for an object whose alignment is
> specified by `alignment`, whose size is specified by `size`, and whose value is
> indeterminate. The value of `alignment` shall be a valid alignment supported by
> the implementation and the value of `size` shall be an integral multiple of
> `alignment`.

to:

> The `aligned_alloc` function allocates space for an object whose alignment is
> specified by `alignment`, whose size is specified by `size`, and whose value is
> indeterminate. If the value of `alignment` is not a valid alignment supported by
> the implementation the function shall fail by returning a null pointer.

In addition, in section **J.2 Undefined behavior**, remove the following bullet:

> — The alignment requested of the aligned\_alloc function is not valid or not
> supported by the implementation, or the size requested is not an integral
> multiple of the alignment (7.22.3.1).


</div>


---

---

<div id="issue0461">

## Issue 0461: problems with references to objects in signal handlers

Authors: WG14, [Martin Sebor](mailto:msebor@gmail.com)  
Date: 2014-03-25  
Reference document: [N1812](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1812.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

We believe there are two problems in section **7.14.1.1 The signal function**,
paragraph 5, which specifies the constraints under which signal handlers can
access objects declared in other scopes. The problems are summarized in the
following two subsections. The section titled Suggested Technical Corrigendum
then proposes a correction to both.

Section **7.14.1.1 The signal function**, paragraph 5, specifies the following
constraints. Note, in particular, to use of the word "refers," and the reference
to objects with "static or thread storage duration" underscored in the text
below.

> If the signal occurs other than as the result of calling the `abort` or `raise`
> function, the behavior is undefined if the signal handler <ins>refers</ins> to
> any object with <ins>static or thread storage duration</ins> that is not a
> lock-free atomic object other than by assigning a value to an object declared as
> `volatile sig_atomic_t`, or the signal handler calls any function in the
> standard library other than the abort function, the `_Exit` function, the
> `quick_exit` function, or the `signal` function with the first argument equal to
> the signal number corresponding to the signal that caused the invocation of the
> handler.

**Underspecification of referring to objects**

The standard doesn't formally define the term *refer* but its uses in the text
suggest that it denotes any use of an object, including one that doesn't involve
accessing it. The term *access* is defined in 3.1 to mean an \<execution-time
action\> *to read or modify the value of an object.*

Preventing signal handlers from accessing objects is necessary in order to avoid
data races between accesses (reads and writes) to the same object in the rest of
the program that are in progress but not completed at the time the signal is
delivered.

However, by making use of the word "refers," the sentence in 7.14.1.1 quoted
above implies that even mentioning the name of an object in an unevaluated
context such as the `sizeof` expression, or taking its address is undefined in a
signal handler. This restriction is unnecessary, since such references are safe
because they cannot introduce any sort of a data race between the signal handler
and the rest of the program. Thus, referring to such objects without accessing
them should be permitted in conforming programs.

Furthermore, accessing a `const` object to read (but not modify) its value also
cannot introduce a data race and is safe as well. Thus, the restriction can be
relaxed even further to allow signal handlers to read constant objects. Note
that `const` objects are those that are declared `const`. In particular,
accessing an object that was not declared const via a pointer to a
`const`-qualified type does not change the fact that the object itself is not
`const`. This distinction is important to understand that relaxing this
constraint cannot introduce the potential for a data race when such a
non-`const` object is modied in the program while it's accessed via a
`const`-qualified pointer in a signal handler.

The comments in the following example should make this distinction clear:

> `const int safe = (1 << SIGINT) | (1 << SIGQUIT);`  
>       `int unsafe = (1 << SIGHUP) | (1 << SIGTERM);`  
>     
> `volatile sig_atomic_t sigcount [2];`  
>     
> `void handler (int signo) {`  
>     
>     `const int *pmask;   // pointer to` <ins>`const`</ins> `int`  
>     
>     `// taking the address of any object is safe and should be allowed`  
>     `pmask = &safe;`  
>     
>     `// access to safe should be allowed since it's a` <ins>`const object`</ins>  
>     `if ((1 << signo) & *pmask)`  
>         `++sigcount [0];`  
>     
>     `// safe and should be allowed`  
>     `pmask = &unsafe;`  
>     
>     `// access to unsafe remains undefined since it's` <ins>`not a const object`</ins>  
>     `if ((1 << signo) & *pmask)`  
>         `++sigcount [1];`  
> `}`

**Missing restriction to access other functions' local objects**

The sentence from paragraph 5 quoted above specifically singles out objects with
static or thread storage duration, but permits signal handlers to access objects
with automatic storage duration without a similar restriction. However, a signal
handler that has access to a local variable defined in another function whose
execution is interrupted by the delivery of a signal resulting in the invocation
of the signal handler contains the same potential data race as if the two
functions both accessed the same object with static storage duration.

To make clear how this condition could arise, consider the following program
which, when `atomic_intptr_t` is a lock-free type, is strictly conforming
according to the letter of the standard despite the data race.

> ```c
> atomic_intptr_t p;   // assume atomic_intptr_t is lock-free
>
> void handler (int signo) {
>     // the following write access should be undefined since it modifies
>     // an object with automatic storage duration declared in f
>     ++*(int*)p;
> }
>
> void f (void) {
>     int i = 0;
>     p = (atomic_intptr_t)&i;
>
>     signal (SIGINT, handler);
>
>     while (i < 7)
>         printf ("%i\n", i);
> }
> ```

### Suggested Technical Corrigendum

The proposed corrigendum below changes the standard to remove the unnecessary
constraints discussed above, and to add the missing restriction to prevent
accessing local variables defined elsewhere in the program. The reference to the
lifetime of auto objects makes sure that accesses to local variables defined in
signal handlers themselves as well as in functions called from them remain well
defined.

In section 7.14.1.1, modify the first sentence of paragraph 5 as indicated
below:

> If the signal occurs other than as the result of calling the `abort` or `raise`
> function, the behavior is undefined if the signal handler <del>refers
> to</del><ins>accesses</ins> any <ins>non-`const`</ins> object with static or
> thread storage duration<ins>, or any non-`const` object with automatic storage
> duration whose lifetime started before the signal handler has been
> entered,</ins> that is not a lock-free atomic object other than by...

In addition, make the corresponding change to section **J.2 Undefined
behavior**.

---

Comment from WG14 on 2015-10-29:

Apr 2014 meeting

### Committee Discussion

* The committee agrees that clarifying "refers" would be beneficial.
* Allowing access to `const` qualified objects would be a feature and cannot be accomplished by the mechanism of a defect report. Such a feature can be proposed in a separate paper.
* Access to objects of allocated storage duration should also be addressed.
* It is suggested that automatic storage duration objects should also be addressed.
* Further revisions have been solicited from the author.

Oct 2014 meeting

### Committee Discussion

> The paper [N1874](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1874.htm)
> was submitted and discussed, again, as a defect, rather than as a new proposal,
> and the suggested changes to allow new behavior were again rejected. It was
> noted that a `const volatile` object implemented in hardware, such as random
> number generator, might not provide a consistent value if accessed from a signal
> handler, and so there was general agreement that any changes in this area
> warrant very careful consideration.

### Proposed Committee Response

> Extending the behavior as requested is a feature and appropriate as input to the
> next revision of this Standard. It was noted that a `const volatile` object that
> might seem acceptable to reference from a signal handler might not be if it were
> implemented in hardware (e.g. a hardware random number generator).


</div>


---

---

<div id="issue0462">

## Issue 0462: Clarifying objects accessed in signal handlers

Authors: WG14, [Robert Seacord](mailto:rcs@cert.org)  
Date: 2014-03-25  
Reference document: [N1813](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1813.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

It appears the intent of the committee in Subclause 5.1.2.3 paragraph 5 was to
allow lock-free atomic objects or objects of type `volatile sig_atomic_t` to be
accessed from a signal handler.  Objects of type `atomic_flag` are an obvious
choice operations on an object of type `atomic_flag` are required to be lock
free. However, objects of type `atomic_flag` can only be meaningfully accessed
by a call to a function, and calls to these functions from a signal handler are
undefined behavior according to subclause 7.14.1.1 paragraph 5\.

### Suggested Technical Corrigendum

Change subclause 7.14.1.1 paragraph 5 from:

If the signal occurs other than as the result of calling the `abort` or `raise`
function, the behavior is undefined if the signal handler refers to any object
with static or thread storage duration that is not a lock-free atomic object
other than by assigning a value to an object declared as `volatile
sig_atomic_t`, or the signal handler calls any function in the standard library
other than the `abort` function, the `_Exit` function, the `quick_exit`
function, or the `signal` function with the first argument equal to the signal
number corresponding to the signal that caused the invocation of the handler.
Furthermore, if such a call to the `signal` function results in a `SIG_ERR`
return, the value of `errno` is indeterminate.<sup>252\)</sup>

to:

If the signal occurs other than as the result of calling the `abort` or `raise`
function, the behavior is undefined if the signal handler refers to any object
with static or thread storage duration that is not a lock-free atomic object
other than by assigning a value to an object declared as `volatile
sig_atomic_t`, or the signal handler calls any function in the standard library
other than the `abort` function, the `_Exit` function, the `quick_exit`
function, <ins>the `atomic_flag_test_and_set` functions, the `atomic_flag_clear`
functions,</ins> or the `signal` function with the first argument equal to the
signal number corresponding to the signal that caused the invocation of the
handler. Furthermore, if such a call to the `signal` function results in a
`SIG_ERR` return, the value of `errno` is indeterminate.<sup>252\)</sup>

Sublcause J.2 Undefined behavior. Page 566

Change:

A signal occurs other than as the result of calling the `abort` or `raise`
function, and the signal handler refers to an object with static or thread
storage duration that is not a lock-free atomic object other than by assigning a
value to an object declared as `volatile sig_atomic_t`, or calls any function in
the standard library other than the `abort` function, the `_Exit` function, the
`quick_exit` function, or the `signal` function (for the same signal number)
(7.14.1.1).

to:

A signal occurs other than as the result of calling the `abort` or `raise`
function, and the signal handler refers to an object with static or thread
storage duration that is not a lock-free atomic object other than by assigning a
value to an object declared as `volatile sig_atomic_t`, or calls any function in
the standard library other than the `abort` function, the `_Exit` function, the
`quick_exit` function, <ins>the `atomic_flag_test_and_set` functions, the
`atomic_flag_clear` functions,</ins> or the `signal` function (for the same
signal number) (7.14.1.1).

---

Comment from WG14 on 2017-11-03:

Apr 2014 meeting

### Committee Discussion

> The Suggested Technical Corrigendum was accepted as the Proposed Technical
> Corrigendum.

Oct 2014 meeting

### Committee Discussion

> Upon further consideration, since by implication 5.1.2.3p5 allows by implication
> any of the atomic functions on lock-free atomic objects, the following revision
> to the Suggested Technical Corrigendum was substantially adopted from the new
> paper [N1887](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1887.htm)

### Proposed Technical Corrigendum (superceded)

Change subclause 7.14.1.1 paragraph 5 from:

> If the signal occurs other than as the result of calling the `abort` or `raise`
> function, the behavior is undefined if the signal handler refers to any object
> with static or thread storage duration that is not a lock-free atomic object
> other than by assigning a value to an object declared as `volatile
> sig_atomic_t`, or the signal handler calls any function in the standard library
> other than the `abort` function, the `_Exit` function, the `quick_exit`
> function, or the `signal` function with the first argument equal to the signal
> number corresponding to the signal that caused the invocation of the handler.
> Furthermore, if such a call to the `signal` function results in a `SIG_ERR`
> return, the value of `errno` is indeterminate.<sup>252\)</sup>

to:

> If the signal occurs other than as the result of calling the `abort` or `raise`
> function, the behavior is undefined if the signal handler refers to any object
> with static or thread storage duration that is not a lock-free atomic object
> other than by assigning a value to an object declared as `volatile
> sig_atomic_t`, or the signal handler calls any function in the standard library
> other than
>
> * the `abort` function,
> * the `_Exit` function,
> * the `quick_exit` function,
> * the atomic functions from `stdatomic.h`, when the atomic arguments are
>   lock-free,
> * the `atomic_is_lock_free` function with any atomic argument,
> * or the `signal` function with the first argument equal to the signal number
>   corresponding to the signal that caused the invocation of the handler.
>   Furthermore, if such a call to the `signal` function results in a `SIG_ERR`
>   return, the value of `errno` is indeterminate.<sup>252</sup><sup>)</sup>

In subclause J.2 Undefined behavior, change:

> A signal occurs other than as the result of calling the `abort` or `raise`
> function, and the signal handler refers to an object with static or thread
> storage duration that is not a lock-free atomic object other than by assigning a
> value to an object declared as `volatile sig_atomic_t`, or calls any function in
> the standard library other than the `abort` function, the `_Exit` function, the
> `quick_exit` function, or the `signal` function (for the same signal number)
> (7.14.1.1).

to:

> A signal occurs other than as the result of calling the `abort` or `raise`
> function, and the signal handler refers to an object with static or thread
> storage duration that is not a lock-free atomic object other than by assigning a
> value to an object declared as `volatile sig_atomic_t`, or calls any function in
> the standard library other than the `abort` function, the `_Exit` function, the
> `quick_exit` function, the atomic functions from `stdatomic.h` (when the atomic
> arguments are lock-free) , the `atomic_is_lock_free` function with any atomic
> argument, or the `signal` function (for the same signal number) (7.14.1.1).

Apr 2015 meeting

### Committee Discussion

> The committee noted that `atomic_init` was not safe to call. It was decided that
> the best place to say this was in the `atomic_init` description as a pattern to
> follow for future possible additions. As such, the following revised Proposed
> Technical Corrigendum was provided and accepted.

### Proposed Technical Corrigendum

Change subclause 7.14.1.1 paragraph 5 from:

> If the signal occurs other than as the result of calling the **abort** or
> **raise** function, the behavior is undefined if the signal handler refers to
> any object with static or thread storage duration that is not a lock-free atomic
> object other than by assigning a value to an object declared as **volatile
> sig\_atomic\_t**, or the signal handler calls any function in the standard
> library other than the **abort** function, the **\_Exit** function, the
> **quick\_exit** function, or the signal function with the first argument equal
> to the signal number corresponding to the signal that caused the invocation of
> the handler. Furthermore, if such a call to the signal function results in a
> SIG\_ERR return, the value of errno is indeterminate.<sup>252</sup>

to

> If the signal occurs other than as the result of calling the **abort** or
> **raise** function, the behavior is undefined if the signal handler refers to
> any object with static or thread storage duration that is not a lock-free atomic
> object other than by assigning a value to an object declared as **volatile
> sig\_atomic\_t**, or the signal handler calls any function in the standard
> library other than
>
> * the **abort** function,
> * the **\_Exit** function,
> * the **quick\_exit** function,
> * the functions in **\<stdatomic.h\>** (except where explicitly stated otherwise) when the atomic arguments are lock-free,
> * the **atomic\_is\_lock\_free** function with any atomic argument, or
> * the **signal** function with the first argument equal to the signal number corresponding to the signal that caused the invocation of the handler. Furthermore, if such a call to the **signal** function results in a **SIG\_ERR** return, the value of errno is indeterminate.<sup>252</sup>

Add a new paragraph after 7.17.2.2 paragraph 3:

> If a signal occurs other than as the result of calling the **abort** or
> **raise** function, the behavior is undefined if the signal handler calls the
> **atomic\_init** generic function.

In subclause J.2 Undefined behavior, change:

> A signal occurs other than as the result of calling the **abort** or **raise**
> function, and the signal handler refers to an object with static or thread
> storage duration that is not a lock-free atomic object other than by assigning a
> value to an object declared as **volatile sig\_atomic\_t**, or calls any
> function in the standard library other than the **abort** function, the
> **\_Exit** function, the **quick\_exit** function, or the **signal** function
> (for the same signal number) (7.14.1.1).

to

> A signal occurs other than as the result of calling the **abort** or **raise**
> function, and the signal handler refers to an object with static or thread
> storage duration that is not a lock-free atomic object other than by assigning a
> value to an object declared as **volatile sig\_atomic\_t**, or calls any
> function in the standard library other than the **abort** function, the
> **\_Exit** function, the **quick\_exit** function, the functions in
> **\<stdatomic.h\>** (except where explicitly stated otherwise) when the atomic
> arguments are lock-free, the **atomic\_is\_lock\_free** function with any atomic
> argument, or the **signal** function (for the same signal number) (7.14.1.1).


</div>


---

---

<div id="issue0463">

## Issue 0463: Left-shifting into the sign bit

Authors: WG14, Aaron Ballman  
Date: 2014-04-02  
Reference document: [N1817](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1817.pdf)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Harmonizing left-shift with C\+\+14

It is not uncommon to see code such as:

```c
signed someint_t min_value = 1 << (CHAR_BIT * sizeof(someint_t));
```

However, left-shifting a one bit into the sign bit is undefined behavior,
despite the fact that the majority of (twos-complement) architectures handle it
properly.

### Suggested Technical Corrigendum

6.5.7p4 should be modified to read:

> The result of `E1 << E2` is `E1` left-shifted `E2` bit positions; vacated bits
> are filled with zeros. If `E1` has an unsigned type, the value of the result is
> `E1 x 2`<sup>`E2`</sup>, reduced modulo one more than the maximum value
> representable in the result type. If `E1` has a signed type and nonnegative
> value, and `E1 x 2`<sup>`E2`</sup> is representable in the <ins>corresponding
> unsigned type of the</ins> result type, then that <ins>value, converted to the
> result type,</ins> is the resulting value; otherwise, the behavior is undefined.

C\+\+ addressed this in C\+\+14 with DR1457 with identical wording
modifications.

---

Comment from WG14 on 2015-04-17:

Apr 2014 meeting

### Proposed Committee Response

This is not a defect.

The committee will track this and consider it for the next revision of the
standard.


</div>


---

---

<div id="issue0464">

## Issue 0464: Clarifying the Behavior of the `#line` Directive

Authors: WG14, David Keaton (suggested by Max Woodbury)  
Date: 2014-06-27  
Reference document: [N1842](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1842.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Context:

In a distributed development environment, the exact file name passed to the
compiler or preprocessor may vary from site to site. It is therefore desirable
to be able to set the file name as seen by `__FILE__` and elsewhere to a uniform
value. The mechanism to do this is the '`#line <num> "<string>"`' form of the
'`#line`' preprocessor directive. It is also necessary that such a directive
leave the line numbering sequence unchanged. Further, it is desirable that edits
that change the location of the directive in the source module should not
require modification to the directive and that comments embedded in the
directive likewise do not have to be accounted for.

Searches of the online literature show that a directive of the form '`#line
__LINE__ "string"`' is expected to have this property.

Despite this, at least one compiler/preprocessor does not allow this.

Technical argument:

The value substituted for the predefined macro '`__LINE__`' is specified in
6.10.8.1p1 as the presumed line number of the current source line. The presumed
line number is initially (6.10.4p2) the number of newline characters (or their
equivalent) seen in phase 1 of the translation process, plus 1, *at the time of
substitution*. (Note that this is *not* the same as the time of tokenization,
which is where the failing compilers make their mistake.) The mechanism for
transferring this count between phase 1 and phase 4, where macro substitution
takes place, is not specified, but may be presumed to exist and be reliable. (If
it were not, the `__LINE__` predefined macro would be useless.) That makes the
question 'when does the substitution take place?'

Macro substitution in directives is a separate issue from macro expansion in
code. It does *not* always take place. If and when it occurs depends on the
directive and the details of its form. That means the entire directive has to be
'in hand' in order to be evaluated, and that means, in turn, that the newline
that terminates the directive has to have been seen. The standard goes to some
length to specify the various directive forms and all include the terminating
newline in their specification.

Therefore, when a substitution is made for '`__LINE__`', its value should be the
line count following the end of the directive, which is the same as the line
number of next line in the source module. This is precisely the value that
produces the desired property of the '`#line __LINE__ "string"`' directive.

Correction requested:

While there is no need to change the standard's normative text, a note that
'`#line __LINE__ "string"`' and similar directives leaves line numbering
unchanged would both be educational and make misinterpretations more difficult.

### Suggested Technical Corrigendum

Append the following to footnote 177 in 6.10.8.1p1:

`#line __LINE__ "newfilename"` changes the presumed file name without changing
the presumed line number.

---

Comment from WG14 on 2017-11-03:

Oct 2014 meeting

### Committee Discussion

> The committee discussed the Proposed Technical Corrigendum from
> [N1842](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1842.htm) and found
> that it didn't sufficiently clarify the issue. Investigation during the meeting
> revealed that several (in fact all that were tested) compilers did not seem to
> follow the interpretation of the standard as given in N1842, and that it would
> be best to acknowledge this as unspecified behavior.

### Proposed Committee Response

> 6.10.4 paragraph 2 states that “The *line number* of the current source line is
> one greater than the number of new-line characters read or introduced in
> translation phase 1 (5.1.1.2) while processing the source file to the current
> token.” Note that it does not say the number of new-line characters that exist
> prior to the current token; it says the number of new-line characters that have
> been read while processing to the current token.
>
> In the case of the `#line` directive of the form
>
> `#line` *pp-tokens new-line*
>
> there are two possible values for the number of new-line characters that have
> been read when processing begins on the first *pp-token*. In a one-pass
> preprocessor, the line number at the first *pp-token* will be the number of
> new-line characters that exist prior to the `#line` directive, because that
> number of new-lines will have been read. In a preprocessor that must see the
> entire directive before processing it, since the directive explicitly includes a
> new-line, the line number at the first *pp-token* will be the number of new-line
> characters that exist prior to the `#line` directive plus one.
>
> Therefore, in a `#line` directive of the form
>
> ```c
> #line __LINE__ “filename”
> ```
>
> there are two possible values for `__LINE__`, which leads to two possible values
> for the line number following the `#line` directive. Both are valid.

### Proposed Technical Corrigendum

Add the following footnote to the end of 6.10.4 paragraph 5\.

> Because a new-line is explicitly included as part of the `#line` directive, the
> number of new-line characters read while processing to the first *pp-token* may
> be different depending on whether or not the implementation uses a one-pass
> preprocessor. Therefore, there are two possible values for the line number
> following a directive of the form `#line __LINE__ new-line`.

Add the following to J.1 Unspecified behavior.

> The line number following a directive of the form `#line __LINE__ new-line`
> (6.10.4).


</div>


---

---

<div id="issue0465">

## Issue 0465: Fixing an inconsistency in `atomic_is_lock_free`

Authors: WG14, David Keaton (suggested by Hans Boehm)  
Date: 2014-07-14  
Reference document: [N1847](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1847.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The C committee intended to adopt the same model for atomics as C\+\+ to ensure
compatibility. Somewhere along the way, there was an error in synchronizing with
the C\+\+ atomic model. This could have serious consequences for code that needs
to share atomic objects between modules written in C and modules written in
C\+\+ (for example, in the case of libraries written in one language being used
by a program written in the other).

The C\+\+ standard states the following in 29.4p2.

> The function `atomic_is_lock_free` (29.6) indicates whether the object is
> lock-free. *In any given program execution, the result of the lock-free query
> shall be consistent for all pointers of the same type.*

However, the C standard states the following in 7.17.5.1p3.

> The `atomic_is_lock_free` generic function returns nonzero (true) if and only if
> the object's operations are lock-free. *The result of a lock-free query on one
> object cannot be inferred from the result of a lock-free query on another
> object.*

The primary issue is compatibility. Secondarily, if the lock-free property for a
given pointer type can change after an algorithm starts, then
`atomic_is_lock_free` cannot be used to select an algorithm in advance if the
algorithm will allocate new atomic objects. The C\+\+ model is therefore more
useful.

The error in synchronizing with C\+\+ should be fixed by correcting the behavior
of `atomic_is_lock_free` to be the same in C as in C\+\+.

### Suggested Technical Corrigendum

Replace the following sentence from 7.17.5.1p3

> The result of a lock-free query on one object cannot be inferred from the result
> of a lock-free query on another object.

with the following.

> In any given program execution, the result of the lock-free query shall be
> consistent for all pointers of the same type.

---

Comment from WG14 on 2017-11-03:

Oct 2014 meeting

### Committee Discussion

> The Suggested Technical Corrigendum needed revision, and new words were crafted
> and adopted. One consequence from this change that a NULL pointer is now a valid
> argument.

Apr 2015 meeting

### Committee Discussion

> No revisions were deemed necessary. Value 1 remains in 7.17.5p1 for
> implementations where only the runtime can determine if an operation on a
> particular type is lock-free due to architectural differences.

Oct 2015 meeting

### Committee Discussion

> As solicited, a new paper
> [N1976](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1976.htm) was
> presented and discussed to clarify that null pointers to atomic types are
> allowed and thus can be used at compile time. After discussion, the Proposed
> Technical Corrigendum was modified to incorporate this point as a non-normative
> explanatory footnote.

### Proposed Technical Corrigendum

Change 7.17.5.1 paragraph 2 from:

> The `atomic_is_lock_free` generic function indicates whether or not the object
> pointed to by `obj` is lock-free.

to:

> The `atomic_is_lock_free` generic function indicates whether or not atomic
> operations on objects of the type pointed to by `obj` are lock-free.

Change 7.17.5.1 paragraph 3 from:

> The `atomic_is_lock_free` generic function returns nonzero (true) if and only if
> the object's operations are lock-free. The result of a lock-free query on one
> object cannot be inferred from the result of a lock-free query on another
> object.

to:

> The `atomic_is_lock_free` generic function returns nonzero (true) if and only if
> atomic operations on objects of the type pointed to by the argument are
> lock-free. In any given program execution, the result of the lock-free query
> shall be consistent for all pointers of the same type.<sup>new</sup>

<sup>new)</sup>`obj` may be a null pointer.


</div>


---

---

<div id="issue0466">

## Issue 0466: scope of a `for` loop control declaration

Authors: WG14, Martin Sebor  
Date: 2014-09-19  
Reference document: [N1865](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1865.htm)  
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


</div>


---

---

<div id="issue0467">

## Issue 0467: maximum representable finite description vs math

Authors: WG14, Fred J. Tydeman  
Date: 2014-09-26  
Reference document: [N1870,](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1870.htm) [N1871](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1871.htm)  
Status: Closed  
Cross-references: [0432](log_c11c17.md#issue0432)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

formula for maximum representable finite (normalized) floating-point numbers in
5.2.4.2.2#12, and epsilon floating-point numbers in 5.2.4.2.2#13.

### Details

The math formula is for a normalized number, while the words are missing
'normalized'. Now, in the floating-point model in paragraph 2, the maximum
finite number is the same as the maximum finite normalized number, so it did not
matter.

However, if long double is a pair of doubles (not matching the model in
paragraph 2), then there can be finite numbers larger than the largest
normalized finite number. The largest normalized finite number is
DBL\_MAX\*(1.\+DBL\_EPSILON/2.), while the largest finite number can be
DBL\_MAX\*2.

Also, if long double is a pair of doubles (not matching the model in paragraph
2), then 'least value greater than 1 that is representable in the given floating
point type' is (for double) 1.0\+DBL\_TRUE\_MIN. That makes the difference
DBL\_TRUE\_MIN, which is not the same at the math formula (b to the power
(1-p)).

### Suggested Technical Corrigendum

In 5.2.4.2.2#13, add 'normalized' between 'least' and 'value'.

In 5.2.4.2.2#12, add 'normalized' between 'finite' and 'floating-point'.

Add a new paragraph:

12b The values given in the following list shall be replaced by constant
expressions with implementation-defined values that are greater than or equal to
those shown:

\-- maximum representable finite floating-point number (footnote),

* **FLT\_TRUE\_MAX 1E\+37**
* **DBL\_TRUE\_MAX 1E\+37**
* **LDBL\_TRUE\_MAX 1E\+37**

(footnote): Need not be normalized.

---

Comment from WG14 on 2018-10-18:

Oct 2014 meeting

### Committee Discussion

> The committee accepts the correction of "normalized" but concludes that adding
> the suggested macros is a feature and out of scope for a DR.

Oct 2015 meeting

### Committee Discussion

> There has been discussion of this Proposed Technical Corrigendum on the WG 14
> email reflector starting with [(SC22WG14.13764)
> LDBL\_MAX](https://www.open-std.org/jtc1/sc22/wg14/13764) suggesting that since
> `double double` implementations do not follow (nor are provided by) the IEEE
> model that the implementation is free to define additional macros to describe
> the behavior as they see fit. To some degree a consensus on LDBL\_MAX was
> formed, and the following words are provided as food for further committee
> thought.
>
> > In 5.2.4.2.2#12, first item change the phrase
> >
> > maximum representable finite floating-point number, \[math formula\]
> >
> > to
> >
> > maximum representable finite floating-point number; if that value is normalized,
> > its value is \[math formula\]

Apr 2016 meeting

### Committee Discussion

> The committee agrees with the reflector discussion.

Apr 2017 meeting

### Committee Discussion

> Additional input to the Proposed Technical Corrigendum was suggested and adopted
> by the committee from [DR 467
> PTC](https://www.open-std.org/jtc1/sc22/wg14/14655).
>
> Further, after discussion, the change from [DR 432](log_c11c17.md#issue0432) is now viewed as
> necessary but not sufficient, and so it will be further reviewed before being
> incorporated into a future version of the standard along with these changes.

### Proposed Change

In §5.2.4.2.2#1 after the definition of the floating point model parameters,
add:

> For each floating-point type: *b*, *e<sub>min</sub>*, *e<sub>max</sub>*, *p* are
> fixed constants.

In §5.2.4.2.2#3 change:

> In addition to normalized floating-point numbers ( *f<sub>1</sub>* \> 0 if *x* ≠
> 0),

to:

> In addition to *normalized floating-point numbers* ( *f<sub>1</sub>* \> 0 if *x*
> ≠ 0), all possible *f<sub>k</sub>* digits result in values representable in the
> type<sup>footnote</sup>.
>
> <sup>footnote</sup>: Some implementations may have types with numeric values
> which are not covered by this model.

In 5.2.4.2.2#12, first item change the phrase

> maximum representable finite floating-point number, \[ math formula \]

to

> maximum representable finite floating-point number; if that value is normalized,
> its value is \[ math formula \],

In 5.2.4.2.2#13, first item change the phrase

> the difference between 1 and the least value greater than 1

to

> the difference between 1 and the least normalized value greater than 1

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that this proposed change and that from [CR 432](log_c11c17.md#issue0432) be
> combined in a new paper to completely resolve this issue.


</div>


---

---

<div id="issue0468">

## Issue 0468: `strncpy_s` clobbers buffer past `null`

Authors: WG14, Martin Sebor  
Date: 2014-09-19  
Reference document: [N1872](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1872.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

K.3.7.1.4, p5 permits `strncpy_s` to "clobber" characters in the destination
buffer past the terminating `null`:

> All elements following the terminating null character (if any) written by
> `strncpy_s` in the array of `s1max` characters pointed to by `s1` take
> unspecified values when `strncpy_s` returns. <sup>420\)</sup>

Footnote 420 explains that the intent is to allow implementations to copy
characters from `s2` to `s1` while simultaneously checking if any of those
characters are null. Such an approach might write a character to every element
of `s1` before discovering that the first element should be set to the null
character.

This intent is to allow efficient implementations to make a single pass over the
source sequence that simultaneously copies characters and checks the runtime
constraints. (Otherwise two passes would be required, one to compute the length
of the source sequence and another to copy it.)

It has been pointed out that the implementation latitude granted by this text
goes too far, since the function only might need to write past the null after a
constraint violation. Otherwise, when all runtime constraints are satisfied, the
function stops copying characters after either the first null is encountered or
all `n` characters have been copied.

Since the mention of unspecified values tends to raise security concerns about
information leakage, and since permitting the implementations to modify the
contents of the destination buffer past the terminating null on success serves
no useful purpose, the requirements on the function can and should be tightened
up.

### Suggested Technical Corrigendum

The proposed corrigendum below tightens up the requirements on the function so
as to leave intact the contents of the destination buffer past the terminating
null on success, while allowing it to clobber its contents on runtime constraint
violation.

Modify K.3.7.1.4, p5 as indicated below:

> All elements following the terminating null character (if any) written by
> `strncpy_s` in the array of `s1max` characters pointed to by `s1` take
> unspecified values when `strncpy_s` returns <ins>a non-zero value</ins>.
> <sup>420\)</sup>

---

Comment from WG14 on 2017-11-03:

Oct 2014 meeting

### Proposed Technical Corrigendum

Change K.3.7.1.4, p5 from

> All elements following the terminating null character (if any) written by
> `strncpy_s` in the array of `s1max` characters pointed to by `s1` take
> unspecified values when `strncpy_s` returns. <sup>420\)</sup>

to

> All elements following the terminating null character (if any) written by
> `strncpy_s` in the array of `s1max` characters pointed to by `s1` take
> unspecified values when `strncpy_s` returns a non-zero value. <sup>420\)</sup>


</div>


---

---

<div id="issue0469">

## Issue 0469: lock ownership vs. thread termination

Authors: WG14, Torvald Riegel  
Date: 2014-10-07  
Reference document: [N1881](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1881.htm)  
Status: Closed  
Cross-references: [0414](log_c11c17.md#issue0414), [0416](log_c11c17.md#issue0416), [0479](log_c11c17.md#issue0479), [0493](log_c11c17.md#issue0493)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

If a mutex M is acquired by a thread T, and afterwards T terminates without
releasing ownership of M, then the resulting state after termination of T seems
to be unspecified.

Specifically, N1570 7.26.4.5p2 states:

> The mtx\_trylock function endeavors to lock the mutex pointed to by mtx. If the
> mutex is already locked, the function returns without blocking.

However, there is no statement about whether a mutex whose owner has terminated
remains locked. This seems to be a source of confusion, and it affects
implementations. C\+\+11 specifies that such a case results in undefined
behavior (see 30.4.1.2.1p5). On the other hand, POSIX wants (PThreads) mutexes
to remain locked in this case (see Austin Group Bug
[755](http://austingroupbugs.net/view.php?id=755)).

From an implementation perspective, the C\+\+11 semantics are more practical
because they do not require implementations to maintain identities of threads
that do not exist any more. For example, with C\+\+11 semantics, an
implementation can just use a thread ID to identify an owner, even if another
thread eventually reuses the same ID (e.g., a process ID) after the former
owning thread terminated. In contrast, the POSIX semantics require an
implementation to avoid ABA issues on the thread identities (i.e., the same
value representing different states of ownership). This effectively results in a
higher runtime overhead for lock acquisition or for lock initialization of at
least recursive mutexes, or address space leakage (or other workarounds).

### Suggested Technical Corrigendum

I would like the expected behavior to be explicitly specified. To me, C should
do what C\+\+11 states. In particular, add the following or a similar sentence
at an appropriate place:

> The behavior of a program is undefined if a thread terminates while owning a
> mutex.

---

Comment from WG14 on 2018-10-18:

Oct 2014 meeting

### Committee Discussion

> The committee is sympathetic to this concern. A review uncovered the possible
> need to further specify the behavior of a recursive mutex. A new paper was
> solicited to discuss this and other issues and their proposed resolutions.

Apr 2015 meeting

### Committee Discussion

> The paper [N1907](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1907.pdf)
> was presented.
>
> Issue 1 from that paper has already been addressed in [DR414](log_c11c17.md#issue0414)
>
> Issue 2, that recursive mutex behavior is essentially unspecified, needs
> addressing, but the words provided are unclear about accounting for additional
> lock and matching unlocks. It may be necessary to introduce the notion of
> counting to express the nested pattern succinctly.
>
> Issue 3, from the original paper, was thought by the committee to be worth
> addressing, although in which section was not clear to the committee.
>
> A revised paper was solicited.

Oct 2015 meeting

### Committee Discussion

> No new papers were presented and a new paper was again solicited. It may be that
> the resolution to [DR 414](log_c11c17.md#issue0414) be folded into any Suggested Technical
> Corrigendum as well.

Apr 2016 meeting

### Committee Discussion

> Papers [N2019](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2019.pdf) and
> [N2026](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2026.htm) were
> provided and discussed as potential resolutions. The second paper borrows from
> the similar POSIX description and makes the recursion count more explicit, and
> introduces *acquire* terminology. The preceding section on condition variables
> would be impacted by such changes, however, and a combined paper was solicited.
>
> Section 2 from
> [N2019](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2019.pdf) needs to be
> reconciled with the first item from the PTC of [DR 416](log_c11c17.md#issue0416). It was also
> suggested that “or through program termination” be added.
>
> [DR 479](log_c11c17.md#issue0479) and [DR 493](log_c11c17.md#issue0493) raise other issues that must be
> found in any committee approved Proposed Technical Corrigendum to this DR.

Oct 2016 meeting

### Committee Discussion

> As noted above there are several related issues and there have been several
> attempts to accurately specify the missing information. Nomenclature changes
> affecting mutexes must additionally be reflected throughout *7.26.3 Condition
> variable functions*, and such extensive changes are not suited for rectification
> via the Defect Report process.
>
> As such, this DR and those related are to be considered in a future version of
> this standard.

Apr 2018 meeting

### Committee Discussion

> The committee solicited a combined resolution for these issues with those raised
> in [DR 479](log_c11c17.md#issue0479) and [DR 493](log_c11c17.md#issue0493).
>
> It was noted that there may well be missing language to tie these operations to
> the formal memory model, e.g. total memory order. It may also be the case that
> implementations may need to add explicit barriers in their wrappers in order to
> achieve C semantics. In no event shall C impose new requirements directly upon
> any underlying OS implementations.

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> These issues were not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that issues from [CR 469](log_c11c17.md#issue0469), [CR 479](log_c11c17.md#issue0479), and [CR
> 493](log_c11c17.md#issue0493), as well as potentially other small issues be combined in a new
> paper to completely resolve this issue for the next revision of the standard.


</div>


---

---

<div id="issue0470">

## Issue 0470: mtx\_trylock should be allowed to fail spuriously

Authors: WG14, Torvald Riegel, Hans Boehm  
Date: 2014-10-10  
Reference document: [N1882](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1882.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 does not *appear* to allow `mtx_trylock` to fail spuriously (i.e., return
`thrd_busy` even thought the lock was not acquired, yet eventually acquire the
lock if it is not acquired by any thread), but C\+\+11 does (see 30.4.1.1/16):

> An implementation may fail to obtain the lock even if it is not held by any
> other thread. \[ Note: This spurious failure is normally uncommon, but allows
> interesting implementations based on a simple compare and exchange (Clause 29).
> \-- end note \] An implementation should ensure that try\_lock() does not
> consistently return false in the absence of contending mutex acquisitions.

It might be better to point out explicitly that programmers should treat
`mtx_trylock` as if spurious failure were allowed, since the memory model is
intentionally too weak to support correct reasoning that is based on a return
value of `thrd_busy`. There has been debate on this issue, and we would prefer
the standard to be clearer. Consider the following example:

```c
Thread 1:
  v1 = 1;
  mtx_lock(l1);

Thread 2:
  r1 = mtx_trylock(l1);
  while (r1 == thrd_success /* was unlocked */) {
    unlock(l1);
    r1 = mtx_trylock(l1);
  }
  r2 = v1;
  out(r2);
```

This program is not data-race-free according to C11, independently of whether
`mtx_trylock` is allowed to fail spuriously or not; the happens-before-based
definition of a data race and the current specification of synchronizes-with
relations between mutex operations makes it clear that the program above has a
data race on `v1`.

However, if spurious failures are not allowed, an intuitive understanding of the
memory model in the sense that everything will appear to be sequentially
consistent if only locks are used to synchronize does not hold anymore. The
intuitive understanding would make the program above correct; in particular the
store to `v1` by the first thread would be expected to "happen before" the load
from `v1` by the second thread.

Therefore, to make an intuitive understanding of the C11 memory model and locks
match the actual specification, it would be helpful to point out that
programmers should assume `mtx_trylock` to fail spuriously. Otherwise, without
spurious failure, we have cases like the example above in which two operations
race according to the specification in spite of the fact that they intuitively
can't execute at the same time.

Allowing spurious failures does not affect the typical uses of `mtx_trylock`,
for example to acquire several locks without risk of deadlock. It does rule out
uses like the example above, however, in which locks are attempted to be used as
a replacement for atomics.

(Note that we are not arguing for specifying that `mtx_lock` should synchronize
with a `mtx_trylock` that returns `thrd_busy`. This would make the
implementation of lock acquisition less efficient on architectures such as ARM
or PowerPC. In particular, an `atomic_compare_exchange` or similar that
transitions the lock's state from not acquired to acquired would have to use
`memory_order_acq_rel` instead of `memory_order_acquire`.)

### Suggested Technical Corrigendum

It seems that the normative specification already states the preferred
semantics, although the return value specification for `thrd_busy` may make
readers believe that this return code allows one to infer a certain ordering
(see the example above).

We propose to add a clarifying note at an appropriate place (e.g., in
7.26.4.5p3):

> Programmers should treat `mtx_trylock` as if spurious failures were allowed; the
> memory model is intentionally too weak to support reasoning based on a return
> value of `thrd_busy`.

---

Comment from WG14 on 2017-11-03:

Oct 2014 meeting

### Committee Discussion

> A spurious failure can occur on PPC/ARM style architectures if, after the
> load-word-and-reserve instruction is issued the operating system schedules the
> task out, and upon resumption the corresponding store-word fails because the
> reservation is lost, even if the lock is unlocked. This failure can be seen by
> `mtx_trylock` if it is implemented with `atomic_compare_exchange_weak` where
> this failure can occur.
>
> A new paper was solicited to extract the corresponding words from C\+\+ so as to
> keep the two standards as close as possible in this area.

Apr 2015 meeting

### Committee Discussion

> The paper [N1922](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1922.pdf)
> was presented and adopted with an editorial improvement.

### Proposed Technical Corrigendum

In 7.26.4.5 replace paragraph 3

> The **mtx\_trylock** function returns **thrd\_success** on success, or
> **thrd\_busy** if the resource requested is already in use, or **thrd\_error**
> if the request could not be honored.

with

> The **mtx\_trylock** function returns **thrd\_success** on success, or
> **thrd\_busy** if the resource requested is already in use, or **thrd\_error**
> if the request could not be honored. **mtx\_trylock** may spuriously fail to
> lock an unused resource, in which case it shall return **thrd\_busy**.


</div>


---

---

<div id="issue0471">

## Issue 0471: Complex math functions cacosh and ctanh

Authors: WG14, Fred Tydeman  
Date: 2014-10-28  
Reference document: [N1886](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1886.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Complex math functions (cacosh (G.6.2.1) and ctanh(G.6.2.6)) are incorrectly
specified.

1. cacosh( 0.0 \+ I\*NaN ) should be NaN \+ I\*pi/2 (not NaN \+ I\*NaN).

Reasons: Mathematically, cacosh(0.0\+I\*y) \= asinh(y) \+ I\*pi/2. Also, C
requires cacos(0\+I\*NaN) to be pi/2\+I\*NAN, which along with the
mathematically identity cacosh(z) \= \+/-I \* cacos(z), means cacosh(0.0 \+
I\*NaN) is NaN \+ I\*pi/2.

2. ctanh(\+0.0\+I\*NaN) should be 0.0 \+ I\*NaN (not NaN\+I\*NaN)
3. ctanh(\+0.0\+I\*INF) should be 0.0 \+ I\*NaN w/ invalid (not NaN\+I\*NaN w/ invalid)

Reason for above two: Since ctanh(x\+I\*y) \= (sinh(2x) \+ I\*sin(2y)) /
(cosh(2x) \+ cos(2y)), for any rational number y, cos(2y) cannot be exactly -1,
so no 0/(1\+(-1)),so no 0/0, so no NaN for the real component of the result


### Suggested Technical Corrigendum

Add to G.6.2.1 cacosh before 4th bullet: cacosh(0.0\+I\*NaN) returns NaN \+
I\*pi/2

Add to G.6.2.1 cacosh 4th bullet: "non-zero" so it reads: cacosh(x \+ iNaN)
returns NaN \+ i\*NaN and optionally raises the “invalid” floating-point
exception, for finite non-zero x.

Add to G.6.2.6 ctanh before 3rd bullet: ctanh(0.0\+I\*INF) returns 0.0\+I\*NAN
and raises the “invalid” floating-point exception.

Add to G.6.2.6 ctanh 3rd bullet: "non-zero" so it reads: ctanh(x \+ I\*INF)
returns NaN \+ i\*NaN and raises the “invalid” floating-point exception, for
finite non-zero x.

Add to G.6.2.6 ctanh before 4th bullet: ctanh(0.0\+I\*NaN) returns 0.0\+I\*NAN

Add to G.6.2.6 ctanh 4th bullet: "non-zero" so it reads: ctanh(x \+ I\*NAN)
returns NaN \+ i\*NaN and optionally raises the “invalid” floating-point
exception, for finite non-zero x.

---

Comment from WG14 on 2017-11-03:

Oct 2014 meeting

### Committee Discussion

> This DR is derived from
> [N1867.](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1867.htm) The
> committee agrees with the Suggested Technical Corrigendum.

Oct 2017 meeting

### Committee Discussion

> In light of the paper
> [N2173](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2173.htm) the
> committee agrees to amend the PTC to specify that
>
> > cacosh(0.0\+*i*NaN) returns NaN ± *i*π/2

### Proposed Technical Corrigendum

Add new paragraph to G.6.2.1 cacosh before 4th bullet:

> cacosh(0.0\+*i*NaN) returns NaN ± *i*π/2

Change G.6.2.1 cacosh 4th bullet from:

> cacosh(x \+ *i*NaN) returns NaN \+ *i*NaN and optionally raises the “invalid”
> floating-point exception, for finite x.

to

> cacosh(x \+ *i*NaN) returns NaN \+ *i*NaN and optionally raises the “invalid”
> floating-point exception, for finite non-zero x.

Add new paragraph to G.6.2.6 ctanh before 3rd bullet:

> ctanh(0.0\+*i*∞) returns 0.0\+*i*NAN and raises the “invalid” floating-point
> exception.

Change G.6.2.6 ctanh 3rd bullet clause from:

> ctanh(x \+ *i*∞) returns NaN \+ *i*NaN and raises the “invalid” floating-point
> exception, for finite x.

to

> ctanh(x \+ *i*∞) returns NaN \+ *i*NaN and raises the “invalid” floating-point
> exception, for finite non-zero x.

Add new paragraph to G.6.2.6 ctanh before 4th bullet:

> ctanh(0.0\+*i*NaN) returns 0.0\+*i*NAN

Change G.6.2.6 ctanh 4th bullet from:

> ctanh(x \+ *i*NAN) returns NaN \+ *i*NaN and optionally raises the “invalid”
> floating-point exception, for finite x.

to

> ctanh(x \+ *i*NAN) returns NaN \+ *i*NaN and optionally raises the “invalid”
> floating-point exception, for finite non-zero x.


</div>


---

---

<div id="issue0472">

## Issue 0472: Introduction to complex arithmetic in 7.3.1p3 wrong due to CMPLX

Authors: WG14, Fred J. Tydeman  
Date: 2015-01-07  
Reference document: [N1902](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1902.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The introduction to complex arithmetic in 7.3.1p3 is wrong on several counts,
all due to CMPLX.

The text in question is:

> Each synopsis specifies a family of functions consisting of a principal function
> with one or more **double complex** parameters and a **double complex** or
> **double** return value; and other functions with the same name but with **f**
> and **l** suffixes which are corresponding functions with **float** and **long
> double** parameters and return values.

The items that are wrong are:

* CMPLX is a macro (not a function).
* CMPLX takes **double** parameters (not **double complex**).
* CMPLX has **F** and **L** suffixes (not **f** and **l**).

### Suggested Technical Corrigendum

---

Comment from WG14 on 2017-11-03:

Apr 2015 meeting

### Committee Discussion

> The following Proposed Technical Corrigendum was presented, discussed, and
> accepted.

### Proposed Technical Corrigendum

In 7.3.1#3, change:

> Each synopsis specifies a family of functions

to

> Each synopsis other than the CMPLX macros specifies a family of functions
>
> (add forward reference to 7.3.9.3)


</div>


---

---

<div id="issue0473">

## Issue 0473: "A range error occurs if x is too large." is misleading

Authors: WG14, Fred J. Tydeman  
Date: 2015-01-07  
Reference document: [N1903](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1903.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

"A range error occurs if **x** is too large." is misleading (or ambiguous) for
expm1 (7.12.6.3p2), erfc (7.12.8.2p2), and lgamma (7.12.8.3p2).

"too large" could mean either \+/-large value (in which case "too small" means
\+/-near zero) or just \+large value (in which case "too small" means -large
value).

7.12.6.3p2: expm1(-DBL\_MAX) is -1, which is not a range error.

7.12.8.2p2: erfc(-DBL\_MAX) is 2, which is not a range error.

7.12.8.3p2: lgamma(-DBL\_MAX) is a pole error, which is not a range error.

### Suggested Technical Corrigendum

Add the word "positive" before **x** in those three cases so that they are:

> A range error occurs if positive **x** is too large.

---

Comment from WG14 on 2017-11-03:

Apr 2015 meeting

### Committee Discussion

> The Suggested Technical Corrigendum was accepted.

Oct 2015 meeting

### Committee Discussion

* A new paper [N1941](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1941.htm) was submitted and discussed as well as the refinement proposed in [(SC22WG14.13872) DR 473, 409](https://www.open-std.org/jtc1/sc22/wg14/13872) .
* The “only if” refinement from [(SC22WG14.13872) DR 473, 409](https://www.open-std.org/jtc1/sc22/wg14/13872) met approval from the committee and is adopted in the revised Proposed Technical Corrigendum below.
* This Proposed Technical Corrigendum will, however, invalid practice in one set of compilers where “range error” is used for other purposes. No changes, however, were proposed or accepted to resolve this issue in what remains as The Proposed Technical Corrigendum.
* The implication of this change affects all functions in this section and the committee expressed concern that this impact is unknown and hard to assess.

Apr 2016 meeting

### Committee Discussion

> The committee agreed to change “only occurs if” to “occurs if and only if” in
> three places, and these changes have been made in The Proposed Technical
> Corrigendum below.

### Proposed Technical Corrigendum

Change 7.12.1p2 first sentence from:

> For all functions, a *domain error* occurs if . . .

to:

> For all functions, a *domain error* occurs if and only if . . .

Change 7.12.1p3 first sentence from:

> Similarly, a *pole error* (also known as a singularity or infinitary) occurs if
> . . .

to:

> Similarly, a *pole error* (also known as a singularity or infinitary) occurs if
> and only if . . .

Change 7.12.1p4 from:

> Likewise, a *range error* occurs if the mathematical result of the function
> cannot be represented in an object of the specified type, due to extreme
> magnitude.

to:

> Likewise, a *range error* occurs if and only if the mathematical result of the
> function cannot be represented in an object of the specified type, due to
> extreme magnitude. The description of each function lists any required range
> errors; an implementation may define additional range errors, provided that such
> errors are consistent with the mathematical definition of the function and are
> the result of either overflow or underflow.

In 7.12.6.3 The expm1 function p2 change

> A range error occurs if **x** is too large.<sup>237</sup>

to

> A range error occurs if positive **x** is too large.<sup>237</sup>

In 7.12.8.2 The erfc function p2 change

> A range error occurs if **x** is too large.

to

> A range error occurs if positive **x** is too large.

In 7.12.8.3 The lgamma functions p2 change

> A range error occurs if **x** is too large.

to

> A range error occurs if positive **x** is too large.


</div>


---

---

<div id="issue0474">

## Issue 0474: NOTE 1 Clarification for `atomic_compare_exchange`

Authors: WG14, Blaine Garst  
Date: 2014-11-11  
Reference document: [N1909](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1909.htm)  
Status: Closed  
Cross-references: [0431](log_c11c17.md#issue0431)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

In **7.17.7.4 The atomic\_compare\_exchange generic functions** paragraph 3
states

NOTE 1 For example, the effect of atomic\_compare\_exchange\_strong is

```c
    if (memcmp(object, expected, sizeof (*object) == 0)
         memcpy(object, &desired, sizeof (*object));
    else
        memcpy(expected, object, sizeof (*object));
```

The goal for this note was to show that either object or expected was updated
rather than just being a conditional operation on object alone. It is being read
by some parties, however, to mean that atomic\_compare\_and\_exchange is
intended to do bit comparison instead of value comparison. This is an erroneous
reading.

Consider first non-lock-free atomic types. These obviously require use of the
lock, whether inline or in an external table. So the first conclusion is that an
implementation must already select different implementations for these generic
functions based on whether the type is lock-free or not (ignoring lock bits
leads to data races). The basic algorithm is to take the lock on the target
object, extract and compare values with expected, and store or update desired as
appropriate, and release the lock. The extraction and comparison would likely be
done by the compiler through the use of type specific intrinsics that may or may
not get inlined by the optimizer.

Consider second the cases of padded integer types, padded struct or union types,
and float types.. All of these types have multiple bit representations for one
or more values and will fail erroneously when object and expected differ in
representation but not value. An implementation should, as for non-lock-free
data types, select an appropriate intrinsic to perform this operation. There are
two basic choices for the intrinsic. First, make all these atomic types locking,
and use the locking strategy already in place to attain the lock and extract and
compare the value bits appropriately. An alternate strategy might be to first
"normalize" \*object and \*expected, and then perform bitwise compare and
exchange.

To support this conclusion, I propose clarifying the note to apply to unpadded
lock-free integer types.

### Suggested Technical Corrigendum

In **7.17.7.4 The atomic\_compare\_exchange generic functions** paragraph 3
replace

> NOTE 1 For example, the effect of `atomic_compare_exchange_strong` is ...

with

> NOTE 1 For example, the effect of `atomic_compare_exchange_strong` is, for
> unpadded lock-free integer types, atomically ...

---

Comment from WG14 on 2016-04-14:

Apr 2015 meeting

### Proposed Committee Response

> This change, especially in light of [DR431](log_c11c17.md#issue0431), was thought to likely
> add confusion rather than clarify matters, and no change is desired.


</div>


---

---

<div id="issue0475">

## Issue 0475: Misleading Atomic library references to atomic types

Authors: WG14, Blaine Garst  
Date: 2015-04-15  
Reference document: [N1927](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1927.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The 7.17 atomic library section of the standard and the syntax for atomic types
arose from different authors. The library section was adopted first and then
amended when the syntax proposal was approved during the development of the C11
Standard. The syntax is constructive and applies, with a few exceptions, to all
types, including floats and bitfields.

There are a few unfortunate phrasings remaining in the **7.17 Atomics
\<stdatomic.h\>** section, however, that have caused a small degree of confusion
and are worth fixing.

### Suggested Technical Corrigendum

In **7.17.1 Introduction** p3 Replace

> and several atomic analogs of integer types.

with

> and atomic types declared with the \_Atomic or \_Atomic() construct.

In **7.17.1 Introduction** p5 Replace

> \- An A refers to one of the atomic types.

with

> \- An A refers to an atomic type.

In **7.17.6 Atomic Integer Types** paragraph 2 replace

> The semantics of the operations on these types are defined in 7.17.7

with

> The semantics of the operations on atomic types are defined in 7.17.7

---

Comment from WG14 on 2017-11-03:

Apr 2015 meeting

### Committee Discussion

> The first suggested change is incorrect since it is deliberately speaking of the
> types declared in `<std atomic.h>`.
>
> After discussion, the direction is
>
> In **7.17.1 Introduction** p5 replace
>
> > \- An A refers to one of the atomic types.
>
> with
>
> > \- An A refers to an atomic type.
>
> Delete 7.17.6 paragraph 2\.

Oct 2015 meeting

### Committee Discussion

> The committee accepts the proposed direction as the Proposed Technical
> Corrigendum.

### Proposed Technical Corrigendum

In 7.17.1p5 replace

> \- An A refers to one of the atomic types.

with

> \- An A refers to an atomic type.

Delete 7.17.6 paragraph 2\.


</div>


---

---

<div id="issue0476">

## Issue 0476: volatile semantics for lvalues

Authors: WG14, Martin Sebor  
Date: 2015-08-26  
Reference document: [N1956](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1956.htm)  
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
was a variant of the following snippet copied from early UNIX sources \[1\]:

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
\[11\]. However, they did not have the same ability when the access was through
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
visibility but those are orthogonal to the subject of this paper. See \[3\].

Similar examples can be found in other system or embedded programs as well as in
many other pre-C11 and pre-C\+\+11 code bases that don't rely on the Atomic
types and operations newly inroduced in those standards. They are often cited in
programming books \[4\] and in online articles \[5, 6, 7, 8\].

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

Note in particular that the text refers to <ins>volatile objects</ins>, which
are defined as regions of storage storing the representation of their values.
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
volatile* \[9\], Jonathan Corbet quotes Linus Torvalds, the author and
maintainer of the Linux kernel, as saying:

> Also, more importantly, "`volatile`" is on the wrong <ins>part</ins> of the
> whole system. In C, it's "data" that is volatile, but that is insane. Data isn't
> volatile — <ins>accesses</ins> are volatile. So it may make sense to say "make
> this particular <ins>access</ins> be careful", but not "make all accesses to
> this data use some random strategy".

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

The C99 Rationale \[10\], in §6.7.3 makes it clear that the committee's intent
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

> Accessing a<ins>n object through the use of an lvalue of volatile-qualified
> type</ins><del>volatile object</del>, modifying a file, or calling a function
> that does any of those operations are all side effects...

In §5.1.2.3, Program execution, p4:

> An actual implementation need not evaluate part of an expression if it can
> deduce that its value is not used and that no needed side effects are produced
> (including any caused by calling a function or accessing a<ins>n object through
> the use of an lvalue of volatile-qualified type</ins><del>volatile
> object</del>).

In §5.1.2.3, Program execution, p6, bullet 1:

> Accesses to <ins>objects through the use of lvalues of volatile-qualified
> types</ins><del>volatile objects</del> are evaluated strictly according to the
> rules of the abstract machine.

In §6.7.3, Type qualifiers, p7:

> What constitutes an access to an object <ins>through the use of an lvalue
> of</ins><del>that has</del> volatile-qualified type is implementation-defined.

In §6.8.5, Iteration statements, p6:

> An iteration statement whose controlling expression is not a constant
> expression,<sup>156\)</sup> that performs no input/output operations, does not
> access <ins>objects through the use of lvalues of volatile-qualified types</ins>
> <del>volatile objects</del>, ... may be assumed by the implementation to
> terminate.

In §J.3.10, Qualifiers, p1:

> What constitutes an access to an object <ins>through the use of an lvalue
> of</ins><del>that has</del> volatile-qualified type (6.7.3).

In §L.2.1, p1:

> out-of-bounds store
>
> an (attempted) access (3.1) that, at run time, for a given computational state,
> would modify (or, for an <del>object declared</del><ins>lvalue of</ins>
> volatile<ins>-qualified type</ins>, fetch) one or more bytes that lie outside
> the bounds permitted by this Standard.

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


</div>


---

---

<div id="issue0477">

## Issue 0477: `nan` should take a string argument

Authors: WG14, Martin Sebor  
Date: 2015-08-27  
Reference document: [N1957](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1957.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The Description for the `nan(const char *tagp)` function reads as follows:

> The call `nan("`*n-char-sequence*`")` is equivalent to
> `strtod("NAN(`*n-char-sequence*`)", (char**) NULL)`; the call `nan("")` is
> equivalent to `strtod("NAN()", (char**) NULL)`. If `tagp` does not point to an
> *n-char sequence* or an empty string, the call is equivalent to `strtod("NAN",
> (char**) NULL).`

An *n-char sequence* is a string of an implementation-defined form.

§7.1.4, Use of library functions, requires that arguments to library functions
must have valid values. Specifically, pointers must not be null or point outside
the address space of the program. In addition, arguments described as arrays
(including strings) must be such that all address computations and accesses to
objects that would be valid if the pointer argument did point to the first
element of such an array are in fact valid.

Since `tagp` argument is not required to point to a string or array, only the
first condition in §7.1.4 applies: it must not point outside the address space
of the program or be null.

Therefore, in the snippet below, since `tagp` is a valid pointer that does not
point to an *n-char-sequence* or the empty string, the `nan` call is valid and
required to be be equivalent to `strtod("NAN", (char**) NULL).`

```c
    char c = '1';   // not a n-char-sequence (no terminating NUL)
    char *tagp = &c;
    double x = nan (tagp);
```

But for an implementation that recognizes *n-char-sequences* of length greater
than 1 the requirement to determine whether `tagp` points to one is impossible
to implement since to do so `nan` would have to attempt to read past the end of
`c`.

It seems obvious that this is not intended and that the standard text is simply
missing a requirement that the `tagp` argument point to a string.

### Suggested Technical Corrigendum

The solution is to require the argument to the `nan` family of functions to be a
pointer to a string, analogously to all other library functions that operate on
strings.

Change §7.12.11.2 as follows:

> <ins>The `nan`, `nanf`, and `nanl` functions convert the string pointed to by
> `tagp` according to the following rules.</ins> The call
> `nan("`*n-char-sequence*`")` is equivalent to
> `strtod("NAN(`*n-char-sequence*`)", (char**) NULL)`; the call `nan("")` is
> equivalent to `strtod("NAN()", (char**) NULL)`. If `tagp` does not point to an
> *n-char sequence* or an empty string, the call is equivalent to `strtod("NAN",
> (char**) NULL).`

---

Comment from WG14 on 2017-11-03:

Oct 2015 meeting

### Committee Discussion

* The committee agrees with the author and accepts his Suggested Technical Corrigendum as the committee‘s Proposed Technical Corrigendum.
* This issue is likely a defect in the recently published ISO/IEC TS 18661 Floating Point extensions for C \- Part 1, and the author is solicited to submit a DR against FPE-1 to this committee.

### Proposed Technical Corrigendum

To §7.12.11.2 insert as first sentence:

> The `nan`, `nanf`, and `nanl` functions convert the string pointed to by `tagp`
> according to the following rules. The call `nan("`*n-char-sequence*`")` is
> equivalent ...


</div>


---

---

<div id="issue0478">

## Issue 0478: valid uses of the `main` function

Authors: WG14, Martin Sebor  
Date: 2015-09-10  
Reference document: [N1960](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1960.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The text of the standard isn't entirely clear as to whether or not the function
`main` can be used by strictly conforming C programs in hosted environments. The
following passages quote the permissions and requirements that at the same time
suggest that `main` may not be used by such programs, and that there may be more
than the one call to the function made by the implementation at program startup.

§5.1.2.2.2 Program execution says:

> In a hosted environment, a program may use all the functions, macros, type
> definitions, and objects described in the library clause (clause 7).

suggesting that, since `main` is not described in the library clause but rather
in §5.1.2.2.1, it may not be used by a program.

However, §5.1.2.2.3 Program termination, immediately following the section
quoted above, then goes on to state (emphasis added):

> If the return type of the `main` function is a type compatible with `int`, a
> return from the **initial call** to the `main` function is equivalent to calling
> the `exit` function with the value returned by the `main` function as its
> argument; ...

In addition, §7.21.3 Files contains the following sentence (emphasis also
added):

> If the `main` function returns to **its original caller**, all open files are
> closed...

Finally, since the C\+\+ standard explicitly prohibits programs from calling or
otherwise using `main`, one might expect C to do the same. However the
references to `main`'s initial call and its original caller in the latter two
paragraphs suggest otherwise.

The question was raised and discussed on the committee's mailing list starting
with message [(SC22WG14.13780) valid uses of
main](https://www.open-std.org/jtc1/sc22/wg14/13780). In response, members of
the committee who participated in the preparation of the version of the C
standard that introduced the words clarified that the intent was and remains for
C to allow programs to use `main`. In particular, the intent of §5.1.2.2.2
Program execution is to grant permission to programs to use the facilities of
the standard library but not to preclude the uses of `main` or other symbols
defined by them.

However, since the function `main` is special and unlike any other symbol
defined by a program, and since C\+\+ contains a rule to the contrary, we feel
that the intent isn't sufficiently clearly and unambiguously reflected in the
quoted passages or the rest of the standard, and that a clarification is called
for.

### Suggested Technical Corrigendum

In light of the intent of the passages quoted above as made clear by the mailing
list discussion, we offer two proposals to clarify the text of the standard.

#### Proposal 1

Change §5.1.2.2.2 Program execution as follows:

> In a hosted environment, a program may use <ins>the function `main` as well
> as</ins> all the functions, macros, type definitions, and objects described in
> the library clause (clause 7).

#### Proposal 2

Add a footnote to the end of §5.1.2.2.2 Program execution, with the following
text:

> <ins>A program may also use the function `main`.</ins>

---

Comment from WG14 on 2016-10-21:

Oct 2015 meeting

### Committee Discussion

> The committee does not agree that any further clarification is needed in the
> standard. We know of no actual confusion in a practical sense on this matter. As
> such, the committee agrees with and draws substantially from [(SC22WG14.13787)
> RE: RE: RE: valid uses of main](https://www.open-std.org/jtc1/sc22/wg14/13780)
> in the formulation of its Proposed Committee Response below.

### Proposed Committee Response

> As there is no "only" in 5.1.2.2.2 the interpretation should be that the
> statement is granting permission, not making a restriction. It is drawing a
> distinction between freestanding environments, where only a subset of the
> library can be used, and hosted environments, where all of the library can be
> used. Programs are always free, in either kind of environment, to use things in
> addition to the library, like their own functions and objects. Additionally, the
> reference in 5.1.2.2.3 to the **initial** call to `main` strongly suggests that
> recursive calls are allowed.


</div>


---

---

<div id="issue0479">

## Issue 0479: unclear specification of `mtx_trylock` on non-recursive muteness

Authors: WG14, Torvald Riegel, Martin Sebor  
Date: 2015-09-25  
Reference document: [N1963](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1963.htm)  
Status: Closed  
Cross-references: [0469](log_c11c17.md#issue0469), [0493](log_c11c17.md#issue0493)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The specification of `mtx_trylock` if applied to a non-recursive mutex is not
clear. Whereas it is spelled out for `mtx_lock` that a thread must not attempt
to lock a non-recursive mutex more than once, there is no such requirement for
`mtx_trylock`. The existing wording for `mtx_trylock` could be understood as
requiring `mtx_trylock` to fail; however, that would defeat the purpose of
separating recursive from non-recursive mutexes because it would require
implementations to track which thread owns the mutex.

(It might also be good if the standard would define what recursive locking
actually is, but this is outside of the focus of this paper.)

### Suggested Technical Corrigendum

The standard should specify the requirement for `mtx_lock` explicitly for
`mtx_trylock` as well. Specifically, add the following sentence to 7.26.4.5p2:

> If the mutex is non-recursive, it shall not be locked by the calling thread.

---

Comment from WG14 on 2018-10-18:

Oct 2015 meeting

### Committee Discussion

* The committee agrees that this clarification would be useful, that is, that `mtx_trylock` should fail if attempted on an already held non-recursive mutex. We did not agree that the Proposed Technical Corrigendum addressed this defect correctly.
* Coordinated new wording is solicited from the authors to both this and the solicited author for the resolution of [DR 469](log_c11c17.md#issue0469) since it also is proposing potentially overlapping wording changes in this area.

Apr 2016 meeting

### Committee Discussion

> This resolution continues to be bound to [DR 469](log_c11c17.md#issue0469)

Apr 2018 meeting

### Committee Discussion

> The committee solicited a combined comprehensive resolution for these issues
> with those raised in [DR 469](log_c11c17.md#issue0469) and [DR 493](log_c11c17.md#issue0493). The authors
> will be invited to review and provide input to said paper.
>
> As discussed in committee, an approach for resolving copying that parallels FILE
> treatment will be considered. In that case, 7.21.3p6 is germaine:
>
> > The address of a `FILE` object used to control a stream may be significant; a
> > copy of a `FILE` object need not serve in place of the original.
>
> The committee advised that this alone would not be sufficient, but would serve
> as a preferred starting point.

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> These issues were not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that issues from [CR 469](log_c11c17.md#issue0469), [CR 479](log_c11c17.md#issue0479), and [CR
> 493](log_c11c17.md#issue0493), as well as potentially other small issues be combined in a new
> paper to completely resolve this issue for the next revision of the standard.


</div>


---

---

<div id="issue0480">

## Issue 0480: `cnd_wait` and `cnd_timewait` should allow spurious wake-ups

Authors: WG14, Torvald Riegel, Martin Sebor  
Date: 2015-09-25  
Reference document: [N1964](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1964.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Both ISO C\+\+ and POSIX allow for spurious wake-ups from their condition
variable wait functions. However, C11 has no wording that would allow that.
(This applies to both `cnd_wait` and `cnd_timewait`, but just `cnd_wait` is
referred to in what follows.)

If spurious wake-ups are allowed, then some implementations become significantly
easier; it also allows to implement the C standard on top of POSIX using just a
thin wrapper. In contrast, implementing a condition variable that does not allow
spurious wake-ups on top of a condition variable implementation that does allow
that is likely close to implementing a condition variable from scratch in terms
of complexity.

Another reason for allowing spurious wake-ups is that to actually exploit having
no spurious wake-ups, a program needs to take quite some care to establish the
happens-before relations required to make just the return from `cnd_wait` mean
something that can be used to infer something about the then current state of
memory (for example, if the wake-up is supposed to also mean that some state has
been initialized).

Specifically, the program must make sure that it actually calls `cnd_signal` (or
`cnd_broadcast`) after `cnd_wait` has started to block; this can be ensured by
calling `cnd_signal` from a critical section protected by the same mutex as
supplied to the respective `cnd_wait`, and checking the ordering of the
`cnd_wait` and `cnd_signal` critical sections in some way (e.g., through access
to variables protected by the same mutex, or by not letting the signaling thread
enter the `cnd_signal` critical section before the `cnd_wait` critical section).
Second, `cnd_wait` is not specified to synchronize with `cnd_signal`, so either
`cnd_signal` must be in such a critical section (ie, there is a second reason
for that), or the signaler and the waiter must establish a happens-before
relation through other means such as atomics.

### Suggested Technical Corrigendum

Change this sentence from the specification of `cnd_wait` (7.26.3.6p2):

> The cnd\_wait function atomically unlocks the mutex pointed to by mtx and
> endeavors to block until the condition variable pointed to by cond is signaled
> by a call to cnd\_signal or to cnd\_broadcast.

to this:

> The cnd\_wait function atomically unlocks the mutex pointed to by mtx and
> endeavors to block until the condition variable pointed to by cond is signaled
> by a call to cnd\_signal or to cnd\_broadcast, or until it is unblocked due to a
> spurious, unspecified reason.

Likewise for `cnd_timedwait`.

---

Comment from WG14 on 2017-11-03:

Oct 2015 meeting

### Committee Discussion

> The committee agrees with the authors’ interpretation and accepts their
> Suggested Technical Corrigendum with one minor edit. The word “spurious” is felt
> to be implied by the use of the verb “endeavors” and is struck.

Apr 2016 meeting

### Committee Discussion

> The committee decided to change “endeavors to block” to “blocks”, and that
> change is made in the Proposed Technical Corrigendum below.

### Proposed Technical Corrigendum

In §7.26.3.5p2 change

> The `cnd_timedwait` function atomically unlocks the mutex pointed to by `mtx`
> and endeavors to block until the condition variable pointed to by `cond` is
> signaled by a call to `cnd_signal` or to `cnd_broadcast`, or until after the
> `TIME_UTC`-based calendar time pointed to by `ts`.

to

> The `cnd_timedwait` function atomically unlocks the mutex pointed to by `mtx`
> and blocks until the condition variable pointed to by `cond` is signaled by a
> call to `cnd_signal` or to `cnd_broadcast`, or until after the `TIME_UTC`-based
> calendar time pointed to by `ts`, or until it is unblocked due to an unspecified
> reason.

In §7.26.3.6p2 change

> The `cnd_wait` function atomically unlocks the mutex pointed to by `mtx` and
> endeavors to block until the condition variable pointed to by `cond` is signaled
> by a call to `cnd_signal` or to `cnd_broadcast`.

to:

> The `cnd_wait` function atomically unlocks the mutex pointed to by `mtx` and
> blocks until the condition variable pointed to by `cond` is signaled by a call
> to `cnd_signal` or to `cnd_broadcast`, or until it is unblocked due to an
> unspecified reason.


</div>


---

---

<div id="issue0481">

## Issue 0481: Controlling expression of `_Generic` primary expression

Authors: WG14, Jens Gustedt  
Date: 2015-04-24  
Reference document: [N1930](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1930.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

This is a follow up of the now closed DR 423 which resulted in the clarification
of the status of qualifications of rvalues.

This defect report aims to clarify the status of the controlling expression of
`_Generic` primary expression:

***Does the controlling expression of a `_Generic` primary expression undergo
any type of conversion to calculate the type that is used to do the
selection?***

Implementers have given different answers to this question; gcc (*choice 1* in
the following) on one side and clang and IBM (*choice 2*) on the other side went
quite opposite ways, resulting in severe incompatibility for `_Generic`
expression that use qualifiers or arrays.

```c
char const* a = _Generic("bla", char*: "blu");                 // clang error
char const* b = _Generic("bla", char[4]: "blu");               // gcc error
char const* c = _Generic((int const){ 0 }, int: "blu");        // clang error
char const* d = _Generic((int const){ 0 }, int const: "blu");  // gcc error
char const* e = _Generic(+(int const){ 0 }, int: "blu");       // both ok
char const* f = _Generic(+(int const){ 0 }, int const: "blu"); // both error
```

The last two lines, where gcc and clang agree, points to the nature of the
problem: gcc treats all such expressions as rvalues and does all applicable
conversions of 6.3.2.1, that is lvalue to rvalue and array to pointer
conversions. clang treats them as lvalues.

### Problem discussion

The problem arises to know whether or not the conversions of 6.3 apply to the
controlling expression.

* **promotions:** There is no general rule to which expressions these apply, but their application is hard coded for the individual operators, where it makes reference to "its (promoted) operand".
* **lvalue conversion:** I didn't find any text that would impose lvalue conversion performed to the controlling expression. All wording in 6.3 is "some" and "may". Also it talks of "operators" and "operations", but `_Generic` is not an operator, but a primary expression. The wording in 6.5.1.1 is *has a type* and doesn't make any reference to type conversion.
* **array conversion:** The support for array conversion is stronger. Array conversion has an explicit list of cases (*6.3.2.1 p3*) were an array is an *operand* where it doesn't apply. But
  + The case of arrays as an exception in *6.3.2.1 p3* doesn't list the *associations* of `_Generic` either, which are listed in *6.5.1.1*.
  + There is another precedent, namely *parenthesized expressions*, which are also not listed in *6.3.2.1 p3* and where nobody expects an array conversion, either.

#### Integer promotions

Applying promotions would have as an effect that we wouldn't be able to
distinguish narrow integer types from `int`. There is no indication that the
text implies that form or conversion, nor that anybody has proposed to use
`_Generic` like this.

#### Choice 1: Consequences of lvalue conversion

All conversion in *6.3.2.1 p2* describe what would in normal CS language be
named the evaluation of an object. It has no provision to apply it to types
alone. In particular it includes the special clause that uninitialized
`register` variables lead to undefined behavior when undergoing lvalue
conversion. As a consequence:

*Any lvalue conversion of an uninitialized `register` variable leads to
undefined behavior.*

And thus

***Under the hypothesis that the controlling expression undergoes lvalue
conversion, any `_Generic` primary expression that uses an uninitialized
`register` variable as controlling expression leads to undefined behavior.***

#### Choice 2: Consequences not doing conversions

In view of the resolution of DR 423 (rvalues drop qualifiers) using `_Generic`
primary expressions with objects in controlling expression may have results that
appear surprising.

```c
#define F(X) _Generic((X), char const: 0, char: 1, int: 2)
char const strc[] = "";
F(strc[0])   // -> 0
F(""[0])     // -> 1
F(+strc[0])  // -> 2
```

So the problem is here, that there is no type agnostic operator that results in
a simple lvalue conversion for `char const` objects to `char`; all such
operators also promote `char` to `int`.

***Under the hypothesis that the controlling expression doesn't undergo
conversion, any `_Generic` primary expression that uses a qualified lvalue of
narrow type `T` can't directly trigger the association for `T` itself.***

#### non-equivalence of the two approaches

For many areas the two approaches are feature equivalent, that is both allow to
implement the same semantic concepts, but with different syntax. Rewriting code
that was written with one of choices in mind to the other choice is in general
not straight forward and probably can't be automated.

* Code that was written with *choice 1* in mind (enforced lvalue and array conversion) when translated to *choice 2* has to enforce such conversions. E.g as long as we know that the type of `X` is only a wide integer type or an array or pointer type, a macro such as

  ```c
          #define bla(X) _Generic((X), ... something ... )
  ```

  would have to become

  ```c
          #define bla(X) _Generic((X)+0, ... something ... )
  ```

  Writing code that takes care of narrow integer types is a bit more difficult, but can be done with 48 extra case selections, taking care of all narrow types (6) and all their possible qualifications (8, `restrict` is not possible, here). Code that uses `struct` or `union` types must use bizarre things like `1 ? (X) : (X)` to enforce lvalue conversion.

  ```c
          #define blaOther((X),                                  \
            char: blub, char const: blub, ...,                   \
            short: ...,                                          \
            default: _Generic(1 ? (X) : (X), struct toto: ... )

          #define bla(X) _Generic((X)+0, ... something ... ,     \
            default: blaOther(X))
  ```
* Code that was written with *choice 2* in mind (no lvalue or array conversion) when translated to *choice 1* has to pass to a setting where qualifiers and arrays are preserved in the type. The only such setting is the address-of operator `&`.

  ```c
          #define blu(X) _Generic((X), \
             char const: blub,         \
             char[4]: blob,            \
             ...)
  ```

  has to be changed to something like

  ```c
          #define blu(X) _Generic(&(X),\
            char const*: blub,         \
            char(*)[4]: blob,          \
            ...)
  ```

  That is each individual type selection has to be transformed, and the syntactical change that is to be apply is no simple textual replacement.

### Application work around

Since today C implementations have already taken different paths for this
feature, applications should be careful when using `_Generic` to remain in the
intersection of these two interpretations. A certain number of design questions
should be answered when implementing a type generic macro:

* Do I want to differentiate the outcome according to the qualification of the argument?
* Do I want to distinguish arrays from pointer arguments?
* Do I want to distinguish narrow types?
* Do I want to apply it to composite types, namely `struct` types?

The following lists different strategies for common scenarios, that can be used
to code type generic macros that will work with both of the choices 1 or 2\.

#### Wide integers and floating point types

This is e.g the case of the C library interfaces in `<tgmath.h>`. If we know
that the possible type of the argument is restricted in such a way, the easiest
is to apply the unary plus operator `+`, as in

```c
  #define F(X) _Generic(+(X),             \
    default: doubleFunc,                  \
    int: intFunc,                         \
    ...                                   \
    _Complex long double: cldoubleFunc)(X)

  #define fabs(X) _Generic(+(X),          \
    default: fabs,                        \
    float: fabsf,                         \
    long double: fabsl)(X)
```

This `+` sign ensures an lvalue to rvalue conversion, and, that it will error
out at compilation time for pointer types or arrays. It also forcibly promotes
narrow integer types, usually to `int`. For the later case of `fabs` all integer
types will map to the `double` version of the function, and the argument will
eventually be converted to `double` before the call is made.

#### Adding pointer types and converting arrays

If we also want to capture pointer types *and* convert arrays to pointers, we
should use `+0`.

```c
  #define F(X) _Generic((X)+0),           \
    default: doubleFunc,                  \
    char*: stringFunc,                    \
    char const*: stringFunc,              \
    int: intFunc,                         \
    ...                                   \
    _Complex long double: cldoubleFunc)(X)
```

This binary `+` ensures that any array is first converted to a pointer; the
properties of `0` ensure that this constant works well with all the types that
are to be captured, here. It also forcibly promotes narrow integer types,
usually to `int`.

#### Converting arrays, only

If we k now that a macro will only be used for array and pointer types, we can
use the `[]` operator:

```c
  #define F(X) _Generic(&((X)[0]),        \
    char*: stringFunc,                    \
    char const*: stringFunc,              \
    wchar_t*: wcsFunc,                    \
    ...                                   \
    )(X)
```

This operator only applies to array or to pointer types and would error if
present with any integer type.

#### Using qualifiers of types or arrays

If we want a macro that selects differently according to type qualification or
according to different array size, we can use the `&` operator:

```c
  #define F(X) _Generic(&(X),        \
    char**: stringFunc,              \
    char(*)[4]: string4Func,         \
    char const**: stringFunc,        \
    char const(*)[4]: string4Func,   \
    wchar_t**: wcsFunc,              \
    ...                              \
    )(X)
```

### Possible solutions

The above discussion describes what can be read from the text of C11, alone, and
not the intent of the committee. I think if the committee would have wanted a
*choice 2*, the standard text would not have looked much different than what we
have, now. Since also the intent of the committee to go for *choice 1* seems not
to be very clear from any additional text (minutes of the meetings, e.g) I think
the reading of *choice 2* should be the preferred one.

### Suggested Technical Corrigendum (any choice)

Amend the list in footnote 121 for objects with `register` storage class. Change

> Thus, the only operators that can be applied to an array declared with
> storage-class specifier `register` are `sizeof` and `_Alignof`.

<ins>Thus, an identifier with array type and declared with storage-class
specifier `register` may only appear in primary expressions and as operand to
`sizeof` and `_Alignof`.</ins>

### Suggested Technical Corrigendum (Choice 2\)

Change 6.5.1.1 p3, first sentence

> The controlling expression of a generic selection is not evaluated <ins>and the
> type of that expression is used without applying any conversions described in
> Section 6.3</ins>.

Add `_Generic` to the exception list in *6.3.2.1 p3* to make it clear that array
to pointer conversion applies to none of the controlling or association
expression if they are lvalues of array type.

> Except when it is <ins>the controlling expression or an association expression
> of a `_Generic` primary expression, or is</ins> the operand of the `sizeof`
> operator, the `_Alignof` operator, or the unary `&` operator, or is a string
> literal used to initialize an array, an expression that has type “array of type”
> is converted to an expression with type “pointer to type” that points to the
> initial element of the array object and is not an lvalue. If the array object
> has register storage class, the behavior is undefined.

Also add a forward reference to `_Generic` in 6.3.2.

### Suggested Technical Corrigendum (Choice 1\)

If the intent of the committee had been *choice 1* or similar, bigger changes of
the standard would be indicated. I only list some of the areas that would need
changes:

* Move `_Generic` from primary expressions to a proper subsection, and rename the feature to `_Generic` operator.
* Clarify which *as-if* conversions must be applied to determine the type.
* Reformulate those conversions as conversions of types instead of values.

Also, add `_Generic` to the exception list in *6.3.2.1 p3* to make it clear that
array to pointer conversion applies to none of the association expression if
they are lvalues of array type.

> Except when it is <ins>an association expression of a `_Generic` expression, or
> is</ins> the operand of the `sizeof` operator, the `_Alignof` operator, or the
> unary `&` operator, or is a string literal used to initialize an array, an
> expression that has type “array of type” is converted to an expression with type
> “pointer to type” that points to the initial element of the array object and is
> not an lvalue. If the array object has register storage class, the behavior is
> undefined.

### Suggested Technical Corrigendum (Status quo)

A third possibility would be to leave this leeway to implementations. I strongly
object to that, but if so, I would suggest to add a phrase to 6.5.1.1 p3 like:

> ... in the default generic association. <ins>Whether or not the type of the
> controlling expression is determined as if any of conversions described in
> Section 6.3 are applied is implementation defined.</ins> None of the expressions
> ...

---

Comment from WG14 on 2017-11-03:

Oct 2015 meeting

### Committee Discussion

* This paper elicited a long and productive discussion. The committee agrees with the author of the `_Generic` proposal that the intent was that selecting on qualified types was explicitly to be avoided as was selecting on arrays by size. The intent of `_Generic` was to give C a mechanism to somewhat express the notion of “overloaded function” found in C\+\+, and in particular a possible mechanism for implementors to use to implement the atomic type generic functions from section 7.17.7. Although this sentiment is most closely reflected in Choice 1 above, and it is reported that clang has also now adopted that approach, the committee feels that the wording in the Suggested Technical Corrigendum is not appropriate.
* The sentiment of the committee is to state that the type of arrays should decay into pointers in the controlling expression of a `_Generic` primary expression.
* The sentiment of the committee is that a better approach to the lvalue conversion issue is to revise 6.5.1.1p2 by adding something along the lines of
  > The type of the controlling expression of a generic selection is the unqualified
  > type determined by applying the lvalue conversions described in 6.3.2.1p2 as if
  > by evaluation.
* The author is requested to incorporate this feedback into a new proposal and is encouraged to solicit input directly from committee members and on the WG14 reflector.

Apr 2016 meeting

### Committee Discussion

> The paper [N2001](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2001.pdf)
> was presented and, with revision, adopted as the Proposed Technical Corrigendum
> below.

Oct 2016 meeting

### Committee Discussion

> It was noted that bitfields are of integer type.

### Proposed Technical Corrigendum

In §6.5.1.1p2 change:

> The controlling expression of a generic selection shall have type compatible
> with at most one of the types named in its generic association list.

to

> The type of the controlling expression is the type of the expression as if it
> had undergone an lvalue conversion<sup>new</sup>, array to pointer conversion,
> or function to pointer conversion. That type shall be compatible with at most
> one of the types named in the generic association list.
>
> <sup>new)</sup>lvalue conversion drops type qualifiers.


</div>


---

---

<div id="issue0482">

## Issue 0482: Macro invocation split over many files

Authors: WG14, Fred J. Tydeman  
Date: 2015-06-23  
Reference document: [N1942](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1942.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Based upon my reading of the standard, it appears that the following is strictly
conforming code. However, many compilers refuse to translate it (which I think
is good).

main.c:

```c
#include <string.h>  /* strcpy(), strcmp() */
#undef NDEBUG
#include <assert.h>  /* assert() */

int main(void) {
  int line1;
  int line2;
  char file1[1023];
  char file2[1023];

  #include "file1.h"    /* start of call of assert() split over many files */
  );                    /* end of assert() */

  assert( 2 == line1 );
  assert( 3 == line2 );
  assert( 0 != strcmp( file1, file2 ) );

  return 0;
} /* end main() */
```

file2.h:

```c
assert(
       ( (void)strcpy(file1,__FILE__), line1 = __LINE__ )
```

file1.h:

```c
#include "file2.h"
!=
  ( (void)strcpy(file2,__FILE__), line2 = __LINE__ )
```

There already are some ways to have a macro invocation be split over two files
that result in undefined behaviour.

5.1.1.2 Translation phases, paragraph 1, bullet 2 has:

> A source file that is not empty shall end in a new-line character, which shall
> not be immediately preceded by a backslash character before any such splicing
> takes place.

which makes using line splicing (as a way to split a macro invocation over many
files) undefined.

6.10.3 Macro replacement, paragraph 11 has:

> If there are sequences of preprocessing tokens within the list of arguments that
> would otherwise act as preprocessing directives,172) the behavior is undefined.

which makes using #include of arguments (as a way to split a macro invocation
over many files) between the outside-most matching parentheses undefined.

### Suggested Technical Corrigendum

Add to 5.1.1.2, paragraph 1, bullet 3, words along the lines of:

> A macro invocation shall be contained within one source file.

---

Comment from WG14 on 2017-04-07:

Oct 2015 meeting

### Committee Discussion

> The committee was unsympathetic to the Suggested Technical Corrigendum. It was
> noted that function invocations are allowed to span files and that there are
> some implementations that do support macro invocations that the Suggested
> Technical Corrigendum would invalidate.
>
> The committee agrees that such uses should probably have been prohibited in the
> original specification and may consider adding such restrictions in a possible
> future revision of the Standard, and will record this intent in the next
> revision of WG 14 Standing Document 3 currently at
> [N1972](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1972.htm) .

Apr 2016 meeting

### Committee Discussion

> The Proposed Committee Response was augmented.

### Proposed Committee Response

> The committee agrees that such uses should probably have been prohibited in the
> original specification and may consider adding such restrictions in a possible
> future revision of the Standard, and has recorded this intent in WG 14 Standing
> Document 3\.
>
> Although the committee agrees that such invocations are not necessarily best
> practice, they are supported in existing implementations and as such the
> committee sees no benefit to accepting changes that would invalidate this
> practice.


</div>


---

---

<div id="issue0483">

## Issue 0483: `__LINE__` and `__FILE__` in macro replacement list

Authors: WG14, Fred J. Tydeman  
Date: 2015-06-23  
Reference document: [N1943](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1943.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Based upon my reading of the standard, it appears that the following are
ambiguous, so are a possible defect.

* The line number associated with a \_\_LINE\_\_ in a macro replacment list. It could be the line number of the macro replacment list or of the macro invocation.
* The source file name associated with a \_\_FILE\_\_ in a macro replacment list. It could be the file name of the macro replacment list or of the macro invocation.

An example of that.

```c
  #line 500
  #define MAC() __LINE__

  #line 1000
 int j = MAC();         /* is this 500 or 1000? */
```

However, 7.2.1.1 requires that the **assert** macro write information about the
call that has a false expression. That information includes the \_\_LINE\_\_ and
\_\_FILE\_\_ preprocessing macros. So, there is a requirement that this specific
macro using \_\_LINE\_\_ and \_\_FILE\_\_ have the line number and file name of
the invocation, not the line number and file name of the replacment list (in
\<assert.h\>).

### Suggested Technical Corrigendum

Add to 6.10.8.1, paragraph 1, item \_\_LINE\_\_:

> The line number associated with a \_\_LINE\_\_ in a macro replacment list is the
> line number of the macro invocation.

Add to 6.10.8.1, paragraph 1, item \_\_FILE\_\_:

> The source file name associated with a \_\_FILE\_\_ in a macro replacment list
> is the source file name of the macro invocation.

---

Comment from WG14 on 2016-10-21:

Oct 2015 meeting

### Committee Discussion

> The committee notes that these issues are also raised in the WG21 C\+\+
> committee document
> [N4220](https://www.open-std.org/jtc1/sc22/wg21/www/docs/papers/2014/n4220.pdf).
> However, the committee also notes that among all implementations “nobody gets
> this wrong” and as such there is no actual confusion, and although there is
> sentiment that the standard might not perfectly express its intent, it is clear
> enough to warrant no change.

### Proposed Committee Response

> The committee believes that since there is no evidence of confusion over the
> intent of the standard in this area by any implementor that there is no defect
> worth correcting at this time.


</div>


---

---

<div id="issue0484">

## Issue 0484: invalid characters in `strcoll()`

Authors: WG14, Fred J. Tydeman  
Date: 2015-06-23  
Reference document: [N1944](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1944.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

7.24.4.3 strcoll makes the assumption that the result of comparing two strings
can only have one of three outcomes: greater than, equal to, or less than.
However, there is a fourth outcome that is possible: not comparable.

I have been told that there are locales or codesets that have strings of bytes
that do not form valid characters. Those invalid characters could be considered
Not-a-Character (similar to Not-a-Number for floating-point). And, they are not
comparable to anything.

I do not know if the same issue can apply to wchar\_t. If so, then 7.29.4.4.1
wcscmp(), 7.29.4.4.3 wcsncmp(), and 7.29.4.4.5 wmemcmp() have the same problem.

### Suggested Technical Corrigendum

Replace the start of 7.24.4.3, paragraph 3,

> The **strcoll** ...

with

> If either string contains invalid characters, **errno** is set to an
> implementation defined value and the return value is unspecified; otherwise,
> **errno** is left alone and the **strcoll** ...

The same change should also be applied to 7.29.4.4.2 wcscoll.

---

Comment from WG14 on 2016-10-21:

Oct 2015 meeting

### Committee Discussion

> The committee agrees that the standard does not specify behavior under these
> conditions and as such there is undefined behavior by way of §7.1.4p1 “If an
> argument to a function has an invalid value … the behavior is undefined”. There
> is strong sentiment to keep the library fast and that imposing new requirements
> to set `errno` is to be generally avoided. Whereas POSIX does define behavior
> that sets `errno` under these conditions, it is explicitly the intent of the
> committee to leave such behavior undefined in the standard to allow such
> refinements by others.

### Proposed Committee Response

> By way of §7.1.4p1 “If an argument to a function has an invalid value … the
> behavior is undefined” the behavior of `strcoll` in the face of invalid input is
> already clearly undefined. The committee wishes to leave it so specified. This
> latitude allows POSIX to further refine the semantics according to their needs.
> We therefore do not accept the Proposed Technical Corrigendum.


</div>


---

---

<div id="issue0485">

## Issue 0485: Problem with the specification of `ATOMIC_VAR_INIT`

Authors: WG14, Jens Gustedt  
Date: 2015-08-07  
Reference document: [N1951](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1951.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The current version of the standard states that the argument to this macro
should be a value of the corresponding base type of the atomic object that is to
be initialized.

> The `ATOMIC_VAR_INIT` macro expands to a token sequence suitable for
> initializing an atomic object of a type that is initialization-compatible with
> value.

This is problematic, because it excludes the primary form of initializers, the
`{ }` form, from the possible uses, that would be necessary to initialize
`struct` or `union` types properly.

**Problem discussion**

As a consequence, there is a problem for atomic objects that combine the two
properties:

1. The base type is a `struct` or `union` type.
2. The object has static or thread-local storage duration.

The problem is, that for such types there are no compile time constants that
could be used as *value*, here. As a consequence the standard *doesn't allow
explicit initialization* for these objects.

1. Atomic objects of `struct` or `union` type and static or thread-local storage duration can only be default initialized.
2. At program and thread startup, respectively, atomic objects of `struct` or `union` type and static or thread-local storage duration are in an indeterminate state.

This is an important drawback that doesn't seem to be intentional:

* The `ATOMIC_VAR_INIT` had exactly been introduce for the purpose of initializing objects of static storage to a valid state with known value.
* `struct` atomics play an important role for lock-free data structures to avoid the ABA problem.

**Current practice**

Both compilers that I have my hands on (gcc 4.9 and clang 3.6) that implement
`<stdatomic.h>` have something equivalent to

```c
#define ATOMIC_VAR_INIT(VALUE)  (VALUE)
```

This is of course conforming to the standard text as it is now, but exhibit the
exact problem. They don't allow for a compile time initializer since the `()`
around `VALUE` result in invalid syntax if `VALUE` is a `{ }` initializer.

Clang has an implementation specific way out of this: they allow compound
literals with constant initializers in that context. Gcc provides no such
solution.

For both compilers, it is easily possible to overwrite the macro definition into
one that omits the parenthesis and all works fine.

### Suggested Technical Corrigendum

Change the beginning of the corresponding section, 7.17.2.1p2, to:

<ins>7.17.2.1 The `ATOMIC_VAR_INIT` macro  
**Synopsis**</ins>

<ins>`#include <stdatomic.h>`  
`#define ATOMIC_VAR_INIT(initializer)`</ins>

<ins>**Description**  
The `ATOMIC_VAR_INIT` macro expands to a token sequence suitable for
initializing an atomic object `X`. For any invocation of this macro, the
*initializer* argument shall expand to a token sequence that would be suitable
to initialize `X` if the atomic qualification would be dropped.**footnote**That
is, it could be used to initialize an object `Y` of the same base type, storage
duration and place of declaration as `X`, but without atomic qualification.**end
footnote**  
An atomic object with automatic storage duration ...</ins>

Then append a new note after the actual para 4:

<ins>*Note:* Since *initializer* may be a token sequence that contains commas
which are not protected by `()` it may constitute a variable number of arguments
for the macro evaluation. Implementations should be able to deal with such
situations by defining `ATOMIC_VAR_INIT` as accepting a variable argument
list.</ins>

---

Comment from WG14 on 2017-11-03:

Oct 2015 meeting

### Committee Discussion

* The fundamental issue is the apparent inability to initialize atomic structures or unions due to the definition of the `ATOMIC_VAR_INIT` macro as taking a single argument. Some implementations have already taken the liberty of treating the macro as variadic for purposes of atomic structure initialization and moreover to also implicitly provide surrounding `{` and `}` that form the syntax for a structure initializer or compound literal as appropriate to the implementation.
* The committee agrees with the sentiment expressed in the suggested NOTE although the wording was not discussed.
* The suggested changes to 7.17.2.1 were not acceptable to the committee, however, and may not be needed at all since, in particular the declared type `C` is already the non-atomic version of the atomic type `A` of the variable being initialized. Use of the term “base type” is undefined in C for example.
* The committee requests that the author take this input under advisement in a new solicited paper that would, in effect, make explicit the extended practice.

Apr 2016 meeting

### Committee Discussion

> A short paper was provided with a Suggested Technical Corrigendum and, although
> close, more work was solicited from the authors. The direction discussed by the
> committee was given that in the section `C` is defined to be the non-atomic
> equivalent of type `A`,
>
> * new wording must be provided to say it takes an initializer for an object of type `C`, and the macro expands to an object of type `A`, and that
> * the macro can be defined as in the Suggested Technical Corrigendum:
>
>   ```c
>       #define ATOMIC_VAR_INIT(...)
>   ```

Oct 2016 meeting

### Committee Discussion

> The definition of `ATOMIC_VAR_INIT` as a macro is problematic. Several
> implementations use locks introduced by compiler magic for larger structures and
> the macro cannot provide for the proper initialization of a lock that is not
> visible. For these and other implementations, `ATOMIC_VAR_INIT` should be fully
> implemented as compiler magic.
>
> Since removing the definition of the macro is outside the scope of a DR, this
> issue may only be addressable in a future revision of the standard.

Apr 2017 meeting

### Committee Discussion

> Although discussed at the last meeting, the point that there are no known
> implementations using *embedded* locks was not accurately reflected in the prior
> discussion. Atomic structures may still differ in size due to potentially
> increased alignment requirements. It was further noted that some implementations
> use "compiler magic" at initialization time.
>
> Since the macro definition is neither necessary nor sufficient for structures,
> the email [(SC22WG14.14645) DR 485 wording for TC
> 2017](https://www.open-std.org/jtc1/sc22/wg14/14645) containing two suggested
> technical corrigenda was discussed at some length. Neither change, however, is
> appropriate as a technical corrigendum, and as such this issue cannot be
> addressed using the Defect Report process.

### Proposed Committee Response

> The `ATOMIC_VAR_INIT` macro was added to the standard without wide
> implementation experience with the intent being to allow implementations to use
> embedded locks in atomic types. It was not, however, well formulated to
> accommodate the extension of atomics to structures since it would, perhaps,
> require variadic arguments. No known implementations use embedded locks,
> however, and as such there is no technical requirement for the use of the
> `ATOMIC_VAR_INIT` macro.
>
> Correcting this is beyond the scope of the Defect Report process.
>
> There was consensus in the committee to deprecate this macro in the next
> revision of the standard. The following words, drawn from [(SC22WG14.14645) DR
> 485 wording for TC 2017](https://www.open-std.org/jtc1/sc22/wg14/14645), are the
> proposed direction:
>
> In §7.17.2.1 replace paragraph 2 with:
>
> > An atomic object with automatic storage duration that is not explicitly
> > initialized is initially in an indeterminate state.


</div>


---

---

<div id="issue0486">

## Issue 0486: Inconsistent specification for arithmetic on atomic objects

Authors: WG14, Jens Gustedt  
Date: 2015-08-07  
Reference document: [N1955](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1955.htm)  
Status: Closed  
Cross-references: [0495](log_c11c17.md#issue0495)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Whereas its intent is clear, the text in the C standard that concerns atomics
has several consistency problems. There are contradictions and the standard
vocabulary is not always applied correctly.

**Problem discussion**

*— Memory order of operators —*

The following sections on arithmetic operators, all specify that if they are
applied to an atomic object as an operand of **any** arithmetic base type, the
memory order sematic is `memory_order_seq_cst`:

* 6.2.6.1 Loads and stores of objects with atomic types are done with `memory_order_seq_cst` semantics.
* 6.5.2.4 (postfix `++` and `--`)
* 6.5.16.2 Compound assignment. No constraints formulated concerning traps for integer types. In contrast to that, no floating exceptions for floating types are allowed. Also, this defines atomic operations for **all** arithmetic operands, including some that don't have library calls (`*=`, `/=`, `%=`, `<<=`, `>>=`)

No such mention is made for

* 6.5.3.1 (prefix `++` and `--`), although it explicitly states that these operators are defined to be equivalent to `+= 1` and `-= 1`, respectively.
* 6.5.16.1 Simple assignment, although the paragraph about store says that such a store should be `memory_order_seq_cst`.

*— Integer representations and erroneous operations —*

Concerning the generic library calls, they state in 7.17.7.5

> For signed integer types, arithmetic is defined to use two’s complement
> representation with silent wrap-around on overflow; there are no undefined
> results.

and

> For address types, the result may be an undefined address, but the operations
> otherwise have no undefined behavior.

Can the sign representation depend on the operation that we apply to an object?  
Are these operations supposed to be consistent between operator and function
notation?  
What is an *address type*?  
What is "*no undefined behavior*"? How is the behavior then defined, when we are
not told about it?

*— Operators versus generic functions —*

Then a **Note** (7.17.7.5 p 5\) states

> The operation of the atomic\_fetch and modify generic functions are nearly
> equivalent to the operation of the corresponding `op=` compound assignment
> operators. The only differences are that the **compound assignment operators are
> not guaranteed to operate atomically**, ...

Although there are obviously also operators that act on atomic objects, 5.1.2.4
p 4 gives the completely false impression that atomic operations would only be a
matter of the C library:

> The library defines a number of atomic operations (7.17) ...

*— Pointer types are missing for `atomic_fetch_OP` —*

In the general introduction (7.17.1 p4) there is explicitly an extension of the
notations to atomic pointer types:

> For atomic pointer types, `M` is `ptrdiff_t`.

Whereas the only section where this notation is relevant (7.17.7.5
`atomic_fetch_OP`) is restricted to *atomic integer types*, but then later talks
about the result of such operations on *address types*.

*— Vocabulary —*

For the vocabulary, there is a mixture of the use of the verb combinations
between *load/store*, *read/write* and *fetch/assign*. What is the difference?
Is there any?

*— Over all —*

This is

* contradictory (the Note is not normative, but still wrong),
* confusing (`=` is handled different from `op=`, operators are not mentioned where they should),
* weird (the sign representation is described as the result of an operation, not as the value representation of a data type; what is "no undefined behavior" of a address operation?)
* inconsistent (operators may result in any sign representation ?, and can trap, generic functions are safe)
* incomplete (the set of operators and generic functions are distinct)

**Conclusion**

Combining all these texts, a number of constraints emerge for arithmetic types
on platforms that support the atomics extension. They would better be stated as
such.

1. Since sign representation is a property of a type and not an operation. To comply to the atomics extension all signed integer types must have two's representation for negative values.
2. Pointer arithmetic must have a variant that always has defined behavior, only that the stored address may be invalid, if the addition or subtraction passed beyond the boundaries of the object. But that behavior is **not** defined by the standard, the negation of undefined doesn't give a definition.
3. Binary integer operations `+`, `-`, `&`, `|` and `^` must have versions that do not trap.
4. All floating point operations must have versions that don't raise signals.

The distinction in operations on atomics that are realized by operators (all
arithmetic) and only by generic functions is arbitrary. As soon as a type has a
lock-free `atomic_compare_exchange` operation, all `fetch_op` or `op_fetch`
generic functions can be synthesized almost trivially.

* Why are atomic operations on pointer types and floating point types restricted to applying the operator, and don't allow for the generic function?

**Current practice**

Both gcc and clang permit `atomic_fetch_add` and `atomic_fetch_sub` on atomic
pointer types.

Both disallow floating point types for the functions but allow them for the
operators.

Gcc extends the infrastructure that it provides of atomics to `op_fetch` generic
fuctions and adds a new operator `nand`.

**Suggested strategy for improvement**

I suggest to first do some minimal changes to the text with a TC to avoid its
contradictions and to centralize its requirements. Then, in a feature request
for a new version of the standard we could discuss to add some more features
that would make the approach internally consistent.

### Suggested Technical Corrigendum

Change the beginning of 5.1.2.4 p5:

<del>The library defines a number of atomic operations (7.17) and operations on
mutexes (7.26.4) that are specially identified as synchronization
operations.</del>

to

<ins>There are a number of operations that are specially identified as
synchronization operations: if the implementation supports the atomics extension
these are operators and generic functions that act on atomic objects (6.5 and
7.17); if the implementation supports the thread extension these are operations
on mutexes (7.26.4).</ins>

Replace paragraph 6.2.6.1 p9

<del>Loads and stores of objects with atomic types are done with
memory\_order\_seq\_cst semantics.</del>

by the following

<ins>All operations that act on atomic objects that do not specify otherwise
have `memory_order_seq_cst` memory consistency. If the operation with identical
values on the unqualified type is erroneous it results in an unspecific object
representation, that may or may not be an invalid value for the type, such as an
invalid address or a floating point NaN. Thereby no such operation may by itself
raise a signal, a trap, a floating point exception or result otherwise in an
interruption of the control flow.FOOTNOTE</ins>

<ins>FOOTNOTE Whether or not an atomic operation may be interrupted by a signal
depends on the lock-free property of the underlying type.</ins>

Insert a new paragraph after 6.2.6.2 p2

<ins>Implementations that support the atomics extension, represent all signed
integers with two's complement such that the object representation with sign bit
1 and all value bits zero is a normal value.</ins>

Insert a new paragraph after 6.5 p3

<ins>An operation on an lvalue with an atomic type, that consists of the
evaluation of the object, an optional arithmetic operation and a side effect for
updating the stored value forms a single read-modify-write operation.</ins>

Remove the following phrase in 6.5.2.4 p2:

<del>Postfix `++` on an object with atomic type is a read-modify-write operation
with memory\_order\_seq\_cst memory order semantics.</del>

Remove the following phrase in 6.5.16.2 p3:

<del>If **E1** has an atomic type, compound assignment is a read-modify-write
operation with memory\_order\_seq\_cst memory order semantic</del>

Replace 7.17.7 p1

<del>There are only a few kinds of operations on atomic types, though there are
many instances of those kinds. This subclause specifies each general kind.</del>

by

<ins>In addition to the operations on atomic objects that are described by
operators, there are a few kinds of operations that are specified as generic
functions. This subclause specifies each generic function. After evaluation of
its arguments, each of these generic functions forms a single read, write or
read-modify-write operation with same general properties as described in 6.2.6.1
p9.</ins>

Assuming that the intent of 7.17.7.5 has been to allow operations on atomic
pointer types, in p1, change:

<del>... to an object of any atomic integer type. None of these operations is
applicable to `atomic_bool`</del>

to

<ins>... to an object of any atomic integer or pointer type, as long as the
unqualified type is valid as left operand of the corresponding operator
`op=`.FOOTNOTE  

FOOTNOTE: Thus these operations are not permitted for pointers to atomic
`_Bool`, and only "add" and "sub" variants are permitted for atomic pointer
types.</ins>

Since this topic is then covered already by a more general section, remove this
sentence from p3:

<del>For address types, the result may be an undefined address, but the
operations otherwise have no undefined behavior.</del>

In 7.17.7.5 p 5 replace:

<del>... the compound assignment operators are not guaranteed to operate
atomically, and ...</del>

by

<ins>... the `order` parameter may make the memory consistency less strict than
`memory_order_seq_cst`, and that ...</ins>

**Future Directions**

An editorial revision of the C standard should clarify the vocabulary for the
use of the terms *load*, *store*, *read*, *write*, *modify*, *fetch* and
*assign*.

A feature revision of the standard should:

* Add generic interfaces for all arithmetic operations. That is, it should add function-like interfaces for the missing operators `*=`, `/=`, `%=`, `<<=`, `>>=`
* Add atomic pointer types (if not by the TC above) and atomic floating point types to the permitted types of the function-like arithmetic operations, such that they are uniformly defined for all types where the corresponding operator applies.
* Add generic interfaces `atomic_OP_fetch` for all `atomic_fetch_OP`.
* Reduce 7.17.6 "Atomic integer types" to just a definition of `typedef` as indicated in the table.

---

Comment from WG14 on 2018-10-18:

Oct 2015 meeting

### Committee Discussion

* The committee agrees that there are small inconsistencies remaining in the standard but that they are largely editorial in nature, and yet of potentially of such a sweeping scope that is difficult to assess as a defect. In particular, the various uses of *load/store*, *read/write*, and *fetch/assign* should be clarified and made consistent where possible. It may be advantageous to use ISO standardized vocabulary for this and perhaps other new terms introduced in C11.
* Additional related issues were raised in [(SC22WG14.13844) atomic\_fetch and modify generic functions](https://www.open-std.org/jtc1/sc22/wg14/13844).
* The committee does not feel that this DR is “actionable” and should, in this form, result in a Proposed Committee Response. The author is encouraged to extract and provide in a new paper a simpler list of inconsistencies that can be addressed in a DR. The author is also solicited to address the broader issues as a proposal in a new paper for consideration in a new revision of the standard.

Oct 2015 meeting

### Committee Discussion

The proposed changes to §6.2.6.1 paragraph 9 are superfluous and unnecessary.

The other changes require a comprehensive review of the standard and as such
will be addressed in a future revision of the standard.

Apr 2018 meeting

### Committee Discussion

> The committee solicited the author for a combined resolution for this issue with
> that raised in [DR 495](log_c11c17.md#issue0495).

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that this proposed change and that from [CR 495](log_c11c17.md#issue0495) be
> combined in a new paper to completely resolve this issue.


</div>


---

---

<div id="issue0487">

## Issue 0487: `timespec` vs. `tm`

Authors: WG14, Fred J. Tydeman  
Date: 2015-11-22  
Reference document: [N1987](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1987.pdf)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The standard appears to be inconsistent on `timespec` structure versus `tm`
structure with respect to normative requirements. Both have: The semantics of
the members and their normal ranges are expressed in the comments. But, for
`timespec`, it appears as a footnote, while for `tm`, it appears in the body of
the standard.

### Suggested Technical Corrigendum

Move that sentence from footnote 317 in 7.27.1#4 to be in paragraph 4

---

Comment from WG14 on 2017-11-03:

Apr 2016 meeting

### Committee Discussion

> The committee spent considerable time understanding the change requested and
> accepted it as The Proposed Technical Corrigendum below.

### Proposed Technical Corrigendum

Change §7.27.1p4 sentence 2 and footnote 317 from:

> The `timespec` structure shall contain at least the following members, in any
> order.<sup>317\)</sup>
>
> <sup>317\)</sup> The `tv_sec` member is a linear count of seconds and may not
> have the normal semantics of a `time_t`. The semantics of the members and their
> normal ranges are expressed in the comments.

to:

> The `timespec` structure shall contain at least the following members, in any
> order, where the semantics of the members and their normal ranges are expressed
> in the comments.
>
> <sup>317\)</sup> The `tv_sec` member is a linear count of seconds and may not
> have the normal semantics of a `time_t`.


</div>


---

---

<div id="issue0488">

## Issue 0488: `c16rtomb()` on wide characters encoded as multiple `char16_t`

Authors: WG14, Philipp Klaus Krause  
Date: 2015-12-09  
Reference document: [N1991](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1991.htm)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Section 7.28.1 describes the function c16rtomb(). In particular, it states "When
c16 is not a valid wide character, an encoding error occurs". "wide character"
is defined in section 3.7.3 as "value representable by an object of type
wchar\_t, capable of representing any character in the current locale". This
wording seems to imply that, e.g. for the common cases (e.g, an implementation
that defines \_\_STDC\_UTF\_16\_\_ and a program that uses an UTF-8 locale),
c16rtomb() will return -1 when it encounters a character that is encoded as
multiple char16\_t (for UTF-16 a wide character can be encoded as a surrogate
pair consisting of two char16\_t). In particular, c16rtomb() will not be able to
process strings generated by mbrtoc16().

I would like to implement a standard-conforming c16rtomb() for SDCC, that allows
conversion from all of UTF-16 (not just the basic multilingual plane) to UTF-8.
It seems to me that this is currently not possible.

On the other hand, the description of mbrtoc16() described in section 7.28.1
states "If the function determines that the next multibyte character is complete
and valid, it determines the values of the corresponding wide characters". So it
considers it possible that a single multibyte character translates into multiple
wide characters. So maybe the meaning of "wide character" in section 7.28.1 is
different from definition of "wide character" in section 3.7.3.

In either case, the intended behaviour of c16rtomb() for characters encoded as
multiple char16\_t seems unclear. The issue has been discussed in the thread "A
function to convert char16\_t strings to char strings" in comp.std.c.

### Suggested Change

I see two possible options:

* State clearly that passing a char16\_t that is not a valid character by itself to c16rtomb() is an error. In this case, another function to convert char16\_t strings to char strings should be provided by the standard. The term "wide character" should then not be used in the description of mbrtoc16() the way it currently is.
* State clearly that c16rtomb() can handle characters consisting of multiple char16\_t. For such characters the first call would return 0, and only once all char16\_t encoding the character had been seen, c16rtomb() could write the character as multibyte character. The current wording "When c16 is not a valid wide character, an encoding error occurs" should be changed accordingly.

---

Comment from WG14 on 2018-10-18:

Apr 2016 meeting

### Committee Discussion

> After discussion, the committee concluded that `mbstate` was already specified
> to handle this case, and as such the second interpretation is intended. The
> committee believes that there is an underspecification, and solicited a further
> paper from the author along the lines of the second option. Although not
> discussed a Suggested Technical Corrigendum can be found at
> [N2040](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2040.htm).

Oct 2016 meeting

### Committee Discussion

> The paper [N2040](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2040.htm).
> was discussed and found inadequate: it does not link the first call with the
> second as is intended by the standard.
>
> Additional input was solicited and found in [(SC22WG14.14481) DR488 Suggested
> Corrigendum](https://www.open-std.org/jtc1/sc22/wg14/14481) and is repeated
> below:

In 7.28.1.2 paragraph 3, change:

> If `s` is not a null pointer, the `c16rtomb` function determines the number of
> bytes needed to represent the multibyte character that corresponds to the wide
> character given by `c16` (including any shift sequences), and stores the
> multibyte character representation in the array whose first element is pointed
> to by `s`.

to:

> If `s` is not a null pointer, the `c16rtomb` function determines the number of
> bytes needed to represent the multibyte character that corresponds to the wide
> character given or completed by `c16` (including any shift sequences), and
> stores the multibyte character representation in the array whose first element
> is pointed to by `s`, or stores nothing if `c16` does not represent a complete
> character.

Apr 2017 meeting

### Committee Discussion

The words discussed and reported in the last meeting were adopted.

### Proposed Change

In 7.28.1.2 paragraph 3, change:

> If `s` is not a null pointer, the `c16rtomb` function determines the number of
> bytes needed to represent the multibyte character that corresponds to the wide
> character given by `c16` (including any shift sequences), and stores the
> multibyte character representation in the array whose first element is pointed
> to by `s`.

to:

> If `s` is not a null pointer, the `c16rtomb` function determines the number of
> bytes needed to represent the multibyte character that corresponds to the wide
> character given or completed by `c16` (including any shift sequences), and
> stores the multibyte character representation in the array whose first element
> is pointed to by `s`, or stores nothing if `c16` does not represent a complete
> character.


</div>


---

---

<div id="issue0489">

## Issue 0489: Integer Constant Expression

Authors: WG14, Fred J. Tydeman  
Date: 2016-01-18  
Reference document: [N1994](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1994.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

In an integer constant expression (ICE) in 6.6p6, if an operand is NOT
evaluated, must it follow the constraints and semantics of 6.6?

WG14 messages 14092 to 14102 (with subject of: Fixed size array or VLA?) discuss
this issue.

Places where expressions are not evaluated:

* `0 && funny`
* `1 || funny`
* `0 ? funny : other`
* `1 ? other : funny`
* `_Generic(funny,...)`
* `sizeof(funny)`
* `_Alignof(funny)`

Examples of 'funny' code (that are allowed in expressions that are not
evaluated):

* `assignment = operator`
* `inc++ and ++inc`
* `dec-- and --dec`
* `func_call()`
* `(comma,operator)`
* `3.0`
* `0/0`
* `1.0/0.0`

Places where ICEs are used:

* size of bit-fields, eg, `struct s1{ int bit : ICE; }s2;`
* enum constant, eg, `enum e1{a=ICE}e2;`
* size of non-VLA arrays, eg, `static int ary[ICE];`
* conditional inclusion, eg, `#if ICE`
* null pointer constant, eg, `#define NULL ICE`
* alignment specifier, eg, `_Alignas(ICE)`
* initialization, eg, `{[ICE] = value}`
* static assertions, eg, `_Static_assert(ICE,"string");`
* **case** labels, eg, `case ICE:`
* some object-like macros, eg, `#define EDOM ICE`

Several people expressed an opinion that just parsing the expression (syntax)
without depending upon any values (semantics) is a good thing. However,
**sizeof**(var) depends upon var being a fixed size array versus VLA to
determine if it is a valid ICE. So, some semantic checking must be done.

Some parts of the C standard that might help answer the question follow.

Footnote 118 in 6.6p11 shows the use of 'funny' code:

> ```c
> static int i = 2 || 1 / 0;
> ```

6.6p2:

> A constant expression can be evaluated during translation rather than runtime,
> and accordingly may be used in any place that a constant may be.

6.4.6p2 has:

> An operand is an entity on which an operator acts.

Seems to me that if an operand is not evaluated, then nothing is being acted
upon, so is not an operand.

By 6.6p10

> An implementation may accept other forms of constant expressions.

any implementation may accept these unevaluated expressions; but that does not
mean that all implementations must accept them. And, by the committee discussion
in DR 312 against C99, these "other forms" cannot be an ICE (those words are not
in C99 or C11).

3.1 **access** note 3:

> Expressions that are not evaluated do not access objects.

### Suggested Technical Corrigendum

Add (something along the lines of) either

* (that are evaluated)
* (even if not evaluated)

after "operands" in the first line of 6.6p6 and second line in 6.6p8.

Perhaps, add a footnote giving an example to the phrase being added.

Add to the end of 6.6p10:

> however, they are not integer constant expressions.

Also, update J.2 items on ICE and arithmetic constant expression.

---

Comment from WG14 on 2017-04-07:

Apr 2016 meeting

### Committee Discussion

> The committee does not consider this a defect.

Oct 2016 meeting

### Committee Discussion

> The paper [N2085](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2085.htm)
> offered a suggested improvement to the Proposed Committee Response below, but
> the suggestion was not viewed as an improvement by the committee.

### Proposed Committee Response

> Extending integer constant expressions could be considered for the next revision
> of the standard.
>
> To the question, unevaluated operands of integer constant expressions must
> adhere to the constraints of §6.6.


</div>


---

---

<div id="issue0490">

## Issue 0490: Unwritten Assumptions About if-then

Authors: WG14, Fred J. Tydeman  
Date: 2016-01-18  
Reference document: [N1995](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1995.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

In trying to determine if exp(infinity) is a range error, I have come across an
unwritten assumption (held by many members of the committee) with respect to:
"if \<violation\> then \<consequence\>". WG14 email messages 13920 to 13937
(with subject of: Meaning of IF-THEN) have a discussion of this.

Message 13925 has in part: That these "if-then" statements were meant to follow
the ordinary-language model, where "if \<violation\> then \<consequence\>"
promises that \<violation\> would necessarily lead to \<consequence\>, but
nothing more. That is similar to the Boolean model. But that has to be combined
with a general rule that when the C standard doesn't mention \<consequence\> as
a visible action in some well-defined circumstance, then it is guaranteed that
it does not occur.

Message 13925 also has: There is a related issue: Just because some defined
behavior is allowed to fail, it was not intended that it could always fail.

Message 13937 has in part: In general, when the C standard doesn't say that
something specific is supposed to happen, it intended that nothing happens.
Explicit permission is given for errno to be set under certain circumstances

### Suggested Technical Corrigendum

Add to 4.0 Conformance after paragraph 1, words along the lines of:

> Unless stated otherwise (**errno** is one such otherwise), when the C standard
> doesn't say that something specific is supposed to happen, it is intended that
> nothing happens. Also, just because some defined behavior is allowed to fail, it
> was not intended that it could always fail.

---

Comment from WG14 on 2017-04-07:

Apr 2016 meeting

### Committee Discussion

> After discussion, the committee consensus was that this was not in fact a
> defect.

### Proposed Committee Response

> This is not a defect.
>
> The Standard is written in English using normal conventions.


</div>


---

---

<div id="issue0491">

## Issue 0491: Concern with Keywords that Match Reserved Identifiers

Authors: WG14, Douglas Walls  
Date: 2016-02-23  
Reference document: [N2000](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2000.htm)  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Should a conforming program be allowed to use identifiers spelled with a leading
underscore followed by an uppercase letter that match the spelling of a keyword?  

The C committee has been adding keywords to the C standard spelled with a
leading underscore followed by an uppercase letter so that they will not
conflict with identifiers that are not already reserved to the implementation,
i.e. so existing programs that conform to the C standard are not impacted by
addition of new keywords in a new revision of the C standard.  

So the C standard spells keywords in two ways:

* Leading underscore followed by an uppercase letter
* Leading lowercase letter

7.1.2p4 provides restrictions on when macros with names lexically identical to
keywords can be defined, thus infering when macro names lexically identical to
keywords can be defined.  

As specified in 7.1.3, identifiers spelled with a leading underscore followed by
an uppercase letter are reserved to the implementation.  While those identifiers
beginning with a lowercase letter are not.  Thus, for example, a conforming
program can use `inline` as a macro name, but a conforming program cannot use
`_Noreturn` as a macro name.  

Though the C committee has added new keywords from the reserved identifier
namespace, the committee has not updated the rules about reserved identifiers. 
What I don't know is if that is intentional or an oversight, as I don't ever
remember discussing the issue from that perspective during a committee meeting.   

The issue came to my attention when I found some C standard headers defining
\_`Noreturn` as a macro because they knew it is an identifier reserved to the
implementation.  I was a bit surprised, as it required a otherwise conforming
program to `#undef _Noreturn` in order to use the \_`Noreturn` keyword as a
function specifier.  The macro in this case was expanding to a gcc like
attribute syntax recognized by the compiler.

### Suggested Technical Corrigendum

Replace the first two bullets under 7.1.3p1 with:

  — All identifiers that begin with an underscore and either an uppercase letter
or another underscore are always reserved for any use<ins>, except those
identifiers which are lexically identical to keywords</ins>.
<ins><sup>footnote)</sup></ins>  
  — All identifiers that begin with an underscore are always reserved for use as
identifiers with file scope in both the ordinary and tag name spaces<ins>,
except those identifiers which are lexically identical to keywords</ins>.

<ins><sup>footnote)</sup> Allows identifiers spelled with a leading underscore
followed by an uppercase letter that match the spelling of a keyword to be used
as macro names.</ins>

---

Comment from WG14 on 2017-11-03:

Apr 2016 meeting

### Committee Discussion

> The committee accepts the first suggestion as the Proposed Technical
> Corrigendum.

### Proposed Technical Corrigendum

Change §7.1.3.p1 first bullet from:

>   — All identifiers that begin with an underscore and either an uppercase letter
> or another underscore are always reserved for any use.

to

>   — All identifiers that begin with an underscore and either an uppercase letter
> or another underscore are always reserved for any use, except those identifiers
> which are lexically identical to keywords. <sup>footnote)</sup>
>
> <sup>footnote)</sup> Allows identifiers spelled with a leading underscore
> followed by an uppercase letter that match the spelling of a keyword to be used
> as macro names by the program.


</div>


---

---

<div id="issue0492">

## Issue 0492: Named Child struct-union with no Member

Authors: WG14, Clive H. Pygott  
Date: 2016-03-01  
Reference document: [N2007](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2007.pdf)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

**Introduction**

Some weeks ago I posted the following code to the reflector after an argument at
work as to whether it was legal, and if so, what was it meant to do?

```c
       struct  S1
            {  union U11
                    {int    m11;
                     float  m12;
                    };

               int m13;
            } s1;
```

The issue is that U11 isn't an anonymous union (because it has a name U11) but
doesn't declare a member of S1. When tried with a number of compilers the result
was either that it was rejected as a constraint error or it was treated as an
anonymous union, with m11 and m12 accessible as though they were members of S1
(e.g. s1.m11 \= 42;). The declaration of union U11 was also added at file scope,
so could be used in other structs.

After some discussion (thanks to Doug and Roberto), it was concluded that the
code was intended to be a constraint error because it can be argued that it
violates the first constraint in 6.7.2.1 para 2 "A *struct-declaration* that
does not declare an anonymous structure or anonymous union shall contain a
*struct-declarator-list*". The syntax fragment its referring to is:

> *struct-declaration:   
>        specifier-qualifier-list struct-declarator-list<sub>opt</sub>* `;`   
>        *static\_assert-declaration*

In parsing the above code “`union U11 {int m11; float m12;} ;`” is a
*struct-declaration*. It is believed that the intended reading is:

> * “`union U11 {int m11; float m12;}`” is a *specifier-qualifier-list*
> * There is no *struct-declarator-list*

Hence, as U11 isn't an anonymous union and doesn't have a
*struct-declarator-list*, it violates the quoted constraint.

However, there would appear to be a different reading that says that this
*struct-declaration* does “contain a *struct-declarator-list*”. So it shouldn't
be a constraint error hence the potential need for a DR to clarify the intent
(discussed in the next section).

The alternative reading of the constraint requirement comes about because the
*specifier-qualifier-list* `union U11 {int m11; float m12;}` is interpreted by
recursively entering the same part of the syntax tree. As its interpreted, int
m11; and float m12; are *struct-declarations*, where “m11” and “m12” are
*struct-declarator-lists,*. So the *struct-declaration* for U11 does contain a
*struct-declarator-lists*, so shouldn't be a constraint error.

The response to that argument on the reflector was that ‘whenever a constraint
refers to elements of the syntax tree, it means those elements in the term
currently being processed, and not any terms that may be found by recursively
traversing the tree’. However, I cannot see this principle stated anywhere in
the standard.

Hence, I'd argue that whether this code is legal or not is ambiguous and a DR is
required, either to:

> * Establish the principle that “whenever a constraint refers to elements of the syntax tree, it means those elements in the term currently being processed, and not any terms that maybe found by recursively traversing the tree”, or
> * Reword the constraint in 6.7.2.1 para 2 to clarify that the above code is intended to be aconstraint error, for example by adding ‘shall contain a struct-declarator-list, <ins>other than any that may be found in the interpretation of the *specifier-qualifier-list*</ins>’

---

Comment from WG14 on 2017-04-07:

Apr 2016 meeting

### Committee Discussion

> The committee formed a strong consensus that this was not a defect.

### Proposed Committee Response

> There are implementations that allow this construct and other variations, but
> the committee is clear that since `union U11` isn‘t anonymous, it is a
> constraint violation.


</div>


---

---

<div id="issue0493">

## Issue 0493: Mutex Initialization Underspecified

Authors: WG14, Martin Sebor  
Date: 2016-01-21  
Reference document: [N2025](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2025.htm)  
Status: Closed  
Cross-references: [0414](log_c11c17.md#issue0414), [0469](log_c11c17.md#issue0469), [0479](log_c11c17.md#issue0479)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The C11 threads library defines a mutex type, `mtx_t`, and a number of functions
that operate objects of the type. The `mtx_t` is fully described in **§7.26.1,
Introduction** (to the **Threads** section) as follows:

> a complete object type that holds an identifier for a mutex;

No other description of the type appears elsewhere in the text.

Among the functions provided by the C11 threads library that operate on objects
of the `mtx_t` type are `mtx_init()` and `mtx_destroy()`.

The `mtx_init(mtx_t *mtx, int type)` function is described in **§7.26.4.2** as
follows:

> -2- The `mtx_init` function creates a mutex object with properties indicated by
> `type`, which must have one of the six values:
>
> * `mtx_plain` for a simple non-recursive mutex,
> * `mtx_timed` for a non-recursive mutex that supports timeout,
> * `mtx_plain | mtx_recursive` for a simple recursive mutex, or
> * `mtx_timed | mtx_recursive` for a recursive mutex that supports timeout.
>
> -3- If the `mtx_init` function succeeds, it sets the mutex pointed to by `mtx`
> to a value that uniquely identifies the newly created mutex.
>
> **Returns**  
> -4- The mtx\_init function returns `thrd_success` on success, or `thrd_error` if
> the request could not be honored.

The `mtx_destroy(mtx_t *mtx)` function is then described in **§7.26.4.1** like
so:

> The `mtx_destroy` function releases any resources used by the mutex pointed to
> by `mtx`. No threads can be blocked waiting for the mutex pointed to by `mtx`.

#### Problems With `mtx_t`

Since `mtx_t` is a complete object type, what are the semantics of copying
objects of the type (either by assignment or by passing them by value between
functions) and passing pointers to distinct copies of the same mutex object as
arguments to the C11 threads functions?

#### Problems With `mtx_init()`

The specification of `mtx_init()` raises the following questions to which the
standard doesn't provide clear answers.

1. What is the behavior of `mtx_init()` when called with a pointer to an object initialized to all zeros (such as a mutex object with static storage duration)? Are such calls valid, or if not, must the function fail by returning `thrd_error`, or is its behavior unspecified, or perhaps undefined? (If it is the same as calling it on an uninitialized object then how does one statically initialize a mutex?)
2. Similarly, what is the function's behavior when called with a pointer to an uninitialized mutex object (one whose value is indeterminate)? (Presumably, it should be to initialize the object to a valid state and not require the object to have been initialized to all zeros, but this is not specified.)
3. What is the function's behavior when called with the same pointer more than once (without a call to `mtx_destroy()` in between)?
4. What is the function's behavior when called with a pointer to a locked mutex object?
5. The function description specifies that the `type` argument must have one of six values but lists only four. What are the remaining two values of the `type` argument? (Note: this problem is the subject of DR [479](log_c11c17.md#issue0479).)
6. What is the function's behavior when `type` argument does not have one of the listed values? (Note that since the argument is a plain `int`, choosing not to define the behavior will make the function more dangerous to use than alternatives such as POSIX threads. Choosing to require the function to detect invalid arguments and reject them with an error exposes a problem due to its binary return value's inability to indicate different kinds of errors.)
7. If the function is required to fail when the `type` argument isn't valid, what is its required behavior in this case when the `mtx` argument is null?

#### Problems With `mtx_destroy()`

The specification of `mtx_destroy()` raises the following questions:

1. What is the behavior of `mtx_destroy()` when called with a pointer to an object initialized to all zeros (such as a mutex object with static storage duration) that has not been passed to `mtx_init()`? (This is important because it might mean that programs need to associate an external flag with each mutex object indicating whether or not it has been initialized in a way that requires `mtx_destroy()` to be called on it.)
2. What is the behavior of the function when called with the same pointer more than once? Is it required to have no effect or is it undefined?
3. What is the behavior of the function when threads are blocked waiting for the mutex it's called on? (The text is lax with the wording here, and assuming the function's behavior is undefined in this case, the text should phrase the requirement using the word "*shall*" rather than "*can*" and preferably make the undefined behavior explicit, for example similarly to how POSIX specifies the similar requirement in its API.)
4. What state is a mutex object in after `mtx_destroy()` has been called with it as an argument? Can such an object be subsequently passed as argument to any of the other mutex functions? For example, can such a mutex object be safely passed to `mtx_init()`? To any of the other mutex functions such as `mtx_lock()` and, if so, with what effects? (Undefined or error?)

#### Other Problems Due to the Underspecification Of Mutex Initialization

Neither `mtx_init()` nor `mtx_destroy()` discussed above, nor any of the other
functions that operate on `mtx_t` objects specifies what state the object is
required to be in when the function is called. In particular, none of the
functions specfies whether the object is required to be initialized or how.

That gives rise to the following general questions to which the standard fails
to provide clear answers:

1. Is an uninitialized mutex object (i.e., one with an indeterminate value) a valid argument to any of the other mutex functions besides those discussed above? If it isn't a valid argument (as is the most likely answer), are the mutex functions expected to detect the condition and fail by returning `thrd_error` or is the behavior unspecified, or perhaps undefined?
2. Similarly, is a statically initialized mutex object (one declared with static storage duration and initialized to all zeros) a valid argument to any of the the other mutex functions? For instance, is such a mutex a valid argument to `mtx_lock()` and if so, what is the "type" of such a mutex (is it plain, recurisive, or timed), and what state is it in? (Put another way, what are the effects of calling `mtx_lock()` on such a mutex?)
3. Assuming a statically initialized mutex object is a valid argument to only `mtx_init()` but not any of the mutex functions, what mechanism are C11 programs expected to use to statically initialize mutex objects to make them valid arguments to functions such as `mtx_lock()` (the equivalent of the POSIX threads `PTHREAD_MUTEX_INITIALIZER`)? Note that while some systems do not provide an API to statically initialize a native mutex object the functionality can be emulated by storing a flag in the C11 `mtx_t` object and checking that flag in every mutex function, lazily initializing the object as necessary. It is unclear whether C11 intends to require implementations to provide this functionality.
4. Is there any limit on the the number of times `mtx_init()` cam be called with a distinct object as an argument without an intervening call to `mtx_destroy()`? (In other words, must calls to `mtx_init()` and `mtx_destroy()` with the same mutex object be paired?) If it is intended to allow implementations to impose such a limit (as some do) how do programs distinguish the usually transient nature of exceeding such a limit from permanent mutex initialization errorss (such as invalid type arguments)?

One might be able to guess what some of the answers to the questions above might
be intended to be if one assumes that the library is meant to be implemented on
top of an existing threads library such as POSIX threads, but that is not
reflected in the specification in any way. Other reasonable guesses include that
C11 threads library is intended to provide a simpler though no less safe
interface to the underlying threads library on the system (i.e., with no
instances of undefined behavior the underlying threads library isn't already
subject to), but the lack of even the most basic requirements raises doubt about
this intent. Another possible guess is that the C11 threads library is intended
to be (or should be possible to be) independent of the underlying threads
implementation and provide its own distinct guarantees and impose its own
requirements (even though it in many cases fails to articulate them). In the
absence of answers to these questions the C11 threads library is essentially
unusable as a specification either for the development of implementations
facilitating portable code, or for writing portable code.

### Suggested Technical Corrigendum

The C11 threads specification should be amended to clearly answer the questions
above. Any new requirements should consider the goal of implementing the
specification in terms of an existings threads implementation such as the POSIX
threads library.

---

Comment from WG14 on 2018-10-18:

Apr 2016 meeting

### Committee Discussion

> This DR records the committee’s understanding of the intent of the standard. The
> resolution to [DR 469](log_c11c17.md#issue0469) must include a Proposed Technical Corrigendum
> consistent with the answers provided below.
>
> As one example required to be resolved in [DR 469](log_c11c17.md#issue0469),
>
> > change ‘creates’ to ‘initializes’ in `mtx_init` and `mtx_destroy`,

Oct 2017 meeting

### Committee Discussion

> After extensive discussion, the committee response for the return value for
> `mtx_init` when passed a null pointer was changed.

Apr 2018 meeting

### Committee Discussion

> The papers [N2190](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2190.htm),
> [N2191](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2191.htm),
> [N2192](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2192.htm), and
> [N12193](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2193.htm) were
> discussed as directions for a future revision of the standard.
>
> There are similar and potentially interrelated issues with respect to `cnd_t`.
>
> The committee solicited a combined comprehensive resolution for these issues
> with those raised in [DR 469](log_c11c17.md#issue0469) and [DR 479](log_c11c17.md#issue0479).

### Proposed Committee Response

> This document asks quite a number of questions, and they are answered according
> to the section title in which they were asked. These answers rely on changes
> made in [DR 469](log_c11c17.md#issue0469).
>
> **Problems with `mtx_t`**
>
> The semantics of copying a `mtx_t` are not specified, much like `FILE`
> §7.21.3p6.
>
> **Problems with `mtx_init()`**
>
> 1. `mtx_init` will attempt to initialize whatever memory is referenced by the pointer passed in, so it will initialize static memory preset to zero. Such calls are valid.
> 2. `mtx_init` will attempt to initialize whatever memory is referenced by the pointer passed in, so it will initialize memory that has previously been used as a `mtx_t`.
> 3. It is undefined behavior to call `mtx_init()` on memory without an intervening `mtx_destroy`.
> 4. It is undefined behavior to call `mtx_init()` on memory without an intervening `mtx_destroy` regardless of the lock condition.
> 5. See [DR 414](log_c11c17.md#issue0414) for the resolution to the miscounted variations of `mtx_init()` options.
> 6. Undefined behavior is the result of passing values other than those specified in the standard. The wording in the Standard shall change from ‘must’ to ‘shall’ in §7.26.4.2p2.
> 7. The value returned by `mtx_init()` when passed a NULL pointer shall be unspecified.
>
> **Problems with `mtx_destroy()`**
>
> 1. It is undefined behavior to call `mtx_destroy()` with a pointer to an object that has not been initialized by a call to `mtx_init()`. In §7.26.4.1p2 the editor should consider changing ‘can’ to ‘shall’.
> 2. It is undefined behavior to call `mtx_destroy()` with a pointer to an object that has not been initialized by a call to `mtx_init()`, so calling it twice without an intervening `mtx_init` results in undefined behavior.
> 3. Calling `mtx_destroy()` while it is locked is intended to be undefined and will be resolved by [DR 469](log_c11c17.md#issue0469).
> 4. The memory that had been used as an `mtx_t` object has indeterminate value. Undefined behavior results if it is subsequently used as an argument to other `mtx` functions other than `mtx_init`.
>
> **Other Problems**
>
> 1. Memory with indeterminate value is appropriate to be used only with `mtx_init` as described above. All other uses result in undefined behavior.
> 2. Static memory preset to zeros is appropriate to be used only with `mtx_init` as described above. All other uses result in undefined behavior.
> 3. The C Standard provides no mechanism to statically initialize a `mtx_t`.
> 4. There is the limit of 1 call to `mtx_init()` without an intervening call to `mtx_destroy()`.

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> These issues were not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that issues from [CR 469](log_c11c17.md#issue0469), [CR 479](log_c11c17.md#issue0479), and [CR
> 493](log_c11c17.md#issue0493), as well as potentially other small issues be combined in a new
> paper to completely resolve this issue for the next revision of the standard.


</div>


---

---

<div id="issue0494">

## Issue 0494: Part 1: Alignment specifier expression evaluation

Authors: WG14, Clark Nelson  
Date: 2016-03-17  
Reference document: [N2027](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2025.htm)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Point D of DR439 (a.k.a. N1729) raises the question of the meaning of a
non-constant expression in an abstract declarator. The other points of that DR
are rather more straightforward, but point D requires more thought. Here I
present some additional analysis I have done on the question.

### Overview

There are three places an abstract declarator or type name can appear and (at
least potentially) not be part of a larger expression:

1. *parameter-declaration*
2. *alignment-specifier*
3. *atomic-type-specifier*

(When this topic comes up, the case of a generic selection is generally raised
as well. However, it should be clearly understood that a type name appearing in
a generic selection is necessarily part of a larger expression, so any
expression therein isn't a full expression, so DR439 does not raise any issues
about it. It's certainly possible that there are issues, but if so, they need to
be spelled out. Once they have been clearly defined, it will hopefully become
clear whether they should be considered along with DR439 or separately.)

So let's consider three file-scope declarations:

1. `void f(int [rand()]);`
2. `_Alignas(int [rand()]) int i;`
3. `_Atomic(int [rand()]) a;`

The first declaration has a clearly defined meaning. According to 6.7.6.2p5, the
expression is “treated as if it were replaced by `*`”. Therefore:

* the expression is not evaluated; and
* the parameter is declared as a VLA of unspecified size.

These are both true even if the declaration appears in a block scope.

For the second and third declarations, the standard today gives no clue how the
expression should be handled. The only thing that is clear (even though the
standard doesn't say so) is that, if the declarations are at file scope, any
answer that requires evaluating the expressions is wrong.

### The alignment specifier case

The interesting thing about `_Alignas` is that the “answer” is just a number;
all other details of the type named are irrelevant. Since the alignment of an
array type must be the same as that of its element type, the value of the array
size is irrelevant, so strictly speaking it need not be evaluated.

This is similar to `sizeof`; according to 6.7.6.2p5:

> Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.

For an alignment specifier, I would prefer that the behavior not depend on the
scope in which it appears. It would also be simpler to require that a
non-constant size expression **not** be evaluated than to permit implementation
latitude. That would be consistent with the parameter declaration case, and I
doubt that any real-world code would change behavior as a result.

As an aside, here is an interesting related example:

```c
size_t s = sizeof(int [rand()]);
```

According to 6.5.3.4p2:

> If the type of the operand is a variable length array type, the operand is
> evaluated; otherwise, the operand is not evaluated and the result is an integer
> constant.

If the declaration of `s` appeared at file scope, the fact that the result of
`sizeof` is not an integer constant would run afoul of the constraints on
initialization, so a diagnostic would be required. That might be considered
enough to override the requirement that “the operand is evaluated” in an
initializer at file scope – but the phrasing would seem to be suboptimal.

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

> From [(SC22WG14.14483) Suggested TC for DR
> 494](https://www.open-std.org/jtc1/sc22/wg14/14483) the following suggestion was
> made:

In 6.7.6.2 paragraph 5, change:

> ... Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.

to:

> ... Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.
> Where a size expression is part of the operand of an `_Alignof` operator, that
> expression is not evaluated.

Apr 2017 meeting

### Committee Discussion

The words discussed and reported in the last meeting were adopted.

### Proposed Change

In 6.7.6.2 paragraph 5, change:

> ... Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.

to:

> ... Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.
> Where a size expression is part of the operand of an `_Alignof` operator, that
> expression is not evaluated.


</div>


---

---

<div id="issue0495">

## Issue 0495: Part 2: Atomic specifier expression evaluation

Authors: WG14, Clark Nelson  
Date: 2016-03-17  
Reference document: [N2027](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2025.htm)  
Status: Closed  
Cross-references: [0486](log_c11c17.md#issue0486)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Point D of DR439 (a.k.a. N1729) raises the question of the meaning of a
non-constant expression in an abstract declarator. The other points of that DR
are rather more straightforward, but point D requires more thought. Here I
present some additional analysis I have done on the question.

### Overview

There are three places an abstract declarator or type name can appear and (at
least potentially) not be part of a larger expression:

1. *parameter-declaration*
2. *alignment-specifier*
3. *atomic-type-specifier*

(When this topic comes up, the case of a generic selection is generally raised
as well. However, it should be clearly understood that a type name appearing in
a generic selection is necessarily part of a larger expression, so any
expression therein isn't a full expression, so DR439 does not raise any issues
about it. It's certainly possible that there are issues, but if so, they need to
be spelled out. Once they have been clearly defined, it will hopefully become
clear whether they should be considered along with DR439 or separately.)

So let's consider three file-scope declarations:

1. `void f(int [rand()]);`
2. `_Alignas(int [rand()]) int i;`
3. `_Atomic(int [rand()]) a;`

The first declaration has a clearly defined meaning. According to 6.7.6.2p5, the
expression is “treated as if it were replaced by `*`”. Therefore:

* the expression is not evaluated; and
* the parameter is declared as a VLA of unspecified size.

These are both true even if the declaration appears in a block scope.

For the second and third declarations, the standard today gives no clue how the
expression should be handled. The only thing that is clear (even though the
standard doesn't say so) is that, if the declarations are at file scope, any
answer that requires evaluating the expressions is wrong.

### The atomic type specifier case

`_Atomic`-of-array types are already disallowed; see 6.7.2.4p3. The following
example avoids that restriction, but still has a non-constant expression in an
atomic specifier:

```c
_Atomic(int (*)[rand()]) p1;
```

What would such a declaration mean, if it were allowed?

It would be tempting to conclude that it is not allowed at file scope, since a
variably modified type is involved. Unfortunately, the standard doesn't actually
say so – or at least not yet. According to 6.7.6p3:

> Furthermore, any type derived by declarator type derivation from a variably
> modified type is itself variably modified.

But an atomic type specifier isn't described as involving declarator type
derivation. There is definitely a kind of type derivation involved, but possibly
of a new and different kind.

On the other hand, because of the unique dual nature of the syntax for
`_Atomic`, the preferred answer is probably that the previous declaration would
have the same meaning as this declaration:

```c
int (*_Atomic p2)[rand()];
```

If a qualifier other than `_Atomic` were used, the interpretation of the
declaration and the contained expression would be pretty clear from the
standard. But for `_Atomic`, the words of the standard seem to more or less
rewrite this declaration into the prior form, about which the standard has less
to say, by and large.

If it is true, as seems likely, that any atomic type specifier containing a
non-constant expression can be expressed equivalently using an atomic type
qualifier instead, then presumably the question of what to do when the
expression is syntactically a full expression is not all that interesting.

What remains interesting is how to express this intention normatively.

---

Comment from WG14 on 2018-10-18:

Oct 2017 meeting

### Committee Discussion

> The committee believes that there will be a review of the atomic specification
> in the next revision of the standard and that this issue will be examined in
> that context.

Apr 2018 meeting

### Committee Discussion

> The committee solicited a combined resolution for this issue with those raised
> in [DR 486](log_c11c17.md#issue0486).

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that this proposed change and that from [CR 486](log_c11c17.md#issue0486) be
> combined in a new paper to completely resolve this issue.


</div>


---

---

<div id="issue0496">

## Issue 0496: `offsetof` questions

Authors: WG14, Martin Sebor  
Date: 2016-03-23  
Reference document: [N2031](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2031.htm)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The `offsetof` macro is specified in the normative text of the C11 standard in
**§7.19 Common Definitions `<stddef.h>`** as follows:

> The macros \[defined in the header `<stddef.h>`\] are...
>
> > `offsetof(`*type*`,` *member-designator*`)`
>
> which expands to an integer constant expression that has type `size_t`, the
> value of which is the offset in bytes, to the structure member (designated by
> *member-designator*), from the beginning of its structure (designated by
> *type*). The type and member designator shall be such that given
>
> > ```c
> > static type t;
> > ```
>
> then the expression `&(t.`*member-designator*`)` evaluates to an address
> constant. (If the specified member is a bit-field, the behavior is undefined.)

In addition, undefined uses of the macro are mentioned in the informative **§J.2
Undefined Behavior** using the following words:

> — The member designator parameter of an `offsetof` macro is an invalid right
> operand of the `.` operator for the type parameter, or designates a bit-field
> (7.19).

A number of questions have been independently raised about this specification
over the years, both by C (and C\+\+) committee members and by implementers of
both languages (the C\+\+ defintion of the macro is largely equivalent to C's),
pointing out gaps or aspects lacking in clarity. Most recently some of the
questions were raised in the thread [(SC22WG14.13852) what's a
member-designator?](https://www.open-std.org/jtc1/sc22/wg14/13852) As a result
of the lack of clarity, implementations diverge in what `offsetof` expressions
they accept. In one case, an implementer of a compiler known for its conformance
and high quality of diagnostics interpreted the specification as restricting the
`member-designator` operand of the macro to ordinary identifiers and to the
exclusion of references to subobjects.

For example, given the following code:

> ```c
> struct A { int n, a [2]; };
> struct B { struct A a; };
>
> int noff = offsetof (struct B, a.n);
> int aoff = offsetof (struct B, a.a [1]);
> ```

this implemenation issues the diagnostics below.

> ```c
> warning: using extended field designator is an extension [-Wextended-offsetof]
> int noff = offsetof (struct B, a.n);
>            ^                    ~~
> warning: using extended field designator is an extension [-Wextended-offsetof]
> int aoff = offsetof (struct B, a.a [1]);
>            ^                    ~~~~~~
> ```

In other instances, some implementations reject the following example with an
error, indicating that they are not prepared to handle the `->` operator in this
context.

> ```c
> struct A { int i; };
> struct B { struct A a [1]; };
>
> int ioff = offsetof (struct B, a->i);
> ```

Some of the questions that have been identified are outlined in the following
list.

* In the specification, the *member-designator* operand is referred to as a
  *structure member*. Is this intended to include members of subobjects (members
  of structures other thant *type*, subobjects of which are members of *type*), or
  of and array elements as in the code examples above, or are the diagnostics
  required?
* The *type* operand is described as designating a structure. Is a *type* that
  that refers to a union not a valid operand? (No implementation has been observed
  to reject union operands.)
* Does C intend to permit defining a new type as the *type* operand? For example,
  is the following a well-formed expression? (No implementation has been observed
  to reject such operands.)

  > ```c
  > offsetof (struct A { int i; }, i)
  > ```
* If C does intend to permit defining a new type in `offsetof` expressions, does
  it intend to permit defining arbitrarily complex types such as the one below?
  (No implementation is known to accept the definition of a type containing commas
  since they are interpreted by the preprocessor as separating macro arguments.
  But since implementations often define the `offsetof` macro in terms of a
  built-in function, it would be possible to implement each as a variadic macro
  and function, respectively, and handle this corner case. This isn't a question
  about whether it would be worthwhile to do so but rather about whether the
  standard text can be interpreted so as to require implementers to accept this
  admittedly unusual case.)

  > ```c
  > offsetof (struct A { struct B { int i, j; } b [1]; }, b->j)
  > ```

Some of the same questions and others were summarized a number of years ago by
Joseph Myers in his paper on
[`offsetof`](https://www.polyomino.org.uk/computer/c/pre-dr-3.txt). Althugh
Joseph chose not to submit the paper to WG14 we believe many are still relevant
and should be dealt with by clarifying the text of the standard.

---

Comment from WG14 on 2019-05-03:

Oct 2016 meeting

### Committee Discussion

> The committee notes that since all known implementations but one "get it right"
> this may well not be a defect at all.

Apr 2017 meeting

### Committee Discussion

> The committee discussed this issue at some length. By the strict reading of the
> standard, one concludes that only structures are supported, not unions, and that
> only named members of structures rather than extended references to sub-objects
> in a recursive fashion are allowed.
>
> Implementations commonly treat the standard as if it had been defined in terms
> of named members and sub-objects recursively, and would likely be sympathetic to
> a paper that consolidates existing practice since this seems to be a nearly
> universal extension.
>
> There was no discussion asserting that this extension, however, was the actual
> intent of the standard, and as such there is was no sentiment to accept these
> extensions with clarified wording. Such a change could only be made in a new
> revision of the standard.

Oct 2017 meeting

### Committee Discussion

A small paper was discussed and its contents reflected below in the PTC.
Although the committee believes that allowing this for unions was originally
intended, there was no opinion expressed that allowing new type declarations was
intended. So the answers to questions in the first two bullet points are yes,
and to the third, no, and the fourth is moot.

Apr 2018 meeting

### Committee Discussion

> There was committee consensus that such a construct should be a new constraint
> violation. A new paper was solicited.

### Proposed Committee Response

> There was no intent to allow new types to be declared in an `offsetof`
> expression.

### Proposed Change

Change the following words in §7.19 p 3 from:

> ..., to the structure member (designated by *member-designator*),

to:

> ..., to the subobject (designated by *member-designator*),

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> The committee discussed this issue at some length. By the strict reading of the
> standard, one concludes that only structures are supported, not unions, and that
> only named members of structures rather than extended references to sub-objects
> in a recursive fashion are allowed.
>
> Implementations commonly treat the standard as if it had been defined in terms
> of named members and sub-objects recursively, and such a paper was presented and
> its proposed change accepted below.

### Proposed Committee Response

> There was no intent to allow new types to be declared in an `offsetof`
> expression.
>
> Although the committee believes that allowing this for unions was originally
> intended, there was no opinion expressed that allowing new type declarations was
> intended. So the answers to questions in the first two bullet points are yes,
> and to the third, no, and the fourth is moot.

### Proposed Change

Change the following words in §7.19 p 3 from:

> ..., to the structure member (designated by *member-designator*),

to:

> ..., to the subobject (designated by *member-designator*),
>
> April 2019 meeting
>
> > A new paper [N2350](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2350.htm)
> > was submitted for C2x and has been accepted.


</div>


---

---

<div id="issue0497">

## Issue 0497: "white-space character" defined in two places

Authors: WG14, Fred J. Tydeman  
Date: 2016-03-24  
Reference document: [N2032](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2032.htm)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

"white-space character" is defined differently in two places in the standard.

white-space character is defined in 6.4 as:

> space, horizontal tab, new-line, vertical tab, form-feed

standard white-space character is defined in 7.4.1.10 for **isspace()** as:

> space, horizontal tab, new-line, vertical tab, form-feed, carriage return

One place it matters is 7.21.6.2 fscanf().

7.21.6.2 fscanf() in paragraph 5 talks about white-space character(s) in the
directive. Since there is no reference to **isspace**, it must be referring to
6.4 (which I believe is wrong).

Paragraph 8, in the same section, talks about input white-space characters, but
refers to **isspace**.

In the following code, the \\r (carriage return) is a directive:

```c
#include  <stdio.h>
int main(void){
  static int rc, cnt1, cnt2, i;
  rc = sscanf( " 123", "\r%n%i%n", &cnt1, &i, &cnt2);
  printf("rc=%i, cnt1=%i, i=%i, cnt2=%i\n", rc, cnt1, i, cnt2);
  return 0;
}
```

Is the \\r a white-space character or an ordinary multibyte character?

By 5.2.1#3, the \\r is part of the basic execution character set, but is not
part of the basic source character set (as Doug Gwyn pointed out in message
14152).

By 6.4#3, the \\r is not a white-space character.

By 7.21.6.2#3, #5 and #6, since the \\r is not a white-space character, it is an
ordinary multibyte character. Therefore, since the \\r does not match the
characters of the stream, cnt1, i, and cnt2 are not altered. However, this not
what most implementations do. They output: rc\=1, cnt1\=1, i\=123, cnt2\=4

I see a mismatch between what implementations are doing and what the standard
requires.

Another issue is "white space" in 7.21.6.2#15. It should be "white-space
characters". Section 6.4 defines "white space" as both comments and white-space
characters. So, the use of "white space" in 7.21.6.2#15 would cause /\* comments
\*/ to be matched. The same issue applies to 7.29.2.2#15, 7.29.4.1.2#4,
7.22.1.4#4.

Another issue is "white-space wide character" is not well defined (in
7.30.2.1.10) and is missing from the index. Does the "C" locale matter?

### Suggested Technical Corrigendum

There are several ways this basic issue can be addressed.

1. Add 'carriage return' to the definition of white-space in 6.4. However, this only makes 6.4 and **isspace** match for the "C" locale.
2. Add '(as specified by the **isspace** function)' to 'white-space characters' throughout clause 7 of the standard. Add '(as specified by the **iswspace** function)' to 'white-space wide characters' throughout clause 7\.
3. Throughout clauses 5 and 6 (except for 5.1.1.2#7 which is execution), change 'white-space characters' to 'source white-space characters'. There might be an issue with 'non-white-space character' being changed to 'non-source-white-space character'.

   In clause 7.1.1, add definitions of 'execution white-space character' and
   'execution white-space wide character'. Change 'white-space character' to
   'execution white-space character' throughout clause 7\. Change 'white-space wide
   character' to 'execution white-space wide character' throughout clause 7\.

   Throughout clause 7, remove '(as specified by the **isspace** function)' and
   '(as specified by the **iswspace** function)'.
4. In (perhaps) 7.1.1, add something along the lines of:
   > In this clause, references to "white-space character" refer to execution
   > white-space character as defined by **isspace()**. References to "white-space
   > wide character" refer to execution white-space wide character as defined by
   > **iswspace()**.

   Throughout clause 7, remove '(as specified by the **isspace** function)' and
   '(as specified by the **iswspace** function)'.

Some of the above changes also require corresponding changes to Annexes A and J.

Also do these changes:

1. In 7.21.6.2#15, 7.29.2.2#15, 7.29.4.1.2#4, change "white space" to "white-space characters".
2. Give a better definition of "white-space wide character" in 7.30.2.1.10 with respect to "C" locale.
3. Add "white-space wide character" to the index.

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

> The committee rejects options 1 and 3 and prefers options 2 and 4\.

Apr 2017 meeting

### Committee Discussion

> The committee discussed this and solicited further input from the author for a
> possible suggested technical corrigendum. Such was provided in [(14657) DR 497
> PTC](https://www.open-std.org/jtc1/sc22/wg14/14657). From that document the
> following sections were found appropriate and have been adopted.

### Proposed Change

In 7.1.1, add a new paragraph:

> In this clause, references to "white-space character" refer to (execution)
> white-space character as defined by **isspace()**. References to "white-space
> wide character" refer to (execution) white-space wide character as defined by
> **iswspace()**.

Remove '(as specified by the **isspace** function)' in: 7.21.6.2#8 (fscanf),
7.22.1.3#2 (strtod), 7.22.1.4#2 (strtol).

Remove '(as specified by the **iswspace** function)' in: 7.29.2.2#8 (fwscanf),
7.29.4.1.1#2 (wcstod), 7.29.4.1.2#2 (wcstol).

Change "white space" to "white-space characters": 7.21.6.2#15 (fscanf),
7.22.1.4#4 (strtol).

Change "white space" to "white-space wide characters": 7.29.2.2#15 (fwscanf),
7.29.4.1.2#4 (wcstol).

Add "white-space wide character" to the index.


</div>


---

---

<div id="issue0498">

## Issue 0498: `mblen`, `mbtowc`, and `wctomb` thread-safety

Authors: WG14, Philipp Klaus Krause  
Date: 2016-04-11  
Reference document: [N2037](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2037.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

This corresponds to Austin Group Defect #708 by Rich Felker. The following four
paragraphs are copies of that Defect Report and the three responses, all from
2013\.

dalias (Rich Felker, musl libc): Per C11 7.1.4 paragraph 5, "Unless explicitly
stated otherwise in the detailed descriptions that follow, library functions
shall prevent data races as follows: A library function shall not directly or
indirectly access objects accessible by threads other than the current thread
unless the objects are accessed directly or indirectly via the function's
arguments. A library function shall not directly or indirectly modify objects
accessible by threads other than the current thread unless the objects are
accessed directly or indirectly via the function's non-const arguments.
Implementations may share their own internal objects between threads if the
objects are not visible to users and are protected against data races." 7.22.7
(Multibyte/wide character conversion functions) does not specify that these
functions are not required to avoid data races with other calls. The only time
they would even potentially be subject to data races is for state-dependent
encodings, which are all but obsolete; for single-byte or modern multi-byte
(i.e. UTF-8) encodings, these functions are pure. Note that 7.29.6.3
(Restartable multibyte/wide character conversion functions) does make exceptions
that the "r" versions of these functions are not required to avoid data races
when the state argument is NULL.

geoffclare: It seems odd that C11 would have different thread-safety
requirements for mbrlen, mbrtowc, and wcrtomb with a null state argument than
for mblen, mbtowc, and wctomb. We should query this with the C committee, as it
may well be unintentional.

dalias: I think there's a very good reason for the discrepancy: the restartable
versions can store a partially-decoded character in the mbstate\_t object, so
even for state-independent encodings, there is state which would need to be
protected against data races. The non-restartable versions, on the other hand,
are pure except in the case of state-dependent encodings, which are mostly a
relic of the past and which were never supported on most POSIX systems, since
these encodings are mostly incompatible with POSIX filesystem semantics. Only
implementations supporting such encodings (which might not even exist \- can
anyone confirm?) would incur the burden of avoiding data races. Note that these
functions give applications access to information on whether the locale's
encoding is state-dependent, so a portable application could use the restartable
interfaces when the locale is state-dependent, and the non-restartable ones
otherwise. As to the motivation behind my request for this change, I have spent
a good deal of time investigating the performance bottlenecks in
character-at-a-time multibyte processing, and it turns out that there is a
fundamental bottleneck in the restartable interfaces due to their interface
requirements for handling the ps argument and partially-decoded characters. For
applications which don't need partial-character processing capability, I believe
it would make sense to encourage a transition to the non-restartable interfaces,
but of course this is problematic if the non-restartable interfaces are not
thread-safe. In my experiments, I found the non-restartable interfaces capable
of reaching roughly a 50% performance advantage over the restartable ones; this
difference would of course become even more extreme if the core decoding
algorithms were further optimized.

nick: This will be raised as a potential defect with the C committee, and any
decision on how to proceed should be made there first.

It seems however that this was so far not brought to the attention of WG 14\.
There seems to be confusion about the thread-safety of mblen(), mbtowc() and
wctomb() when the encoding is not state-dependent. While the C standard seems to
imply that the functions are thread-safe when the encoding is not
state-dependent, apparently some think otherwise. The GNU/Linux manpage for
these functions states "MT-Unsafe race", and recommends to use mbrlen() instead.
Thus clarification is needed.

**Possible Change**

A footnote could be added to 7.22.7 clarifying that the functions mblen(),
mbtowc() and wctomb() do not keep internal state if the encoding is not
state-dependent.

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

> The text in §7.1.4 paragraph 5 requires implementations to avoid data races in
> library functions that maintain their internal state. The `mblen`, `mbtowc`, and
> `wctomb` functions are among those that maintain such state. Although the state
> is typically needed only for state-dependent, multibyte encodings, the standard
> doesn't intend to prevent implementations from accessing it for other encodings
> as well. And indeed implementations are known to exist that access the state for
> other encodings as well. Multi-threaded programs that need the functionality
> provided by these functions are intended to make use of the corresponding
> restartable forms of these functions instead (i.e., `mbrlen`, `mbrtowc`, and
> `wcrtomb`, respectively) with a non-null state pointer.

In §7.22.7 paragraph 1 , change:

> Changing the `LC_CTYPE` category causes the conversion state of these functions
> to be indeterminate.

to:

> Changing the `LC_CTYPE` category causes the conversion state of these functions
> to be indeterminate. A call to any one of these functions may introduce a data
> race with a call to any other function in this section.

In §7.29.6.3 paragraph 1 , change:

> The implementation behaves as if no library function calls these functions with
> a null pointer for `ps`.

to:

> The implementation behaves as if no library function calls these functions with
> a null pointer for `ps`. A call to one of these functions with a null `ps`
> pointer may introduce a data race with another call to the same function.

Apr 2017 meeting

### Committee Discussion

> The committee adopted the words discussed in the previous meeting, with a small
> refinement as suggested in [(SC22WG14.14652) editorial tweak for DR 498
> PTC](https://www.open-std.org/jtc1/sc22/wg14/14652).

Apr 2017 meeting

### Committee Discussion

> A new paper [N2246](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2246.htm)
> was not discussed at WG14 and has been postponed until the next meeting.

### Proposed Change

In §7.22.7 paragraph 1 , change:

> Changing the `LC_CTYPE` category causes the conversion state of these functions
> to be indeterminate.

to:

> Changing the `LC_CTYPE` category causes the conversion state of these functions
> to be indeterminate. A call to any one of these functions may introduce a data
> race with a call to any other function in this subclause.

In §7.29.6.3 paragraph 1 , change:

> The implementation behaves as if no library function calls these functions with
> a null pointer for `ps`.

to:

> The implementation behaves as if no library function calls these functions with
> a null pointer for `ps`. A call to one of these functions with a null `ps`
> pointer may introduce a data race with another call to the same function.

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> A new paper [N2281](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2281.htm)
> was discussed at some length for possible inclusion in a new edition of the
> standard.
>
> The committee believes that the goal of these papers is to establish a normative
> requirement that calls to `mblen`, `mbtowc`, and `wctomb` be data-race free when
> operating upon state-independent encodings. The committee notes that interleaved
> calls to `setlocale` that change even among non-state-dependent encodings must
> necessarily atomically change a reference to the encoding tables used by these
> functions, and that such change would impede the desired speed advantage sought
> by this change. Any assertion of data-race free must also disallow interleaved
> calls to `setlocale` to maintain the speed advantage.
>
> It was also noted in earlier discussions that some implementations are known to
> use shared state even for non-state dependent encodings.
>
> A new paper is solicited from the author for inclusion in a new edition of the
> standard. An affirmative statement is requested, perhaps along the lines of: The
> total order of `mblen`, `mbtowc`, and `wctomb` shall be data-race free when
> there are no calls to `setlocale` in that order and, proabably, that a
> state-indepenent encoding has been determined by a call to `mblen` in the
> normative manner.


</div>


---

---

<div id="issue0499">

## Issue 0499: Anonymous structure in union behavior

Authors: WG14, Rajan Bhakta  
Date: 2016-04-12  
Reference document: [N2038](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2038.htm)  
Status: Fixed  
Fixed in: C23  
Cross-references: [0502](log_c11c17.md#issue0502)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

```c
Given the following code:

union U {
  struct {
    char B1;
    char B2;
    char B3;
    char B4;
  };
  int word;
} u;

Does the storage of B1, B2, B3 and B4 overlap?

According to 6.7.2.1#13, the members should overlap in storage as they become members of 'union U'.
At least one implementation (GCC) seems to NOT consider them to be overlapping.
At least one implementation (IBM's XL LE AIX) considers them to be overlapping as the standard currently states.

Similar code present in example 1 on 6.7.2.1#19.

Suggested TC:
  If the intent is that the members do NOT overlap:
    Append to 6.7.2.1#13:
      Anonymous structures maintain the structure type if they are considered to be members of the containing union.*)
      *) This means the structure members are not considered to occupy the same storage as if they were directly union members.
  If the intent is that the members DO overlap:
    No change, or perhaps add on a comment to 6.7.2.1#19 Example 1:
    ...
    struct { int i, j; }; // anonymous structure, i and j now overlap in storage
    ...
```

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

> The storage does not overlap.
>
> A related issue is to be found in [DR 502](log_c11c17.md#issue0502) and both may be resolved
> with coordinated wording changes.

Apr 2017 meeting

### Committee Discussion

> The committee briefly discussed [(SC22WG14.14628) My approach to DR 499 and
> 502](https://www.open-std.org/jtc1/sc22/wg14/14628) which argues that this might
> be simply an editorial issue, such that a change as simple as:
>
> Change §6.7.2.1 p13 from:
>
> > An unnamed member of structure type with no tag is called an *anonymous
> > structure*; an unnamed member of union type with no tag is called an *anonymous
> > union*. The members of an anonymous structure or union are considered to be
> > members of the containing structure or union. This applies recursively if the
> > containing structure or union is also anonymous.
>
> to:
>
> > An unnamed member of structure type with no tag is called an *anonymous
> > structure*; an unnamed member of union type with no tag is called an *anonymous
> > union*. The names of members of an anonymous structure or union are added to the
> > name space of the containing structure or union. This applies recursively if the
> > containing structure or union is also anonymous.
>
> would adequately resolve the issue.

Oct 2017 meeting

### Committee Discussion

> The suggestion almost works but not quite, as discussed in [(SC22WG14.14632) My
> approach to DR 499 and 502,](https://www.open-std.org/jtc1/sc22/wg14/14632)
> where a flexible array member following an anonymous structure would no longer
> be allowed.
>
> Further thought is needed.

Apr 2018 meeting

### Committee Discussion

> A short paper was solicited, discussed, and adopted as the Proposed Change to a
> new revision of the Standard.
>
> It was noted that additional wording might be appropriate with regard to both
> tail padding and to address flexible array members.

### Proposed Change

Change §6.7.2.1 p13 from:

> An unnamed member of structure type with no tag is called an *anonymous
> structure*; an unnamed member of union type with no tag is called an *anonymous
> union*. The members of an anonymous structure or union are considered to be
> members of the containing structure or union. This applies recursively if the
> containing structure or union is also anonymous.

to:

> An unnamed member of structure type with no tag is called an *anonymous
> structure*; an unnamed member of union type with no tag is called an *anonymous
> union*. The members of an anonymous structure or union are considered to be
> members of the containing structure or union, keeping their structure or union
> layout. This applies recursively if the containing structure or union is also
> anonymous.


</div>


---

---

<div id="issue0500">

## Issue 0500: Ambiguous specification for **FLT\_EVAL\_METHOD**

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

5.2.4.2.2#9:

> Except for assignment and cast (which remove all extra range and precision), the
> values yielded by operators with floating operands and values subject to the
> usual arithmetic conversions and of floating constants are evaluated to a format
> whose range and precision may be greater than required by the type. The use of
> evaluation formats is characterized by the implementation-defined value
> of `FLT_EVAL_METHOD`:
>
> `-1` indeterminable;
>
> `0` evaluate all operations and constants just to the range and precision of the
> type;
>
> `1` evaluate operations and constants of type `float` and `double` to the range
> and precision of the `double` type, evaluate `long double` operations and
> constants to the range and precision of the `long double` type;
>
> `2` evaluate all operations and constants to the range and precision of the
> `long double` type.
>
> All other negative values for `FLT_EVAL_METHOD` characterize
> implementation-defined behavior

Do the words:

> the values yielded by operators with floating operands and values subject to the
> usual arithmetic conversions

in the first sentence mean the same as:

> Interpretation 1: the values yielded by operators with: (a) floating operands
> and (b) values subject to the usual arithmetic conversions

or:

> Interpretation 2: (a) the values yielded by operators with floating operands and
> (b) the values subject to the usual arithmetic conversions?

Interpretation 2 is problematic because the evaluation methods pertain only to
operators that return a value of floating type, not to, for example, the
relational operators with floating operands. Nor do they apply to all values
subject to the usual arithmetic conversions, and so (b) doesn’t add anything.
Thus, reasonableness suggests Interpretation 1\. However, the mention of
assignment and cast (which are not subject to the usual arithmetic conversions)
suggests Interpretation 2\.

Interpretation 2, unlike Interpretation 1, implies that values yielded by unary
operators are widened to the evaluation format. In some cases whether a unary
operator is widened matters. Widening a signaling NaN operand raises the
“invalid” floating-point exception. Widening an operand with a non-canonical
encoding canonicalizes the encoding.

The IEC 60559 *copy* and *negate* operations are bit manipulation operations
that affect at most the sign. C operations bound to these IEC 60559 operations
are expected to behave accordingly, but won’t if they entail widening.

Widening unary operators would introduce conversions that might affect
performance but which have no benefit.

According to personal notes, this issue came up at the WG14 meeting in Chicago
in 2013, but was not resolved and did not result in an action item.

Recently, this issue came up again as underlying the issue raised by Joseph
Myers in email SC22WG14.14278:

> Suppose that with an implementation of C11 \+ TS 18661-1, that defines
>
> `FLT_EVAL_METHOD` to `2`, you have:
>
> > ```c
> > static volatile double x = SNAN;
> >
> > (void) x;
> > ```
>
> Suppose also that the implementation defines the "`(void) x;`" statement to
>
> constitute an access to volatile-qualified `x`.
>
> May the implementation define that access to convert `x` from the format of
>
> `double` to the format of `long double`, with greater range and precision,
>
> that format being used to represent `double` operands in accordance with the
>
> setting of `FLT_EVAL_METHOD`, and thereby to raise the "invalid" exception?
>
> That is, may a convertFormat operation be applied as part of
>
> lvalue-to-rvalue conversion where `FLT_EVAL_METHOD` implies that a wider
>
> evaluation format is in use?
>
> Even without signaling NaNs, the issue can apply to the case of exact
>
> underflow, which can be detected using pragmas from TS 18661-5, if the
>
> wider format has extra precision but not extra range and so exact underflow
> occurs on converting a subnormal value to the wider format.

The following suggested Technical Corrigendum is intended to clarify the wording
in favor of Interpretation 1, which excludes widening unary operators to the
evaluation format.

### Suggested Technical Corrigendum

In 5.2.4.2.2#9, replace:

> Except for assignment and cast (which remove all extra range and precision), the
> values yielded by operators with floating operands and values subject to the
> usual arithmetic conversions and of floating constants are evaluated to a format
> whose range and precision may be greater than required by the type.

with:

> The values of floating type yielded by operators subject to the usual
> arithmetic conversions and the values of floating constants are evaluated to a
> format whose range and precision may be greater than required by the type. In
> all cases, assignment and cast remove all extra range and precision.

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

> The current text is ambiguous. It might be read to imply that unary operators
> must widen, which is not the intent since it would be incompatible with IEEE
> 60559\. Widening can cause signaling NaNs to be triggered and representations to
> be canonicalized.

### Proposed Change

In 5.2.4.2.2#9, replace:

> Except for assignment and cast (which remove all extra range and precision), the
> values yielded by operators with floating operands and values subject to the
> usual arithmetic conversions and of floating constants are evaluated to a format
> whose range and precision may be greater than required by the type.

with:

> The values of floating type yielded by operators subject to the usual
> arithmetic conversions and the values of floating constants are evaluated to a
> format whose range and precision may be greater than required by the type. In
> all cases, assignment and cast remove all extra range and precision.


</div>


---

---

<div id="issue0501">

## Issue 0501: Can **DECIMAL\_DIG** be larger than necessary?

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14285:

> C11 defines `DECIMAL_DIG` as "number of decimal digits, *n*, such that any
> floating-point number in the widest supported floating type with
> *p<sub>max</sub>* radix *b* digits can be rounded to a floating-point number
> with *n* decimal digits and back again without change to the value," and then
> gives a formula.
>
> Is it OK for the value of `DECIMAL_DIG` to be larger than given by the formula?
>  Such a value would still seem to meet the textual description, though being
> suboptimal.
>
> This is an issue for implementing TS 18661-3 when that involves types wider than
> `long double`.  In C11, "real floating type" means `float`, `double` or `long
> double` (6.2.5#10) (and then those types plus the three complex types are
> defined to be the floating types).  TS 18661-3 is supposed to be compatible with
> C11, so that an implementation can conform to both simultaneously.  The
> definition of `DECIMAL_DIG` in TS 18661-3 covers all supported floating types
> and non-arithmetic encodings.  And that's not conditional on
> `__STDC_WANT_IEC_60559_TYPES_EXT__`.  So in an implementation of TS 18661-3 that
> supports `_Float128`, `DECIMAL_DIG` must be big enough for `_Float128`, even if
> `__STDC_WANT_IEC_60559_TYPES_EXT__` is not defined when `<float.h>` is included.
>  And that's only compatible with C11 (if `long double` is narrower than
> `_Float128`) if C11 allows `DECIMAL_DIG` to be larger than given by the formula.

Agreed. The current specification for `DECIMAL_DIG` in TS 18661-3 is
incompatible with C11, as explained.

The suggested Technical Corrigendum below allows `DECIMAL_DIG` to be larger than
the value of the given formula. Thus an implementation that supports a floating
type wider than `long double`, for example a wide type in TS 18661-3, could
define `DECIMAL_DIG` to be large enough for its widest type and still conform as
a C implementation without extensions.

Where `DECIMAL_DIG` is used to determine a sufficient number of digits, this
change might lead to conversions with more digits than needed and with more
digits than would have been used without the change. However, programs wishing
the minimal sufficient number of digit are better served by the type-specific
macros `FLT_DECIMAL_DIG`, etc.

We considered the alternative of changing TS 198661-3 to make `DECIMAL_DIG`
dependent on `__STDC_WANT_IEC_60559_TYPES_EXT__`.  But this could lead to errors
resulting from separately compiled parts of a program using inconsistent values
of `DECIMAL_DIG`.

### Suggested Technical Corrigendum

In 5.2.4.2.2#11, change the bullet defining `DECIMAL_DIG` from:

> —      number of decimal digits, *n*, such that any floating-point number in the
> widest supported floating type with *p<sub>max</sub>* radix *b* digits can be
> rounded to a floating-point number with n decimal digits and back again without
> change to the value,
>
> > \< … formula … \>

to:

> —      number of decimal digits, *n*, such that any floating-point number in the
> widest supported floating type with *p<sub>max</sub>* radix *b* digits can be
> rounded to a floating-point number with n decimal digits and back again without
> change to the value, at least
>
> > \< … formula … \>

---

Comment from WG14 on 2019-05-03:

Oct 2016 meeting

### Committee Discussion

> The committee agrees with the recommendation. The following example was
> solicited and provided for a committee response.
>
> (The committee’s Proposed Committee Response and Proposed Technical Corrigendum
> have been superceded)

Apr 2017 meeting

### Committee Discussion

> The committee’s Proposed Committee Response and Proposed Technical Corrigendum
> from the last meeting was discussed and a new paper
> [N2108](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2108.pdf) by the WG14
> Floating Point study group was written and discussed at some length. After due
> consideration the committee agreed with their conclusion that `DECIMAL_DIG`
> could not in fact be implemented properly, and adopted their Suggested Technical
> Corrigendum below. For reference, the committee's previous direction can be
> found in [N2109](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2109.htm) and
> has been elided in this document.

Oct 2017 meeting

> A proposed change was adopted.

Apr 2018 meeting

### Committee Discussion

> Alternative input to the Proposed Change was presented in paper
> [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.htm) by the C
> Floating Point working group.
>
> These changes were, however, not reviewed by the Committee.

Oct 2018 meeting

### Committee Discussion

> Alternative input to the Proposed Change was presented in paper
> [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.htm) by the C
> Floating Point working group.
>
> N2108 suggested obsolescing `DECIMAL_DIG`, as part of the resolution of CR 501\.
> This document updates the suggested CR in N2108 to eliminate references in C11
> to `DECIMAL_DIG`, and to clarify. Changes below (along with changes to TS
> 18661\) were identified in N2211.
>
> The Floating Point Study Group was requested to extract the changes for C from
> N2211 and present them separately. This was done and presented (without change)
> in paper [N2253](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2253.pdf) and
> these changes were accepted by the committee as the proposed resolution to this
> issue.

### Proposed Change

In 7.31, add a subclause:

> **7.31.x Mathematics** `<math.h>`
>
> Use of the `DECIMAL_DIG` macro is an obsolescent feature. A similar
> type-specific macro, such as `LDBL_DECIMAL_DIG` can be used instead.

In 5.2.4.2.2#11, in the bullet defining `DECIMAL_DIG`, attach a footnote to the
wording:

> ```c
> DECIMAL_DIG
> ```

where the footnote is:

> \*) See ‘‘future library directions’’ (7.31.x).

In 5.2.4.2.2#14, change:

>  \[14\] Conversion from (at least) `double` to decimal with `DECIMAL_DIG` digits
> and back should be the identity function.

to:

> \[14\] Conversion between real floating type and decimal character sequence with
> at most *T*`_DECIMAL_DIG` digits should be correctly rounded, where *T* is the
> macro prefix for the type. This assures conversion from real floating type to
> decimal character sequence with *T*`_DECIMAL_DIG` digits and back, using
> to-nearest rounding, is the identity function.

In 5.2.4.2.2#16, in the list of macro values in EXAMPLE 2, omit:

> ```c
> DECIMAL_DIG          17
> ```

In 5.2.4.2.2#16, at the end of EXAMPLE 2, omit:

> If a type wider than `double` were supported, then `DECIMAL_DIG` would be
> greater than 17\. For example, if the widest type were to use the minimal-width
> IEC 60559 double-extended format (64 bits of precision), then `DECIMAL_DIG`
> would be 21\.

In 7.21.6.1#13 and 7.29.2.1#13, change:

> \[13\] For `e`, `E`, `f`, `F`, `g`, and `G` conversions, if the number of
> significant decimal digits is at most `DECIMAL_DIG`, then the result should be
> correctly rounded.283) If the number of significant decimal digits is more than
> `DECIMAL_DIG` but the source value is exactly representable with `DECIMAL_DIG`
> digits, then the result should be an exact representation with trailing zeros.
> Otherwise, the source value is bounded by two adjacent decimal strings *L* \<
> *U*, both having `DECIMAL_DIG` significant digits; the value of the resultant
> decimal string *D* should satisfy *L* ≤ *D* ≤ *U*, with the extra stipulation
> that the error should have a correct sign for the current rounding direction.

to:

> \[13\] For `e`, `E`, `f`, `F`, `g`, and `G` conversions, if the number of
> significant decimal digits is at most the maximum value *M* of the
> *T*`_DECIMAL_DIG` macros (defined in `<float.h>`), then the result should be
> correctly rounded.283) If the number of significant decimal digits is more than
> *M* but the source value is exactly representable with *M* digits, then the
> result should be an exact representation with trailing zeros. Otherwise, the
> source value is bounded by two adjacent decimal strings *L* \< *U*, both having
> *M* significant digits; the value of the resultant decimal string *D* should
> satisfy *L* ≤ *D* ≤ *U*, with the extra stipulation that the error should have a
> correct sign for the current rounding direction.

In 7.22.1.3#9 and 7.29.4.1.1#9, change:

> \[9\] If the subject sequence has the decimal form and at most `DECIMAL_DIG`
> (defined in `<float.h>`) significant digits, the result should be correctly
> rounded. If the subject sequence *D* has the decimal form and more than
> `DECIMAL_DIG` significant digits, consider the two bounding, adjacent decimal
> strings *L* and *U*, both having `DECIMAL_DIG` significant digits, such that the
> values of *L*, *D*, and *U* satisfy *L* ≤ *D* ≤ *U*. The result should be one of
> the (equal or adjacent) values that would be obtained by correctly rounding *L*
> and *U* according to the current rounding direction, with the extra stipulation
> that the error with respect to *D* should have a correct sign for the current
> rounding direction.294)

to:

> \[9\] If the subject sequence has the decimal form and at most *M* significant
> digits, where *M* is the maximum value of the *T*`_DECIMAL_DIG` macros (defined
> in `<float.h>`), the result should be correctly rounded. If the subject sequence
> *D* has the decimal form and more than *M* digits, consider the two bounding,
> adjacent decimal strings *L* and *U*, both having *M* significant digits, such
> that the values of *L*, *D*, and *U* satisfy *L* ≤ *D* ≤ *U*. The result should
> be one of the (equal or adjacent) values that would be obtained by correctly
> rounding *L* and *U* according to the current rounding direction, with the extra
> stipulation that the error with respect to *D* should have a correct sign for
> the current rounding direction.294)

In 7.22.1.3 footnote 294 and 7.29.4.1.1 footnote 345, change:

> `DECIMAL_DIG`, defined in `<float.h>`, should be sufficiently large that *L* and
> *U* will usually round to the same internal floating value, but if not will
> round to adjacent values.

to:

> *M* is sufficiently large that *L* and *U* will usually correctly round to the
> same internal floating value, but if not will correctly round to adjacent
> values.

In F.5, omit footnote 361:

> If the minimum-width IEC 60559 extended format (64 bits of precision) is
> supported, `DECIMAL_DIG` shall be at least 21\. If IEC 60559 double (53 bits of
> precision) is the widest IEC 60559 format supported, then `DECIMAL_DIG` shall be
> at least 17\. (By contrast, `LDBL_DIG` and `DBL_DIG` are 18 and 15,
> respectively, for these formats.)

The following change is needed only if TS 18661-1 (with CR 20\) is not
incorporated into C.

In F.5, replace::

> \[1\] Conversion from the widest supported IEC 60559 format to decimal with
> **DECIMAL\_DIG** digits and back is the identity function.361)
>
> \[2\] Conversions involving IEC 60559 formats follow all pertinent recommended
> practice. In particular, conversion between any supported IEC 60559 format and
> decimal with `DECIMAL_DIG` or fewer significant digits is correctly rounded
> (honoring the current rounding mode), which assures that conversion from the
> widest supported IEC 60559 format to decimal with `DECIMAL_DIG` digits and back
> is the identity function.

with:

> \[1\] Conversions involving IEC 60559 formats follow all pertinent recommended
> practice. Conversion between any supported IEC 60559 format and decimal
> character sequence with *M* or fewer significant digits is correctly rounded
> (honoring the current rounding mode), where *M* is the maximum value of the
> *T*`_DECIMAL_DIG` macros (defined in `<float.h>`). Conversion from any supported
> IEC 60559 format to decimal character sequence with at least *T*`_DECIMAL_DIG`
> digits (for the corresponding *type*) and back, using to-nearest rounding, is
> the identity function.

and renumber the subsequent paragraph.


</div>


---

---

<div id="issue0502">

## Issue 0502: Flexible array member in an anonymous struct

Authors: WG14, Martin Sebor  
Date: 2016-09-18  
Reference document: [N2080](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2080.htm)  
Status: Closed  
Cross-references: [0499](log_c11c17.md#issue0499)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

**EXAMPLE 3** in paragraph 26 of **§6.7.2.1 Structure and union specifiers**
shows a valid definition of a struct containing both an anonymous struct and a
flexible array member:

> –26–   EXAMPLE 3   Because members of anonymous structures and unions are
> considered to be members of the containing structure or union, `struct s` in the
> following example has more than one named member and thus the use of a flexible
> array member is valid.
>
> ```c
>     struct s {
>         struct { int i; };
>         int a[];
>     };
> ```

Now consider the following ever so slightly modified but seemingly equivalent
version of the same example. Is it also valid?

```c
    struct s {
        int i;
        struct { int a[]; };
    };
```

Paragraph 13 of the section referenced above specifies that:

> An unnamed member whose type specifier is a structure specifier with no tag is
> called an anonymous structure; \[...\]. The members of an anonymous structure or
> union are considered to be members of the containing structure or union. This
> applies recursively if the containing structure or union is also anonymous.

Subsequently, paragraph 18 of the same section defines a *flexible array member*
as follows:

> As a special case, the last element of a structure with more than one named
> member may have an incomplete array type; this is called a *flexible array
> member*.

A possible interpretation of these two paragraphs applied to the modified
example above is that, since the flexible array member `a` is considered to be a
member of `struct s` that has a preceding data member and no members following
the anonymous struct, the example is valid.

However, another possible interpretation (offered in reflector message
[SC22WG14.14299](https://www.open-std.org/jtc1/sc22/wg14/14299 "flexible array
member in an anonymous struct")) is that:

> *...the layout \[of a struct containing an anonymous struct\] is exactly as if
> the contained anonymous structure or union had a name (so it acts like a
> structure is declared as such even if contained in a union, or like a union if
> declared as such even if contained in a structure), with all the usual
> constraints applying to the contained structure or union, and the only
> difference being a shorthand notation for naming members of the contained
> structure or union.*

According to this interpretation, the defintion in the example is not valid.
This interpretation appears to be reflected in the behavior of a number of
tested implementations: they all diagnose it, indicating that a flexible array
may not be the sole member of a struct.

We believe both of these interpretations are reasonable and the standard,
therefore, to be ambiguous on this point. In addition, despite support for the
latter interpretation in existing practice, we don't know of any technical
reason to disallow flexible arrays as sole members in anonymous structs.

It is worth noting that the lack of clarity in this area has also given rise to
DR [499](log_c11c17.md#issue0499).

As a separate issue, the definition of a flexible array member cited above
refers to such a member as an *element* of a structure. This is unusual (and
raises a question about the meaning of the word in this context) because the
term element is otherwise reserved to refer to elements of an array or to
enumerators, but not to members of structures. If the text doesn't intend to
differentiate flexible array members from other members beyond the explicitly
spelled out constraints it should make use of the word member consistently and
avoid using the term *element*.

### Suggested Technical Corrigendum

The standard needs to be clarified to avoid the ambiguity discussed above.

We suggest that the standard be made clear that defining a flexible array as the
sole member of an anonymous struct is permitted as long as the flexible array is
not the sole member of the enclosing object.

Since we believe the standard can already be interpreted as proposed, we suggest
to add a new paragraph to the end of **§6.7.2.1 Structure and union specifiers**
with the following text.

> –27–   EXAMPLE 4   Similarly to example 3, since the flexible array member `a`
> defined in the anonymous struct is considered a member of the enclosing `struct
> t` that declares a preceding named member and no subsequent members, the use of
> the flexible array member is valid:
>
> ```c
>     struct t {
>         int i;
>         struct { int a[]; };
>     };
> ```

In addition, we suggest that the word *element* in the definition of the term
*flexible array member* be replaced with the word *member* (or, alternatively,
that the meaning of the term element in this context be defined and clearly
distinguished from other uses of the term in the text such as those referring to
elements of arrays).

To that end, we propose to modify **§6.7.2.1 Structure and union specifiers**,
paragraph 18, as indicated below:

> –18–   As a special case, the last <ins>member</ins> <del>element</del> of a
> structure with more than one named member may have an incomplete array type;
> this is called a *flexible array member*. …

---

Comment from WG14 on 2018-04-26:

Oct 2016 meeting

### Committee Discussion

> The committee agrees that defining a flexible array as the sole member of an
> anonymous struct is permitted as long as the flexible array is not the sole
> member of the enclosing object.
>
> This issue might also be resolved via [DR 499](log_c11c17.md#issue0499)

Apr 2017 meeting

### Committee Discussion

> After further discussion and review, the committee does not support the
> interpretation that §6.7.2.1 paragraph 13 overrides the paragraph 18\.

### Proposed Committee Response

> The committee does not support the interpretation that §6.7.2.1 paragraph 13
> overrides the paragraph 18\. No struct or union, even anonymous, should have a
> size of zero, and since the effect desired is easily achieved, there is no
> motivation for creating a second mechanism to achieve that purpose.


</div>


---

---

<div id="issue0503">

## Issue 0503: Hexadecimal floating-point and `strtod`

Authors: WG14, Clark Nelson  
Date: 2016-09-13  
Reference document: [N2082](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2082.htm)  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 7.22.1.3 paragraph 3 bullet 2 says:

> a `0x` or `0X`, then a nonempty sequence of hexadecimal digits optionally
> containing a decimal-point character, then an optional binary exponent part as
> defined in 6.4.4.2;

but the grammar in C11 6.4.4.2 makes the binary-exponent-part mandatory, not
optional.

**Suggested resolution**

Strike "optional" before "binary exponent part" and add a comma before "as
defined in" to highlight that "as defined in" applies to the entire sentence,
not only to the last part.

---

Comment from WG14 on 2017-11-03:

Oct 2016 meeting

### Committee Discussion

> This turns out to not be a defect.

### Proposed Committee Response

> The reference to §6.4.4.2 is only for the definition of "binary exponent part",
> it does not apply to the entire sentence. The specification of allowable subject
> sequences for these library functions is intentionally looser than the grammar
> for floating constants in order to accept as many reasonable input strings as
> possible. Thus, both 123 and 0x123 are valid subject sequences even though
> neither is acceptable as a floating constant.


</div>


---

