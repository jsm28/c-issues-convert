## Issue 0210: `fprintf %a` and `%A` conversions recommended practice

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred Tydeman (US)  
Date: 1999-10-20  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_210.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_210.htm)

### Summary

What should `fprintf` do when it is printing a floating-point number using `%a`
and `%A` conversions and it is exactly representable in the given precision?
That is, what is the result of: `fprintf("%a", 1.0);`? The current wording
appears to say that it be converted into either `0x1.0p0+DBL_EPSILON` or
`0x1.0p0-DBL_EPSILON/FLT_RADIX`, instead of the correct value `0x1.0p0` (this
appears to be an oversight that forgot about exactly representable values).

What should the `strtod` family of functions do when converting a hexadecimal
form of input and the result is exactly representable? That is, what is the
result of: `strtod("0x1.0p0", (char **)NULL);`? The current wording appears to
say that it be converted into either `1.0+DBL_EPSILON` or
`1.0-DBL_EPSILON/FLT_RADIX`, instead of the correct value `1.0` (this appears to
be an oversight that forgot about exactly representable values).

---

Comment from WG14 on 2001-01-22:

### Technical Corrigendum

7.19.6.1 The `fprintf` function:

Page 279, Paragraph 12 should be changed from:

> If `FLT_RADIX` is not a power of 2, the result should be one of the two adjacent
> numbers in hexadecimal floating style with the given precision, with the extra
> stipulation that the error should have a correct sign for the current rounding
> direction.

to:

> For `a` and `A` conversions, if `FLT_RADIX` is not a power of 2 and the result
> is not exactly representable in the given precision, the result should be one of
> the two adjacent numbers in hexadecimal floating style with the given precision,
> with the extra stipulation that the error should have a correct sign for the
> current rounding direction.

7.20.1.3 The `strtod` ... functions:

Page 308, paragraph 8 should be changed from:

> If the subject sequence has the hexadecimal form and `FLT_RADIX` is not a power
> of 2, the result should be one of the two numbers in the appropriate internal
> format that are adjacent to the hexadecimal floating source value, with the
> extra stipulation that the error should have a correct sign for the current
> rounding direction.

to:

> If the subject sequence has the hexadecimal form, `FLT_RADIX` is not a power of
> 2 and the result is not exactly representable, the result should be one of the
> two numbers in the appropriate internal format that are adjacent to the
> hexadecimal floating source value, with the extra stipulation that the error
> should have a correct sign for the current rounding direction.

7.24.2.1 The `fwprintf` function:

Page 354, Paragraph 12 should be changed from:

> If `FLT_RADIX` is not a power of 2, the result should be one of the two adjacent
> numbers in hexadecimal floating style with the given precision, with the extra
> stipulation that the error should have a correct sign for the current rounding
> direction.

to:

> For `a` and `A` conversions, if `FLT_RADIX` is not a power of 2 and the result
> is not exactly representable in the given precision, the result should be one of
> the two adjacent numbers in hexadecimal floating style with the given precision,
> with the extra stipulation that the error should have a correct sign for the
> current rounding direction.

7.24.4.1.1 The `wcstod` ... functions:

Page 372, paragraph 8 should be changed from:

> If the subject sequence has the hexadecimal form and `FLT_RADIX` is not a power
> of 2, the result should be one of the two numbers in the appropriate internal
> format that are adjacent to the hexadecimal floating source value, with the
> extra stipulation that the error should have a correct sign for the current
> rounding direction.

to:

> If the subject sequence has the hexadecimal form, `FLT_RADIX` is not a power of
> 2 and the result is not exactly representable, the result should be one of the
> two numbers in the appropriate internal format that are adjacent to the
> hexadecimal floating source value, with the extra stipulation that the error
> should have a correct sign for the current rounding direction.
