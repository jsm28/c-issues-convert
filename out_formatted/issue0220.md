## Issue 0220: Definition of "decimal integer"

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 2000-04-04  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_220.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_220.htm)

### Summary

7.19.6.1\[#4] reads in part:

> * An optional minimum field width. \[...] The field width takes the form of an asterisk `*` (described later) or a decimal integer<sup>.232)</sup>
> * An optional precision \[...] The precision takes the form of a period `.` followed either by an asterisk `*` (described later) or by an optional decimal integer; \[...]

7.19.6.2 #3 reads in part:

> * An optional nonzero decimal integer that specifies the maximum field width (in characters).

7.24.2.1 and 7.24.2.2 have essentially the same wording.

The term "decimal integer" is defined neither in the Standard nor in ISO 2382-1.
Therefore it is not possible to tell whether, in each case:

> * the value may be zero
> * a non-significant leading zero digit may be used
> * the value may be negative.

### Suggested Technical Corrigendum

Add a new paragraph to 7.1.1:

> \[#x] A *decimal integer* is a sequence of digits which may begin with one or
> more zeros, but is nonetheless interpreted as decimal, not octal.

Append to the first cited text in 7.19.6.1:

> (A leading zero will be interpreted as a flag, not as part of the width).

---

Comment from WG14 on 2000-11-02:

### Technical Corrigendum

In 7.19.6.1P4, which reads in part:

> An optional minimum field width. \[...] The field width takes the form of an
> asterisk `*` (described later) or a decimal integer.\[232] An optional precision
> \[...] The precision takes the form of a period `.` followed either by an
> asterisk `*` (described later) or by an optional decimal integer; \[...]

change "decimal integer" to "non-negative decimal integer".

In 7.19.6.2P3, which reads in part:

> An optional nonzero decimal integer that specifies the maximum field width (in
> characters).

change "non-zero decimal integer" to "decimal integer greater than zero".

In 7.24.2.1P4, make similar changes of "decimal integer" to "non-negative
decimal integer".

In 7.24.2.2P3, make similar changes of "non-zero decimal integer" to "decimal
integer greater than zero".
