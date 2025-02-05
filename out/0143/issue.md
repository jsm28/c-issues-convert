*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 027: fopen modes

*\[BSI characterize this issue as minor.\]*

The definition of file opening modes is self-contradictory.

Subclause 7.9.5.3 reads in part:

> The argument mode points to a string beginning with one of the following
> sequences:

and then lists all of `r`, `r+`, `rb`, and `rb+` or `r+b`, with different
meanings. Obviously, it is possible for a string to begin with up to three of
these simultaneously, and thus the quoted text is contradictory.

Also, the wording is confusing since it can easily be misread as "beginning with
exactly one of the following sequences," which would prohibit those of the
specified modes that are longer than one character.

### Suggested Technical Corrigendum:

Change the quoted text to:

> The mode is determined by the longest match of the following sequences to the
> initial characters of the string pointed to by the argument `mode`; at least the
> initial character shall match.
