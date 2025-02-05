This Defect Report requests a clarification regarding the valid interpretations
of the `abort` function, especially when the implementation must also match the
requirements of POSIX.1 (ISO/IEC 9945-1:1990).

The C Standard states (subclause 7.10.4.1, page 155):

> The `abort` function causes abnormal termination to occur, unless the signal
> `SIGABRT` is being caught and the signal handler does not return. Whether open
> output streams are flushed or open streams closed or temporary files removed is
> implementation-dependent. An implementation-defined form of the status
> *unsuccessful termination* is returned to the host environment by means of the
> function call `raise(SIGABRT)`.

and (subclause 7.10.4.3, page 156):

> The `exit` function causes normal program termination to occur.

and (subclause 7.10.4.1, page 101 \[Rationale\]):

> The Committee vacillated over whether a call to `abort` should return if the
> signal `SIGABRT` is caught or ignored. To minimize astonishment, the final
> decision was that `abort` never returns.

The POSIX.1 Standard states (subclause 3.2, page 46):

> There are two kinds of process termination:
>
> (1) Normal termination occurs by a return from `main()` or when requested with
> the `exit()` or `_exit()` functions.
>
> (2) Abnormal termination occurs when requested by the `abort()` function or when
> some signals are received (see 3.3.1).
>
> The `exit()` and `abort()` functions shall be as described in the C Standard
> {2}. Both `exit()` and `abort()` shall terminate a process with the consequences
> specified in 3.2.2, except that the status made available to `wait()` or
> `waitpid()` by `abort()` shall be that of a process terminated by the `SIGABRT`
> signal.

and (subclause 8.2.3.12, page 161):

> The `exit()` function shall have the effect of `fclose()` ... as described
> above. The `abort()` function shall also have these effects if the call to
> `abort()` causes process termination, but shall have no effect on streams
> otherwise. The C Standard {2} specifies the conditions where `abort()` does or
> does not cause process termination. For the purposes of that specification, a
> signal that is blocked shall not be considered caught.

and (subclause B.8.2.3.12, page 291 \[Rationale\]):

> POSIX.1 intends that processing related to the `abort()` function will occur
> unless “the signal `SIGABRT` is being caught, and the signal handler does not
> return,” as defined by the C Standard {2}. This processing includes at least the
> effect of `fclose()` on all open streams, and the default actions defined for
> `SIGABRT`.
>
> The `abort()` function will override blocking or ignoring the `SIGABRT` signal.
> Catching the signal is intended to provide the application writer with a
> portable means to abort processing, free from possible interference from any
> implementation-provided library functions.
>
> Note that the term “program termination” in the C Standard {2} is equivalent to
> “process termination” in POSIX.1.

The above quotes make it clear that the POSIX.1 Standard intends to have the
abort function implementation be roughly the following:

1. Inquire about `SIGABRT` handling.
2. If currently blocked, unblock `SIGABRT`.
3. If currently `SIG_IGN`, reset `SIGABRT` to `SIG_DFL`.
4. If currently `SIG_DFL`, flush all open output streams.
5. `raise(SIGABRT)`.
6. Reset `SIGABRT` to `SIG_DFL` (handler must have returned).
7. Go to step 5\.

As far as the C Standard is concerned, step 2 is outside its scope, so it can be
part of a valid implementation. (The effects cannot be noticed by a strictly
conforming program.) Step 4 is clearly permitted as well. It is step 3 and the
loop that are the key of this Defect Report. (Note that step 3 could have been
skipped above as it would be handled by the 5-6-7 loop, but I've left it
explicit for clarity.)

The special case in the C Standard regarding `SIGABRT` handlers that don't
return is intended to keep the implementation straightforward. (It is, in
general, difficult to determine whether a handler will return without calling
it!) The POSIX.1 Standard has understood the C Standard to require, in effect,
an implementation to force an uncaught `SIGABRT` to terminate the program. But,
is this actually the C Standard's intent? The Rationale quote can certainly be
taken to indicate that catching and ignoring `SIGABRT` are in the same category.

Does the C Standard either permit or require an implementation to reset an
ignored `SIGABRT` to `SIG_DFL`? Or, does the C Standard permit or require a call
similar to `exit(EXIT_FAILURE)`? Is the distinction between abnormal termination
and unsuccessful normal termination beyond the scope of the C Standard? (After
all, how can it be tested?) And, finally, can a portable application find any
utility in setting `SIGABRT` to `SIG_IGN`?
