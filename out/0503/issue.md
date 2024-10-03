### Summary

C11 7.22.1.3 paragraph 3 bullet 2 says:

> a `0x` or `0X`, then a nonempty sequence of hexadecimal digits optionally
> containing a decimal-point character, then an optional binary exponent part as
> defined in 6.4.4.2;

but the grammar in C11 6.4.4.2 makes the binary-exponent-part mandatory, not
optional.

**Suggested resolution**

Strike "optional" before "binary exponent part" and add a comma before "as
defined in" to highlight that "as defined in" applies to the entire sentence,
not only to the last part.
