## Issue 0023: If 99,999 is larger than `DBL_MAX_10_EXP`, what is the result of `strtod("0.0e99999", &ptr)`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-003  
Submitted against: C90  
Status: Closed  
Cross-references: [0025](issue0025.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_023.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_023.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

According to our response to [Defect Report #025, Question 1](issue0025.md), the
result of `strtod("0.0e99999", &ptr)` is exactly representable, i.e., it lies
within the range of representable values. Therefore, by subclause 7.10.1.4,
**Returns**, the value zero shall be returned in this case, and `errno` shall
not be set. (This means that implementations have to test for the special case
of zero when creating floating-point representations from characters.)

Note also that `strtod("0.0e-99999", &ptr)` is not a case of underflow, so
`errno` shall not be set to `ERANGE` in this case either.
