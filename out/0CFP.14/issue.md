### Summary

The specification in TS 18661-2 for `a`,`A` conversion specifiers for decimal
describes the behavior in terms of  `f` and `e` formatting. The intention was
that the `A` conversion specifier would have the effects of `F` and `E`
formatting. The following Technical Corrigendum corrects this oversight, using
wording similar to that in C11 for the `g`,`G` conversion specifiers.

### Suggested Technical Corrigendum

In 12.5, in the text added to 7.21.6.1#8 and 7.29.2.1#8, under `a`,`A`
conversion specifiers, replace the bullets:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` formatting with formatting precision
> equal to −*q*,
>
> —    otherwise, use style `e` formatting with …

with:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` (or style `F` in the case of an `A`
> conversion specifier) with formatting precision equal to −*q*,
>
> —    otherwise, use style `e` (or style `E` in the case of an `A` conversion
> specifier) with …
