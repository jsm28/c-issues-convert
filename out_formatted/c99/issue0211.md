## Issue 0211: Accuracy of decimal string to/from "binary" (non-decimal) floating-point conversions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: NCITS J11, Fred Tydeman (US)  
Date: 1999-10-20  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_211.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_211.htm)

### Summary

What is the accuracy of decimal string to/from "binary" (non-decimal)
floating-point conversions?

What is the accuracy of hexadecimal string to/from "decimal" (non-power-of-2)
floating-point conversions?

In the following, the phrase "decimal to binary" shall cover any pair of bases
that are not both a power of the same number. It also shall cover both the
string to internal floating-point and internal floating-point to string
conversions.

There are two basic cases to consider at run-time:

* decimal string to internal binary (`scanf` family, `strtod` family)
* internal binary to decimal string (`printf` family)

For each of those basic cases, there are two generic sub-cases: base 10 to base
2 and base 2 to base 10\.

**Background**  
7.19.6.1 The `fprintf` function:

> Paragraph 8 on "`f,F`" and "`e,E`" conversion specifiers says: The value is
> rounded to the appropriate number of digits.
>
> Does that mean round to nearest, round by truncating, round by add 0.5 and
> truncate, round as per the current rounding direction, or something else? Must
> the rounding used for `f,F` match the rounding used for `e,E`? Since there is no
> explicit allowance for multiple values (as there is in 6.4.4.2 Floating
> constants), must the value produced be as if the infinitely precise value were
> rounded (and the rounding produce an error less than or equal to 0.5 units in
> the last place (ulp) for nearest and less than 1.0 ulp otherwise)?
>
> For round to nearest, IEEE-754 (IEC-60559) requires that the maximum error be
> 0.5 ulp for a large subset of its values and 0.97 ulp for all values. For the
> other roundings, the maximum error allowed by IEEE-754 is 1.47 ulp. The fourth
> committee draft (1999-09-30) of ISO/IEC 10967-2 (LIA-2) appears to require the
> maximum error be in the range 0.5 to 0.75 ulp. These bounds appear to apply to
> both directions of conversions.

7.19.6.2 The `fscanf` function:

> Paragraph 10 discusses conversion. Paragraph 12 on "`a,e,f,g`" conversion
> specifiers discusses format. Neither discuss accuracy of the decimal to binary
> conversion, e.g., it is not specified.
>
> What is the accuracy of floating-point string to internal representation
> conversions? Is it the same as translation time? Is it the same as `strtod`? Is
> it undefined behavior if the value is not exactly representable? Is it round to
> nearest? Is it affected by the current rounding mode, e.g., correctly rounded?

7.20.1.3 The `strtod` ... functions:

> What is the required accuracy of `strtod` family functions? It appears to be
> either not specified or the same as 6.4.4.2. It appears to depend upon what
> paragraph 4 "interpreted as a floating constant according to the rules of
> 6.4.4.2" means.

### Suggested Changes

Changes to 7.19.6.1 The `fprintf` function:

Add near paragraph 11 before Recommended practice:

> The roundings used by %`f`, %`F`, %`e`, and %`E` shall be the same and shall
> have an accuracy of better than 1 ulp in round to nearest and better than 2 ulp
> in other roundings.

Changes to 7.19.6.2 The `fscanf` function:

In paragraph 12, "`a,e,f,g`" conversion specifier, add the sentence:

> The accuracy of this conversion shall be no worse than that of `strtold` for the
> same subject.

Change 7.20.1.3 The `strtod` ... functions:

In paragraph 4, change "rules of 6.4.4.2" to "rules of 6.4.4.2 (including
accuracy requirements)"

Add a third recommended practice paragraph:

> Conversions done by `strtod` family functions and `fscanf` family functions of
> the same valid floating-point subject string shall produce the same value.

An alternative (not liked by this author) to all of the above is to add to
5.2.4.2.2 Characteristics of floating types \<`float.h`\> in paragraph 4 before
"and": ", binary-decimal conversions(footnote),".

> footnote: binary-decimal covers both string to internal representations and
> internal to string representations, and covers any pair of bases.

---

Comment from WG14 on 2001-09-18:

### Committee Discussion

5.2.4.2.2 paragraph 4 (which covers the accuracy of `+`, `-`, `*`, `/`, and math
library functions) does not cover decimal \<--\> binary conversions. Therefore,
the rest of 5.2.4.2.2 covers these conversions (F.P. characteristics must meet
the minimum-maximum requirements for the \<`float.h`\> parameters (even though
the exact model need not be followed)). That appears to require that the actual
representation be able to express \>\= `FLT`/`DBL`/`LDBL_DIG` digits precise to
the last of those digits (for decimal to binary conversions) and \>\=
`DECIMAL_DIG` digits (for binary to decimal conversions).

6.3.1.5 para. 1 implies that the different widths of F.P. types must have
similar representations differing only in number of bits in exponent, mantissa,
and padding.

In 7.19.6.1 `f,F` format, the value is rounded to the appropriate number of
digits, which indicates that the displayed value differs from the "numerical"
value only with regard to that rounding. (Of course, *all* the `fprintf`
conversions of numeric values to display form are on the assumption that what is
displayed is the same value as the numeric value, but in human-comprehensible
form and subject to specified rounding etc.)

7.20.1.3 says that the numeric string is interpreted as a value according to the
rules in 6.4.4.2 for floating constants.

Details of rounding are not specified, although certain modes are described in
5.2.4.2.2.

The latitude allowed for inexactness by the standard applies only to precision
of representation and to rounding mode.

---

Comment from WG14 on 2001-09-18:

### Technical Corrigendum

Change 5.2.4.2.2 paragraph #4 to:

> The accuracy of the floating-point operations ( `+`, `-`, `*`, `/`) and of the
> library functions in \<`math.h`\> and \<`complex.h`\> that return floating-point
> results is implementation defined, as is the accuracy of the conversion between
> floating-point internal representations and string representations performed by
> the libray routine in \<`stdio.h`\>, \<`stdlib.h`\> and \<`wchar.h`\>. The
> implementation may state that the accuracy is unknown.
