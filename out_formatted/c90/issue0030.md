## Issue 0030: May `sin(DBL_MAX)` set `errno` to `EDOM`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Pawel Molenda, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-017  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_030.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_030.html)

Reference: subclause 7.5.1 **Treatment of error conditions**, page 111, lines
14-17:

> For all functions, a *domain error* occurs if an input argument is outside the
> domain over which the mathematical function is defined. ... an implementation
> may define additional domain errors, provided that such errors are consistent
> with the mathematical definition of the function.

If `sin(DBL_MAX)` results in `errno` being set to `EDOM`, is this a violation of
the standard? If yes, what should be the result of this call?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.5.1 does not give license for an implementation to set `errno` to
`EDOM` for `sin(DBL_MAX)`. The mathematical function is defined for that
argument value. While a conforming hosted implementation must not set `errno` to
`EDOM` for this case, the standard imposes no constraint on the accuracy of the
result value.
