## Issue 0306: 6.10.3p9: Clarifying that rescanning applies to object-like macros

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG21, WG21  
Date: 2004-10-26  
Reference document: [ISO/IEC WG14 N1068](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1068.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_306.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_306.htm)

### Summary

I suspect that this was introduced as a result of a public comment from someone
who was confused (honestly or perversely) about 6.10.3.4p1: "**After all
parameters in the replacement list have been substituted,** the resulting
preprocessing token sequence is rescanned *...*" (emphasis added). This clearly
describes the rescanning of function-like macros, but because of the reference
to parameters, may be taken as not applying to object-like macros.

### Suggested Technical Corrigendum

Add a new sentence to the end of 6.10.3p9:

> A preprocessing directive of the form
>
> > ```c
> > # define identifier replacement-list new-line
> > ```
>
> defines an object-like macro that causes each subsequent instance of the macro
> name<sup>145\)</sup> to be replaced by the replacement list of preprocessing
> tokens that constitute the remainder of the directive. <u>The replacement list
> is then rescanned for more macro names as specified below.</u>

---

Comment from WG14 on 2006-03-05:

### Technical Corrigendum

Add a new sentence to the end of 6.10.3p9:

> A preprocessing directive of the form
>
> > ```c
> > # define identifier replacement-list new-line
> > ```
>
> defines an object-like macro that causes each subsequent instance of the macro
> name<sup>145\)</sup> to be replaced by the replacement list of preprocessing
> tokens that constitute the remainder of the directive. <u>The replacement list
> is then rescanned for more macro names as specified below.</u>
