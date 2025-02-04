## Issue 0017.14: `const void` type as a parameter

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0110](issue0110.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

`const void` type as a parameter

Refer to subclause 6.5.4.3, page 67, line 37\. `f(const void)` should be
explicitly undefined; also `f(register void)`, `f(volatile void)`, and
combinations thereof.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause G.2, page 201:***

\- A storage-class specifier or type qualifier modifies the keyword `void` as a
function parameter type list (6.5.4.3).
