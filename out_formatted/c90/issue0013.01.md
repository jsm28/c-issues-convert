## Issue 0013.01: How does one form the composite type of mixed array and pointer parameter types?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0017.15](../c90/issue0017.15.md), [0040.01](../c90/issue0040.01.md), [0110](../c90/issue0110.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

Compatible and composite function types

A fix to both problems Mr. Jones raises in X3J11 Document Number 90-006 is: In
subclause 6.5.4.3 on page 68, lines 23-25, change the two occurrences of “its
type for these comparisons” to “its type for compatibility comparisons, and for
determining a composite type.” This change makes the sentences pretty awkward,
but I think they remain readable.

This change makes all three of Mr. Jones's declarations compatible:

```c
int f(int a[4]);
 int f(int a[5]);
 int f(int *a);
```

This should be the case; it is consistent with the base document's idea of
“rewriting” the parameter type from array to pointer.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.4.3, page 68, lines 22-25, change:***

(For each parameter declared with function or array type, its type for these
comparisons is the one that results from conversion to a pointer type, as in
6.7.1. For each parameter declared with qualified type, its type for these
comparisons is the unqualified version of its declared type.)

***to:***

(In the determination of type compatibility and of a composite type, each
parameter declared with function or array type is taken as having the type that
results from conversion to a pointer type, as in 6.7.1, and each parameter
declared with qualified type is taken as having the unqualified version of its
declared type.)
