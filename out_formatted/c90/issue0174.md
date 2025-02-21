## Issue 0174: Is there a number of errors in the usual arithmetic conversions section?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_174.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_174.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 022: Implicit conversions

The wording dealing with the usual arithmetic conversions contains a number of
errors; while the correct meaning is usually clear, a strict reading of the C
Standard shows some contradictions and/or unwanted side-effects.

Subclause 6.2.1.5 reads in part:

Many binary operators that expect operands of arithmetic type cause conversions
and yield result types in a similar way. The purpose is to yield a common type,
which is also the type of the result.

Subclause 6.3.15 reads in part:

The second operand is evaluated only if the first compares unequal to 0; the
third operand is evaluated only if the first compares equal to 0; the value of
the second or third operand (whichever is evaluated) is the result.

If both the second and third operands have arithmetic type, the usual arithmetic
conversions are performed to bring them to a common type and the result has that
type ... in which case the other operand is converted to type pointer to void,
and the result has that type.

These citations have several defects:

The relational and equality operators apply the usual arithmetic conversions,
but not to yield the type of result.

The conditional operator `?:` is not a binary operator, but is specified as
performing the usual arithmetic conversions.

The concept of conversions applies only to a value; subclause 6.3.15 is
therefore contradicting itself when it calls for both the second and third
operands to be subject to conversion when only one of them is evaluated.

The value of the result of the `?:` operator is not necessarily that of the
second or third operand, as the value may have been converted (possibly yielding
a different value).

### Suggested Technical Corrigendum

In subclause 6.2.1.5, change the cited sentences to:

Many operators cause the same pattern of conversions to be applied to two
operands of arithmetic type. The purpose is to yield a common type, which,
unless explicitly stated otherwise, is also the type of the operator's result.

In 6.3.15, change the cited wording to:

The second operand is evaluated only if the first compares unequal to 0; the
third operand is evaluated only if the first compares equal to 0; the result of
the operator is the value of the second or third operand (whichever is
evaluated), converted to the type described below.

If both the second and third operands have arithmetic type, the type that the
usual arithmetic conversions would yield if applied to those two operands is the
type of the result ... in which case the type of the result is pointer to
`void`.
