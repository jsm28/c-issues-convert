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
