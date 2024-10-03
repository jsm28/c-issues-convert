### Summary

What should `fprintf` do when it is printing a floating-point number using `%a`
and `%A` conversions and it is exactly representable in the given precision?
That is, what is the result of: `fprintf("%a", 1.0);`? The current wording
appears to say that it be converted into either `0x1.0p0+DBL_EPSILON` or
`0x1.0p0-DBL_EPSILON/FLT_RADIX`, instead of the correct value `0x1.0p0` (this
appears to be an oversight that forgot about exactly representable values).

What should the `strtod` family of functions do when converting a hexadecimal
form of input and the result is exactly representable? That is, what is the
result of: `strtod("0x1.0p0", (char **)NULL);`? The current wording appears to
say that it be converted into either `1.0+DBL_EPSILON` or
`1.0-DBL_EPSILON/FLT_RADIX`, instead of the correct value `1.0` (this appears to
be an oversight that forgot about exactly representable values).
