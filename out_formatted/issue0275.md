## Issue 0275: bitwise-OR of nothing

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_275.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_275.htm)

### Problem

`FE_ALL_EXCEPT` is defined in 7.6#6 as:

> \[#6] The macro
>
> ```c
>             FE_ALL_EXCEPT
> ```
>
> is simply the bitwise OR of all floating-point exception macros defined by the
> implementation.

If no floating-point exception macros are defined, is `FE_ALL_EXCEPT`:

* required to be defined as zero
* required to be undefined
* unspecified whether it is either of the above ?

\[This appears to be the only case of its kind.]

### Suggested Technical Corrigendum

Append to 7.6#6:

> If no such macros are defined, `FE_ALL_EXCEPT` can either be defined as 0 or
> left undefined.

---

Comment from WG14 on 2002-05-15:

### Technical Corrigendum

Append to 7.6#6:

> If no such macros are defined, `FE_ALL_EXCEPT` shall be defined as 0\.
