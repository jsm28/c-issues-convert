## Issue 0204: `size_t` and `ptrdiff_t` as a `long long` type

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Canada C Working Group, Raymond Mak (Canada C Working Group)  
Date: 1999-09-15  
Reference document: [ISO/IEC WG14 N893](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n893.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_204.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_204.htm)

### Summary

`size_t` and `ptrdiff_t` can now be a `long long` type, which is not necessary
for hardwares that do not support 64-bit addressing. Implementors should be
encouraged to choose a type for these two that minimizes compatibility problems
to existing (32-bit) code.

### Suggested Correction

In 7.17 at the end of p2, add the following:

> **Recommended Practice**
>
> The `long long` type should be used only if no other integer types can represent
> the value range required by the implementation.

---

Comment from WG14 on 2000-11-02:

### Technical Corrigendum

Add to the end of 7.17:

> **Recommended Practice**
>
> \[#4] The types used for `size_t` and `ptrdiff_t` should not have an integer
> conversion rank greater than that of `signed long` unless the implementation
> supports objects large enough to make this necessary.
