## Issue 0017.30: Do `fseek/fsetpos` require values from successful calls to `ftell/fgetpos`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Successful call to `ftell` or `fgetpos`

In subclause 7.9.9.2 on page 145, lines 39-40, “... a value returned by an
earlier call to the `ftell` function ...” should actually read “... a value
returned by an earlier successful call ...” Similarly for subclause 7.9.9.3.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.9.9.2, page 145, lines 39-40, change:***

a value returned by an earlier call to the `ftell` function

***to:***

a value returned by an earlier successful call to the `ftell` function

***In subclause 7.9.9.3, page 146, lines 10-11, change:***

a value obtained from an earlier call to the `fgetpos` function

***to:***

a value obtained from an earlier successful call to the `fgetpos` function
