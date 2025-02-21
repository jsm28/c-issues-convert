## Issue 0228: `wmemcmp` declaration in Annex B

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Bill Plauger (US)  
Date: 2000-04-10  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_228.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_228.htm)

### Summary

The `wmemcmp` declaration in Annex B should not have `restrict` for the
arguments, and the first argument should be a `const`.

---

Comment from WG14 on 2000-11-02:

### Technical Corrigendum

In Annex B, change:

> ```c
> int wmemcmp(wchar_t * restrict s1, const wchar_t * restrict s2, size_t n);
> ```

to:

> ```c
> int wmemcmp(const wchar_t *s1, const wchar_t *s2, size_t n);
> ```

Also, `wmemcmp` should follow `wcsncpy`, `wmemcpy` and `wmemmove` should follow
`wcsxfrm`, and `wcslen` should follow `wmemchr`.
