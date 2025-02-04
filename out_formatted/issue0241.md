## Issue 0241: Make the base standard and Annex F consistent for `pow(0, <0)`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman (US)  
Date: 2001-02-25  
Reference document: [ISO/IEC WG14 N943](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n943.txt)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_241.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_241.htm)

### Summary

> `pow(0, <0)` should be considered a pole error (result is an exact infinity) in
> the base standard (it already is in Annex F).

### Details

> `pow(0, <0)` is inconsistent between 7.12.7.4 (domain error) and Annex F (range
> error via divide-by-zero).
>
> `pow(0, <0)` is effectively 1/0, which is a pole or singularity error, which is
> a divide-by-zero exception to Annex F and a range error to 7.12.
>
> Counter-argument: The domain error for this case is a **may**, not a **shall**.
> In addition, 7.12.7.4 has
>
> > A range error may occur
>
> without any qualifications. So, an implementation is allowed to treat this case
> as a range error.

### Suggested Technical Corrigendum

In 7.12.7.4 `pow`:

Split:

> A domain error may occur if `x` is zero and `y` is less than or equal to zero.

into

> A domain error may occur if `x` is zero and `y` is zero.

and

> A range error may occur if `x` is zero and `y` is less than zero.

---

Comment from WG14 on 2001-10-16:

### Technical Corrigendum

In 7.12.7.4 `pow`:

Split:

> A domain error may occur if `x` is zero and `y` is less than or equal to zero.

into:

> A domain error may occur if `x` is zero and `y` is zero.

and

> A domain error or range error may occur if `x` is zero and `y` is less than
> zero.
