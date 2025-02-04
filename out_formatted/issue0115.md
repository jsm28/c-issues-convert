## Issue 0115: What it means to *declare* a declarator?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_115.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_115.html)

ANSI/ISO C Defect Report #rfg22:

Subject: Member declarators as declarators.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
 struct { int mbr; };   /* ? */
 union  { int mbr; };   /* ? */
```

Background:

Subclause 6.5 (**Constraints**):

> A declaration shall declare at least a declarator, a tag, or the members of an
> enumeration.

It is not entirely clear what it means to “declare” a declarator. Neither is it
clear whether or not a declarator for a member should be considered to satisfy
the constraint quoted above. (Many existing implementations behave as if member
declarators *do not* satisfy the constraint.)

---

Comment from WG14 on 1997-09-23:

### Response

The Committee agrees that the quoted constraint can be read either way. Hence, a
diagnostic is not required, but a program that uses such a form has undefined
behavior. In the case of an aggregate, the intent was to require a tag or
declarator for the aggregate itself. Thus, it is not unreasonable to issue a
diagnostic for the given example. However, since the constraint can be read
either way, an implementation could actually compile such a case though it is
marginally useful at best.
