Description: the rounding functions in 7.18a.6.3 require that

> Fractional bits beyond the rounding point are set to zero in the result.

This should not apply when saturation has occurred.

Proposed solution: replace the offending text by:

> When saturation has not occurred, fractional bits beyond the rounding point are
> set to zero in the result.
