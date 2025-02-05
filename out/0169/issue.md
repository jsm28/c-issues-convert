*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 017: Trigraphs

The C Standard's description of the replacement of trigraphs is contradictory.

Subclause 5.2.1.1 reads in part:

All occurrences in a source file of the following sequences of three characters
(called trigraph sequences \[7\]) are replaced with the corresponding single
character... Each `?` that does not begin one of the trigraphs listed above is
not changed.

Since the second character in each trigraph is a `?` that does not begin the
trigraph, this is a direct contradiction.

### Suggested Technical Corrigendum

Change the last sentence of the cited text to:

Each `?` that is not part of one of the trigraphs listed above is not changed.
