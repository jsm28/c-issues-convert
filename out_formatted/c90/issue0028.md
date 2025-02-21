## Issue 0028: What are the aliasing rules for dynamically allocated objects?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Randall Meyers, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-009  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_028.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_028.html)

Subclause 6.3, page 38, lines 18-27 state some very important rules governing
how a strictly conforming program can access the value of an object. The basic
theme of the rules is that an object's value may only be accessed through an
lvalue of the appropriate type. These rules are required to permit C programs to
be optimized.

The rules depend on the “declared type of the object.” This seems to make the
rules not apply if the object was not declared, which is the case for an object
allocated using `malloc()`.

Do the rules somehow apply to dynamically allocated objects? Is a compiler free
to optimize the following function:

```c
void f(int *x, double *y)
 {
 *x = 0;
 *y = 3.14;
 *x = *x + 2;
 }
```

into the equivalent function:

```c
void f(int *x, double *y)
 {
 *x = 0;
 *y = 3.14;
 *x = 2; /* *x known to be zero */
 }
```

Or must an optimizer prove that pointers are not pointing at dynamically
allocated storage before performing such optimizations?

---

Comment from WG14 on 1997-09-23:

### Response

Case 1: unions `f(&u.i, &u.d)`

Subclause 6.3.2.3, page 42, lines 5-6:

> ... if a member of a union object is accessed after a value has been stored in a
> different member of the object, the behavior is implementation-defined.

Therefore, an alias is not permitted and the optimization is allowed.

Case 2: declared objects `f((int *)&d, &d)`

Subclause 6.3, page 38, lines 18-27 list specific ways in which declared objects
can be accessed. Therefore, an alias is not permitted and the optimization is
allowed.

Case 3: any other, including `malloc`ed objects `f((int *)dp, dp)`

We must take recourse to intent. The intent is clear from the above two
citations and from Footnote 36 on page 38:

The intent of this list is to specify those circumstances in which an object may
or may not be aliased.

Therefore, this alias is not permitted and the optimization is allowed.

In summary, yes, the rules do apply to dynamically allocated objects.
