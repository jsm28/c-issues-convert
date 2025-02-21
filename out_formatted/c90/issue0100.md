## Issue 0100: Do functions return values by copying?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0001](../c90/issue0001.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_100.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_100.html)

ANSI/ISO C Defect report #rfg7:

Subclause 6.6.6.4 **The `return`** statement says:

> If the expression has a type different from that of the function in which it
> appears, it is converted as if it were assigned to an object of that type.

This is nonsensical. The type of the containing function is a function type, and
that's different from an object type. I believe that should be changed to read:

> If the expression has a type different from that of the return type of the
> function in which it appears, it is converted as if it were assigned to an
> object having the same type as the return type of the containing function.

---

Comment from WG14 on 1997-09-23:

### Response

This error was corrected in response to [Defect Report #001](../c90/issue0001.md).
