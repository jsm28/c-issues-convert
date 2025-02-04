## Issue 0017.31: Are object sizes always in bytes?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Size in bytes

References to the size of an object in other parts of the standard specify that
size is measured in bytes. The following lines do not follow this convention:
subclause 7.10.3.1 on page 154, lines 26-27 and subclause 7.10.3.3 on page 155,
line 8\.

---

Comment from WG14 on 1997-09-23:

### Response

There are numerous places in the standard where “size in bytes” is used, and
numerous places where “size” alone is used. The Committee does not feel that any
of these places need fixing \- the meaning is everywhere clear, especially since
for `sizeof` in subclause 6.3.3.4 size is specifically mentioned in terms of
bytes.
