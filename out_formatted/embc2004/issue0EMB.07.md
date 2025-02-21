## Issue 0EMB.07: Error in 7.18.a.6.3

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the rounding functions in 7.18a.6.3 require that

> Fractional bits beyond the rounding point are set to zero in the result.

This should not apply when saturation has occurred.

Proposed solution: replace the offending text by:

> When saturation has not occurred, fractional bits beyond the rounding point are
> set to zero in the result.

---

Comment from WG14 on 2004-11-15:

Problem: The description of the fixed-point rounding functions in the
replacement text for 7.18a.6.3 require that fractional bits beyond the rounding
point are set to zero in the result. This should not apply when saturation has
occurred.

Solution: Replace the text as proposed.

Change: Modify the third sentence of the description of 7.18a.6.3 to read: 'When
saturation has not occurred, fractional bits beyond the rounding point are set
to zero in the result.'
