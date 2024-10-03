### Problem

6.10.8 reads in part:

> `__STDC_ISO_10646__`
> 
> > An integer constant of the form `yyyymmL` (for example, `199712L`), intended to
> > indicate that values of type `wchar_t` are the coded representations of the
> > characters defined by ISO/IEC 10646, along with all amendments and technical
> > corrigenda as of the specified year and month.

Firstly, this wording is less than optimal, in that it could be read as making
an implementation non-conforming if `wchar_t` has a value that does not
correspond to an ISO 10646 (Unicode) character. Since Unicode has gaps in the
encoding tables, this would mean that no implementation could define this
symbol.

Secondly, is this wording meant to put a lower bound on the size of `wchar_t`,
or does the (`wchar_t` \= \= Unicode) mapping only apply to those values that
`wchar_t` can take. In other words, if a given version of Unicode defines
characters up to U\+12345, can `WCHAR_MAX` be less than `0x12345` on a system
that defines this symbol ?

### Suggested Technical Corrigendum

Replace the cited text by:

> `__STDC_ISO_10646__`
> 
> > An integer constant of the form `yyyymmL` (for example, `199712L`). If this
> > symbol is defined, then every character in the "Unicode required set", when
> > stored in an object of type `wchar_t`, has the same value as the short
> > identifier of that character.

and then either:

> The "Unicode required set" consists of all the characters that are defined by
> ISO/IEC 10646, along with all amendments and technical corrigenda, as of the
> specified year and month.

if the intent is to put a minimum on the value of `WCHAR_MAX`, or then:

> The "Unicode required set" consists of all the characters that:
> 
> * are defined by ISO/IEC 10646, along with all amendments and technical corrigenda, as of the specified year and month; and
> * have short identifiers that lie within the range of values that can be represented by the type `wchar_t`.
