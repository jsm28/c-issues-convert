There are many places in C11 that assume a floating-point zero value, e.g., 0.0,
is representable.

* 6.3.1.7 Real and complex #1 has:
  > When a value of real type is converted to a complex type, the real part of the
  > complex result value is determined by the rules of conversion to the
  > corresponding real type and the imaginary part of the complex result value is a
  > positive zero or an unsigned zero.
* 6.7.9 Initialization, #10 (second bullet) has (for static and thread storage initialzation):
  > if it has arithmetic type, it is initialized to (positive or unsigned) zero;
* 7.22.1.3 The strtod, strtof, and strtold functions, #10 has:
  > If no conversion could be performed, zero is returned.
* 7.29.4.1.1 The wcstod, wcstof, and wcstold functions, #10 has:
  > If no conversion could be performed, zero is returned.
* Annex F and Annex G, being based upon IEEE-754, require signed floating-point zeros.

There are many places in C11 that allow for a representable floating-point zero
value.

* 5.2.4.2.2 Characteristics of floating types \<float.h\> #4 has:
  > An implementation may give zero and values that are not floating-point numbers
  > (such as infinities and NaNs) a sign or may leave them unsigned.
* 7.3.3 Branch cuts, #1 and #2 talk about signed zeros.
* 7.6 Floating-point environment \<fenv.h\>, #6, lists **FE\_DIVBYZERO** (divide-by-zero) as a possible floating-point exception. And, 7.12.1 Treatment of error conditions gives more details.
* 7.12 Mathematics \<math.h\> #6 says that zero, subnormal, normal, NaN, and infinite are mutually exclusive kinds of floating-point values. And 7.12.3.1 The fpclassify macro uses those classification macros.
* 7.12.3.2 The isfinite macro, #2 says that zero is a finite value.
* 7.12.3.5 The isnormal macro, #2 says that zero is not a normal value.
* 7.12.\*; many of the math functions (atan2, frexp, ilogb, log, log10, log2, logb, pow, lgamma, tgamma, fmod, remainder, remquo, copysign) mention zero as special cases.

The C Rationale in its discussion of 5.2.4.2.2 has:

> Note that the floating-point model adopted permits all common representations,
> including sign-magnitude and two's-complement, but precludes a logarithmic
> implementation.
>
> The C89 Committee also endeavored to accommodate the IEEE 754 floating-point
> standard by not adopting any constraints on floating-point which were contrary
> to that standard.

However, if one carefully reads 5.2.4.2.2 Characteristics of floating types
\<float.h\>, #2 and #3, one finds that zero is not required to be representable.
As I read those paragraphs, normalized floating-point numbers are the only
things required to be contained in floating types. Subnormal floating-point
numbers, unnormalized floating-point numbers, infinities, and NaNs are
additional (optional) things that may be contained in floating types. Zero is
not mentioned explicitly.

So, it appears that some parts of C11 require that floating-point zeros be
representable, while other parts do not require that they be representable.

I think that the first sentance in 5.2.4.2.2 #3 should be changed to:

> Floating types shall be able to represent normalized floating-point numbers
> (f<sub>1</sub> \> 0 if x !\= 0\) and (positive or unsigned) zero. In addition,
> floating types may be able to contain other kinds of floating-point numbers,
> such as negative zero and subnormal ...
