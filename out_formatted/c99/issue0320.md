## Issue 0320: Scope of variably modified type

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Willem Wakker  
Date: 2005-05-02  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_320.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_320.htm)

### Summary

The first sentence of 6.7.5.2p2 seems to suggest that **any** ordinary
identifier both block scope or function prototype scope and no linkage **has** a
variably modified type. This is clearly wrong.

### Suggested Technical Corrigendum

Rewrite the first sentence of 6.7.5.2p2 to read:

> An ordinary identifier (as defined in 6.2.3) that has a variably modified type
> shall have either block scope or function prototype scope, and no linkage.

---

Comment from WG14 on 2006-04-04:

### Technical Corrigendum

Change the first sentence of 6.7.5.2p2 to:

> An ordinary identifier (as defined in 6.2.3) that has a variably modified type
> shall have either block scope and no linkage or function prototype scope.
