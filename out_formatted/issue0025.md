## Issue 0025: What is meant by *representable floating-point value?*

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-005  
Submitted against: C90  
Status: Closed  
Cross-references: [0023](issue0023.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_025.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_025.html)

What is meant by “representable floating-point value?” Assume double precision,
unless stated otherwise.

First, some definitions based partially upon the floating-point model in
subclause 5.2.4.2.2, on pages 14-16 of the C Standard:

1. \+Normal Numbers: `DBL_MIN` to `DBL_MAX`, inclusive; normalized (first significand digit is non-zero), sign is \+1.
2. -Normal Numbers: `-DBL_MAX` to `-DBL_MIN`, inclusive; normalized.
3. \+Zero: All digits zero, sign is \+1; (true zero).
4. -Zero: All digits zero, sign is -1.
5. Zero: Union of \+zero and -zero.
6. \+Denormals: Exponent is “minimum” (biased exponent is zero); first significand digit is zero; sign is \+1. These are in range `+DBL_DeN` (inclusive) to `+DBL_MIN` (exclusive). (Let `DBL_DeN` be the symbol for the minimum positive denormal, so we can talk about it by name.)
7. -Denormals: same as \+denormals, except sign, and range is `-DBL_MIN` (exclusive) to `-DBL_DeN` (inclusive).
8. \+Unnormals: Biased exponent is non-zero; first significand digit is zero; sign is \+1. These overlap the range of \+normals and \+denormals.
9. -Unnormals: Same as \+unnormals, except sign; range is over -normals and -denormals.
10. \+infinity: From IEEE-754.
11. -infinity: From IEEE-754.
12. Quiet NaN (Not a Number); sign does not matter; from IEEE-754.
13. Signaling NaN; sign does not matter; from IEEE-754.
14. NaN: Union of Quiet NaN and Signaling NaN.
15. Others: Reserved (VAX?) and Indefinite (CDC/Cray?) act like NaN.

On the real number line, these symbols order as:

```c
[   1   )[   2   ](   3   ](  4 )[5](  6 )[   7   )[   8   ](   9   ]
+--------+-------+--------+------+-+------+--------+-------+--------+
-INF -DBL_MAX -DBL_MIN -DBL_Den -0 +0 +DBL_Den +DBL_MIN +DBL_MAX +INF
```

Non-real numbers are: SNaN, QNaN, and NaN; call this region 10\.

Regions 1 and 9 are overflow, 2 and 8 are normal numbers, 3 and 7 are denormal
numbers (pseudo underflow), 4 and 6 are true underflow, and 5 is zero.

So, the question is: What does “representable (double-precision) floating-point
value” mean:

a. Regions 2, 5 and 8 (\+/- normals and zero)

b. Regions 2, 3, 5, 7, and 8 (\+/- normals, denormals, and zero)

c. Regions 2 through 8 \[`-DBL_MAX` ... `+DBL_MAX`]

d. Regions 1 through 9 \[-INF ... \+INF]

e. Regions 1 through 10 (reals and non-reals)

f. What the hardware can represent

g. Something else? What?

Some things to consider in your answer follow. The questions that follow are
rhetorical and do not need answers.

Subclause 5.2.4.2.2 **Characteristics of floating types `<float.h>`**, page 14,
lines 32-34:

> The characteristics of floating types are defined in terms of a model that
> describes a representation of floating-point numbers and values that provide
> information about an implementation's floating-point arithmetic.

Same section, page 15, line 6:

> A normalized floating-point number *x* ... is defined by the following model:
> ...

That model is just normalized numbers and zero (appears to include signed
zeros). It excludes denormal and unnormal numbers, infinities, and NaNs. Are
signed zeros required, or just allowed?

Subclause 6.1.3.1 **Floating constants**, page 26, lines 32-35: “If the scaled
value is in the range of representable values (for its type) the result is
either the nearest representable value, or the larger or smaller representable
value immediately adjacent to the nearest value, chosen in an
implementation-defined manner.”

```c
A B y C x D E z F
 -DBL_Den 0.0 +DBL_Den +DBL_MIN +DBL_MAX +INF
```

