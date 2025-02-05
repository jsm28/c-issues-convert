### Summary

In analyzing the differences in this paragraph between C99 and C\+\+, I
discovered that C89 admitted only letters in include file names with guaranteed
unique mappings. C99 later added digits, while C\+\+ independently added
underscores. I personally don't recall any discussion or rationale behind either
decision. It's clear that simply synchronizing C\+\+ to C99 would be a technical
change, and could (from a pedantic perspective) invalidate some existing code.
The only way to synchronize the two standards without invalidating any existing
code would be to allow underscores and digits in both standards. This may be
considered a good thing in any event.

Note that in my proposed change the terms of reference have changed slightly.
That's because, in the C\+\+ standard, for good or ill, the terms *letter* and
*digit* aren't defined in the (earlier) section describing the character set, as
they are in C99 (whereas in C89, the terms appeared there without being
definitions). In C\+\+, *letter* is defined in the (later) library section, and
*digit* is defined only as a non-terminal. It would of course be possible to
rearrange things in the C\+\+ standard to more closely match the C standard, but
synchronizing things in this way would be much easier. And again, using the
non-terminal symbols in this context may be considered an improvement in itself.

### Suggested Technical Corrigendum

Change 6.10.2p5:

> The implementation shall provide unique mappings for sequences consisting of one
> or more <del>letters or digits (as defined in 5.2.1)</del> <ins>*nondigits* or
> *digits* (6.4.2.1)</ins> followed by a period (.) and a single <del>letter</del>
> <ins>*nondigit*</ins>. The first character shall <del>be a letter</del> <ins>not
> be a *digit*</ins>. The implementation may ignore the distinctions of
> alphabetical case and restrict the mapping to eight significant characters
> before the period.
