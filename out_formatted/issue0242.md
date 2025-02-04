## Issue 0242: Make the base standard and Annex F consistent for `logb(0)`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman (US)  
Date: 2001-02-25  
Reference document: [ISO/IEC WG14 N943](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n943.txt)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_242.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_242.htm)

### Summary

> `logb(0)` should be considered a pole error in the base standard (it already is
> in Annex F).

### Details

> `logb(0)` is inconsistent between 7.12.6.11 (domain error) and Annex F (range
> error via divide-by-zero).
>
> `logb(0)` is effectively the same as `log(0)`, `log2(0)`, or `log10(0)`, all of
> which are a pole or singularity error, which is a divide-by-zero exception to
> Annex F and a range error to 7.12. But, `logb` treats it as a domain error in
> 7.12.6.11.

### Suggested Technical Corrigendum

In 7.12.6.11 `logb`:

Change:

> A domain error may occur if the argument is zero.

to

> A range error may occur if the argument is zero.

---

Comment from WG14 on 2001-10-16:

### Technical Corrigendum

In 7.12.6.11 `logb`:

Change:

> A domain error may occur if the argument is zero.

to

> A domain error or range error may occur if the argument is zero.
