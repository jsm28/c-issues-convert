## Issue 0EMB.11: Initialization of global named-registers

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208), [209](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/209), [210](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/210)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the current specification allows global named-registers to be
initialized:

```c
register REG_A int reg_a = 32;
```

It is however unclear when, and by whom this initialization should be done (one
could imagine that the register storage onto which the variable maps does not
really exist until some device is initialized by some user code).

Proposed solution: disallow initializers on named-register variables.

---

Comment from WG14 on 2004-11-15:

Problem: The current specification allows global named-registers to be
initialized. It is however unclear when, and by whom this initialization should
be done (one could imagine that the register storage onto which the variable
maps does not really exist until some device is initialized by some user code).

Solution: Disallow initializers on named-register variables.

Change: Add the following new constraint to section 6.7: 'A declaration
containing a named- register storage-class specifier shall not contain an
initializer.'
