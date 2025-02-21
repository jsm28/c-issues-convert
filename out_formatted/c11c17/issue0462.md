## Issue 0462: Clarifying objects accessed in signal handlers

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, [Robert Seacord](mailto:rcs@cert.org)  
Date: 2014-03-25  
Reference document: [N1813](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1813.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

It appears the intent of the committee in Subclause 5.1.2.3 paragraph 5 was to
allow lock-free atomic objects or objects of type `volatile sig_atomic_t` to be
accessed from a signal handler.  Objects of type `atomic_flag` are an obvious
choice operations on an object of type `atomic_flag` are required to be lock
free. However, objects of type `atomic_flag` can only be meaningfully accessed
by a call to a function, and calls to these functions from a signal handler are
undefined behavior according to subclause 7.14.1.1 paragraph 5\.

### Suggested Technical Corrigendum

Change subclause 7.14.1.1 paragraph 5 from:

If the signal occurs other than as the result of calling the `abort` or `raise`
function, the behavior is undefined if the signal handler refers to any object
with static or thread storage duration that is not a lock-free atomic object
other than by assigning a value to an object declared as `volatile
sig_atomic_t`, or the signal handler calls any function in the standard library
other than the `abort` function, the `_Exit` function, the `quick_exit`
function, or the `signal` function with the first argument equal to the signal
number corresponding to the signal that caused the invocation of the handler.
Furthermore, if such a call to the `signal` function results in a `SIG_ERR`
return, the value of `errno` is indeterminate.<sup>252\)</sup>

to:

If the signal occurs other than as the result of calling the `abort` or `raise`
function, the behavior is undefined if the signal handler refers to any object
with static or thread storage duration that is not a lock-free atomic object
other than by assigning a value to an object declared as `volatile
sig_atomic_t`, or the signal handler calls any function in the standard library
other than the `abort` function, the `_Exit` function, the `quick_exit`
function, <ins>the `atomic_flag_test_and_set` functions, the `atomic_flag_clear`
functions,</ins> or the `signal` function with the first argument equal to the
signal number corresponding to the signal that caused the invocation of the
handler. Furthermore, if such a call to the `signal` function results in a
`SIG_ERR` return, the value of `errno` is indeterminate.<sup>252\)</sup>

Sublcause J.2 Undefined behavior. Page 566

Change:

A signal occurs other than as the result of calling the `abort` or `raise`
function, and the signal handler refers to an object with static or thread
storage duration that is not a lock-free atomic object other than by assigning a
value to an object declared as `volatile sig_atomic_t`, or calls any function in
the standard library other than the `abort` function, the `_Exit` function, the
`quick_exit` function, or the `signal` function (for the same signal number)
(7.14.1.1).

to:

A signal occurs other than as the result of calling the `abort` or `raise`
function, and the signal handler refers to an object with static or thread
storage duration that is not a lock-free atomic object other than by assigning a
value to an object declared as `volatile sig_atomic_t`, or calls any function in
the standard library other than the `abort` function, the `_Exit` function, the
`quick_exit` function, <ins>the `atomic_flag_test_and_set` functions, the
`atomic_flag_clear` functions,</ins> or the `signal` function (for the same
signal number) (7.14.1.1).

---

Comment from WG14 on 2017-11-03:

Apr 2014 meeting

### Committee Discussion

> The Suggested Technical Corrigendum was accepted as the Proposed Technical
> Corrigendum.

Oct 2014 meeting

### Committee Discussion

> Upon further consideration, since by implication 5.1.2.3p5 allows by implication
> any of the atomic functions on lock-free atomic objects, the following revision
> to the Suggested Technical Corrigendum was substantially adopted from the new
> paper [N1887](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1887.htm)

### Proposed Technical Corrigendum (superceded)

Change subclause 7.14.1.1 paragraph 5 from:

> If the signal occurs other than as the result of calling the `abort` or `raise`
> function, the behavior is undefined if the signal handler refers to any object
> with static or thread storage duration that is not a lock-free atomic object
> other than by assigning a value to an object declared as `volatile
> sig_atomic_t`, or the signal handler calls any function in the standard library
> other than the `abort` function, the `_Exit` function, the `quick_exit`
> function, or the `signal` function with the first argument equal to the signal
> number corresponding to the signal that caused the invocation of the handler.
> Furthermore, if such a call to the `signal` function results in a `SIG_ERR`
> return, the value of `errno` is indeterminate.<sup>252\)</sup>

to:

