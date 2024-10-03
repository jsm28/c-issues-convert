### Summary

The standard does not specify if or when destructors for thread specific data
keys (created with the `tss_create` function) are invoked.

This proposal suggests to align the behavior with that specified by POSIX for
`pthread_key_t`. This behavior is hoped to both match the intention of the
standard, and be possible to implement on other systems (it is noted that a
pthreads implementation exists for Windows, for example, while the behavior of
POSIX and Windows thread local storage implementations differ greatly)

### Suggested Technical Corrigendum

After 7.26.5.1p2, add

> Returning from `func` shall have the same behaviour as invoking `thrd_exit` with
> the returned value

Change 7.26.5.5 parts 2 and 3 from

> The `thrd_exit` function terminates execution of the calling thread and sets its
> result code to `res`.
> 
> The program shall terminate normally after the last thread has been terminated.
> The behavior shall be as if the program called the exit function with the
> status EXIT\_SUCCESS at thread termination time.

to

> For every thread specific storage key which was created with a non-NULL
> destructor and for which the value is non-NULL, `thrd_exit` shall set the value
> associated with the key to NULL and then invoke the destructor with its previous
> value. The order in which destructors are invoked is unspecified.
> 
> If after this process there remain keys with both non-NULL destructors and
> values, the implementation shall repeat this process up to `TSS_DTOR_ITERATIONS`
> times.
> 
> If `thrd_exit` is not being invoked in the last thread in the process, then the
> implementation shall terminate execution of the calling thread and set its
> result code to `res`. Otherwise, the implementation shall behave as
> if `exit(EXIT_SUCCESS)` was invoked.

(This change provides application writers guarantees about the identity of the
thread executing functions registered with `atexit`)

After 7.26.6.1p2, add

> The value NULL shall be associated with the newly created key in all existing
> threads. Upon thread creation, the value associated with all keys shall be
> initialized to NULL
> 
> Note that destructors associated thread specific storage are not invoked at
> process exit.

To 7.26.6.2p2, append

> If `tss_delete` is called while another thread is executing destructors, whether
> this will affect the number of invocations of the destructor associated
> with `key` on that thread is unspecified. If the thread from which `tss_delete`
> is invoked is executing destructors, then no further invocations of the
> destructor associated with `key` will occur on said thread.
> 
> Calling `tss_delete` will not result in the invocation of any destructors.

After 7.26.6.4p2, add

> This action will not invoke the destructor associated with the key on the value
> being replaced.
