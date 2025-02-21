## Issue 0034.02: If so, can one then write conflicting declarations in disjoint scopes?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Stephen D. Clamage, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-038  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_034.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_034.html)

If no size information is known in the outer scope, then consider the following
example:

```c
extern int a[];
 int f() {
 extern int a[10];
 ...
 }
 int g() {
 extern int a[20]; /* error? */
 ...
 }
```

Is this legal? If not, does it violate a constraint?

---

Comment from WG14 on 1997-09-23:

### Response

The example exhibits undefined behavior. It does not violate a constraint.
Subclause 6.1.2.2, page 21, lines 10-13 describe “same object;” subclause
6.1.2.6, page 25, lines 9-10 require that “All declarations that refer to the
same object or function shall have compatible type; otherwise, the behavior is
undefined.”
