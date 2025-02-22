## Issue 0406: Visible sequences of side effects are redundant

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Cross-references: [0402](../c11c17/issue0402.md)  
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
> * Should be contingent on [Defect 402](../c11c17/issue0402.md).

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
