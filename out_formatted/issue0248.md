## Issue 0248: limits are required for optional types

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_248.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_248.htm)

### Problem

The types `sig_atomic_t` and `wchar_t` are optional on freestanding
implementations, since they don't have to provide the relevant headers. But the
limits `SIG_ATOMIC_MIN`, `SIG_ATOMIC_MAX`, `WINT_MIN`, and `WINT_MAX` are in
`<stdint.h>`, which all implementations must provide. So a freestanding
implementation must provide limits for types which it doesn't implement.

### Suggested Technical Corrigendum

Append to 7.18.3#2:

> A freestanding implementation shall only define the symbols corresponding to
> those typedef names it actually provides.

---

Comment from WG14 on 2002-03-06:

### Technical Corrigendum

Append to 7.18.3#2:

> An implementation shall define only the macros corresponding to those typedef
> names it actually provides.

Add a footnote to the last sentence of 7.18.3#2 to read:

> A freestanding implementation need not provide all of these types.
