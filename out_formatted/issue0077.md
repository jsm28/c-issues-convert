## Issue 0077: Is the address of an object constant throughout its lifetime?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_077.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_077.html)

Item 14 \- stability of addresses

Is the address of an object constant throughout its lifetime? For example, if a
pointer to an object is written to a binary file using `fwrite`, and then read
back later during the same run of the program using `fread`, is it guaranteed to
compare equal to the address of the original object taken again?

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard does not explicitly state that the address of an object remains
constant throughout the life of the object. That this is the intent of the
Committee can be inferred from the fact that an address constant is considered
to be a constant expression. The framers of the C Standard considered that it
was so obvious that addresses should remain constant that they neglected to
craft words to that effect.

The Committee should revisit this issue during the revision of the C Standard.
