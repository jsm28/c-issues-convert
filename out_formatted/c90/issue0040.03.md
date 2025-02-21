## Issue 0040.03: Is an **Environmental Constraint** a constraint?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

Is an “environmental constraint” a constraint?

In subclause 7.6.1.1, page 118, lines 22-30, we have a set of environmental
constraints on where `setjmp` may occur.

Does violating these rules require a constraint error to be flagged, or is it
undefined behavior?

Some examples:

```c
i = setjmp(a);
 if (setjmp(a) == i)
 ...
```

---

Comment from WG14 on 1997-09-23:

### Response

Must an implementation diagnose violations of environmental constraints?

Answer: Diagnostics are not required for constraint violations in clause 7,
since subclause 5.1.1.3 refers to a constraint as defined in clause 3, which
applies to language elements only.
