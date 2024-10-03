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
