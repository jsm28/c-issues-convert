## Issue 0218: Signs of non-numeric floating point values

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 2000-04-04  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_218.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_218.htm)

### Summary

There is an implication at various points in the standard, notably the copysign
function, that infinities and NaNs have signs. This is not the case in all
implementations, and this needs to be allowed for.

### Suggested Technical Corrigendum

Add a new paragraph to 5.2.4.2.2, preferably after \[#3]:

> \[#3a] An implementation may give zero and non-numeric values (such as
> infinities and `NaNs`) a sign or may leave them unsigned. Wherever such values
> are unsigned, any requirement in this International Standard to retrieve the
> sign shall act as if the value were positive, and any requirement to set the
> sign shall be ignored.

or:

> \[...]  
> to retrieve the sign shall produce an unspecified sign, and any requirement to
> set the sign shall be ignored.

---

Comment from WG14 on 2001-09-18:

### Committee Response

In addition to the following Technical Corrigendum, add to the Rationale section
that discusses 5.2.4.2.2 of the C Standard:

> The committee has been made aware of at least one implementation (VAX and Alpha
> in VAX mode) whose floating-point format does not support signed zeros. The
> hardware representation that one thinks would represent -0.0 is in fact treated
> as a non-numeric value similar to a NaN. Therefore, `copysign(+0.0,-1.0)`
> returns \+0.0, not the expected -0.0, on this implementation. Some places that
> mention (or might have) signed zero results and the sign might be different than
> you expect:
>
> The complex functions, in particular with branch cuts;
>
> > ```c
> > ceil()
> > conj()
> > copysign()
> > fmod()
> > modf()
> > fprintf() (Footnote 233 is OK)fwprintf() (Footnote 273 is OK)nearbyint()
> > nextafter()
> > nexttoward()
> > remainder() (Footnote 201 does not need to be changed)remquo()
> > rint()
> > round()
> > signbit()
> > strtod() (Footnote 249 is OK)trunc()
> > wcstod() (Footnote 285 is OK)
> > ```
>
> Underflow: In particular: `ldexp()`, `scalbn()`, `scalbln()`.

### Technical Corrigendum

Add a new paragraph to 5.2.4.2.2, after \[#3]:

> \[#3a] An implementation may give zero and non-numeric values (such as
> infinities and NaNs) a sign or may leave them unsigned. Wherever such values are
> unsigned, any requirement in this International Standard to retrieve the sign
> shall produce an unspecified sign, and any requirement to set the sign shall be
> ignored.
