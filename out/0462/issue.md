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
function, <u>the `atomic_flag_test_and_set` functions, the `atomic_flag_clear`
functions,</u> or the `signal` function with the first argument equal to the
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
`quick_exit` function, <u>the `atomic_flag_test_and_set` functions, the
`atomic_flag_clear` functions,</u> or the `signal` function (for the same signal
number) (7.14.1.1).
