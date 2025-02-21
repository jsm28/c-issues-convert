## Issue 0285: Conversion of an `imaginary` type to `_Bool`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14 Convener  
Date: 2003-02-26  
Reference document: [ISO/IEC WG14 N1002](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1002.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Cross-references: [0447](../c11c17/issue0447.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_285.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_285.htm)

### Summary

6.3.1.2 is clear that any non-zero scalar value gets turned into 1 by a `_Bool`
conversion.

However, G.4.2 says that when an `imaginary` value is converted to a real, the
result is zero.

### Suggested Technical Corrigendum

Change G.4.2 to:

> When a value of `imaginary` type is converted to a real type other than `_Bool`,
> the result is a positive zero. See 6.3.1.2.

---

Comment from WG14 on 2004-03-17:

### Technical Corrigendum

Change G.4.2 to:

> When a value of `imaginary` type is converted to a real type other than `_Bool`,
> the result is a positive zero. See 6.3.1.2.
