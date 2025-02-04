## Issue 0017.32: Are `strcmp/strncmp` defined when `char` is signed?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

`char` parameters to `strcmp` and `strncmp`

Refer to subclause 7.11.4, page 164\. If `char` is signed then `char *` cannot
be interpreted as pointing to `unsigned char`. The required cast may give
undefined results. This applies to `strcmp` and `strncmp`.

---

Comment from WG14 on 1997-09-23:

### Response

`strcmp` can compare two `char` strings, even though the representation of
`char` may be signed, because subclause 7.11.4, page 164, line 7 says that the
interpretation of bytes is done as if each byte were accessed as an `unsigned
char`. We believe the standard is clear.
