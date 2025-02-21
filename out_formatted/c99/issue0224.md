## Issue 0224: `fpclassify` return is not defined

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Bill Plauger (US)  
Date: 2000-04-10  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_224.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_224.htm)

### Summary

The standard header `<math.h>` does not define a use for `FP_INFINITE` and does
not define what the function `fpclassify` returns.

---

Comment from WG14 on 2002-03-06:

### Committee Discussion

This seems clear from a combination of 7.12.3.1 paragraph 2 and 7.12 paragraph
6\.

Don't see what Plauger's comments in regard to `FP_INFINITE` is, and didn't
consider that there is any problem.

### Technical Corrigendum

In 7.12 paragraph #6 a new term "number classification macro" should be
introduced, and the reword the first sentence to:

> The *number classification macros* are:
>
> > ```c
> > FP_INFINITE
> > FP_NAN
> > FP_NORMAL
> > FP_SUBNORMAL
> > FP_ZERO
> > ```
