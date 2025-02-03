### Summary:

**Consider:** `remainder( DBL_MIN*(1.0+2.0*DBL_EPSILON),
DBL_MIN*(1.0+DBL_EPSILON) )`

The result is `DBL_MIN*DBL_EPSILON`, a subnormal number. But, if the
implementation does not support subnormal numbers, such as IBM S/360 hex
floating-point, then it is either zero or `DBL_MIN`, depending upon the current
rounding direction mode. Hence, the sentence "Thus, the remainder is always
exact." in footnote 204 in C99\+TC1\+TC2
([N1124](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1124.pdf)) is wrong.
This problem also applies to `remquo` and `fmod`.

After finding that flaw, I looked at the other math functions and their
relationship to directed rounding. That search found several areas where things
could be improved and one area (`nextafter`) that took an informal request for
interpretation to the IEEE-754 committee to find the answer.

7.12.6.4 The `frexp` functions should be updated along the lines of:

> When the radix of the argument is a power of 2, the returned value is exact and
> is independent of the current rounding direction mode.

7.12.6.5 The `ilogb` functions should be updated along the lines of:

> When the returned value is representable in the range of the return type, the
> returned value is exact and is independent of the current rounding direction
> mode.

7.12.6.11 The `logb` functions should be updated along the lines of:

> The returned value is exact and is independent of the current rounding direction
> mode.

7.12.6.12 The `modf` functions should be updated along the lines of:

> The returned values are exact and are independent of the current rounding
> direction mode.

7.12.7.2 The `fabs` functions should be updated along the lines of:

> The returned value is exact and is independent of the current rounding direction
> mode.

7.12.9.1 The `ceil` functions should be updated along the lines of:

> The returned value is exact and is independent of the current rounding direction
> mode.

7.12.9.2 The `floor` functions should be updated along the lines of:

> The returned value is exact and is independent of the current rounding direction
> mode.

7.12.9.8 The `trunc` functions should be updated along the lines of:

> The returned value is exact and is independent of the current rounding direction
> mode.

7.12.10.1 The `fmod` functions should be updated along the lines of:

> When subnormal results are supported, the returned value is exact and is
> independent of the current rounding direction mode.

7.12.10.2 The `remainder` functions should be updated along the lines of:

> When subnormal results are supported, the returned value is exact and is
> independent of the current rounding direction mode.

7.12.10.3 The `remquo` functions should be updated along the lines of:

> When subnormal results are supported, the returned value is exact and is
> independent of the current rounding direction mode.

7.12.11.1 The `copysign` functions should be updated along the lines of:

> The returned value is exact and is independent of the current rounding direction
> mode.

7.12.11.2 The `nan` functions should be updated along the lines of:

> The returned value is exact and is independent of the current rounding direction
> mode.

7.12.11.3 The `nextafter` functions should be updated along the lines of:

> Even though underflow or overflow may happen, the returned value is independent
> of the current rounding direction mode.

7.12.11.4 The `nexttoward` functions should be updated along the lines of:

> Even though underflow or overflow may happen, the returned value is independent
> of the current rounding direction mode.

7.12.12.2 The `fmax` functions should be updated along the lines of:

> The returned value is exact and is independent of the current rounding direction
> mode.

7.12.12.3 The `fmin` functions should be updated along the lines of:

> The returned value is exact and is independent of the current rounding direction
> mode.

F.9.4.5 The `sqrt` functions could be updated along the lines of:

> The returned value is dependent on the current rounding direction mode.

Consider adding the following to section 7.12.1 (or make it its own section) of
the Rationale.

> There are several functions that are independent of the current rounding
> direction. Some are documented as such: `round`, `lround`, `llround`,
> `remainder` (when subnormal results are supported), `remquo` (when subnormal
> results are supported), `nextafter` (as per IEEE-754), and `nexttoward` (as per
> C99 and `nextafter`). Note, even though `nextafter` and `nexttoward` can raise
> underflow\+inexact and overflow\+inexact, they are not affected by the rounding
> direction.
>
> Some are independent because they are exact: `frexp` (when radix is power of 2),
> `logb`, `modf`, `ilogb`, `fabs`, `ceil`, `floor`, `trunc`, `fmod` (when
> subnormal results are supported), `copysign`, `nan`, `fmax`, and `fmin`.
>
> There are several functions that are dependent on the current rounding
> direction: `sqrt` (as per IEEE-754), `nearbyint`, `rint`, `lrint`, `llrint`, and
> `fma`.
>
> There are many functions (it is implementation defined as to which ones) that
> may honor the current rounding direction. First are functions that are inexact
> for most arguments: `acos`, `asin`, `atan`, `atan2`, `cos`, `sin`, `tan`,
> `acosh`, `asinh` ,`atanh`, `cosh`, `sinh`, `tanh`, `exp`, `exp2`, `expm1`,
> `frexp` (when radix is not a power of 2), `ldexp` (when radix is not 2), `log`,
> `log10`, `log1p`, `log2`, `hypot`, `pow`, `cbrt`, `erf`, `erfc`, `tgamma`,
> `lgamma`, and `fdim`.
>
> Second are functions that are exact for most arguments (but are inexact when
> they overflow or underflow): `ldexp` (when radix is 2), `scalbn`, `scalbln`,
> `fmod` (when subnormal results are not supported), `remainder` (when subnormal
> results are not supported), and `remquo` (when subnormal results are not
> supported).
