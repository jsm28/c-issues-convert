### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14285:

> C11 defines `DECIMAL_DIG` as "number of decimal digits, *n*, such that any
> floating-point number in the widest supported floating type with
> *p<sub>max</sub>* radix *b* digits can be rounded to a floating-point number
> with *n* decimal digits and back again without change to the value," and then
> gives a formula.
>
> Is it OK for the value of `DECIMAL_DIG` to be larger than given by the formula?
>  Such a value would still seem to meet the textual description, though being
> suboptimal.
>
> This is an issue for implementing TS 18661-3 when that involves types wider than
> `long double`.  In C11, "real floating type" means `float`, `double` or `long
> double` (6.2.5#10) (and then those types plus the three complex types are
> defined to be the floating types).  TS 18661-3 is supposed to be compatible with
> C11, so that an implementation can conform to both simultaneously.  The
> definition of `DECIMAL_DIG` in TS 18661-3 covers all supported floating types
> and non-arithmetic encodings.  And that's not conditional on
> `__STDC_WANT_IEC_60559_TYPES_EXT__`.  So in an implementation of TS 18661-3 that
> supports `_Float128`, `DECIMAL_DIG` must be big enough for `_Float128`, even if
> `__STDC_WANT_IEC_60559_TYPES_EXT__` is not defined when `<float.h>` is included.
>  And that's only compatible with C11 (if `long double` is narrower than
> `_Float128`) if C11 allows `DECIMAL_DIG` to be larger than given by the formula.

Agreed. The current specification for `DECIMAL_DIG` in TS 18661-3 is
incompatible with C11, as explained.

The suggested Technical Corrigendum below allows `DECIMAL_DIG` to be larger than
the value of the given formula. Thus an implementation that supports a floating
type wider than `long double`, for example a wide type in TS 18661-3, could
define `DECIMAL_DIG` to be large enough for its widest type and still conform as
a C implementation without extensions.

Where `DECIMAL_DIG` is used to determine a sufficient number of digits, this
change might lead to conversions with more digits than needed and with more
digits than would have been used without the change. However, programs wishing
the minimal sufficient number of digit are better served by the type-specific
macros `FLT_DECIMAL_DIG`, etc.

We considered the alternative of changing TS 198661-3 to make `DECIMAL_DIG`
dependent on `__STDC_WANT_IEC_60559_TYPES_EXT__`.  But this could lead to errors
resulting from separately compiled parts of a program using inconsistent values
of `DECIMAL_DIG`.

### Suggested Technical Corrigendum

In 5.2.4.2.2#11, change the bullet defining `DECIMAL_DIG` from:

> —      number of decimal digits, *n*, such that any floating-point number in the
> widest supported floating type with *p<sub>max</sub>* radix *b* digits can be
> rounded to a floating-point number with n decimal digits and back again without
> change to the value,
>
> > \< … formula … \>

to:

> —      number of decimal digits, *n*, such that any floating-point number in the
> widest supported floating type with *p<sub>max</sub>* radix *b* digits can be
> rounded to a floating-point number with n decimal digits and back again without
> change to the value, at least
>
> > \< … formula … \>
