## Issue 0244: `tgamma(zero or negative integer)` should be considered a pole error

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman (US)  
Date: 2001-02-25  
Reference document: [ISO/IEC WG14 N943](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n943.txt)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_244.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_244.htm)

### Summary

> `tgamma(zero or negative integer)`should be considered a pole error since the
> correct mathematical result is an exact infinity (whose sign depends upon the
> side that the limit is taken from). Annex F already does this for the zero
> argument case.

### Details

> When the correct mathematical result is an exact infinity (from finite
> arguments), it is considered a pole or singularity error. This is true if the
> result's sign is independent of the direction of the limit. It is believed to be
> true that it still is a pole error if the sign of the infinite result depends
> upon the direction of the limit.
>
> Some symbolic math packages support the concept of \+/-infinity in addition to
> \+infinity and -infinity, and in those, `tgamma(zero or negative integer)` is
> \+/-infinity.
>
> Since \+/-infinity cannot be represented in most (all?) floating-point formats,
> return \+infinity for that value.
>
> LIA-2 treats similar cases (math function with exact non-zero integer argument
> and a result of \+/-infinity, such as tan(90 degrees)) as a pole error with the
> result of signed infinity.
>
> <ins>Counter-argument</ins>: For `0.0` we have the luxury of `+0.0` and `-0.0`.
> Non-zero integers don't have "sides". There is no concept of \+/-infinity in IEC
> 60559 (nor any other hardware floating-point representation), just \+infinity
> and -infinity. If there is no one correct result for a given argument, then that
> case must be considered an invalid operation or a domain error. `tgamma(negative
> integer)` has two results (\+infinity or -infinity), so must be considered
> invalid. `tgamma(x)`, as `x` approaches -infinity, has no unique limit, so must
> also be considered invalid.

### Suggested Technical Corrigendum

In 7.12.8.4 `tgamma`:

Change:

> A domain error occurs if `x` is a negative integer or if the result cannot be
> represented when `x` is zero.

to

> A range error may occur if `x` is a negative integer or zero.

In F.9.5.4 `tgamma`:

Change:

> `tgamma(x)` returns a `NaN` and raises the "invalid" floating-point exception
> for `x` a negative integer.

to

> `tgamma(x)` returns `+INF` and raises the "divide-by-zero" floating-point
> exception for `x` a negative integer.

Change:

> `tgamma(-INF)` returns a `NaN` and raises the "invalid" floating-point
> exception.

to

> `tgamma(-INF)` returns `+INF` and raises the "divide-by-zero" floating-point
> exception.

---

Comment from WG14 on 2001-10-16:

### Technical Corrigendum

In 7.12.8.4 `tgamma`:

Change:

> A domain error occurs if `x` is a negative integer or if the result cannot be
> represented when `x` is zero.

to

> A domain error or range error may occur if `x` is a negative integer or zero.
