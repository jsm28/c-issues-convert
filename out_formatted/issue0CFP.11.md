## Issue 0CFP.11: Part 2: a-style formatting not IEC 60559 conformant

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The `a`-style formatting specified in subclause 12.5 of TS 18661-2 is not an IEC
60559 conversion for cases where the formatting precision is less than the
length of the coefficient of the input. The specification entails an
intermediate rounding to the floating type of the input, which might overflow
resulting in a character sequence representation of infinity. IEC 60559
conversions to character sequences do not overflow, unless the language
over-restricts the exponent range for character sequence output, which C does
not.

Another undesirable aspect of the current specification is that in certain cases
it produces results with more precision than given by a width modifier.

Here are some examples, showing the result of the intermediate conversion, with
different behaviors for the current spec (“old”) and the spec in the suggested
Technical Corrigendum below (“new”):

For `_Decimal32` input *x* with representation (1, 9512345, 90\) and specifier
...

```c
%.3Ha
```

old:                           *x*                -\>             (1, 9510000,
90\)                -\>             `9.510000e96`

new:                         *x*                -\>             (1, 951,
94\)                            -\>             `9.51e96`

```c
%.2Ha
```

old:                           *x*                -\>             (1, 9500000,
90\)                -\>             `9.500000e96`

new:                         *x*                -\>             (1, 95,
95\)                               -\>             `9.5e96`

```c
%.1Ha
```

old:                           *x*                -\>            
Inf                                                -\>             `inf`

new:                         *x*                -\>             (1, 1,
97\)                                  -\>             `1e97`

Here’s another example:

For `_Decimal32` input x with representation (1, 9512345, 86\) and specifier ...

```c
%.2Ha
```

old:                           *x*                -\>             (1, 950,
90\)                            -\>             `9.50e92`

new:                         *x*                -\>             (1, 95,
91\)                               -\>             `9.5e92`

The examples use a to-nearest rounding.

As the examples illustrate, the problematic cases for the current “old” spec
occur because of the exponent range limitation of the format used for the
intermediate conversion.

The suggested Technical Corrigendum below specifies formatting that is IEC 60559
conformant and which honors a width modifier. It does not change the numerical
value of the result, except in overflow cases.

### Suggested Technical Corrigendum

In 12.5, in the addition to 7.21.6.1#8 and 7.29.2.1#8, under `a`,`A` conversion
specifiers, change:

> If the precision is present (in the conversion specification) and is zero or at
> least as large as the precision *p* (5.2.4.2.2) of the decimal floating type,
> the conversion is as if the precision were missing. If the precision is present
> (and nonzero) and less than the precision *p* of the decimal floating type, the
> conversion first obtains an intermediate result by rounding the input in the
> type, according to the current rounding direction for decimal floating-point
> operations, to the number of digits specified by the precision, then converts
> the intermediate result as if the precision were missing. The length of the
> coefficient of the intermediate result is the smallest number, at least as large
> as the formatting precision, for which the quantum exponent is within the
> quantum exponent range of the type (see 5.2.4.2.2a). The intermediate rounding
> may overflow.

to:

> If the precision *P* is present (in the conversion specification) and is zero or
> at least as large as the precision *p* (5.2.4.2.2) of the decimal floating type,
> the conversion is as if the precision were missing. If the precision *P* is
> present (and nonzero) and less than the precision *p* of the decimal floating
> type, the conversion first obtains an intermediate result as follows, where *n*
> is the number of significant digits in the coefficient:
>
> > If *n* \<\= *P*, set the intermediate result to the input.
> >
> > If *n* \> *P*, round the input value, according to the current rounding
> > direction for decimal floating-point operations, to *P* decimal digits, with
> > unbounded exponent range, representing the result with a *P*-digit integer
> > coefficient when in the form (*s*, *c*, *q*).
>
> Convert the intermediate result in the manner described above for the case where
> the precision is missing.

In 12.5, in the addition to 7.21.6.1#8 and 7.29.2.1#8, in EXAMPLE 3, change the
results:

> ```c
> 9.54321e+93
>
> 9.5432e+93
>
> 9.543e+93
>
> 9.540e+93
>
> 9.500e+93
>
> 1.0000e+94
>
> inf
> ```

to:

> ```c
> 9.54321e+93
>
> 9.5432e+93
>
> 9.543e+93
>
> 9.54e+93
>
> 9.5e+93
>
> 1e+94
>
> 1e+97
> ```

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

Apr 2017 meeting

### Committee Discussion

The paper [N2126](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2126.htm)
provides an example that illustrates this change, and the committee agreed to
accept this as an addendum to the Proposed Technical Corrigendum.

However, the committee is concerned that `%a` behavior differs from binary
floating point and more review is needed. In particular, there were concerns
that for the decimal floating point types now the %a format specifier given with
a precision is the total number of significant digits, not the number of digits
after the decimal point as it has been for other data types.

### Proposed Technical Corrigendum

In 12.5, in the addition to 7.21.6.1#8 and 7.29.2.1#8, under `a`,`A` conversion
specifiers, change:

> If the precision is present (in the conversion specification) and is zero or at
> least as large as the precision *p* (5.2.4.2.2) of the decimal floating type,
> the conversion is as if the precision were missing. If the precision is present
> (and nonzero) and less than the precision *p* of the decimal floating type, the
> conversion first obtains an intermediate result by rounding the input in the
> type, according to the current rounding direction for decimal floating-point
> operations, to the number of digits specified by the precision, then converts
> the intermediate result as if the precision were missing. The length of the
> coefficient of the intermediate result is the smallest number, at least as large
> as the formatting precision, for which the quantum exponent is within the
> quantum exponent range of the type (see 5.2.4.2.2a). The intermediate rounding
> may overflow.

to:

> If the precision *P* is present (in the conversion specification) and is zero or
> at least as large as the precision *p* (5.2.4.2.2) of the decimal floating type,
> the conversion is as if the precision were missing. If the precision *P* is
> present (and nonzero) and less than the precision *p* of the decimal floating
> type, the conversion first obtains an intermediate result as follows, where *n*
> is the number of significant digits in the coefficient:
>
> > If *n* \<\= *P*, set the intermediate result to the input.
> >
> > If *n* \> *P*, round the input value, according to the current rounding
> > direction for decimal floating-point operations, to *P* decimal digits, with
> > unbounded exponent range, representing the result with a *P*-digit integer
> > coefficient when in the form (*s*, *c*, *q*).
>
> Convert the intermediate result in the manner described above for the case where
> the precision is missing.

In 12.5, in the addition to 7.21.6.1#8 and 7.29.2.1#8, in EXAMPLE 3, change the
results:

> ```c
> 9.54321e+93
>
> 9.5432e+93
>
> 9.543e+93
>
> 9.540e+93
>
> 9.500e+93
>
> 1.0000e+94
>
> inf
> ```

to:

> ```c
> 9.54321e+93
>
> 9.5432e+93
>
> 9.543e+93
>
> 9.54e+93
>
> 9.5e+93
>
> 1e+94
>
> 1e+97
> ```

Add, as a new EXAMPLE,

```c
#include <stdio.h>

int main(void) {
  _Decimal32 x = 9512345e90df;
  _Decimal32 x2 = 9512345e86df;

  printf("%.3Ha\n", x); // New expected output: 9.51e96
  printf("%.2Ha\n", x); // New expected output: 9.5e96
  printf("%.1Ha\n", x); // New expected output: 1e97
  printf("%.2Ha\n", x2); // New expected output: 9.5e92

  return 0;
}
```
