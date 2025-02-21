## Issue 0426: G.5.1: `-yv` and `-x/v` are ambiguous

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred J. Tydeman  
Date: 2013-01-07  
Reference document: [N1670](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1670.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The tables in G.5.1 have the mathematical formulas -yv and -x/v. I believe that
they are ambiguous as they could have two meanings:

* (-y)/v and (-x)/v
* -(y/v) and -(x/v)

I believe it matters for at least these cases:

1. The two operands are different NaNs, negate flips the sign of a NaN, and the result of \* and / depends upon the sign and value of the NaN.
2. The result is a NaN from non-NaN operands, negate does not flip the sign of a NaN, while both \* and / set the sign of the result as the XOR of the signs of the operands.
3. All operands are non-NaN, the result is inexact and non-NaN, and a rounding that is not symmetric about zero is in effect.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* The committee sees the mathematical formulae as unambiguous since the regroupings presented in the paper are mathematically equivalent, and should not be construed as C expressions. As such, there was considerable skepticism expressed that this was indeed a defect.
* The author promised to provide a supplemental paper that would substantiate his concern about this as a defect.

Oct 2013 meeting

### Committee Discussion

* [N1738](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1738.htm) clarifies a typo in the original document.
* A very long discussion ensued, starting with the fact that C11 notation was used in the clarifying example rather than mathematical notation.
* The concerns raised about `NaNs` were deemed moot by the fact that multiply and divide are not required by either C11 or IEEE-754 to honor the sign of `NaNs`.
* The intended mathematical result seems obvious to most on the committee, and the arguments about mathematical notations were not persuasive.
* The third case, however, has modest merit if one considers an implementation that transcribes the provided notation into C11 directly, in which case when asymmetric rounding mode is selected an incorrect result will be formed if negation is applied after the division (or multiplication). More exactly, in the third case, all operands are non-Nan, the result is inexact and non-NaN, and a rounding that is not symmetric about zero is in effect.
* As such, the committee, with great reluctance, narrowly formed a consensus for change, and is concerned that this issue is almost certainly not significant enough to warrant the effort already expended, let alone further discussion, lest the entire matter be returned with no changes proposed as a Record of Response.

### Proposed Technical Corrigendum

> In the table in G.5.1 #2, change
>
> > -yv
>
> to
>
> > (-y)v
>
> in three places.
>
> In the table in G.5.1 #3, change
>
> > -x/v
>
> to
>
> > (-x)/v
>
> in two places.