> If the signal occurs other than as the result of calling the `abort` or `raise`
> function, the behavior is undefined if the signal handler refers to any object
> with static or thread storage duration that is not a lock-free atomic object
> other than by assigning a value to an object declared as `volatile
> sig_atomic_t`, or the signal handler calls any function in the standard library
> other than
>
> * the `abort` function,
> * the `_Exit` function,
> * the `quick_exit` function,
> * the atomic functions from `stdatomic.h`, when the atomic arguments are
>   lock-free,
> * the `atomic_is_lock_free` function with any atomic argument,
> * or the `signal` function with the first argument equal to the signal number
>   corresponding to the signal that caused the invocation of the handler.
>   Furthermore, if such a call to the `signal` function results in a `SIG_ERR`
>   return, the value of `errno` is indeterminate.<sup>252</sup><sup>)</sup>

In subclause J.2 Undefined behavior, change:

> A signal occurs other than as the result of calling the `abort` or `raise`
> function, and the signal handler refers to an object with static or thread
> storage duration that is not a lock-free atomic object other than by assigning a
> value to an object declared as `volatile sig_atomic_t`, or calls any function in
> the standard library other than the `abort` function, the `_Exit` function, the
> `quick_exit` function, or the `signal` function (for the same signal number)
> (7.14.1.1).

to:

> A signal occurs other than as the result of calling the `abort` or `raise`
> function, and the signal handler refers to an object with static or thread
> storage duration that is not a lock-free atomic object other than by assigning a
> value to an object declared as `volatile sig_atomic_t`, or calls any function in
> the standard library other than the `abort` function, the `_Exit` function, the
> `quick_exit` function, the atomic functions from `stdatomic.h` (when the atomic
> arguments are lock-free) , the `atomic_is_lock_free` function with any atomic
> argument, or the `signal` function (for the same signal number) (7.14.1.1).

Apr 2015 meeting

### Committee Discussion

> The committee noted that `atomic_init` was not safe to call. It was decided that
> the best place to say this was in the `atomic_init` description as a pattern to
> follow for future possible additions. As such, the following revised Proposed
> Technical Corrigendum was provided and accepted.

### Proposed Technical Corrigendum

Change subclause 7.14.1.1 paragraph 5 from:

> If the signal occurs other than as the result of calling the **abort** or
> **raise** function, the behavior is undefined if the signal handler refers to
> any object with static or thread storage duration that is not a lock-free atomic
> object other than by assigning a value to an object declared as **volatile
> sig\_atomic\_t**, or the signal handler calls any function in the standard
> library other than the **abort** function, the **\_Exit** function, the
> **quick\_exit** function, or the signal function with the first argument equal
> to the signal number corresponding to the signal that caused the invocation of
> the handler. Furthermore, if such a call to the signal function results in a
> SIG\_ERR return, the value of errno is indeterminate.<sup>252</sup>

to

> If the signal occurs other than as the result of calling the **abort** or
> **raise** function, the behavior is undefined if the signal handler refers to
> any object with static or thread storage duration that is not a lock-free atomic
> object other than by assigning a value to an object declared as **volatile
> sig\_atomic\_t**, or the signal handler calls any function in the standard
> library other than
>
> * the **abort** function,
> * the **\_Exit** function,
> * the **quick\_exit** function,
> * the functions in **\<stdatomic.h\>** (except where explicitly stated otherwise) when the atomic arguments are lock-free,
> * the **atomic\_is\_lock\_free** function with any atomic argument, or
> * the **signal** function with the first argument equal to the signal number corresponding to the signal that caused the invocation of the handler. Furthermore, if such a call to the **signal** function results in a **SIG\_ERR** return, the value of errno is indeterminate.<sup>252</sup>

Add a new paragraph after 7.17.2.2 paragraph 3:

> If a signal occurs other than as the result of calling the **abort** or
> **raise** function, the behavior is undefined if the signal handler calls the
> **atomic\_init** generic function.

In subclause J.2 Undefined behavior, change:

> A signal occurs other than as the result of calling the **abort** or **raise**
> function, and the signal handler refers to an object with static or thread
> storage duration that is not a lock-free atomic object other than by assigning a
> value to an object declared as **volatile sig\_atomic\_t**, or calls any
> function in the standard library other than the **abort** function, the
> **\_Exit** function, the **quick\_exit** function, or the **signal** function
> (for the same signal number) (7.14.1.1).

to

> A signal occurs other than as the result of calling the **abort** or **raise**
> function, and the signal handler refers to an object with static or thread
> storage duration that is not a lock-free atomic object other than by assigning a
> value to an object declared as **volatile sig\_atomic\_t**, or calls any
> function in the standard library other than the **abort** function, the
> **\_Exit** function, the **quick\_exit** function, the functions in
> **\<stdatomic.h\>** (except where explicitly stated otherwise) when the atomic
> arguments are lock-free, the **atomic\_is\_lock\_free** function with any atomic
> argument, or the **signal** function (for the same signal number) (7.14.1.1).
