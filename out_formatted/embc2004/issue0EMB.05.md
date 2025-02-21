## Issue 0EMB.05: Typo in new text for 6.2.6.3

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [206](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/206)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the new text for clause 6.2.6.3, 3rd para, last sentence: replace
'integer types' by 'fixed-point types' twice.

Proposed solution: obvious

---

Comment from WG14 on 2004-11-15:

Problem: The replacement text for 6.2.6.3 para 3, last sentence says 'integer
types' while it should say 'fixed-point types' (twice).

Solution: Make the change

Change: Replace the last sentence of the replacement text for 6.2.6.3 para 3
with: The width of a fixed-point type is the same but including any sign bit;
thus for unsigned fixed-point types the two values are the same, while for
signed fixed-point types the width is one greater than the precision.
