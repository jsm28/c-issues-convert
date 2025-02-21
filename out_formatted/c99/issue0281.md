## Issue 0281: CLOCKS\_PER\_SEC should not be a constant expression

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Convener, J. Benito (convener)  
Date: 2002-06-06  
Reference document: [ISO/IEC WG14 N982](https://www.open-std.org/jtc1/sc22/wg14/www/docs/)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_281.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_281.htm)

### Summary

In 7.23.1 Components of time, `CLOCKS_PER_SEC` is defined as a macro which
expands to a constant expression with type `clock_t`. `CLOCKS_PER_SEC` need not
be a compile time constant expression, but should be a runtime constant. A value
that is unchanged during program execution.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2003-03-06:

### Technical Corrigendum

In 7.23.1 Components of time, remove the word "constant" in the 2<sup>nd</sup>
paragraph.
