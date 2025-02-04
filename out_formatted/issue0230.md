## Issue 0230: Enumerated type rank

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek Jones (UK)  
Date: 2000-04-11  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_230.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_230.htm)

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

---

Comment from WG14 on 2001-01-29:

### Committee Discussion

Integer conversion rank does not address `enums` that rank equal to `int`.

The words "or equal to" should be added, but there is another issue regarding
`enum` and whether or not it can ever be greater in rank than `int` (or
`unsigned int`) since the *constant-expressions* for the initializers are
constrained to the range of values that may be expressed by an `int`. The words
of the simple proposed change are good. The more general proposal doesn't seem
to fix anything else.

### Technical Corrigendum

In 6.3.1.1 paragraph 2, change the first bullet to:

> An object or expression with an integer type whose integer conversion rank is
> less than or equal to the rank of `int` and `unsigned int`.
