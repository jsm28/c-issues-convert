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
