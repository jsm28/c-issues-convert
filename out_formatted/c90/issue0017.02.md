## Issue 0017.02: Should the absence of function `main` be explicitly undefined?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Behavior if no function called `main` exists

According to subclause 5.1.2.2.1, page 6, it is implicitly undefined behavior if
the executable does not contain a function called `main`.

It ought to be explicitly undefined if no function called `main` exists in the
executable.

---

Comment from WG14 on 1997-09-23:

### Response

You are correct that it is implicitly undefined behavior if the executable does
not contain a function called `main`. This was a conscious decision of the
Committee.

There are many places in the C Standard that leave behavior implicitly
undefined. The Committee chose as a style for the C Standard not to enumerate
these places as explicitly undefined behavior. Rather, subclause 3.16, page 3,
lines 12-16 explicitly allow for implicitly undefined behavior and explicitly
give implicitly undefined behavior equal status with other forms of undefined
behavior.

### Correction

***Add to subclause G.2, page 200:***

\- A program contains no function called `main` (5.1.2.2.1).
