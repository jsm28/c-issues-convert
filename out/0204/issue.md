### Summary

`size_t` and `ptrdiff_t` can now be a `long long` type, which is not necessary
for hardwares that do not support 64-bit addressing. Implementors should be
encouraged to choose a type for these two that minimizes compatibility problems
to existing (32-bit) code.

### Suggested Correction

In 7.17 at the end of p2, add the following:

> **Recommended Practice**
>
> The `long long` type should be used only if no other integer types can represent
> the value range required by the implementation.
