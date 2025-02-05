It has been suggested that the six macros `SIGABRT`, `SIGFPE`, `SIGILL`,
`SIGINT`, `SIGSEGV`, and `SIGTERM` must have distinct values. Here is the
relevant portion of subclause 7.7:

> “The macros defined are
>
> ```c
> SIG_DFL
>                 SIG_ERR
>                 SIG_IGN
> ```
>
> which expand to constant expressions with distinct values that have type
> compatible with the second argument to and the return value of the `signal`
> function, and whose value compares unequal to the address of any declarable
> function; and the following, each of which expands to a positive integral
> constant expression that is the signal number corresponding to the specified
> condition:
>
> ...
>
> An implementation need not generate any of these signals, except as a result of
> explicit calls to the `raise` function.”

On the one hand, the reference to “the signal number corresponding to the
specified condition” might be assumed to imply different numbers for each
signal. On the other hand, the words “distinct values” were explicitly used for
the three `SIG_*` macros and are conspicuously missing for the others.

Also, I think it's worth noting that the standard expects `raise` to work
meaningfully (i.e. to be able to tell them apart).

Summary: must `SIGABRT`, `SIGFPE`, `SIGILL`, `SIGINT`, `SIGSEGV`, and `SIGTERM`
have distinct values?
