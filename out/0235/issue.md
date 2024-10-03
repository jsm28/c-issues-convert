### Summary

> Usually, the locale-specific behaviour for the library functions is specified
> when it comes to the "`C`" locale. A noteworthy and well-known exception to that
> the set of *printing characters* is **not** restricted. However, other points
> that may be seen as overviews. In 7.21.4.3 (**strcoll**), 7.24.4.4.2
> (`wcscoll`), 7.21.4.5 (`strxfrm`) and 7.24.4.4.4 (`wcsxfrm`), no behaviour is
> specified in the case of the "`C`" locale.
> 
> It is customary to default to respectively `strcmp` for `strcoll`, `wcscmp` for
> `wcscoll`, and the identity function for the latter two, but this is not
> presently required.

**Suggested responses**

There are basically two choices:

> * left things as they are, since use of `strcoll` and alii in the "`C`" locale is not expected to be a noteworthy situation
> * correct the Standard along the customary way

### Suggested Technical Corrigendum

> In 7.21.4.3, add a new sentence (or a new paragraph) under **Description** which
> says:
> 
> > In the "`C`" locale, this function operates in the same way as `strcmp` does.
> 
> In 7.24.4.4.2, add a new sentence in paragraph 2 (or a new paragraph) which
> says:
> 
> > In the "`C`" locale, this function operates in the same way as `wcscmp` does.
> 
> In 7.21.4.5, add a new sentence in paragraph 2 (or a new paragraph) which says:
> 
> > In the "`C`" locale, this function copies at most `n` characters from the string
> > pointed by `s2` to `s1`.
> 
> In 7.24.4.4.4, add a new sentence in paragraph 2 (or a new paragraph) which
> says:
> 
> > In the "`C`" locale, this function copies at most `n` wide characters from the
> > string pointed by `s2` to `s1`.
