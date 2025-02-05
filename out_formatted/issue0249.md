## Issue 0249: Lacuna applying C89:TC1 to C99

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_249.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_249.htm)

### Problem

Defect Report 009 made a change to the text concerning function declarators.
This text seems not have made it into C99, even though the issue remains valid.
The change should be reinstated.

### Suggested Technical Corrigendum

Change 6.7.5.3#11 to:

> \[#11\] If, in a parameter declaration, an identifier can be treated as a
> typedef name or as a parameter name, it shall be taken as a typedef name.

---

Comment from WG14 on 2002-03-06:

### Technical Corrigendum

Change 6.7.5.3#11 to:

> If, in a parameter declaration, an identifier can be treated as a typedef name
> or as a parameter name, it shall be taken as a typedef name.
