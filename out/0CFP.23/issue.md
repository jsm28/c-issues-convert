### Summary

The `llquantexp` functions in 12.4.1 of TS 18661-2 compute the quantum exponent
of a finite argument (of decimal floating type). Infinities and NaNs don’t have
a quantum exponent, so the description in C 7.12.11a.4 says “If `x` is infinite
or NaN, they compute `LLONG_MIN` and a domain error occurs.” In similar cases,
of a function with floating parameters and integer return type, where no return
value is suitable, the “invalid” floating-point exception is raised. Examples in
current C include `ilogb`, `lrint`, and `lround`. However, TS 18661-2 neglects
to specify raising “invalid” for `llquantexp`, which was an oversight.

For the C examples above, the specification of “invalid” is in annex F, because
the functions are not just for IEC 60559 implementations. The `llquantexp`
functions are only for decimal floating types, which C requires to be IEC 60559
conformant. Therefore, the specification for “invalid” can be in the primary
description in 7.12.

CFP has made a similar change for the `quantize` functions. This was done as an
editorial change, because it matches specification for the IEC 60559 quantize
operation, whose specification TS 18661 adopts by reference.

### Suggested Technical Corrigendum

In TS 18661-2 12.4.1, in C 7.12.11a.4#2, change the second sentence from:

> If `x` is infinite or NaN, they compute `LLONG_MIN` and a domain error occurs.

to:

> If `x` is infinite or NaN, they compute `LLONG_MIN`, the “invalid”
> floating-point exception is raised, and a domain error occurs.