The representable numbers are A, B, C, D, E, and F. The number x can be
converted to B, C, or D! But what if B is zero, C is `DBL_DeN` (denormal), and D
is `DBL_MIN` (normalized). Is x representable? It is not in the range `DBL_MIN
... DBL_MAX` and its inverse causes overflow; so those say not valid. On the
other hand, it is in the range `DBL_DeN ... DBL_MAX` and it does not cause
underflow; so those say it is valid.

What if B is zero, A is `-DBL_DeN` (denormal), and C is `+DBL_DeN` (denormal);
is y representable? If so, its nearest value is zero, and the immediately
adjacent values include a positive and a negative number. So a user-written
positive number is allowed to end up with a negative value!

What if E is `DBL_MAX` and F is infinity (on a machine that uses infinities,
IEEE-754)? Does z have a representation? If z came from 1.0/x, then z caused
overflow which says invalid. But on IEEE-754 machines, it would either be
`DBL_MAX` or infinity depending upon the rounding control, so it has a
representation and is valid.

What is “nearest?” In linear or logarithmic sense? If the number is between 0
and `DBL_DeN`, e.g.,

10<sup>-99999</sup>, it is linear-nearest to zero, but log-nearest to `DBL_DeN`.
If the number is between `DBL_MAX` and INF, e.g., 10<sup>\+99999</sup>, it is
linear- and log-nearest to `DBL_MAX`. Or is everything bigger than `DBL_MAX`
nearest to INF?

Subclause 6.2.1.3 **Floating and integral**, page 35, Footnote 29: “Thus, the
range of portable floating values is (-1,`Utype_MAX`\+1).”

Subclause 6.2.1.4 **Floating types**, page 35, lines 11-15: “When a `double` is
demoted to `float` or a `long double` to `double` or `float`, if the value being
converted is outside the range of values that can be represented, the behavior
is undefined. If the value being converted is in the range of values that can be
represented but cannot be represented exactly, the result is either the nearest
higher or nearest lower value, chosen in an implementation-defined manner.”

Subclause 6.3 **Expressions**, page 38, lines 15-17: “If an *exception* occurs
during the evaluation of an expression (that is, if the result is not
mathematically defined or not in the range of representable values for its
type), the behavior is undefined.”

```c
w = 1.0 / 0.0 ; /* infinity in IEEE-754 */
 x = 0.0 / 0.0 ; /* NaN in IEEE-754 */
 y = +0.0 ; /* plus zero */
 z = - y ; /* minus zero: Must this be -0.0? May it be +0.0? */
```

Are the above representable?

Subclause 7.5.1 **Treatment of error conditions**, page 111, lines 11-12: “The
behavior of each of these functions is defined for all representable values of
its input arguments.”

What about non-numbers? Are they representable? What is `sin(`*`NaN`*`)`? If you
got a NaN as input, then you can return NaN as output. But, is it a domain
error? Must `errno` be set to `EDOM`? The NaN already indicates an error, so
setting `errno` adds no more information. Assuming NaN is not part of Standard C
“representable,” but the hardware supports it, then using NaNs is an extension
of Standard C and setting `errno` need not be required, but is allowed. Correct?

Subclause 7.5.1 **Treatment of error conditions**, on page 111, lines 20-27
says: “Similarly, a *range error* occurs if the result of the function cannot be
represented as a `double` value. If the result overflows (the magnitude of the
result is so large that it cannot be represented in an object of the specified
type), the function returns the value of the macro `HUGE_VAL`, with the same
sign (except for the `tan` function) as the correct value of the function; the
value of the macro `ERANGE` is stored in `errno`. If the result underflows (the
magnitude of the result is so small that it cannot be represented in an object
of the specified type), the function returns zero; whether the integer
expression `errno` acquires the value of the macro `ERANGE` is
implementation-defined.”

What about denormal numbers? What is `sin(DBL_MIN/3.0L)`? Must this be
considered underflow and therefore return zero, and maybe set `errno` to
`ERANGE`? Or may it return `DBL_MIN/3.0`, a denormal number? Assuming denormals
are not part of Standard C “representable,” but the hardware supports it, then
using them is an extension of Standard C and setting `errno` need not be
required, but is allowed. Correct?

