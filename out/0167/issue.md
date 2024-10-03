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
[Defect Report #014, Question 2](issue:0014.02), should also be applied to
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
