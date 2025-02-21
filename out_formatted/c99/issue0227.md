## Issue 0227: `strftime %U`, `%V`, and `%W` conversion specifiers

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Bill Plauger (US)  
Date: 2000-04-10  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_227.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_227.htm)

### Summary

In `<time.h>`, `strftime` conversion specifiers `%U`, `%W`, and `%V` do not need
`tm_year`.

---

Comment from WG14 on 2001-09-18:

### Committee Response

The Standard is correct. `tm_year` is provided in the case `%U` and `%W`, to
give freedom to choose the implementation (the output can be determinded using
either `tm_year` or `tm_wday`, along with `tm_yday`). For `%V` it is definitely
required as the computation cannot be made without `tm_year`.
