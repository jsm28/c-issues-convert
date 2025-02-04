## Issue 0CFP.22: P3: changes for obsolescing DECIMAL\_DIG

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, C Floating Point Group  
Date: 2018-03-16  
Reference document: [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Cross-references: [0CFP.20](issue0CFP.20.md)  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

N2211 described changes in C11 and TS 18661 to remove references to
`DECIMAL_DIG`, which CR501 is expected to obsolesce. The changes that apply to
C11 are collected in N2253 as an update to the suggested TC in CR501. The
changes that apply to TS 18661-1 are in the CR in N2254. The remaining change is
for TS 18661-3, which is covered by the CR in this document.

### Suggested Technical Corrigendum

At the end of clause 7, omit:

> With the following change, `DECIMAL_DIG` characterizes conversions of supported
> IEC 60559 encodings, which may be wider than supported floating types.
>
> **Change to C11 \+ TS18661-1 \+ TS18661-2:**
>
> In 5.2.4.2.2#11, change the bullet defining `DECIMAL_DIG` from:
>
> > —  number of decimal digits, *n*, such that any floating-point number in the
> > widest supported floating type with …
>
> to:
>
> > —  number of decimal digits, *n*, such that any floating-point number in the
> > widest of the supported floating types and the supported IEC 60559 encodings
> > with …

---

Comment from WG14 on 2019-05-03:

Apr 2018 meeting

### Committee Discussion

> The paper was only briefly discussed.
>
> This resolution is tied to the Floating Point [CR 20](issue0CFP.20.md) as well as
> to the C2x DR 501\.

Oct 2018 meeting

### Committee Discussion

> A new paper [N2255](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2255.pdf)
> was split out from
> [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.pdf) that
> incorporates directly the Suggested Technical Corrigendum already extracted
> above.
>
> The committee accepts the Suggested Technical Corrigendum as the Proposed Change
> to resolve this issue.

### Proposed Change

At the end of clause 7, omit:

> With the following change, `DECIMAL_DIG` characterizes conversions of supported
> IEC 60559 encodings, which may be wider than supported floating types.
>
> **Change to C11 \+ TS18661-1 \+ TS18661-2:**
>
> In 5.2.4.2.2#11, change the bullet defining `DECIMAL_DIG` from:
>
> > —  number of decimal digits, *n*, such that any floating-point number in the
> > widest supported floating type with …
>
> to:
>
> > —  number of decimal digits, *n*, such that any floating-point number in the
> > widest of the supported floating types and the supported IEC 60559 encodings
> > with …
