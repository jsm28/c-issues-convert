## Issue 0469: lock ownership vs. thread termination

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Torvald Riegel  
Date: 2014-10-07  
Reference document: [N1881](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1881.htm)  
Submitted against: C11 / C17  
Status: Closed  
Cross-references: [0414](issue0414.md), [0416](issue0416.md), [0479](issue0479.md), [0493](issue0493.md)  
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
> Issue 1 from that paper has already been addressed in [DR414](issue0414.md)
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
> the resolution to [DR 414](issue0414.md) be folded into any Suggested Technical
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
> reconciled with the first item from the PTC of [DR 416](issue0416.md). It was also
> suggested that “or through program termination” be added.
>
> [DR 479](issue0479.md) and [DR 493](issue0493.md) raise other issues that must be
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
> in [DR 479](issue0479.md) and [DR 493](issue0493.md).
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
> and asks that issues from [CR 469](issue0469.md), [CR 479](issue0479.md), and [CR
> 493](issue0493.md), as well as potentially other small issues be combined in a new
> paper to completely resolve this issue for the next revision of the standard.
