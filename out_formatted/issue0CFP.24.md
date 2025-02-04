## Issue 0CFP.24: P1 remainder NaN case

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, C Floating Point Group  
Date: 2018-06-26  
Reference document: [N2272](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2272.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The TS 18661-1 specification for remainder in F.10.7.2, says

—             **remainder(***x***,** ±∞**)** returns *x* for *x* not infinite.

For *x* a (quiet) NaN, this specification appears to require that the same NaN
be returned. This unintentionally goes beyond IEC 60559 whose general
specification for NaNs requires only that some (quiet) NaN be returned. The
suggested TC below uses similar words to IEC 60559’s, which allows the general
specification for NaNs to apply.

### Suggested Technical Corrigendum

In TS 18661-1 clause 12, for C F.10.7.2, change the third bullet from:

—             **remainder(***x***,** ±∞**)** returns *x* for *x* not infinite.

to:

—             **remainder(***x***,** ±∞**)** returns *x* for finite *x*.

---

Comment from WG14 on 2019-05-03:

Oct 2018 meeting

### Committee Discussion

> The committee accepts the Suggested Technical Corrigendum as the Proposed Change
> to resolve this issue.

### Proposed Change

In TS 18661-1 clause 12, for C F.10.7.2, change the third bullet from:

—             **remainder(***x***,** ±∞**)** returns *x* for *x* not infinite.

to:

—             **remainder(***x***,** ±∞**)** returns *x* for finite *x*.
