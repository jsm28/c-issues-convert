Assuming that 99999 is larger than `DBL_MAX_10_EXP`, what is the result of:

```c
strtod("0.0e99999", &ptr);
```

Is it 0.0, `HUGE_VAL`, or undefined?

Subclause 6.1.3.1 **Floating constants** on page 26, lines 30-32 says: “The
significand part is interpreted as a decimal rational number; the digit sequence
in the exponent part is interpreted as a decimal integer. The exponent indicates
the power of 10 by which the significand part is to be scaled.” In this case
`0.0e99999` means 0.0 times 10 to the power 99999, or 0.0x10<sup>99999</sup>,
which has a scaled value of 0.0; therefore, return 0.0.

Subclause 7.10.1.4 **The `strtod` function** on page 151, lines 12-14 says: “If
the correct value is outside the range of representable values, plus or minus
`HUGE_VAL` is returned (according to the sign of the value), and the value of
the macro `ERANGE` is stored in `errno`.” Since the exponent (99999 in this
case) is larger than `DBL_MAX_10_EXP`, the value is outside the range of
representable values (overflow). Therefore, return `HUGE_VAL`.

Subclause 5.2.4.2.2 **Characteristics of floating types \<`float.h>`**, pages
14-16, describes the model that defines the floating-point types. The number
`0.0e99999`, as written, is not part of that model (it cannot be represented
since the exponent is larger than *e<sub>max</sub>*). From subclause 6.2.1.4
**Floating types** page 35, lines 11-13, “... if the value being converted is
outside the range of values that can be represented, the behavior is undefined.”
Therefore, since this number, as written, has no representation, the behavior is
undefined.