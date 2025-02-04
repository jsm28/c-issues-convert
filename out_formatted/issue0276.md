## Issue 0276: orientation of `perror`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Cross-references: [0322](issue0322.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_276.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_276.htm)

### Problem

The `perror` function (7.19.10.4) is not listed in 7.19.1 as either a byte
input/output function or a wide character output function. I believe it should
be the former.

### Suggested Technical Corrigendum

In 7.19.1#5, fourth bullet, insert `perror` after `gets`.

---

Comment from WG14 on 2002-03-07:

### Technical Corrigendum

In 7.19.1#5, fourth bullet, insert `perror` after `gets`.
