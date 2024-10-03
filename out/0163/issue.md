*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 011: Undeclared identifiers

The C Standard is not clear on whether the use of an undeclared identifier as a
primary expression requires a diagnostic message.

Subclause 6.3.1 states that:

An identifier is a primary expression, provided it has been declared as
designating an object (in which case it is an lvalue) or a function (in which
case it is a function designator).

It has been suggested that if no declaration of some identifier is visible in
the current scope when that identifier appears in an expression, the identifier
is not a primary expression, and therefore the syntax of subclause 6.3.1 is
violated (in other words, there is no valid parse for the expression). This
would thus require a diagnostic for an undeclared identifier.

Is this interpretation correct? If yes, then it needs to be made clear that this
does not prevent a previously undeclared function from being called by a
strictly conforming program (see 6.3.2.2).

If not, does an undeclared identifier require a diagnostic, and if so, why? If
not, is this a deliberate policy, or is it a defect that needs correction?
