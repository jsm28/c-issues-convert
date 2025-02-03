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
