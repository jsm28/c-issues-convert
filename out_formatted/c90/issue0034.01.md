## Issue 0034.01: Does size information evaporate when a declaration goes out of scope, even for objects with external linkage?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Stephen D. Clamage, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-038  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0011.01](../c90/issue0011.01.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_034.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_034.html)

In *The C Users Journal,* Vol. 8 No. 7, July 1990, P.J. Plauger gives the
following example on page 10:

```c
extern int a[];
 int f() {
 extern int a[10];
 ...
 }
 int sizea = sizeof a; /* error */
```

Mr. Plauger claims that the size information from the inner scope “evaporates”
when its scope ends, and the operand to the `sizeof` operator has an incomplete
type. We cannot find unequivocal support for this claim in the standard.

Subclause 6.1.2.2 says on page 21, lines 10-11:

> ... each instance of a particular identifier with *external linkage* denotes the
> same object or function.

Combining subclause 6.1.2.6 and subclause 6.5.4.2, we find that the two
declarations for `a` are compatible and we may construct a composite type. The
composite type is array of 10 `int`.

Subclause 6.1.2.6 on page 25, lines 19-20, discusses the case of two
declarations in the same scope, but does not discuss the case of two
declarations for the same object in different scopes.

But subclause 6.1.2.5 says on page 24, lines 8-9:

> An array type of unknown size is an incomplete type. It is completed, for an
> identifier of that type, by specifying the size in a later declaration (with
> internal or external linkage).

The identifier `a` appears in two declarations, and denotes the same object. The
second declaration completes the type for the identifier in the inner scope. The
two identifiers denote the same object, so it would seem reasonable to say the
type of that object is completed.

Is the size information in the inner scope lost upon leaving the scope?

---

Comment from WG14 on 1997-09-23:

### Response

Is the size information in the inner scope lost upon leaving the scope?

Answer: Yes.

See the correction in response to [Defect Report #011](../c90/issue0011.01.md).
