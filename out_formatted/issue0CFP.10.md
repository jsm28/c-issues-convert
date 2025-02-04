## Issue 0CFP.10: Part 1: wrong type for **fesetmode** parameter

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14358:

> TS 18661-1 gives the declaration of `fesetmode` as:
>
> ```c
> int fesetmode(const fenv_t *modep);
> ```
>
> The argument should be of type `const femode_t *`, not `const fenv_t *`.
>
> \--

This was an editorial cut-and-past error. The Description says the argument
`modep` shall point to an objet set by a call to `fegetmode`, which sets objects
of type `femode_t`. It’s unlikely the function would be implemented with the
erroneous type.

### Suggested Technical Corrigendum

In 15.3, in the new text for C 7.6.3.1a#1, change:

```c
          int fesetmode(const fenv_t *modep);
```

to:

```c
          int fesetmode(const femode_t *modep);
```

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In 15.3, in the new text for C 7.6.3.1a#1, change:

```c
          int fesetmode(const fenv_t *modep);
```

to:

```c
          int fesetmode(const femode_t *modep);
```
