## Issue 0135: Is the `SVR4 fwrite` different?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Per Bothner, Project Editor (P.J. Plauger)  
Date: 1994-01-31  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_135.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_135.html)

H.J. Lu points out that the SVR4 manual explicitly says that `fwrite(ptr, 0, 1,
stream)` returns 0, not 1\. I don't know what the SVID states.

I think it is more mathematically consistent to return 1 in this case. But in
that case `fread(ptr, 0, 1, stream)` should also return 1, but ANSI explicitly
states that it should return 0\. I don't see any reason why these should be
different, so I think it is best to follow existing practice. I think the ANSI
specification for `fwrite` is a mistake; perhaps it should be fixed in the
revision.

---

Comment from WG14 on 1997-09-23:

### Response

There are no zero-length objects in C. Therefore, if the size argument to
`fwrite` is zero, it is outside the domain of the function and (by subclause
7.1.7), the result is undefined. The C Standard is not in conflict with the
cited behavior of SVR4.
