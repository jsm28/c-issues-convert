## Issue 0296: Is `exp(INFINITY)` overflow? A range error? A divide-by-zero exception? `INFINITY` without any errors?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred Tydeman (USA)  
Date: 2004-02-10  
Reference document: [N1053](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1053.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_296.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_296.htm)

### Summary

I believe that there are some words missing from 7.12.1 Treatment of error
conditions. Currently, the words allow `exp(INFINITY)` to be considered an
overflow of the divide-by-zero type. This is wrong. An infinite result from
infinite operands is not an error; it is an exact unexceptional operation.

**Details from C99\+TC1**

Paragraph 4 in 7.12.1 Treatment of error conditions, currently has:

> A floating result overflows if the magnitude of the mathematical result is
> finite but so large that the mathematical result cannot be represented without
> extraordinary roundoff error in an object of the specified type. If a floating
> result overflows and default rounding is in effect, or if the mathematical
> result is an exact infinity (for example `log(0.0)`), then the function returns
> the value of the macro `HUGE_VAL`, `HUGE_VALF`, or ...; if the integer
> expression `math_errhandling & MATH_ERREXCEPT` is nonzero, the "divide-by-zero"
> floating-point exception is raised if the mathematical result is an exact
> infinity ...

In addition, IEEE-754 has in 6.1 Infinity Arithmetic:

> Arithmetic on INFINITY is always exact and therefor shall signal no exceptions,
> except for the invalid operations specified for INFINITY in 7.1.

The invalid operations on INFINITY in IEEE-754 are: INF-INF, 0\*INF, INF/INF,
INF REM y, sqrt(-INF).

### Suggested Technical Corrigendum

Add ", from finite arguments," as indicated below to paragraph 4 in 7.12.1
Treatment of error conditions.

> A floating result overflows if the magnitude of the mathematical result is
> finite but so large that the mathematical result cannot be represented without
> extraordinary roundoff error in an object of the specified type. If a floating
> result overflows and default rounding is in effect, or if the mathematical
> result is an exact infinity, from finite arguments, (for example `log(0.0)`),
> then the function returns the value of the macro `HUGE_VAL`, `HUGE_VALF`, or ...

In addition, add the following to the Rationale in 7.12.1:

> Operations on INFINITY are either invalid or exact. Some examples of invalid
> operations are: INF-INF, INF\*0, INF/INF, sqrt(-INF), cexp(r\+I\*INF). Some
> examples of exact operations, which also are unexceptional, are INF\+x, INF\*x,
> INF/x, sqrt(\+INF), exp(INF).

---

Comment from WG14 on 2006-04-04:

### Committee Discussion (for history only)

The following table tries to list all math functions that have an infinity for
an input or an infinity for an output, as specified by Annex F.

> Inf -\> Inf
>
> > ```c
> > acosh(+INF)
> > asinh
> > cosh
> > sinh
> > exp(+INF)
> > exp2(+INF)
> > expm1(+INF)
> > frexp
> > ldexp
> > log(+INF)
> > log10(+INF)
> > log1p(+INF)
> > log2(+INF)
> > logb
> > modf
> > scalb
> > cbrt
> > fabs
> > hypot
> > pow(x,-INF), |x| < 1
> > pow(x,+INF), |x| > 1
> > pow(-INF,y), y > 0
> > pow(+INF,y), y > 0
> > sqrt(+INF)
> > lgamma
> > tgamma(+INF)
> > ceil
> > floor
> > nearbyint
> > rint
> > round
> > trunc
> > copysign(INF,y), y is anything
> > nextafter(INF,INF)
> > nexttoward(INF,INF)
> > fdim(INF,-INF)
> > fmax(+INF,any)
> > fmin(-INF,any)
> > fma(INF,INF,INF), x*y has same sign of z
> > ```
>
> Inf -\> NaN \+ FE\_INVALID
>
> > ```c
> > acos
> > asin
> > cos
> > sin
> > tan
> > acosh(-INF)
> > atanh
> > log(-INF)
> > log10(-INF)
> > log1p(-INF)
> > log2(-INF)
> > sqrt(-INF)
> > tgamma(-INF)
> > lrint
> > llrint
> > lround
> > llround
> > fmod(INF,any)
> > remainder(INF,any)
> > remquo(INF,any)
> > fma(INF,INF,INF), x*y has opposite sign of z
> > fma(0,INF,z), z not a NaN
> > fma(x,INF,-INF), x has same sign as INF
> > ```
>
> Inf -\> finite
>
> > ```c
> > atan
> > atan2
> > tanh
> > exp(-INF)
> > exp2(-INF)
> > expm1(-INF)
> > pow(0,+INF)
> > pow(-1,INF)
> > pow(+1,INF)
> > pow(INF,0)
> > pow(x,-INF), |x| > 1
> > pow(x,+INF), |x| < 1
> > pow(-INF,y), y < 0
> > pow(+INF,y), y < 0
> > erf
> > erfc
> > fmod(x,INF), x not infinite
> > remainder(x,INF), x finite
> > remquo(x,INF), x finite
> > copysign(x,INF), x finite
> > fdim(INF,INF)
> > fmax(-INF,y), y finite
> > fmin(+INF,y), y finite
> > ```
>
> finite -\> Inf \+ `FE_DIVBYZERO`
>
> > ```c
> > atanh(+/-1)
> > log(+/-0)
> > log10(+/-0)
> > log1p(-1)
> > log2(+/-0)
> > logb(+/-0)
> > pow(0,y), y an odd integer < 0
> > pow(0,y), y < 0 and not an odd integer [and finite]
> > lgamma(x), x is negative integer or zero
> > tgamma(+/-0)
> > ```

All functions that have an exact infinity result and have an error, have finite
arguments.

### Technical Corrigendum

Add ", from finite arguments," as indicated below to paragraph 4 in 7.12.1
Treatment of error conditions.

> A floating result overflows if the magnitude of the mathematical result is
> finite but so large that the mathematical result cannot be represented without
> extraordinary roundoff error in an object of the specified type. If a floating
> result overflows and default rounding is in effect, or if the mathematical
> result is an exact infinity, from finite arguments, (for example `log(0.0)`),
> then the function returns the value of the macro `HUGE_VAL`, `HUGE_VALF`, or ...

**Rationale Change**

Add the following to 7.12.1:

> Operations on INFINITY are either invalid or exact. Some examples of invalid
> operations are: INF-INF, INF\*0, INF/INF, sqrt(-INF), cexp(r\+I\*INF). Some
> examples of exact operations, which also are unexceptional, are INF\+x, INF\*x,
> INF/x, sqrt(\+INF), exp(INF).
