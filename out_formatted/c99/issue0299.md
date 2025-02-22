## Issue 0299: Is `cabs()` a type-generic macro?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred Tydeman (USA)  
Date: 2004-08-13  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_299.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_299.htm)

### Summary

The standard is not clear as to which type-generic macro(s) should be used to
compute the absolute value of real, complex, and imaginary types.

### Details

Here are two viewpoints.

1\) `cabs()` is not a type-generic macro. Instead `fabs()` covers `fabsf()`,
`fabs()`, `fabsl()`, `cabsf()`, `cabs()`, and `cabsl()`.

If this viewpoint is correct, then 7.22p2 may need to be updated along the lines
of "except `modf` and `cabs`". Also, in 7.22p7 (3rd line from end), `cabs(fc)`
should be changed to `fabs(fc)`.

2\) `cabs()` is a type-generic macro (but only for complex arguments). That is
`cabs()` covers `cabsf()`, `cabs()`, and `cabsl()`. In addition, `fabs()` covers
`fabsf()`, `fabs()`, `fabsl()`, `cabsf()`, `cabs()`, and `cabsl()`.

If this viewpoint is correct, then 7.22p6 needs to be updated with `cabs`. Also,
B.21 needs to have `cabs` added to it.

It seems clear that `cabs()` is not a type-generic macro.

In addition, it is not clear what `modf` is in 7.22p5.

### Suggested Technical Corrigendum

7.22p5 Add ", except `modf`" after "`<math.h>`"

7.22p7 (3rd line from end), `cabs(fc)` should be changed to `fabs(fc)`.

---

Comment from WG14 on 2006-04-04:

### Committee Discussion

7.22p2 says that every function in `<math.h>` and `<complex.h>` without an `l`
or `f` suffix has a corresponding type-generic macro. Except `modf`.

However, 7.22p2 says nothing about what the macro is *called*.

7.22p4 says that if there is a function F() in `<math.h>` and a corresponding
function cF() in `<complex.h>`, then the TG-macro for both F() and cF() is
called "F". In addition, the TG-macro for both `fabs()` and `cabs()` is called
"`fabs`".

7.22p5 and 7.22p6 say that for all remaining functions that have TG-macros, the
macro has the same name as the function.

However, none of 7.22p4 to 7.22p6 say which functions have TG-macros.

Adding "except `cabs`" to 7.22p2 would directly contradict 7.22p4, because it
says that there is *no* TG-macro corresponding to `cabs` (and, therefore,
`fabs`).

If there's a defect in the wording, it's that 7.22p5 should say "except modf"
after "`<math.h>`". Or all of 7.22p4 to 7.22p6 should have something like "Where
a function has a corresponding type-generic macro" inserted in them. But we
don't even believe that is necessary.

To get the absolute value of a `float complex` using a type-generic macro, use
`fabs`. Therefore, 7.22p7 (3rd line from end) needs to change `cabs(fc)` to
`fabs(fc)`.

As G.7p1 correctly shows, to take the absolute value of an imaginary type, use
`fabs`.

### Technical Corrigendum

7.22p5 Add ", except `modf`" after "`<math.h>`"

7.22p7 (3rd line from end), `cabs(fc)` should be changed to `fabs(fc)`.
