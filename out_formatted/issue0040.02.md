## Issue 0040.02: Is an implementation that fails to equal the value of an environmental limit conforming?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

Is an implementation that fails to equal (or exceed) the value of an
environmental limit conforming? Subclause 5.2.4 says that those in that
subclause must be equalled in a conforming implementation. There is no such
wording for the environmental limits in the Library (subclauses 7.9.2, 7.9.3,
7.9.4.4, 7.9.6.1, 7.10.2.1).

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause G.2, page 203:***

\- A call to a library function exceeds an **environmental limit** (7.9.2,
7.9.3, 7.9.4.4, 7.9.6.1, 7.10.2.1).
