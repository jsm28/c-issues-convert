## Issue 0167: The `n` conversion specifier in subclause 7.9.6.2 made by TC1, [Defect Report #014, Question 2](../c90/issue0014.02.md), should be applied to subclause 7.9.6.1

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Cross-references: [0014.02](../c90/issue0014.02.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_167.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_167.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 015: Consistency of the C Standard

The change to the `n` conversion specifier in subclause 7.9.6.2 made by TC1,
[Defect Report #014, Question 2](../c90/issue0014.02.md), should also be applied to
subclause 7.9.6.1. Change:

No argument is converted.

to:

No argument is converted, but one is consumed.

If the conversion specification with this conversion specifier is not one of
`%n`, `%ln`, or `%hn`, the behavior is undefined.

In addition, an entry something like:

A `%n` conversion specification for the `fprintf` or `fscanf` functions is not
one of `%n`, `%ln`, or `%hn` (7.9.6.1, 7.9.6.2).

should be added to Annex G.2.
