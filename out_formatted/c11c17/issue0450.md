## Issue 0450: `tmpnam_s` clears `s[0]` when `maxsize > RSIZE_MAX`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Martin Sebor  
Date: 2013-09-02  
Reference document: [N1752](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1752.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

> The majority of bounds checking functions are specified to set the first element
> of the destination buffer, `s[0]`, to the NUL character when a constraint
> violation occurs and the `s` pointer is non-null and the size of the buffer is
> greater than zero and less than or equal to `SIZE_MAX`.
>
> However, the `tmpnam_s` function sets `s[0]` to NUL even when `maxsize` is
> greater than `RSIZE_MAX`, making its behavior on constraint violation
> inconsistent with the rest.

#### Suggested Technical Corrigendum:

> Change paragraph 8 in the Returns section of tmpnam\_s to read:
>
> * If no suitable string can be generated, or if there is a runtime-constraint violation and `s` is not null and `maxsize` is greater than zero and not greater than `RSIZE_MAX`, the `tmpnam_s` function sets `s[0]` to the null character and returns a nonzero value.

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

> The committee agrees with the issue, and requests that the suggested technical
> corrigendum be broken into more parts for both clarity and consistency.

Apr 2014 meeting

### Committee Discussion

> The committee did not receive revised words and will again solicit them from the
> author.

Oct 2014 meeting

### Committee Discussion

> The paper [N1873](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1873.htm)
> was provided and discussed, and after several revisions the following proposal
> were approved.

### Proposed Technical Corrigendum

Change K.3.5.1.2 paragraph 8 (the Returns section of `tmpnam_s`) from:

> If no suitable string can be generated, or if there is a runtime-constraint
> violation, the `tmpnam_s` function writes a null character to `s[0]` (only if
> `s` is not null and `maxsize` is greater than zero) and returns a nonzero value.

to:

> If no suitable string can be generated, or if there is a runtime-constraint
> violation, the `tmpnam_s` function:
>
> * if `s` is not null and `maxsize` is both greater than zero and not greater than `RSIZE_MAX`, writes a null character to `s[0]`
> * returns a nonzero value.
