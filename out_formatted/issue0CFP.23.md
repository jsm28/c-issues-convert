## Issue 0CFP.23: P2: llquantexp invalid case

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, C Floating Point Group  
Date: 2018-05-26  
Reference document: [N2262](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2262.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The `llquantexp` functions in 12.4.1 of TS 18661-2 compute the quantum exponent
of a finite argument (of decimal floating type). Infinities and NaNs don’t have
a quantum exponent, so the description in C 7.12.11a.4 says “If `x` is infinite
or NaN, they compute `LLONG_MIN` and a domain error occurs.” In similar cases,
of a function with floating parameters and integer return type, where no return
value is suitable, the “invalid” floating-point exception is raised. Examples in
current C include `ilogb`, `lrint`, and `lround`. However, TS 18661-2 neglects
to specify raising “invalid” for `llquantexp`, which was an oversight.

For the C examples above, the specification of “invalid” is in annex F, because
the functions are not just for IEC 60559 implementations. The `llquantexp`
functions are only for decimal floating types, which C requires to be IEC 60559
conformant. Therefore, the specification for “invalid” can be in the primary
description in 7.12.

CFP has made a similar change for the `quantize` functions. This was done as an
editorial change, because it matches specification for the IEC 60559 quantize
operation, whose specification TS 18661 adopts by reference.

### Suggested Technical Corrigendum

In TS 18661-2 12.4.1, in C 7.12.11a.4#2, change the second sentence from:

> If `x` is infinite or NaN, they compute `LLONG_MIN` and a domain error occurs.

to:

> If `x` is infinite or NaN, they compute `LLONG_MIN`, the “invalid”
> floating-point exception is raised, and a domain error occurs.

---

Comment from WG14 on 2019-05-03:

Oct 2018 meeting

### Committee Discussion

> The committee accepts the Suggested Technical Corrigendum as the Proposed Change
> to resolve this issue.

### Proposed Change

In TS 18661-2 12.4.1, in C 7.12.11a.4#2, change the second sentence from:

> If `x` is infinite or NaN, they compute `LLONG_MIN` and a domain error occurs.

to:

> If `x` is infinite or NaN, they compute `LLONG_MIN`, the “invalid”
> floating-point exception is raised, and a domain error occurs.
