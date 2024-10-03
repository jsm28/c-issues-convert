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
