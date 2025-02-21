## Issue 0408: Should locks provide intra-thread synchronization

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Submitted against: C11 / C17  
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
