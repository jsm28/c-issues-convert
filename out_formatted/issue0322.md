## Issue 0322: Problem with TC2 Change #67 (Add `perror` to the list defining byte input/output functions.)

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Donald W. Cragun \<don.cragun@sun.com\>, Cragun (US)  
Date: 2005-09-28  
Reference document: [Defect Report #276](issue0276.md)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Cross-references: [0276](issue0276.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_322.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_322.htm)

### Summary

The perror function should not set the orientation of the standard error stream
if the orientation is not already set.

**Rationale**

*ISO/IEC 9899:1990* as updated by *Amendment 1: C Integrity* did not identify
the `perror` function as a byte input/output function nor as a wide-character
input/output function. Therefore, calling `perror` was not allowed to set the
stream orientation for the standard error stream. Although no rationale was
given in the amendment for not specifying `perror` in either set of functions,
it seemed to be the appropriate behavior. We would like to be able to use
`perror` at any time when an application needs to report an error condition. If
`perror` was defined to be a byte output function or a wide-character output
function and the standard error stream's orientation had been set to the
opposite orientation, the standard requires that `perror` shall not be applied
to the stream. Furthermore, as part of aligning with Amendment 1, The Single
UNIX Specification, version 2's description of `perror` says:

> The `perror()` function does not change the orientation of the standard error
> stream.

This quote was slightly transformed as Single UNIX Specification, version 2;
IEEE Std 1003.1-1996 and IEEE Std 1003.2-1992; and ISO/IEC 9945-1:1996 and
ISO/IEC 9945-2:1993 were merged to create the common Single UNIX Specification,
version 3; IEEE Std 1003.1-2001; and ISO/IEC 9945-1, 9945-2, 9945-3, and
9945-4:2002 to be:

> The `perror()` function shall not change the orientation of the standard error
> stream.

Therefore, the change in TC2 that turned `perror` into a byte input/output
function created a conflict between the C standard and the POSIX standard.

If a fatal error arises and an application wants to use `perror` to print a
diagnostic message, it is now required to be prepared to do something like:

```c
save_errno = errno;
    or = fwide(stderr, 0);
    errno = save_errno;
    perror("error identifying string")
    freopen("", "w", stderr);
    fwide(stderr, or);
```

rather than just calling `perror`. Note that calling `freopen` with a null
pointer as its first argument did not have defined behavior in the previous C
standard and was required to give an `ENOENT` error in the previous revision of
the POSIX standard. Furthermore, if the standard error stream had been
wide-character oriented before the call to `freopen`, no application reading
that stream would know that it needed to switch input methods when the
orientation switched back to byte orientation for the diagnostic. So, not
changing orientation and just printing byte oriented diagnostic messages would
not seem to make any difference to any application that was later trying to read
bytes that had been written to the standard error stream.

If it is believed that `perror` really needs to be classified as a byte output
function, maybe it should also be specified that applications that use any
wide-character input/output functions on the standard error stream produce
undefined behavior (especially if they call `perror`).

### Suggested Technical Corrigendum

Rescind ISO/IEC 9899:1999/Cor.2:2004 change #67 which states:

> *Page 263, 7.19.6.1*  
> In paragraph 5, item 4, insert `perror` after `gets`.

---

Comment from WG14 on 2006-10-25:

### Committee Discussion (for history only)

The Committee discussed making the behavior undefined, which would allow
`perror()` to fail if the stream orientation has already been set to wide.

The proposed TC will permit (but not require) `perror` to set the orientation of
an un-oriented `stderr` to narrow, and has what C calls *undefined* behavior if
`stderr` was previously set to wide. This permits the POSIX required behavior.

### Technical Corrigendum

Rescind ISO/IEC 9899:1999/Cor.2:2004 change #67 which states:

> *Page 263, 7.19.1*  
> In paragraph 5, item 4, insert `perror` after `gets`.
