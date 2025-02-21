## Issue 0056: How accurate must floating-point arithmetic be?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Thomas Plum, Project Editor (P.J. Plauger)  
Date: 1993-04-15  
Submitted against: C90  
Status: Closed  
Cross-references: [0063](../c90/issue0063.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_056.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_056.html)

The following requirement is implied in several places, but not explicitly
stated. It should be explicitly affirmed, or alternative wording adopted.

The representation of floating-point values (such as floating-point constants,
the results of floating-point expressions, and floating-point values returned by
library functions) shall be accurate to one unit in the last position, as
defined in the implementation's `<float.h>` header.

Discussion: The values in `<float.h>` aren't required to document the underlying
bitwise representations. If you want to know how many bits, or bytes, a
floating-point values occupies, use `sizeof`. The `<float.h>` values document
the mathematical properties of the representation, the behaviors that the
programmer can count upon in analyzing algorithms.

It is a quality-of-implementation question as to whether the implementation
delivers accurate bits throughout the bitwise representation, or alternatively,
delivers considerably less accuracy. The point being clarified is that
`<float.h>` documents the delivered precision, not the theoretically possible
precision.

---

Comment from WG14 on 1997-09-23:

**Open Issue**
