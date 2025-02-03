### Summary

> IEC 60559 says very little about the setting of the inexact floating-point
> exception. C99 perhaps says a bit too much. Inexact is a condition that can
> arise when computing an expression as innocuous as 2.0/3.0, so it happens all
> the time during floating-point computations. It is thus arguably of little
> practical use. And it is rather difficult to avoid in writing math functions.
> Requiring math functions to set, or not set, inexact is thus arguably of more
> cost than benefit.
>
> What follows is a review of certain statements in the C99 Standard, with
> suggestions for making them more sensible.

7.12.9.3 promises that `nearbyint` will *not* set inexact. This is a tiresome
but not onerous requirement. It is also all that distinguishes `nearbyint` from
`rint`, so the requirement should probably be retained.

7.12.9.4 says that `rint`:

> *may* raise the inexact floating-point exception if the result differs in value
> from the argument.

This grants license to perform faster operations than are permitted `nearbyint`,
but doesn't promise to reliably set inexact. Note that it is otherwise foolish
for `rint` to set inexact, because the rounded result is *always* exactly the
expected result. It is a false analogy to match the behavior of `lrint` or
`llrint`, where the library functions are arguably mapping floating-point values
to integer values, using a recipe for making the best of matters when the
integer cannot exactly represent the original value.

Given the small distinction between `rint` and `nearbyint`, the latitude to set
inexact should probably also be retained. (It is also worth an explicit mention,
despite the general license suggested below for all math functions.)

Footnote 301 in F.4 says:

> ANSI/IEEE 854, but not IEC 60559 (ANSI/IEEE 754), directly specifies that
> floating-to-integer conversions raise the inexact floating-point exception for
> non-integer in-range values. In those cases where it matters, library functions
> can be used to effect such conversions with or without raising the inexact
> floating-point exception. See `rint`, `lrint`, `llrint`, and `nearbyint` in
> `<math.h>`.

This clearly overstates the case, suggesting as it does that rint reliably sets
inexact.

**SUGGESTION:** Remove `rint` from the list in the last sentence.

F.9, para 8 says:

> Whether or when the trigonometric, hyperbolic, base-e exponential, base-e
> logarithmic, error, and log gamma functions raise the inexact floating-point
> exception is implementation-defined. For other functions, the inexact
> floating-point exception is raised whenever the rounded result is not identical
> to the mathematical result.

Given the difficulty of avoiding inexact exceptions, and their consequential
uselessness in most cases, this license should be extended to *all* library
functions.

**SUGGESTION:** Change the above to:

> Whether or when library functions other than `nearbyint` raise the inexact
> floating-point exception is unspecified.

F.9, para 9 says:

> Whether the inexact floating-point exception can be raised when the rounded
> result actually does equal the mathematical result is implementation-defined.
> Whether the underflow (and inexact) floating-point exception can be raised when
> a result is tiny but not inexact is implementation-defined.(312) Otherwise, as
> implied by F.7.6, the `<math.h>` functions do not raise spurious floating-point
> exceptions (detectable by the user).

The first sentence is mooted by the earlier suggested change. The second
sentence (and the footnote, discussed below) doesn't go far enough. Avoiding
intermediate underflows can be as annoying, and fruitless, as avoiding
intermediate inexact reports. Library functions *should* report underflow if the
final result underflows, but they should also have the latitude not to avoid
reporting intermediate underflows.

**SUGGESTION:** Change the above to:

> Whether or when library functions raise an undeserved underflow floating-point
> exception is unspecified.(312) Otherwise, as implied by F.7.6, the `<math.h>`
> functions do not raise spurious floating-point exceptions (detectable by the
> user).

Footnote 312 says:

> It is intended that undeserved underflow and inexact floating-point exceptions
> are raised only if determining inexactness would be too costly.

**SUGGESTION:** Change the above to:

> It is intended that undeserved underflow and inexact floating-point exceptions
> are raised only if avoiding them would be too costly.

F.9, para 10 says:

> Whether the functions honor the rounding direction mode is
> implementation-defined.

This is inaccurate, since some functions (such as `rint`) are obliged to honor
the rounding direction mode.

**SUGGESTION:** Change the above to:

> Whether the functions honor the rounding direction mode is
> implementation-defined, unless explicitly specified otherwise.

F.9.6.4 says:

> The `rint` functions differ from the `nearbyint` functions only in that they do
> raise the inexact floating-point exception if the result differs in value from
> the argument.

This contradicts 7.12.9.4, which does not require `rint` to set inexact.

**SUGGESTION:** Change the above to:

> The `rint` functions differ from the `nearbyint` functions only in that they may
> raise the inexact floating-point exception if the result differs in value from
> the argument.

F9.8.3 says:

> `-nextafter(x, y)` raises the overflow and inexact floating-point exceptions for
> `x` finite and the function value infinite. `nextafter(x, y)` raises the
> underflow and inexact floating-point exceptions for the function value subnormal
> or zero and `x != y`.

This is inconsistent with the general license for reporting overflow and
underflow in J.3.1.2, which makes the setting of inexact with either of these
exceptions implementation defined. It is also inconsistent with the general
license for not reporting underflow on tiny results in J.3.6.

**SUGGESTION:** Change the above to:

> `-nextafter(x, y)` raises the overflow floating-point exception for `x` finite
> and the function value infinite. `nextafter(x, y)` raises the underflow
> floating-point exception for the function value zero and `x != y`. `nextafter(x,
> y)` may raise the underflow floating-point exception for the function value
> subnormal and `x != y`.

J.3.1.2 includes as implementation-defined behavior:

> Whether or when the trigonometric, hyperbolic, base-e exponential, base-e
> logarithmic, error, and log gamma functions raise the inexact floating-point
> exception in an IEC 60559 conformant implementation (F.9).

This should be unspecified behavior, not implementation defined.

**SUGGESTION:** Remove the above.
