## Issue 0006: How does `strtoul` behave when presented with a subject sequence that begins with a minus sign?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Walter J. Murray, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-020  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_006.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_006.html)

It is unclear how the `strtoul` function behaves when presented with a subject
sequence that begins with a minus sign. The `strtoul` function is described in
subclause 7.10.1.6, which contains the following statements.

> If the subject sequence begins with a minus sign, the value resulting from the
> conversion is negated.
>
> If the correct value is outside the range of representable values, `ULONG_MAX`
> is returned, and the value of the macro `ERANGE` is stored in `errno`.

Assume a typical 32-bit, two's-complement machine with the following limits.

```c
LONG_MIN    -2147483648
 LONG_MAX         2147483647
 ULONG_MAX        4294967295
```

Assuming that the value of `base` is zero, how should `strto ul` behave (return
value and possible setting of `errno`) when present ed with the following
sequences? Case 1: `"-2147483647"` Case 2: `"-2147483648"` Case 3:
`"-2147483649"`

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citations are the ones supplied by you from subclause 7.10.1.6: If
the subject sequence begins with a minus sign, the value resulting from the
conversion is negated. If the correct value is outside the range of
representable values, `ULONG_MAX` is returned, and the value of the macro
`ERANGE` is stored in `errno`. The Committee believes that there is only one
sensible interpretation of a subject sequence with a minus sign: If the subject
sequence (neglecting the possible minus sign) is outside the range \[0,
`ULONG_MAX`], then the range error is reported. Otherwise, the value is
negated(as an `unsigned long int`). The answers to your numeric questions are:

Case 1: 2,147,483,649

Case 2: 2,147,483,648

Case 3: 2,147,483,647
