## Issue 0223: `FP_FAST_FMAF` and `FP_FAST_FMAL` should be integer constant

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Bill Plauger (US)  
Date: 2000-04-10  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_223.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_223.htm)

### Summary

In the standard header `<math.h>`, `FP_FAST_FMAF` and `FP_FAST_FMAL` should be
required to be integer constant expressions.

---

Comment from WG14 on 2000-04-18:

### Technical Corrigendum

`FP_FAST_FMAF` and `FP_FAST_FMAL` should be defined as integer constant 1\.
