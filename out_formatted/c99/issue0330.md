## Issue 0330: Externally visible exceptional conditions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred J. Tydeman, J11  
Date: 2006-07-18  
Reference document: [N1183](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1183.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_330.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_330.htm)

### Summary

C99 7.12.1 Treatment of error conditions paragraph 1 has: Each function shall
execute as if it were a single operation without generating any externally
visible exceptional conditions.

As written, I believe that means that `errno` cannot be altered by any math
function, nor can any of the floating-point exceptions mentioned later in 7.12.1
("invalid", "divide-by-zero", "overflow", "underflow") be raised by any math
function.

That was not our intent.

Seems to me that there are two problems with that text in 7.12.1:

* It should include the word "spurious".
* It should explicitly exclude the "inexact" floating-point exception.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2007-10-30:

### Committee Discussion

In the Rationale, please add to section 6.5 Expressions, as a new paragraph,
words along the lines of:

> The "inexact" floating-point exception is NOT an exceptional condition because
> "inexact" arises from computing a mathematically defined value in the range of
> representable values, therefore, from the definition, "inexact" is not
> exceptional. This matters for spurious exceptional conditions in the math
> library (7.12.1).

### Proposed Technical Corrigendum

Change 7.12.1 paragraph 1 last sentence to:

> Each function shall execute as if it were a single operation without generating
> any of the exceptions "invalid", "divide-by-zero", or "overflow" except to
> reflect the result of the function.
