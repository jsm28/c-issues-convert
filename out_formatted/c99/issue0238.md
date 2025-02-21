## Issue 0238: Decriptions of `fma()` overflow and underflow errors are missing

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman (US)  
Date: 2001-02-25  
Reference document: [ISO/IEC WG14 N943](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n943.txt)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_238.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_238.htm)

### Summary

> The description section for `fma()` needs to mention possible overflow and
> underflow errors.

### Details

> All, but one, of the math functions that can overflow have as part of their
> description, a phrase about **range error**. The one function that is missing it
> is `fma()`.
>
> All, but one, of the math functions that can underflow have as part of their
> description, a phrase about **range error**. The one function that is missing it
> is `fma()`.

### Suggested Technical Corrigendum

In 7.12.13.1 `fma` add to description:

> A range error may occur.

---

Comment from WG14 on 2003-10-23:

### Technical Corrigendum

In 7.12.13.1 `fma` add to description:

> A range error may occur.
