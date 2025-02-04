## Issue 0139: Is an incomplete type compatible with the completed type?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1994-06-13  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Cross-references: [0059](issue0059.md), [0088](issue0088.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_139.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_139.html)

Subject: Compatibility of complete and incomplete types.

The Committee has already endorsed the concept of using incomplete types which
are completed in some translation units and left incomplete in others for
encapsulation and data hiding (cf. [Defect Report #059](issue0059.md)). However, I
can find nothing in the Standard which allows the incomplete type to be
compatible with the completed type, which causes such usage to be not strictly
conforming. I believe this to be an oversight.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.1.2.6, page 25, first paragraph, change:***

Moreover, two structure, union, or enumerated types declared in separate
translation units are compatible if they have the same number of members, the
same member names, and compatible member types; for two structures, the members
shall be in the same order; for two structures or unions, the bit-fields shall
have the same widths; for two enumerated types, the members shall have the same
values.

***to:***

Moreover, two structure, union, or enumerated types declared in separate
translation units are compatible if at least one is an incomplete type or if
they have the same number of members, the same member names, and compatible
member types; for two complete structure types, the members shall be in the same
order; for two complete structure or union types, the bit-fields shall have the
same widths; for two enumerated types, the members shall have the same values.
