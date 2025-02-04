## Issue 0CFP.14: P2: Effect of `%a` vs `%A` conversion specifiers

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas  
Date: 2017-03-04  
Reference document: [N2125](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2125.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The specification in TS 18661-2 for `a`,`A` conversion specifiers for decimal
describes the behavior in terms of  `f` and `e` formatting. The intention was
that the `A` conversion specifier would have the effects of `F` and `E`
formatting. The following Technical Corrigendum corrects this oversight, using
wording similar to that in C11 for the `g`,`G` conversion specifiers.

### Suggested Technical Corrigendum

In 12.5, in the text added to 7.21.6.1#8 and 7.29.2.1#8, under `a`,`A`
conversion specifiers, replace the bullets:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` formatting with formatting precision
> equal to −*q*,
>
> —    otherwise, use style `e` formatting with …

with:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` (or style `F` in the case of an `A`
> conversion specifier) with formatting precision equal to −*q*,
>
> —    otherwise, use style `e` (or style `E` in the case of an `A` conversion
> specifier) with …

---

Comment from WG14 on 2018-10-18:

Apr 2017 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In 12.5, in the text added to 7.21.6.1#8 and 7.29.2.1#8, under `a`,`A`
conversion specifiers, replace the bullets:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` formatting with formatting precision
> equal to −*q*,
>
> —    otherwise, use style `e` formatting with …

with:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` (or style `F` in the case of an `A`
> conversion specifier) with formatting precision equal to −*q*,
>
> —    otherwise, use style `e` (or style `E` in the case of an `A` conversion
> specifier) with …
