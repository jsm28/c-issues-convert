### Summary

Clause 6.3.1.1p2:

> An enumerated type may have a rank equal to that of `int`, or even greater than
> `int`.

The wording in this paragraph does not allow an object having an enumerated type
equal to that of `int` to appear wherever an object of type `int` or `unsigned
int` may appear.

### Suggested Technical Corrigendum

Changing the existing wording to:

> An object or expression with an integer type whose integer conversion rank is
> less than or equal to the rank of `int` and `unsigned int`.

solves the issue, for enumerators, at this point.

A more general solution for enumerations is to add the wording:

> An enumerated type with integer conversion rank not less than the rank of `int`
> and `unsigned int` may be used in an expression wherever the compatible signed
> or unsigned integer may be; the enumerated type is converted to the compatible
> type. These conversions are also called integer promotions.