What about infinity? What is `exp(`*`INF`*`)`? If you got an INF as input, then
you can return INF as output. But, is it a range error? The output value is
representable, so that says: no error. The output value is bigger than
`DBL_MAX`, so that says: an error and set `errno` to `ERANGE`. Assuming infinity
is not part of Standard C “representable,” but the hardware supports it, then
using INFs is an extension of Standard C and setting `errno` need not be
required, but is allowed. Correct?

What about signed zeros? What is `sin(-0.0)`? Must this return -0.0? May it
return -0.0? May it return \+0.0? Signed zeros appear to be required in the
model in subclause 5.2.4.2.2 on page 15\.

What is `sqrt(-0.0)`? IEEE-754 and IEEE-854 (floating-point standards) say this
must be -0. Is -0.0 negative? Is this a domain error?

Subclause 7.9.6.1 **The `fprintf` function** on page 132, lines 32-33 says: “(It
will begin with a sign only when a negative value is converted if this flag is
not specified.)”

What is `fprintf(stdout, "%+.1f", -0.0);`? Must it be -0.0? May it be \+0.0? Is
-0.0 a negative value? The model on page 15 appears to require support for
signed zeros.

What is `fprintf(stdout, "%f %f", 1.0/0.0, 0.0/0.0);`? May it be the IEEE-854
strings of `inf` or `infinity` for the infinity and `NaN` for the quiet NaN?
Would `NaNQ` also be allowed for a quiet NaN? Would `NaNS` be allowed for a
signaling NaN? Must the sign be printed? Signs are optional in IEEE-754 and
IEEE-854. Or, must it be some decimal notation as specified by subclause
7.9.6.1, page 133, line 19? Does the locale matter?

Subclause 7.10.1.4 **The `strtod` function** on page 151, lines 2-3 says: “If
the subject sequence begins with a minus sign, the value resulting from the
conversion is negated.”

What is `strtod("-0.0", &ptr)`? Must it be -0.0? May it be \+0.0? The model on
page 15 appears to require support for signed zeros. All floating-point hardware
I know about support signed zeros at least at the load, store, and
negate/complement instruction level.

Subclause 7.10.1.4 **The `strtod` function** on page 151, lines 12-15 say: “If
the correct value is outside the range of representable values, plus or minus
`HUGE_VAL` is returned (according to the sign of the value), and the value of
the macro `ERANGE` is stored in `errno`. If the correct value would cause
underflow, zero is returned and the value of the macro `ERANGE` is stored in
`errno`.”

If `HUGE_VAL` is \+infinity, then is `strtod("1e99999", &ptr)` outside the range
of representable values, and a range error? Or is it the “nearest” of `DBL_MAX`
and INF?

---

Comment from WG14 on 1997-09-23:

### Response

Principles for C floating-point representation:

(These principles are intended to clarify the use of some terms in the standard;
they are not meant to impose additional constraints on conforming
implementations.)

1. “Value” refers to the abstract (mathematical) meaning; “representation” refers to the implementation data pattern.
2. Some (not all) values have exact representations.
3. There may be multiple exact representations for the same value; all such representations shall compare equal.
4. Exact representations of different values shall compare unequal.
5. There shall be at least one exact representation for the value zero.
6. Implementations are allowed considerable latitude in the way they represent floating-point quantities; in particular, as noted in Footnote 10 on page 14, the implementation need not exactly conform to the model given in subclause 5.2.4.2.2 for “normalized floating-point numbers.”
7. There may be minimum and/or maximum exactly-representable values; all values between and including such extrema are considered to “lie within the range of representable values.”
8. Implementations may elect to represent “infinite” values, in which case all real numbers would lie within the range of representable values.
9. For a given value, the “nearest representable value” is that exactly-representable value within the range of representable values that is closest (mathematically, using the usual Euclidean norm) to the given value.

(Points 3 and 4 are meant to apply to representations of the same floating type,
not meant for comparison between different types.)

This implies that a conforming implementation is allowed to accept a
floating-point constant of any arbitrarily large or small value.
