## Issue 0EMB.03: Typo in 4.1.6.2.1 \- Binary arithmetic operations

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [206](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/206)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: 4.1.6.2.1 (Binary arithmetic operations), last para, the text on
the divi fuctions has 'yielding a fixed-point type result'; this must be
'yielding an integer type result'.

Proposed solution: obvious

---

Comment from WG14 on 2004-11-15:

Problem: 4.1.6.2.1 (Binary arithmetic operations), last para, the text on the
divi functions has 'yielding a fixed-point type result' while the divi functions
have an integer result.

Solution: Change 'yielding a fixed-point type result'; this must be 'yielding an
integer type result'

Change: Modify 4.1.6.2.1 para 5 accordingly.
