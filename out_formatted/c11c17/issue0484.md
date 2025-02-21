## Issue 0484: invalid characters in `strcoll()`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman  
Date: 2015-06-23  
Reference document: [N1944](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1944.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

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

---

Comment from WG14 on 2016-10-21:

Oct 2015 meeting

### Committee Discussion

> The committee agrees that the standard does not specify behavior under these
> conditions and as such there is undefined behavior by way of §7.1.4p1 “If an
> argument to a function has an invalid value … the behavior is undefined”. There
> is strong sentiment to keep the library fast and that imposing new requirements
> to set `errno` is to be generally avoided. Whereas POSIX does define behavior
> that sets `errno` under these conditions, it is explicitly the intent of the
> committee to leave such behavior undefined in the standard to allow such
> refinements by others.

### Proposed Committee Response

> By way of §7.1.4p1 “If an argument to a function has an invalid value … the
> behavior is undefined” the behavior of `strcoll` in the face of invalid input is
> already clearly undefined. The committee wishes to leave it so specified. This
> latitude allows POSIX to further refine the semantics according to their needs.
> We therefore do not accept the Proposed Technical Corrigendum.
