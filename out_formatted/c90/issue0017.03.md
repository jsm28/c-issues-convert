## Issue 0017.03: Does a constraint violation win over undefined behavior?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0102](../c90/issue0102.md), [0105](../c90/issue0105.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Precedence of behaviors

Refer to subclause 6.1.2.6, page 25, lines 9-10 and subclause 6.5, page 57,
lines 20-21. The constructs covered by these sentences overlap. The latter is a
constraint while the former is undefined behavior. In the overlapping case who
wins?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 5.1.1.3, page 6, lines 15-17, change:***

A conforming implementation shall produce at least one diagnostic message
(identified in an implementation-defined manner) for every translation unit that
contains a violation of any syntax rule or constraint.

***to:***

A conforming implementation shall produce at least one diagnostic message
(identified in an implementation-defined manner) for every translation unit that
contains a violation of any syntax rule or constraint, even if the behavior is
also explicitly specified as undefined or implementation-defined.

***Add to subclause 5.1.1.3, page 6:***

**Example**

An implementation shall issue a diagnostic for the translation unit:

```c
char i;
 int i;
```

because in those cases where wording in this International Standard describes
the behavior for a construct as being both a constraint error and resulting in
undefined behavior, the constraint error shall be diagnosed.
