### Summary

Obviously, "before any other processing" is already implied by the phases of
translation, but it doesn't hurt to point out the implication here. And in
general, a distributive description ("each" with singular) tends to be less
ambiguous than a collective one ("all" with plural). The motivation for deleting
the phrase "in a source file" is, as far as I can see, weak at best.

### Suggested Technical Corrigendum

Change 5.2.1.1p1:

> ~~All occurrences in a source file~~ <u>Before any other processing takes place,
> each occurrence of one</u> of the following sequences of three characters
> (called *trigraph sequences*<sup>12\)</sup>) ~~are~~ <u>is</u> replaced with the
> corresponding single character.
