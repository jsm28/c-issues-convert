### Summary

This is about an issue raised by Joseph Myers in SC22WG14.14450:

> The specification for `setpayload` (and likewise `setpayloadsig`) says "If `pl`
> is not a positive floating-point integer representing a valid payload, `*res` is
> set to positive zero."
> 
> Does "positive" as applied to "floating-point integer" here mean "with sign bit
> 0" (the list of definitions in IEEE 754 doesn't include "positive")?  In the
> preferred encodings for binary interchange formats, 0 is a valid payload for
> quiet NaNs.  So should \+0.0 as an argument to `setpayload` result in a quiet
> NaN with payload 0, while -0.0 results in `*res` being set to \+0.0 because -0.0
> isn't positive (and for `setpayloadsig`, both result in `*res` set to \+0.0
> because a payload for a signaling NaN has to be nonzero to avoid all mantissa
> bits being zero)?

A “positive floating-point integer” is a positive integer in the floating-point
format, hence it is greater than zero. So, the current specification for
`setpayload` and `setpayloadsig` is flawed in that it doesn’t allow setting the
payload to zero.

A more basic problem is that TS 18661-1 assumes IEC 60559 interprets payloads as
integers. This is true for decimal formats. IEC 60559 says:

> The payload corresponds to the significand of finite numbers, interpreted as
> an integer with a maximum value of 10^(3×J)−1, …

The significand c interpreted as an integer is assumed throughout to be
non-negative, while the *s* field in (*s*, *q*, *c*) provides the sign. For
decimal, interpreting the bits in the encodings allows the two encoding schemes
to have the same payloads and the payloads to fit conceptually with their
encoding schemes.

However, for binary formats, IEC 60559 says:

> For binary formats, the payload is encoded in the *p*−2 least significant bits
> of the trailing significand field.

Nowhere does it actually interpret the payload for binary formats as an integer.

However, the payload for binary formats has a natural interpretation as an
unsigned integer, so it is reasonable for TS 1866-1 to interpret payloads (for
binary and decimal formats) as such.

The suggested Technical Corrigendum below addresses these problems.

### Suggested Technical Corrigendum

In 14.10, replace the first sentence:

> IEC 60559 defines the payload of a NaN to be a certain part of the NaN’s
> significand interpreted as an integer.

with:

> IEC 60559 defines the payload of a NaN to be a certain part of the NaN’s
> significand. The payload can be interpreted as an unsigned integer.

In 14.10, in the new C subclause F.10.13, replace:

> IEC 60559 defines the *payload* of a quiet or signaling NaN as an integer value
> encoded in the significand.

with:

> IEC 60559 defines the *payload* of a quiet or signaling NaN as information
> encoded in part of the NaN significand. The payload can be interpreted as an
> unsigned integer.

In 14.10, in the new C subclauses F.10.13.2#2 and F.10.13.3#2, change:

> If `pl` is not a positive floating-point integer representing a valid payload,
> `*res` is set to positive zero.

to:

> If `pl` is not a floating-point integer representing a valid payload, `*res` is
> set to positive zero.
