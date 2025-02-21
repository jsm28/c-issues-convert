## Issue 0263: all-zero bits representations

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_263.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_263.htm)

### Problem

Consider the code:

```c
   int v [10];
    memset (v, 0, sizeof v);
```

Most programmers would expect this code to set all the elements of `v` to zero.
However, the code is actually undefined: it is possible for `int` to have a
representation in which all-bits-zero is a trap representation (for example, if
there is an odd-parity bit in the value).

Consider also:

```c
   int *p;
    p = calloc (n_members, sizeof (int));
```

This problem applies to all integer types except for `unsigned char`. I believe
that the idiom is well-enough known that it should be made a part of the
Standard.

### Suggested Technical Corrigendum

Append to 6.2.6.2#5:

> For any integer type, the object representation where all the bits are zero
> shall be a representation of the value zero in that type.

---

Comment from WG14 on 2002-03-07:

### Technical Corrigendum

Append to 6.2.6.2#5:

> For any integer type, the object representation where all the bits are zero
> shall be a representation of the value zero in that type.
