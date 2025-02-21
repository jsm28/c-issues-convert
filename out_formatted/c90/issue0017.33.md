## Issue 0017.33: Are `strcmp/strncmp` defined for strings of differing length

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Different length strings

Refer to subclause 7.11.4, page 164, lines 5-7. What about strings of different
length?

Perhaps the fact that the terminating null character takes part in the
comparison ought to be mentioned.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.1.1 on page 96, lines 4-5 says that a string includes the
terminating null character. Therefore this character takes part in the
comparison. The standard is clear.
