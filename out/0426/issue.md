### Summary

The tables in G.5.1 have the mathematical formulas -yv and -x/v. I believe that
they are ambiguous as they could have two meanings:

* (-y)/v and (-x)/v
* -(y/v) and -(x/v)

I believe it matters for at least these cases:

1. The two operands are different NaNs, negate flips the sign of a NaN, and the result of \* and / depends upon the sign and value of the NaN.
2. The result is a NaN from non-NaN operands, negate does not flip the sign of a NaN, while both \* and / set the sign of the result as the XOR of the signs of the operands.
3. All operands are non-NaN, the result is inexact and non-NaN, and a rounding that is not symmetric about zero is in effect.

### Suggested Technical Corrigendum
