## Issue 0463: Left-shifting into the sign bit

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Aaron Ballman  
Date: 2014-04-02  
Reference document: [N1817](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1817.pdf)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Harmonizing left-shift with C\+\+14

It is not uncommon to see code such as:

```c
signed someint_t min_value = 1 << (CHAR_BIT * sizeof(someint_t));
```

However, left-shifting a one bit into the sign bit is undefined behavior,
despite the fact that the majority of (twos-complement) architectures handle it
properly.

### Suggested Technical Corrigendum

6.5.7p4 should be modified to read:

> The result of `E1 << E2` is `E1` left-shifted `E2` bit positions; vacated bits
> are filled with zeros. If `E1` has an unsigned type, the value of the result is
> `E1 x 2`<sup>`E2`</sup>, reduced modulo one more than the maximum value
> representable in the result type. If `E1` has a signed type and nonnegative
> value, and `E1 x 2`<sup>`E2`</sup> is representable in the <ins>corresponding
> unsigned type of the</ins> result type, then that <ins>value, converted to the
> result type,</ins> is the resulting value; otherwise, the behavior is undefined.

C\+\+ addressed this in C\+\+14 with DR1457 with identical wording
modifications.

---

Comment from WG14 on 2015-04-17:

Apr 2014 meeting

### Proposed Committee Response

This is not a defect.

The committee will track this and consider it for the next revision of the
standard.
