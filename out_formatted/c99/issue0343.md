## Issue 0343: Initializing qualified wchar\_t arrays

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Joseph Myers \<joseph@codesourcery.com\>, Joseph Myers (UK)  
Date: 2007-03-24  
Reference document: [ISO/IEC WG14 N1224](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1224.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_343.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_343.htm)

### Summary

6.7.8 paragraph 15 says:

> \[#15\] An array with element type compatible with `wchar_t` may be initialized
> by a wide string literal, optionally enclosed in braces. \[...\]

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

---

Comment from WG14 on 2007-09-07:

### Proposed Technical Corrigendum

Change 6.7.8 paragraph 15:

> "`wchar_t`"

to

> "a qualified or unqualified version of `wchar_t`".
