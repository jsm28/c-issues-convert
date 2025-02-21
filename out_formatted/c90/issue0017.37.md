## Issue 0017.37: What is the type of a function call?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Function result type

Refer to subclause 6.3.2.2, page 40, line 35\. The result type of a function
call is not defined.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.3.2.2, page 40, line 35, change:***

The value of the function call expression is specified in 6.6.6.4.

***to:***

If the expression that denotes the called function has type pointer to function
returning an object type, the function call expression has the same type as that
object type, and has the value determined as specified in 6.6.6.4. Otherwise,
the function call has type `void`.
