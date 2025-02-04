## Issue 0410: `ilogb` inconsistent with `lrint`, `lround`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred J. Tydeman (USA)  
Date: 2012-01-11  
Reference document: [N1595](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1595.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

For the case of converting a large finite value to an integer value, lrint and
lround have one set of requirements, while ilogb has another set. This is
inconsistent.

Both 7.12.9.5 The lrint and llrint functions and 7.12.9.7 The lround and llround
functions have:

> If the rounded value is outside the range of the return type, the numeric result
> is unspecified and a domain error or range error may occur.

While 7.12.6.5 The ilogb functions has:

> If the correct value is outside the range of the return type, the numeric result
> is unspecified.

I believe that the following changes to C11 should be done.

1. 7.12.6.5 The ilogb functions:

   Change to: If the correct value is outside the range of the return type, the
   numeric result is unspecified and a domain error or range error may occur.

---

Comment from WG14 on 2017-11-03:

Feb 2012 meeting

> ### Committee discussion
>
> > * Some believe the rationale presented as a reason for doing this is not a valid rationale for the change.
>
> ### Proposed Technical Corrigendum
>
> > In 7.12.6.5 paragraph 2, change the last sentence to:
> >
> > > If the correct value is outside the range of the return type, the numeric result
> > > is unspecified and a domain error or range error may occur.
