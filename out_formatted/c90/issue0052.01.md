## Issue 0052.01: Should the `mktime` example use `(time_t)-1` instead of `-1`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Paul Edwards, Project Editor (P.J. Plauger)  
Date: 1993-03-21  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_052.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_052.html)

In subclause 7.12.2.3, page 172, the example is not strictly conforming. The
`mktime` return is compared against `-1` instead of `(time_t)-1`, which could
cause a problem with a strictly conforming implementation.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.12.2.3, page 172, line 16, change:***

> ```c
> if (mktime(&time_str) == -1)
> ```

***to:***

> ```c
> if (mktime(&time_str) == (time_t)-1)
> ```
