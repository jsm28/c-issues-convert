### Summary

C11 does not *appear* to allow `mtx_trylock` to fail spuriously (i.e., return
`thrd_busy` even thought the lock was not acquired, yet eventually acquire the
lock if it is not acquired by any thread), but C\+\+11 does (see 30.4.1.1/16):

> An implementation may fail to obtain the lock even if it is not held by any
> other thread. \[ Note: This spurious failure is normally uncommon, but allows
> interesting implementations based on a simple compare and exchange (Clause 29).
> \-- end note \] An implementation should ensure that try\_lock() does not
> consistently return false in the absence of contending mutex acquisitions.

It might be better to point out explicitly that programmers should treat
`mtx_trylock` as if spurious failure were allowed, since the memory model is
intentionally too weak to support correct reasoning that is based on a return
value of `thrd_busy`. There has been debate on this issue, and we would prefer
the standard to be clearer. Consider the following example:

```c
Thread 1:
  v1 = 1;
  mtx_lock(l1);

Thread 2:
  r1 = mtx_trylock(l1);
  while (r1 == thrd_success /* was unlocked */) {
    unlock(l1);
    r1 = mtx_trylock(l1);
  }
  r2 = v1;
  out(r2);
```

This program is not data-race-free according to C11, independently of whether
`mtx_trylock` is allowed to fail spuriously or not; the happens-before-based
definition of a data race and the current specification of synchronizes-with
relations between mutex operations makes it clear that the program above has a
data race on `v1`.

However, if spurious failures are not allowed, an intuitive understanding of the
memory model in the sense that everything will appear to be sequentially
consistent if only locks are used to synchronize does not hold anymore. The
intuitive understanding would make the program above correct; in particular the
store to `v1` by the first thread would be expected to "happen before" the load
from `v1` by the second thread.

Therefore, to make an intuitive understanding of the C11 memory model and locks
match the actual specification, it would be helpful to point out that
programmers should assume `mtx_trylock` to fail spuriously. Otherwise, without
spurious failure, we have cases like the example above in which two operations
race according to the specification in spite of the fact that they intuitively
can't execute at the same time.

Allowing spurious failures does not affect the typical uses of `mtx_trylock`,
for example to acquire several locks without risk of deadlock. It does rule out
uses like the example above, however, in which locks are attempted to be used as
a replacement for atomics.

(Note that we are not arguing for specifying that `mtx_lock` should synchronize
with a `mtx_trylock` that returns `thrd_busy`. This would make the
implementation of lock acquisition less efficient on architectures such as ARM
or PowerPC. In particular, an `atomic_compare_exchange` or similar that
transitions the lock's state from not acquired to acquired would have to use
`memory_order_acq_rel` instead of `memory_order_acquire`.)

### Suggested Technical Corrigendum

It seems that the normative specification already states the preferred
semantics, although the return value specification for `thrd_busy` may make
readers believe that this return code allows one to infer a certain ordering
(see the example above).

We propose to add a clarifying note at an appropriate place (e.g., in
7.26.4.5p3):

> Programmers should treat `mtx_trylock` as if spurious failures were allowed; the
> memory model is intentionally too weak to support reasoning based on a return
> value of `thrd_busy`.
