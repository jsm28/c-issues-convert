## Issue 0440: Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 1

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Joseph Myers  
Date: 2013-07-21  
Reference document: [N1730](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1730.pdf)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 1: Choice of long double in Annex F

Annex F provides various choices for the long double type (which may or may not
be an IEC 60559 type), but no method is provided for an application to determine
which choice has been made.

If a macro is provided to say whether the type is an IEC 60559 type, all the
other properties can be determined from the existing \<float.h\> macros. So, a
sufficient fix would be:

> In 5.2.4.2.2, insert a new paragraph after paragraph 10: Whether a type matches
> an IEC 60559 type is characterized by the implementation-defined values of
> FLT\_IS\_IEC\_60559, DBL\_IS\_IEC\_60559, and LDBL\_IS\_IEC\_60559:
>
> * 0 type does not match an IEC 60559 format
> * 1 type's values and operations are those of an IEC 60559 basic, interchange or extended type

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

> Committee discussion led to a proposed committee response.

Apr 2014 meeting

> Correspondence with the author led the committee to augment the proposed
> committee response.

### Proposed Committee Response

> To do as suggested, distinguish whether `float`, `double`, and `long double` are
> IEC or not, requires the addition of new macros, which is a feature, which is
> not allowed by the mechanism of defect reports.
>
> The defect originator notes that the underlying issue that needs consideration
> in any further comprehensive publication of the Standard is that all
> implementation defined behaviors need to be strictly called out in the Standard,
> and moreover that they be done so in a manner that is accessible to a client of
> the implementation to allow proper choice of algorithms. It has been asserted
> that leaving implementation defined behaviors formally undefined in the Standard
> has led to significant and unnecessary divergences in implementations.
