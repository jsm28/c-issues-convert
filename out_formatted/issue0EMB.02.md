## Issue 0EMB.02: Order in which overflow handling and rounding is done

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the current text requires that overflow handling is done before
rounding; this is counter intuitive, and not what is done for floating-point
overflow/rounding. As it happens, the order in which overflow and rounding are
done has no effect on the result when saturation is used for overflow handling.

Hence, if we change the order, the result remains the same for saturation.
However, with the current required order, mod\_wrap as overflow handling (which
is allowed but not required) cannot (reasonably) be implemented. It is therefore
proposed to change the order.

Proposed solution: change the required order of overflow handling and rounding.

---

Comment from WG14 on 2004-11-15:

Problem: TR 18037 requires that overflow handling be done before rounding, which
causes problems for alternative overflow modes such as modular wraparound. (When
the overflow mode is saturation, the order in which rounding and overflow
handling are performed has no effect on the end-result.)

Solution: Specify that rounding should be done before overflow handling.

Changes:

* Clause 4.1.3, para 3: strike '(after any overflow handling)'.
* Replacement text for 5.2.4.2.3:
  + Replace in para 6 (staring with 'If the result type of an arithmetic operation') the text 'and then overflow handling and rounding' by 'and then rounding and overflow handling'
  + Strike from para 9 (starting with 'If (after any overflow handling)') the text '(after any overflow handling)'
