### Summary

With reference to ISO/IEC WG14 N1569, subclause 7.20.4.1: The macro
`UINT`*`N`*`_C(`*`value`*`)` shall expand to an integer constant expression
corresponding to the type `uint_least`*`N`*`_t`.

7.20.4 p1 imposes a stricter requirement on the form of the expansion; it must
be an integer constant (for which paragraph 2 points to 6.4.4.1).

The type described in 7.20.4 p3 for the result of the expansion has an
interesting property; we observe this for `uint_least16_t` without reference to
the `UINT16_C` macro by using `u'\0'` in a context where it will be first
promoted as part of the usual arithmetic conversions:

```c
#include <assert.h>

#if u'\0' - 1 < 0
  // Types: #if (uint_least16_t) - (signed int) < (signed int)
  // Due to 6.10.1 p4, near the reference to footnote 167,
  // after applying the integer promotions as part of 6.3.1.8 p1
  // to the operands of the subtraction, the expression becomes:
  // Types: #if (unsigned int) - (signed int) < (signed int)
  // Following 6.3.1.8 p1 through to the last point gives:
  // Types: #if (unsigned int) - (unsigned int) < (signed int)
  // Result: false
# error Expected large unsigned value.
#endif

int main(void) {
  // Types: assert((uint_least16_t) - (signed int) < (signed int))
  // Assuming that signed int can represent all values of uint_least16_t,
  // after applying the integer promotions as part of 6.3.1.8 p1
  // to the operands of the subtraction, the expression becomes:
  // Types: assert((signed int) - (signed int) < (signed int))
  // Result: true
  assert(u'\0' - 1 < 0);
  return 0;
}
```

The code presented should neither fail to compile nor abort when executed (for
example) on a system using two's complement and 8, 16 and 32 bits (respectively)
for `char`, `short` and `int` with no padding bits.

Consider the case for N \= 8 or 16 on systems with `INT_MAX` as \+2147483647,
`UCHAR_MAX` as 255 and `USHRT_MAX` as 65535: it is unclear how a macro can be
formed such that it expands to an integer constant that has the promoted signed
int type in phase 7 of translation and also the promoted `unsigned int` type in
phase 4 of translation without special (non-standard) support from the compiler.

Even if the requirement for an integer constant is relaxed to only require an
integer constant expression, the case for N \= 8 on systems with `INT_MAX` as
\+32767 and `UCHAR_MAX` as 255 remains a problem without the use of casts (since
`uint_least16_t`, for which we can form a literal, has different promotion
behaviour from `uint_least8_t`).

Implementations seen:

1. `#define UINT8_C(c) c ## U`
2. `#define UINT8_C(c) c`

DR 209 seemed to try to address the issue of needing special compiler support in
order to define the macros for integer constants; however, the problem seems to
remain.

### Suggested Technical Corrigendum

1. Add in suffixes for char and short literals.
2. Remove the `UINT{8,16}_C` macros from the standard.
