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
