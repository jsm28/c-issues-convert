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
