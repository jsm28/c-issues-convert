*This Defect Report was prepared with considerable help from Mark Brader, Clive
Feather, Ronald Guilmette, and a person whose employment conditions require
anonymity.*

DIN-003:

Can `longjmp` be used to return from a signal handler invoked other than through
`abort` or `raise`? The descriptions of `signal` and `longjmp` contradict each
other.

According to subclause 7.7.1.1 **The `signal` function**:

If the signal occurs other than as the result of calling the `abort` or `raise`
function, the behavior is undefined if the signal handler calls any function in
the standard library other than the `signal` function itself (with a first
argument of the signal number corresponding to the signal that caused the
invocation of the handler) or refers to any object with static storage duration
other than by assigning a value to a static storage duration variable of type
`volatile sig_atomic_t`.

Since `longjmp` is a function, it cannot be called.

But subclause 7.6.2.1 **The `longjmp` function**, broadly guarantees the
opposite:

As it bypasses the usual function call and return mechanisms, the `longjmp`
function shall execute correctly in contexts of interrupts, signals and any of
their associated functions.

### Suggested Technical Corrigendum:

If the intent is to allow calls to `exit` and `longjmp` from signal handlers not
invoked through calls to `raise` or `abort`, replace in subclause 7.6.2.1:

... other than the `signal` function itself ...

by:

... other than `longjmp`, `exit`, or the `signal` function itself ...

Alternatively, if the intent is to disallow calls to `longjmp` from signal
handlers not invoked through calls to `raise` or `abort`, replace in subclause
7.7.1.1:

As it bypasses the usual function call and return mechanisms, the `longjmp`
function shall execute correctly in contexts of interrupts, signals and any of
their associated functions. However, if the `longjmp` function is invoked from a
nested signal handler (that is, from a function invoked as a result of a signal
raised during the handling of another signal), the behavior is undefined.

by:

If the `longjmp` function is invoked from a nested signal handler (that is, from
a function invoked as a result of a signal raised during the handling of another
signal), the behavior is undefined.