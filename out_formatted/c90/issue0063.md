## Issue 0063: This is [Defect Report 056](../c90/issue0056.md)

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Thomas Plum, Project Editor (P.J. Plauger)  
Date: 1993-12-01  
Submitted against: C90  
Status: Closed  
Cross-references: [0056](../c90/issue0056.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_063.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_063.html)

\[This is Defect Report #056, resubmitted for administrative reasons.\]

The following requirement is implied in several places, but not explicitly
stated. It should be explicitly affirmed, or alternative wording adopted.

The representation of floating-point values (such as floating-point constants,
the results of floating-point expressions, and floating-point values returned by
library functions) shall be accurate to one unit in the last position, as
defined in the implementation's `<float.h>` header.

Discussion: The values in `<float.h>` aren't required to document the underlying
bitwise representations. If you want to know how many bits, or bytes, a
floating-point values occupies, use `sizeof`. The `<float.h>` values document
the mathematical properties of the representation, the behaviors that the
programmer can count upon in analyzing algorithms.

It is a quality-of-implementation question as to whether the implementation
delivers accurate bits throughout the bitwise representation, or alternatively,
delivers considerably less accuracy. The point being clarified is that
`<float.h>` documents the delivered precision, not the theoretically possible
precision.

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard imposes no requirement on the accuracy of floating-point
arithmetic.

Further discussion:

The C Standard speaks directly to the matter of floating-point accuracy only in
one or two areas. Subclause 6.2.1.4 **Floating types**, page 35, says of
conversions from one floating type to one with less range and/or precision:

> If the value being converted is in the range of values that can be represented
> but cannot be represented exactly, the result is either the nearest higher or
> nearest lower value, chosen in an implementation-defined manner.

And in subclause 6.2.1.5 **Usual arithmetic conversions**, page 35:

> The values of floating operands and of the results of floating expressions may
> be represented in greater precision and range than that required by the type;
> the types are not changed thereby.

Otherwise, arithmetic for both integer and floating types is defined in terms of
the usual terminology of mathematics. Nothing in the C Standard suggests that
floating arithmetic is excused from the conventional rules of arithmetic.

Nevertheless, it is commonplace for the functions declared in `<math.h>` to
deliver results less accurate than the underlying representation can support. It
is not uncommon even for simple arithmetic expressions to do the same. And
still, implementations document in `<float.h>` properties of the underlying
*representation,* not the effective range and precision reliably delivered. The
C community has typically tolerated a certain laxity in this area.

Probably the most useful response would be to amend the C Standard by adding two
requirements on implementations:

Require that an implementation document the maximum errors it permits in
arithmetic operations and in evaluating math functions. These should be
expressed in terms of “units in the least-significant position” (ULP) or “lost
bits of precision.”

Establish an upper bound for these errors that all implementations must adhere
to.

The state of the art, as the Committee understands it, is:

correctly rounded results for arithmetic operations (no loss of precision)

1 ULP for functions such as `sqrt`, `sin`, and `cos` (loss of 1 bit of
precision)

4-6 ULP (loss of 2-3 bits of precision) for other math functions.

Since not all commercially viable machines and implementations meet these
exacting requirements, the C Standard should be somewhat more liberal.

The Committee would, however, suggest a requirement no more liberal than a loss
of 3 bits of precision, out of kindness to users. An implementation with worse
performance can always conform by providing a more conservative version of
`<float.h>`, even if that is not a desirable approach in the general case.

The Committee should revisit this issue during the revision of the C Standard.
