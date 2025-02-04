## Issue 0015: How does an unsigned plain bitfield promote?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Craig Blitz, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-051  
Submitted against: C90  
Status: Closed  
Cross-references: [0122](issue0122.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_015.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_015.html)

This question concerns the promoted type of plain `int` bit-fields with length
equal to the size of an object of type `int`. I am interested in implementations
that have chosen not to regard the high-order bit as a sign bit.

The question is: What is the promoted type of such an object?

Subclause 6.5.2.1 states:

> A bit-field shall have a type that is ... `int`, `unsigned int`, or `signed
> int`.

The intent of this, I believe, is that the type of a plain `int` bit-field is
`int`.

Subclause 6.2.1.1 states:

> A `char`, a `short int`, or an `int` b it-field, or their signed or unsigned
> varieties, ... may be used in an expression wherever an `int` or `unsigned int`
> may be used. If an `int` can represent all values of the original type, the
> value is converted to an `int`; otherwise it is converted to an `unsigned
> int`...
>
> The integral promotions preserve value including sign.

Tracing this through, then, the type of any promoted plain `int` bit-field is
`int`, since `int` can hold all the values of the original type, which is `int`.
However, not all values of the bit-field, which may be regarded as non-negative,
can be represented by an `int`. By value-preserving promotion rules, I would
expect the type of the promoted bit-field to be `unsigned int`.

Can you clarify this?

---

Comment from WG14 on 1997-09-23:

### Response

As described in subclause 6.2.1.1, bit-fields that are being treated as unsigned
will promote according to the same rules as other unsigned types: if the width
is less than `int`, and `int` can hold all the values, then the promotion is to
`int`. Otherwise, promotion is to `unsigned int`.
