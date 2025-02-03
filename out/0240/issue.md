### Summary

> `lrint`, `llrint`, `lround`, `llround`, and `ilogb` need to have consistent and
> explicit descriptions when results are too big to represent in an integer type.
> Also, that case should be treated as a domain error.

### Details

> IEC 60559 requires that when a large floating-point value, an infinity, or a NaN
> is converted to an integer, and the result cannot be represented as an integer
> in the result's format, an invalid operation has occurred. This is currently
> mostly reflected in C99's Annex F. This condition corresponds to C's domain
> error.
>
> `ilogb` does not discuss (in either 7.12.6.5 or annex F) what should happen if
> the expected result cannot be represented as an **int**. It should be treated as
> a domain error (because it is an invalid operation to IEC 60559). The "correct"
> result of `ilogb(0)` is -infinity (which cannot be represented as an **int**, so
> should be treated as a domain error). `ilogb(NaN)` does not follow the normal
> convention of NaN in implies NaN out, so this unusual case needs to be
> discussed.
>
> `lrint` and `llrint` are inconsistent on how large arguments are treated between
> 7.12.9.5 (range error) and Annex F (domain error).
>
> `lround` and `llround` are inconsistent on how large arguments are treated
> between 7.12.9.7 (range error) and Annex F (domain error).

### Suggested Technical Corrigendum

In 7.12.6.5 `ilogb`:

Change:

> A range error may occur if `x` is `0`.

to

> A domain error occurs if `x` is `0`, infinite, or `NaN`.

Add:

> If the correct value is outside the range of the return type, the numeric result
> is unspecified, and a domain error occurs.

In 7.12.9.5 `lrint llrint`:

Change:

> If the rounded value is outside the range of the return type, the numeric result
> is unspecified. A range error may occur if the magnitude of `x` is too large.

to

> If the rounded value is outside the range of the return type, the numeric result
> is unspecified, and a domain error occurs.

In 7.12.9.7 `lround llround`:

Change:

> If the rounded value is outside the range of the return type, the numeric result
> is unspecified. A range error may occur if the magnitude of `x` is too large.

to

> If the rounded value is outside the range of the return type, the numeric result
> is unspecified, and a domain error occurs.
