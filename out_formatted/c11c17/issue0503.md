## Issue 0503: Hexadecimal floating-point and `strtod`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Clark Nelson  
Date: 2016-09-13  
Reference document: [N2082](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2082.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 7.22.1.3 paragraph 3 bullet 2 says:

> a `0x` or `0X`, then a nonempty sequence of hexadecimal digits optionally
> containing a decimal-point character, then an optional binary exponent part as
> defined in 6.4.4.2;

but the grammar in C11 6.4.4.2 makes the binary-exponent-part mandatory, not
optional.

**Suggested resolution**

Strike "optional" before "binary exponent part" and add a comma before "as
defined in" to highlight that "as defined in" applies to the entire sentence,
not only to the last part.

---

Comment from WG14 on 2017-11-03:

Oct 2016 meeting

### Committee Discussion

> This turns out to not be a defect.

### Proposed Committee Response

> The reference to §6.4.4.2 is only for the definition of "binary exponent part",
> it does not apply to the entire sentence. The specification of allowable subject
> sequences for these library functions is intentionally looser than the grammar
> for floating constants in order to accept as many reasonable input strings as
> possible. Thus, both 123 and 0x123 are valid subject sequences even though
> neither is acceptable as a floating constant.
