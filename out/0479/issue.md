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
