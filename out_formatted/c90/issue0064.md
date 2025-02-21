## Issue 0064: What is a null pointer constant?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_064.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_064.html)

Item 1 \- Null pointer constants

Consider the following translation unit:

```c
char *f1 (int i, int *pi)
        {
        *pi = i;
        return 0;
        }

 char *f2 (int i, int *pi)
        {
        return (*pi = i, 0);
        }
```

In `f1`, the `0` is a null pointer constant (subclause 6.2.2.3). Since `return`
acts as if by assignment (subclause 6.6.6.4) the function is strictly
conforming.

In `f2`, the `0` is a null pointer constant. However, a constant expression
cannot contain a comma operator (subclause 6.4), and so the expression being
returned is not a null pointer constant per se. Which of the following is the
case?

1. The property of being a null pointer constant percolates upwards through an expression, and the function `f2` is strictly conforming.
2. The property of being a null pointer constant does not percolate upwards, and the expression being notionally assigned in the `return` statement, though of value zero, is not a null pointer constant but only of type `int`, thus violating a constraint (subclause 6.3.16.1).

---

Comment from WG14 on 1997-09-23:

### Response

Function `f2` is not strictly conforming, because it violates a constraint for
simple assignment (which applies to converting the type of the `return`
expression), because the `return` expression is not a null pointer constant.
