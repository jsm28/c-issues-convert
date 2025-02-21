## Issue 0137: Is `printf("%.1f", -0.01)` required to produce `0.0` , `-0.0`, or are both acceptable?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1994-04-30  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_137.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_137.html)

Is `printf("%.1f", -0.01)` required to produce `0.0`, `-0.0`, or are both
acceptable?

Subclause 7.9.6.1 says that when the `+` flag is not specified, the result
begins with a sign only when a negative value is converted. The description of
the `f` conversion (also `e` and `E`) says that the value is rounded to the
appropriate number of digits. Is the value used to determine the sign of the
result the value before or after rounding?

---

Comment from WG14 on 1997-09-23:

### Response

As specified in subclause 7.9.6.1 for the `+` flag, a negative value is being
converted, so a minus sign is required. The intent is that the sign is
determined prior to conversion.
