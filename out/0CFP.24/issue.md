### Summary

The TS 18661-1 specification for remainder in F.10.7.2, says

—             **remainder(***x***,** ±∞**)** returns *x* for *x* not infinite.

For *x* a (quiet) NaN, this specification appears to require that the same NaN
be returned. This unintentionally goes beyond IEC 60559 whose general
specification for NaNs requires only that some (quiet) NaN be returned. The
suggested TC below uses similar words to IEC 60559’s, which allows the general
specification for NaNs to apply.

### Suggested Technical Corrigendum

In TS 18661-1 clause 12, for C F.10.7.2, change the third bullet from:

—             **remainder(***x***,** ±∞**)** returns *x* for *x* not infinite.

to:

—             **remainder(***x***,** ±∞**)** returns *x* for finite *x*.
