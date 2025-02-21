## Issue 0480: `cnd_wait` and `cnd_timewait` should allow spurious wake-ups

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Torvald Riegel, Martin Sebor  
Date: 2015-09-25  
Reference document: [N1964](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1964.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Both ISO C\+\+ and POSIX allow for spurious wake-ups from their condition
variable wait functions. However, C11 has no wording that would allow that.
(This applies to both `cnd_wait` and `cnd_timewait`, but just `cnd_wait` is
referred to in what follows.)

If spurious wake-ups are allowed, then some implementations become significantly
easier; it also allows to implement the C standard on top of POSIX using just a
thin wrapper. In contrast, implementing a condition variable that does not allow
spurious wake-ups on top of a condition variable implementation that does allow
that is likely close to implementing a condition variable from scratch in terms
of complexity.

Another reason for allowing spurious wake-ups is that to actually exploit having
no spurious wake-ups, a program needs to take quite some care to establish the
happens-before relations required to make just the return from `cnd_wait` mean
something that can be used to infer something about the then current state of
memory (for example, if the wake-up is supposed to also mean that some state has
been initialized).

Specifically, the program must make sure that it actually calls `cnd_signal` (or
`cnd_broadcast`) after `cnd_wait` has started to block; this can be ensured by
calling `cnd_signal` from a critical section protected by the same mutex as
supplied to the respective `cnd_wait`, and checking the ordering of the
`cnd_wait` and `cnd_signal` critical sections in some way (e.g., through access
to variables protected by the same mutex, or by not letting the signaling thread
enter the `cnd_signal` critical section before the `cnd_wait` critical section).
Second, `cnd_wait` is not specified to synchronize with `cnd_signal`, so either
`cnd_signal` must be in such a critical section (ie, there is a second reason
for that), or the signaler and the waiter must establish a happens-before
relation through other means such as atomics.

### Suggested Technical Corrigendum

Change this sentence from the specification of `cnd_wait` (7.26.3.6p2):

> The cnd\_wait function atomically unlocks the mutex pointed to by mtx and
> endeavors to block until the condition variable pointed to by cond is signaled
> by a call to cnd\_signal or to cnd\_broadcast.

to this:

> The cnd\_wait function atomically unlocks the mutex pointed to by mtx and
> endeavors to block until the condition variable pointed to by cond is signaled
> by a call to cnd\_signal or to cnd\_broadcast, or until it is unblocked due to a
> spurious, unspecified reason.

Likewise for `cnd_timedwait`.

---

Comment from WG14 on 2017-11-03:

Oct 2015 meeting

### Committee Discussion

> The committee agrees with the authors’ interpretation and accepts their
> Suggested Technical Corrigendum with one minor edit. The word “spurious” is felt
> to be implied by the use of the verb “endeavors” and is struck.

Apr 2016 meeting

### Committee Discussion

> The committee decided to change “endeavors to block” to “blocks”, and that
> change is made in the Proposed Technical Corrigendum below.

### Proposed Technical Corrigendum

In §7.26.3.5p2 change

> The `cnd_timedwait` function atomically unlocks the mutex pointed to by `mtx`
> and endeavors to block until the condition variable pointed to by `cond` is
> signaled by a call to `cnd_signal` or to `cnd_broadcast`, or until after the
> `TIME_UTC`-based calendar time pointed to by `ts`.

to

> The `cnd_timedwait` function atomically unlocks the mutex pointed to by `mtx`
> and blocks until the condition variable pointed to by `cond` is signaled by a
> call to `cnd_signal` or to `cnd_broadcast`, or until after the `TIME_UTC`-based
> calendar time pointed to by `ts`, or until it is unblocked due to an unspecified
> reason.

In §7.26.3.6p2 change

> The `cnd_wait` function atomically unlocks the mutex pointed to by `mtx` and
> endeavors to block until the condition variable pointed to by `cond` is signaled
> by a call to `cnd_signal` or to `cnd_broadcast`.

to:

> The `cnd_wait` function atomically unlocks the mutex pointed to by `mtx` and
> blocks until the condition variable pointed to by `cond` is signaled by a call
> to `cnd_signal` or to `cnd_broadcast`, or until it is unblocked due to an
> unspecified reason.
