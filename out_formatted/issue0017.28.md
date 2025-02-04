## Issue 0017.28: Does `errno` get stored before library functions return?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Ordering of conditions on return

In subclause 7.9.9.1, subclause 7.9.9.3, and subclause 7.9.9.4, the words are
“returns ... and stores an implementation-defined positive value in `errno`.”
This is a strange order of operations \- shouldn't the wording be reversed?

---

Comment from WG14 on 1997-09-23:

### Response

No. In subclause 7.9.9.1, subclause 7.9.9.3, and subclause 7.9.9.4, the words
“returns ... and stores an implementation-defined positive value in `errno`” do
not imply any temporal ordering. There are implementations that may perform
these operations in either order and they still meet the standard.
