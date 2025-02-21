## Issue 0EMB.06: fp arithmetic support functions do not specify what happens if an integer result overflows

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208), [210](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/210)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: 7.18a.6.1 (fp arithmetic support functions) does not specify what
happens if an integer result overflows.

Proposed solution: Isn't there a blanket statement to the effect that when a
specified result is not representable in the type, the behavior is undefined? If
not, there should be.

---

Comment from WG14 on 2004-11-15:

Problem: The replacement text for 7.18a.6.1 (on fixed-point arithmetic support
functions) does not specify what happens if an integer result overflows.

Solution: Undefined behavior is implied by default in the C standard. Mention in
the descriptive text that this should result in undefined behavior.

Change: In 4.1.6.2.1 para 5, add the following sentence to the end of the
paragraph: If an integer result of one of these functions overflows, the
behavior is undefined.
