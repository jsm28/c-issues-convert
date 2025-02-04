## Issue 0EMB.16: \[Embedded C 2004 DR#16]

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-11-15  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: The first sentence of 4.1.6.2.1 para 5 (' According to the rules above,
the result type of an arithmetic operation where (at least) one operand has a
fixed-point type is always a fixed- point type.') is wrong as it does not take
operands with floating-point type into account.

Solution: As it is the intention to only discuss integer types and fixed-point
types in this paragraph, change the sentence accordingly.

Change: Modify the first sentence of 4.1.6.2.1 para 5 to read: 'According to the
rules above, the result type of an arithmetic operation where one operand has a
fixed-point type and the other operand has an integer or a fixed-point type is
always a fixed-point type.'
