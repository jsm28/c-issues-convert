## Issue 0EMB.10: The relationship beween named-registers and external object definitions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208), [210](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/210)  
Submitted against: Embedded C TR 18037:2004  
Status: Closed  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the relationship beween named-registers and 6.9.2 (external object
definitions) need to specified: when there is no initializer in the
named-register declaration, the declaration is not an external definition for
the identifier. The declaration is however also not a tentative definition,
because it has a storage-class specifier. Then, what is it?

Proposed solution: That's one problem with using existing syntactic categories
for new facilities. A workaround would be to change storage-class-specifier to
storage-class- specifier\|whatever in the grammar, where "whatever" is some new
category, and then adjust the text that constrains storage-class-specifier to
say the right thing (just storage-class-specifier or
storage-class-specifier\|whatever, depending). Then the construct would not have
a storage-class-specifier and thus would be a tentative definition.

---

Comment from WG14 on 2004-11-15:

After close reading during the meeting it appeared that Issue 10 of N1071 was
not a defect. The number is maintained for consistency with N1071.
