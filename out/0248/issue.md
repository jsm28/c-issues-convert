### Problem

The types `sig_atomic_t` and `wchar_t` are optional on freestanding
implementations, since they don't have to provide the relevant headers. But the
limits `SIG_ATOMIC_MIN`, `SIG_ATOMIC_MAX`, `WINT_MIN`, and `WINT_MAX` are in
`<stdint.h>`, which all implementations must provide. So a freestanding
implementation must provide limits for types which it doesn't implement.

### Suggested Technical Corrigendum

Append to 7.18.3#2:

> A freestanding implementation shall only define the symbols corresponding to
> those typedef names it actually provides.
