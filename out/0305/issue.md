### Summary

This just clarifies that keywords are not treated specially in `#if` directives.
(In C\+\+, the keywords `true` and `false` **are** treated specially in this
regard; I suspect that someone didn't want the sentence to read, "... all
remaining identifiers, except for `true` and `false`, are replaced ...", for
reasons which seem fairly obvious to me.)

### Suggested Technical Corrigendum

Change the following sentence in 6.10.1p3:

> After all replacements due to macro expansion and the `defined` unary operator
> have been performed, all remaining identifiers <ins>and keywords</ins> are
> replaced with the pp-number `0`, and then each preprocessing token is converted
> into a token.
