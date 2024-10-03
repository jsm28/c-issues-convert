*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 002: Consistency of implementation-defined values

The restrictions that apply to "implementation-defined" entities are not clear.

What restrictions apply to implementation-defined entities? If the value of an
expression is implementation-defined, need the implementation always produce the
same result?

For example, the value of the expressions `7/-3` and `8/-3` must each be either
`3` or `2`. Can an implementation make them different (that is, use a different
implementation-defined choice for each), or must it make the same choice for all
integral divisions involving a negative quantity?

As another example, can the number of significant characters and the
significance of case in an identifier with external linkage depend on the
identifier itself, or must it be the same for all possible identifiers?
