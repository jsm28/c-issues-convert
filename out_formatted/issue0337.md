## Issue 0337: `stdio.h` macro definition problems

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Austin Group, Nick Stoughton (US)  
Date: 2007-02-28  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_337.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_337.htm)

### Summary

The BUFSIZ macro is introduced in 7.19.1 para 3 as

> BUFSIZ  
> which expands to an integer constant expression that is the size of the buffer
> used by the setbuf function

There is no requirement that BUFSIZ should be a non-zero, positive integer
constant expression. Such a requirement should be spelled out clearly.

The same is true for FOPEN\_MAX and FILENAME\_MAX.

### Suggested Technical Corrigendum

Change the definition of BUFSIZ to:

> BUFSIZ  
> which expands to a non-zero, positive integer constant expression that is the
> size of the buffer used by the setbuf function

Similarly,

> FOPEN\_MAX  
> which expands to a non-zero, positive integer constant expression that is the
> minimum number of files that the implementation guarantees can be open
> simultaneously;
>
> FILENAME\_MAX  
> which expands to a non-zero, positive integer constant expression that is the
> size needed for an array of char large enough to hold the longest file name
> string that the implementation guarantees can be opened;

---

Comment from WG14 on 2007-10-30:

### Committee discussion

#### Spring 2007

`FOPEN_MAX` is required to be at least 8, see 7.19.3 paragraph 13\. So
`FOPEN_MAX` does not require any additional words.

`BUFSIZ` likewise must be at least 256, see 7.19.2 paragraph 7\.

`FILENAME_MAX` 7.19.1 paragraph 3 requires that `FILENAME_MAX` must be at least
1\.

### Proposed Committee Response

All of these constants already have required minimum values that are positive,
non-zero. No changes are required.
