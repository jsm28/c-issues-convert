### Summary

6.7.8 paragraph 15 says:

> \[#15] An array with element type compatible with `wchar_t` may be initialized
> by a wide string literal, optionally enclosed in braces. \[...]

What of arrays with element type a qualified version of `wchar_t`? Is

```c
    #include <stddef.h>
    const wchar_t x[] = L"foo";
```

valid? Surely it must be intended to be, but the type `const wchar_t` isn't
compatible with `wchar_t`.

(The validity for character strings (paragraph 14\) depends on "character type"
including qualified character types. The definition of character types in 6.2.5
paragraph 15 does not mention qualified types. Other parts of the Standard also
make more sense if "character type" is taken to include qualified character
types; for example, 6.5 paragraph 7 of which the last point says "a character
type" but the first four points come in matching pairs for qualified and
unqualified types, and 6.3.2.3 paragraph 7.)

### Suggested Technical Corrigendum

6.7.8 paragraph 15, change "`wchar_t`" to "a qualified or unqualified version of
`wchar_t`".
