### Summary

Consider a constant 9223372036854775808 in a C99 implementation that has 64-bit
two's complement `long long`, and no extended integer types.

6.4.4.1 says that an unsuffixed decimal constant has the first of the types on
the following list into which its value will fit: `int`, `long int`, `long long
int`. In this case, the value does not fit into any of those types, and there
are no extended integer types to try. (The value would fit into unsigned long
long, but that's not on the list.)

So I conclude that this constant is invalid, just as a grossly too-large
constant (say, one consisting of a 1 followed by 1,000 zeroes) would be invalid.
(And I think that's a good thing, because otherwise this constant could be
unsigned on some implementations and signed on others that have larger extended
integer types.)

However, I'm not sure 6.4.4.1 (or 6.4.4) says anything that requires an error,
or even gives meaning to this constant. It doesn't say what happens if the
constant doesn't fit in any type on its list and there are no extended integer
types.

Is this a defect, or was this intentionally worded vaguely to allow latitude to
implementations?

A related issue comes up with `UINT64_C(9223372036854775808)`. One plausible
implementation for the macro `UINT64_C` would seem to be to cast the constant to
the proper type. However, that does not work in this particular case, because
the constant before casting is the same invalid constant discussed above.
Another plausible implementation (and suggested by 7.18.4.1p2) is to concatenate
a suffix to the constant, e.g., a "U" in this case. Sounds good, but 7.18.4p2
doesn't say that the argument to the macro must be an unsuffixed constant;
indeed it says that the syntax must match 6.4.4.1, which implies that a suffix
is allowed.

So if 9223372036854775808 is an invalid constant, it seems that an
implementation must rely on compiler magic to get `UINT64_C` right; the tricks
available with standard macros don't work.

### Suggested Technical Corrigendum
