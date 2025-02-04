## Issue 0473: "A range error occurs if x is too large." is misleading

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman  
Date: 2015-01-07  
Reference document: [N1903](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1903.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

"A range error occurs if **x** is too large." is misleading (or ambiguous) for
expm1 (7.12.6.3p2), erfc (7.12.8.2p2), and lgamma (7.12.8.3p2).

"too large" could mean either \+/-large value (in which case "too small" means
\+/-near zero) or just \+large value (in which case "too small" means -large
value).

7.12.6.3p2: expm1(-DBL\_MAX) is -1, which is not a range error.

7.12.8.2p2: erfc(-DBL\_MAX) is 2, which is not a range error.

7.12.8.3p2: lgamma(-DBL\_MAX) is a pole error, which is not a range error.

### Suggested Technical Corrigendum

Add the word "positive" before **x** in those three cases so that they are:

> A range error occurs if positive **x** is too large.

---

Comment from WG14 on 2017-11-03:

Apr 2015 meeting

### Committee Discussion

> The Suggested Technical Corrigendum was accepted.

Oct 2015 meeting

### Committee Discussion

* A new paper [N1941](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1941.htm) was submitted and discussed as well as the refinement proposed in [(SC22WG14.13872) DR 473, 409](https://www.open-std.org/jtc1/sc22/wg14/13872) .
* The “only if” refinement from [(SC22WG14.13872) DR 473, 409](https://www.open-std.org/jtc1/sc22/wg14/13872) met approval from the committee and is adopted in the revised Proposed Technical Corrigendum below.
* This Proposed Technical Corrigendum will, however, invalid practice in one set of compilers where “range error” is used for other purposes. No changes, however, were proposed or accepted to resolve this issue in what remains as The Proposed Technical Corrigendum.
* The implication of this change affects all functions in this section and the committee expressed concern that this impact is unknown and hard to assess.

Apr 2016 meeting

### Committee Discussion

> The committee agreed to change “only occurs if” to “occurs if and only if” in
> three places, and these changes have been made in The Proposed Technical
> Corrigendum below.

### Proposed Technical Corrigendum

Change 7.12.1p2 first sentence from:

> For all functions, a *domain error* occurs if . . .

to:

> For all functions, a *domain error* occurs if and only if . . .

Change 7.12.1p3 first sentence from:

> Similarly, a *pole error* (also known as a singularity or infinitary) occurs if
> . . .

to:

> Similarly, a *pole error* (also known as a singularity or infinitary) occurs if
> and only if . . .

Change 7.12.1p4 from:

> Likewise, a *range error* occurs if the mathematical result of the function
> cannot be represented in an object of the specified type, due to extreme
> magnitude.

to:

> Likewise, a *range error* occurs if and only if the mathematical result of the
> function cannot be represented in an object of the specified type, due to
> extreme magnitude. The description of each function lists any required range
> errors; an implementation may define additional range errors, provided that such
> errors are consistent with the mathematical definition of the function and are
> the result of either overflow or underflow.

In 7.12.6.3 The expm1 function p2 change

> A range error occurs if **x** is too large.<sup>237</sup>

to

> A range error occurs if positive **x** is too large.<sup>237</sup>

In 7.12.8.2 The erfc function p2 change

> A range error occurs if **x** is too large.

to

> A range error occurs if positive **x** is too large.

In 7.12.8.3 The lgamma functions p2 change

> A range error occurs if **x** is too large.

to

> A range error occurs if positive **x** is too large.
