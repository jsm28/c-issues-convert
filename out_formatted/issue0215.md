## Issue 0215: Equality operators

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 2000-04-04  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_215.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_215.htm)

### Summary

When discussing the comparison operators, 6.5.8 says:

> \[#4\] For the purposes of these operators, a pointer to an object that is not
> an element of an array behaves the same as a pointer to the first element of an
> array of length one with the type of the object as its element type.

Given that the restrictions on the arguments for pointer comparison and pointer
equality are very different, it would be advisable to repeat this wording in
6.5.9. The only wording that implies that this applies to equality operators is
the bit about "analogous" in 6.5.9#3. Since other restrictions (e.g. that the
pointers must be in the same array) do *not* apply to equality operators, it is
at best ambiguous whether this text applies. Therefore for clarity it should be
repeated.

---

Comment from WG14 on 2001-09-18:

### Technical Corrigendum

Paragraph 4 from 6.5.8 should be duplicated in the Semantics section of 6.5.9.
