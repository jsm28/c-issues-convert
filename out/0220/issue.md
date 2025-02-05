### Summary

7.19.6.1\[#4\] reads in part:

> * An optional minimum field width. \[...\] The field width takes the form of an asterisk `*` (described later) or a decimal integer<sup>.232)</sup>
> * An optional precision \[...\] The precision takes the form of a period `.` followed either by an asterisk `*` (described later) or by an optional decimal integer; \[...\]

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

> \[#x\] A *decimal integer* is a sequence of digits which may begin with one or
> more zeros, but is nonetheless interpreted as decimal, not octal.

Append to the first cited text in 7.19.6.1:

> (A leading zero will be interpreted as a flag, not as part of the width).
