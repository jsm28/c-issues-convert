## Issue 0407: SC fences do not restrict modification order enough

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Submitted against: C11 / C17  
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
  > -7- ~~For atomic operations *A* and *B* on an atomic object *M*, if there are
  > `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*,
  > *Y* is sequenced before *B*, and *X* precedes *Y* in *S*, then *B* occurs later
  > than *A* in the modification order of *M*.~~ <u>For atomic modifications *A* and
  > *B* of an atomic object *M*, *B* occurs later than *A* in the modification order
  > of *M* if:</u>
  >
  > + <u>there is a `memory_order_seq_cst` fence *X* such that *A* is sequenced before *X*, and *X* precedes *B* in *S*, or</u>
  > + <u>there is a `memory_order_seq_cst` fence *Y* such that *Y* is sequenced before *B*, and *A* precedes *Y* in *S*, or</u>
  > + <u>there are `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*, *Y* is sequenced before *B*, and *X* precedes *Y* in *S*.</u>

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

   ~~For atomic operations *A* and *B* on an atomic object *M*, if there are
   `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*,
   *Y* is sequenced before *B*, and *X* precedes *Y* in *S*, then *B* occurs later
   than *A* in the modification order of *M*.~~ <u>For atomic modifications *A* and
   *B* of an atomic object *M*, *B* occurs later than *A* in the modification order
   of *M* if:</u>

   * <u>there is a `memory_order_seq_cst` fence *X* such that *A* is sequenced before *X*, and *X* precedes *B* in *S*, or</u>
   * <u>there is a `memory_order_seq_cst` fence *Y* such that *Y* is sequenced before *B*, and *A* precedes *Y* in *S*, or</u>
   * <u>there are `memory_order_seq_cst` fences *X* and *Y* such that *A* is sequenced before *X*, *Y* is sequenced before *B*, and *X* precedes *Y* in *S*.</u>

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
