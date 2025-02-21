## Issue 0403: `malloc()` and `free()` in the memory model

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Submitted against: C11 / C17  
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
