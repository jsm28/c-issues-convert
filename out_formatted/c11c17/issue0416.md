## Issue 0416: `tss_t` destruction unspecified

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Owen Shepherd  
Date: 2012-08-12  
Reference document: [N1627](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1627.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Cross-references: [0424](../c11c17/issue0424.md), [0469](../c11c17/issue0469.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

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

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Committee Discussion

> * This paper was discussed in conjunction with [DR424](../c11c17/issue0424.md) which covers one additional related issue.
> * The key observation is that these papers are about the deliberate underspecification of threads, since that allows the greatest opportunity for implementation on a variety of operating systems.
> * Pete Becker, an implementor of the C11 threads library, was asked about these papers and replied in SC22/WG14 message 12813\.
> * Based on that response the committee is concerned that there could be subtleties in adopting the Proposed Technical Corrigendum and that, as such, these changes are substantial enough to warrant a proposal and to not be considered a defect.

Apr 2013 meeting

### Committee Discussion

> * A revised paper [N1687](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1687.pdf) was submitted, although not in the recommended html format.
> * The suggested technical corrigendum would specify new instances of undefined behavior as well as new requirements on implementations.
> * The committee expressed concern that some of the new requirements may be onerous or impossible to provide above the native platform implementation.

Oct 2013 meeting

### Committee Discussion

> After several papers
> [N1750,](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1750.htm)
> [N1751,](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1751.htm) revisions,
> and much discussion, the committee has agreed on the following as the
> resolution.

### Proposed Technical Corrigendum

After 7.26.5.1 paragraph 2, add

> Returning from `func` shall have the same behavior as invoking `thrd_exit` with
> the value returned from `func`.

Change 7.26.5.5, replace paragraph 2 with:

> For every thread-specific storage key which was created with a non-null
> destructor and for which the value is non-null, `thrd_exit` shall set the value
> associated with the key to `NULL` and then invoke the destructor with its
> previous value. The order in which destructors are invoked is unspecified.
>
> If after this process there remain keys with both non-null destructors and
> values, the implementation shall repeat this process up to `TSS_DTOR_ITERATIONS`
> times.
>
> Following this, the `thrd_exit` function terminates execution of the calling
> thread and sets its result code to `res`.

After 7.26.6.1 paragraph 2, add the following new paragraphs:

> The value `NULL` shall be associated with the newly created key in all existing
> threads. Upon thread creation, the value associated with all keys shall be
> initialized to `NULL`.
>
> Destructors associated with thread-specific storage are not invoked at program
> termination.
>
> A call to `tss_create` from within a destructor results in undefined behavior.

In 7.26.6.2 paragraph 2, add the following new second sentence:

> A call to `tss_delete` function results in undefined behavior if the call to
> `tss_create` which set `key` completed after the thread commenced executing
> destructors.

After 7.26.6.2 paragraph 2, add the following new paragraphs:

> If `tss_delete` is called while another thread is executing destructors, whether
> this will affect the number of invocations of the destructor associated with
> `key` on that thread is unspecified.
>
> Calling `tss_delete` will not result in the invocation of any destructors.

In 7.26.6.3 paragraph 2, add the following new second sentence:

> A call to `tss_get` function results in undefined behavior if the call to
> `tss_create` which set `key` completed after the thread commenced executing
> destructors.

In 7.26.6.4 paragraph 2, add the following new second sentence:

> A call to `tss_set` function results in undefined behavior if the call to
> `tss_create` which set `key` completed after the thread commenced executing
> destructors.

After 7.26.6.4 paragraph 2, add the following new paragraph:

> This action will not invoke the destructor associated with the key on the value
> being replaced.
