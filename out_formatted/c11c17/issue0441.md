## Issue 0441: Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 2

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Joseph Myers  
Date: 2013-07-21  
Reference document: [N1730](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1730.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 2: Definition of FLT\_ROUNDS

The C11 definition of FLT\_ROUNDS is inadequate in that it refers to
floating-point addition but does not say addition of what type. If long double
is not an IEC 60559 type, it may not fully support all rounding modes even
though they are supported by other types. (This is an actual issue with real
implementations using non-IEC 60559 types for long double.) A suitable fix would
be:

> In 5.2.4.2.2#8, insert "for type float" after "floating-point addition". At the
> end of F.2#1, insert "The value of FLT\_ROUNDS applies to all IEC 60559 types
> supported by the implementation, but may not apply to non-IEC 60559 types.".

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

> The committee adopted a Proposed Committee Response that has been substantially
> revised.

Oct 2014 meeting

### Committee Discussion

> The Proposed Committee Response was revised for accuracy and more detailed
> information, and is provided below.

**Proposed Committee Response (obsolete)**

> The committee regards the existing definition of `FLT_ROUNDS` as intended to
> apply to types `float`, `double` and `long double`. However, if all three types
> cannot support the same set of rounding modes, the implementation needs to set
> `FLT_ROUNDS` to -1 meaning indeterminable.
>
> As has been pointed out, in Annex F, only the types float and double need be IEC
> 60559 types. If long double is not an IEC 60559 type (for example, a pair of
> doubles), it may not support the same set of rounding modes as float and double.
> In this case, having `FLT_ROUNDS` apply to float and double (but not long
> double) would result in a value of 0, 1, 2, or 3 and would provide new and
> useful information to the programmer.
>
> However, this behavioral change could also break existing programs, and as such
> the committee prefers to leave as is for this revision of the Standard.

Apr 2015 meeting

### Committee Discussion

> The Proposed Committee Response was revised yet again based on the input that
> since FLT\_ROUNDS in existing practice is universally coded as 1, the proposed
> changes won’t affect existing practice.

### Proposed Committee Response

> The implementation of `long double`, for example, may significantly differ from
> IEC floating types and may not support the same choices as would otherwise be
> possible for `FLT_ROUNDS`. All known implementations define `FLT_ROUNDS` as the
> value `1` (round to nearest). and as such exempting non-IEC `long double`
> behavior allows the potential for implementations to provide the full range of
> possible values for IEC floating types.

### Proposed Technical Corrigendum

At the end of F.2#1, insert

> The value of FLT\_ROUNDS applies to all IEC 60559 types supported by the
> implementation, but need not apply to non-IEC 60559 types.
