## Issue 0017.36: Is a function returning `const void` defined?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Qualifiers on function return type

Refer to subclause 6.6.6.4, page 80, line 24-25: “... whose return type is
`void`.”

The behavior of a type qualifier on a function return is explicitly undefined,
according to subclause 6.5.3, page 64, lines 24-25.

This creates a loophole.

An implementation that supports type qualifiers on function return types is not
required to flag the constraint given on page 80\.

---

Comment from WG14 on 1997-09-23:

### Response

A Constraint on subclause 6.7.1 says “The return type of a function shall be
`void` or an object type other than array.”
