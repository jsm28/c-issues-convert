## Issue 0EMB.14: \[Embedded C 2004 DR#14\]

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-11-15  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: The new text for 6.5.8 (relational operators) and 6.5.9 (equality
operators) add as a constraint: 'If the two operands are pointers into different
address spaces, the address spaces must overlap.'. Such a constraint is missing
for 6.5.6 (additive operators), where it is relevant for pointer subtraction.

Solution: Add the requested constraint.

Change: Add the following constraint to 6.5.6 : 'For subtraction, if the two
operands are pointers into different address spaces, the address spaces must
overlap.'
