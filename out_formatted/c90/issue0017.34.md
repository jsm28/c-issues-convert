## Issue 0017.34: Is `strtok` described properly?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Calls to `strtok`

In subclause 7.11.5.8 on page 167, line 36, “... first call ...” should read
“... all calls ...”

I think that the current wording causes confusion. The first call is the one
that takes a non-`NULL` “`s1`” parameter. However, the discussion from line 36
onwards is describing the behavior for all calls.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee felt that the suggested wording for the `strtok` function
description is not an improvement. The existing wording is clear as written.
