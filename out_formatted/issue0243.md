## Issue 0243: Make the base standard and Annex F consistent for `fmod()`, `remainder()`, and `remquo()` for a zero divisor

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman (US)  
Date: 2001-02-25  
Reference document: [ISO/IEC WG14 N943](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n943.txt)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_243.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_243.htm)

### Summary

> `fmod()`, `remainder()`, and `remquo()` should be made consistent with each
> other when the divisor is zero. There are two "correct" behaviours when the
> divisor is zero: Treat it as a domain error (cannot divide by zero), or, based
> upon limits, compute a zero remainder. This series of changes may also require
> that IEEE-754 be changed (to allow a zero result in addition to the currently
> required invalid operation). Assuming that `fmod()`, `remainder()`, and
> `remquo()` should be consistent with each other, the following needs to be done.
>
> An alternative is to do some of these changes, or changes along these lines.
>
> It is assumed that requiring just the return of zero behaviour is too drastic as
> there are many millions of chips already doing the invalid operation behaviour.

### Details

> For a fixed `x`, as one takes the limit as `y` approaches zero, the remainder of
> `x`/`y` approaches zero `(0 <= |result| < |y|)` and the quotient is unspecified.
>
> IEC 60559 requires that `x` REM `y`, when `y` is zero, be an invalid operation,
> e.g., a domain error.
>
> `fmod(x,0)` is currently allowed to be either 0 or a domain error by 7.12.10.1,
> while Annex F requires it to be an invalid exception, e.g., domain error.
>
> `remainder(x,0)` is currently unspecified by 7.12.10.2, while Annex F requires
> it to be an invalid exception, e.g., domain error.
>
> `remquo(x,0)` is currently unspecified by 7.12.10.3, while Annex F requires it
> to be an invalid exception, e.g., domain error. In addition, nothing is said
> about the quotient that is stored for this case.
>
> <u>Counter-argument</u>: These functions are discontinuous along the lines `y =
> mx` or `y = (m+1/2)x` for integers **m**. We see no reason to "take the limit as
> `y` approaches zero".
>
> Allowing two different behaviours for these functions for the same arguments,
> will cause applications to be more complicated, with no real added benefit.
>
> <u>Counter-counter-argument</u>: By discontinuous, I assume you mean that they
> are like saw-tooth shaped functions, e.g., a linear rise and a vertical fall. I
> agree with that, but, as one approaches the line `y=0`, the height of the teeth
> gets smaller and smaller.

### Suggested Technical Corrigendum

In 7.12.10.1 `fmod`:

> No change needed.

In 7.12.10.2 `remainder`:

Add to Returns:

> If `y` is zero, whether a domain error occurs or the `remainder` functions
> return zero is implementation defined.

In 7.12.10.3 `remquo`:

Add to Returns:

> If `y` is zero, whether a domain error occurs or the `remquo` functions return
> zero is implementation defined.
>
> If `y` is zero, the quotient stored is unspecified.

In F.9.7.1 `fmod`:

Change

> `fmod(x,y)` returns a `NaN` and raises the "invalid" floating-point exception
> for `x` infinite or `y` zero.

to two items:

> `fmod(x,y)` returns a `NaN` and raises the "invalid" floating-point exception
> for `x` infinite.

and

> For `y` zero, `fmod(x,y)` either returns a zero (with sign of `x`), or returns a
> `NaN` and raises the "invalid" floating-point exception.

In F.9.7.2 `remainder`:

Add:

> For `y` zero, `remainder(x,y)` either returns a zero (with sign of `x`), or
> returns a `NaN` and raises the "invalid" floating-point exception.

In F.9.7.3 `remquo`:

Add:

> For `y` zero, `remquo(x,y)` either returns a zero (with sign of `x`), or returns
> a `NaN` and raises the "invalid" floating-point exception; and, in both cases,
> has an unspecified quotient stored.

Also add,

> When `remquo` returns a `NaN`, the quotient stored is unspecified.

---

Comment from WG14 on 2001-10-16:

### Technical Corrigendum

In 7.12.10.2 `remainder`:

Add to Returns:

> If `y` is zero, whether a domain error occurs or the `remainder` functions
> return zero is implementation defined.

In 7.12.10.3 `remquo`:

Add to Returns:

> If `y` is zero, whether a domain error occurs or the `remquo` functions return
> zero is implementation defined.
>
> If `y` is zero, the quotient stored is unspecified.

In J.3.12 Library functions:

Add (after fmod):

> Whether a domain error occurs or zero is returned when an `remainder` function
> has a second argument of zero (7.12.10.2).
>
> Whether a domain error occurs or zero is returned when an `remquo` function has
> a second argument of zero (7.12.10.3).
