## Issue 0267: Typos in 5.1.2.3, 7.24.4.4.5, 7.24.6.1, 7.24.6.1

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14 Convener (J. Benito)  
Date: 2001-09-21  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_267.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_267.htm)

### Summary

> 1. 5.1.2.3p12, example 4, expressions should be expression.
> 2. 7.24.4.4.5p1 `* s1` and `* s2` should not have spaces following the `*`s.
> 3. 7.24.6.1.1p3 "The `btowc` returns" should read "The `btowc` function returns".
> 4. 7.24.6.1.2p3 "The `wctob` returns" should read "The `wctob` function returns".

### Suggested Technical Corrigendum

> 1. In 5.1.2.3, paragraph #12 change last line of code fragment expressions to expression.
> 2. In 7.24.4.4.5, paragraph #1 remove the space following the `*` for `s1` and `s2`.
> 3. In 7.24.6.1.1, paragraph #3 change:
>    > "The `btowc` returns"
>
>    to
>    > "The `btowc` function returns"
> 4. In 7.24.6.1.2, paragraph #3 change:
>    > "The `wctob` returns"
>
>    to
>    > The `wctob` function returns"

---

Comment from WG14 on 2003-10-06:

### Technical Corrigendum

> 1. In 5.1.2.3, paragraph #12 change expressions to expression in last line of code fragment.
> 2. In 7.24.4.4.5, paragraph #1 remove the space following the `*` for `s1` and `s2`.
> 3. In 7.24.6.1.1, paragraph #3 change:
>    > "The `btowc` returns"
>
>    to
>    > "The `btowc` function returns"
> 4. In 7.24.6.1.2, paragraph #3 change:
>    > "The `wctob` returns"
>
>    to
>    > The `wctob` function returns"
