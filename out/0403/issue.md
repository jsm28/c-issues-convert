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
