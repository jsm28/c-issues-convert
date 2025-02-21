## Issue 0479: unclear specification of `mtx_trylock` on non-recursive muteness

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Torvald Riegel, Martin Sebor  
Date: 2015-09-25  
Reference document: [N1963](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1963.htm)  
Submitted against: C11 / C17  
Status: Closed  
Cross-references: [0469](../c11c17/issue0469.md), [0493](../c11c17/issue0493.md)  
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
* Coordinated new wording is solicited from the authors to both this and the solicited author for the resolution of [DR 469](../c11c17/issue0469.md) since it also is proposing potentially overlapping wording changes in this area.

Apr 2016 meeting

### Committee Discussion

> This resolution continues to be bound to [DR 469](../c11c17/issue0469.md)

Apr 2018 meeting

### Committee Discussion

> The committee solicited a combined comprehensive resolution for these issues
> with those raised in [DR 469](../c11c17/issue0469.md) and [DR 493](../c11c17/issue0493.md). The authors
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
> and asks that issues from [CR 469](../c11c17/issue0469.md), [CR 479](../c11c17/issue0479.md), and [CR
> 493](../c11c17/issue0493.md), as well as potentially other small issues be combined in a new
> paper to completely resolve this issue for the next revision of the standard.
