## Issue 0044.04: Can one use `offsetof` in a strictly conforming program?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Steve M. Hoxey, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-010  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_044.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_044.html)

Assuming (b) is the correct interpretation of Question 3, if within a
translation unit at a point where an “integer constant expression” is required
to satisfy a language constraint \- such as to specify the size of a bit-field
member of a structure, the value of an enumeration constant, the size of an
array, or the value of a case constant \- does the use of the macro `offsetof`
constitute:

a. a constraint violation?

or

b. the use of undefined behavior, which renders the translation unit to be not
strictly conforming?

---

Comment from WG14 on 1997-09-23:

### Response

The response to Question 1 makes this a moot question.
