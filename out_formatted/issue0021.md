## Issue 0021: What is the result of `printf("%#.4o", 345)`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-001  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_021.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_021.html)

What is the result of: `printf("%#.4o", 345);`? Is it `0531` or is it `00531`?

Subclause 7.9.6.1, on page 132, lines 37-38 says: “For `o` conversion, it
increases the precision to force the first digit of the result to be a zero.”

Is this a conditional or an unconditional increase in the precision if the most
significant digit is not already a `0`? Which is the correct interpretation?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.9.6.1, page 132, lines 37-38, change:***

For `o` conversion, it increases the precision to force the first digit of the
result to be a zero.

***to:***

For `o` conversion, it increases the precision, if and only if necessary, to
force the first digit of the result to be a zero.
