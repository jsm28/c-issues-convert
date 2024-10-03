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
