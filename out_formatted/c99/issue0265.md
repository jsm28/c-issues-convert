## Issue 0265: preprocessor arithmetic

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_265.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_265.htm)

### Problem

Assume that both compile-time and run-time arithmetic have 2's complement, no
trap representations, 8/16/32/48/64 bit integer types. Consider the code:

```c
  #if -0xFFFFFFFF < 0
```

Is this expression true or false ? 6.10.1#3 reads, in part:

> and then each preprocessing token is converted into a token. The resulting
> tokens compose the controlling constant expression which is evaluated according
> to the rules of 6.6, except that all signed integer types and all unsigned
> integer types act as if they have the same representation as, respectively, the
> types `intmax_t` and `uintmax_t` defined in the header `<stdint.h>`.

Does the "except" wording apply to the conversion to a token, or only to the
evaluation of the expression ? If the former, then 0xFFFFFFFF can be represented
in an `int` (`intmax_t`), it has a signed type, and the expression is true. If
the latter, 0xFFFFFFFF cannot be represented in an `int` but can be represented
in an `unsigned int`, so it has unsigned type and the expression is false.

I believe that the former was intended, with the preprocessor only having to
consider one pair of integer types.

### Suggested Technical Corrigendum

Change the cited text to:

> and then each preprocessing token is converted into a token. The resulting
> tokens compose the controlling constant expression which is evaluated according
> to the rules of 6.6. **For the purposes of the conversion and evaluation** all
> signed integer types and all unsigned integer types act as if they have the same
> representation as, respectively, the types `intmax_t` and `uintmax_t` defined in
> the header `<stdint.h>`.

(bold type shows the changed words)

Add a footnote reference to the end of this text, and add the footnote:

> 140a Thus on an implementation where `INT_MAX` is 0x7FFF and `UINT_MAX` is
> 0xFFFF, the constant 0x8000 is signed within a `#if` expression even though it
> is unsigned in translation phase 7\.

---

Comment from WG14 on 2002-05-15:

### Technical Corrigendum

Change 6.10.1#3 to read:

> ...
>
> and then each preprocessing token is converted into a token. The resulting
> tokens compose the controlling constant expression which is evaluated according
> to the rules of 6.6. For the purposes of this token conversion and evaluation
> all signed integer types and all unsigned integer types act as if they have the
> same representation as, respectively, the types `intmax_t` and `uintmax_t`
> defined in the header `<stdint.h>`.

Add a footnote to the end of 6.10.1#3 to read:

> Thus on an implementation where `INT_MAX` is 0x7FFF and `UINT_MAX` is 0xFFFF,
> the constant 0x8000 is signed and positive within a `#if` expression even though
> it is unsigned in translation phase 7\.
