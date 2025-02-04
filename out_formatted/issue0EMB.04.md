## Issue 0EMB.04: Type generic macro's

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [211](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/211)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: The type-generic macro definition sections (2.1.7.6 and 7.18a.6.7)
are incomplete and possibly wrong.

Incomplete because there are no rules on which function should be called when a
type- generic macro is called with a non fixed-point type argument. Possibly
wrong, because it is not clear what the name of the type-generic macro's should
be: 2.1.7.6 suggest to call the type-generic abs function 'absfx', in 7.18a.6.7
the 'fx' part of the name is in italic which might suggest that the name should
really be 'abs'. So, do we want to have 'abs', 'round' and 'countls', or
'absfx', 'roundfx' and 'countls'?

Proposed solution:

---

Comment from WG14 on 2004-11-15:

Problem: The type-generic macro definition sections (4.1.7.6 and 7.18a.6.7) are
incomplete and possibly wrong (see N1071 for more information)

Solution: The generic function names should be 'absfx', 'countlsfx' and
'roundfx'; 7.18a.6.7 should better explain which underlying functions are
selected.

Changes: in the replacement text for 7.18a.6.7:

* Change the type font for 'fx' from bold italic to bold (3 times)
* Add to 7.18a.6.7:
  > For each macro, use of the macro invokes the function whose corresponding real
  > type and type domain is the real type of the first generic argument. If the real
  > type of the first generic argument is not a fixed-point type, the behavior is
  > undefined.
