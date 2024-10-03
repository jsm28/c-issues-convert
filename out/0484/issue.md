### Summary

7.24.4.3 strcoll makes the assumption that the result of comparing two strings
can only have one of three outcomes: greater than, equal to, or less than.
However, there is a fourth outcome that is possible: not comparable.

I have been told that there are locales or codesets that have strings of bytes
that do not form valid characters. Those invalid characters could be considered
Not-a-Character (similar to Not-a-Number for floating-point). And, they are not
comparable to anything.

I do not know if the same issue can apply to wchar\_t. If so, then 7.29.4.4.1
wcscmp(), 7.29.4.4.3 wcsncmp(), and 7.29.4.4.5 wmemcmp() have the same problem.

### Suggested Technical Corrigendum

Replace the start of 7.24.4.3, paragraph 3,

> The **strcoll** ...

with

> If either string contains invalid characters, **errno** is set to an
> implementation defined value and the return value is unspecified; otherwise,
> **errno** is left alone and the **strcoll** ...

The same change should also be applied to 7.29.4.4.2 wcscoll.
