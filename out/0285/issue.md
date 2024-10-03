### Summary

6.3.1.2 is clear that any non-zero scalar value gets turned into 1 by a `_Bool`
conversion.

However, G.4.2 says that when an `imaginary` value is converted to a real, the
result is zero.

### Suggested Technical Corrigendum

Change G.4.2 to:

> When a value of `imaginary` type is converted to a real type other than `_Bool`,
> the result is a positive zero. See 6.3.1.2.
