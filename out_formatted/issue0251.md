## Issue 0251: are `struct fred` and `union fred` the same type ?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_251.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_251.htm)

### Problem

Consider the code:

```c
 union fred { int a; }
    int main (void)
    {
        struct fred *ptr;  /* Line X */
        // ...
```

I can see nothing that forbids this code. In particular, 6.7.2.3#8 reads:

> \[#8] If a type specifier of the form
>
> ```c
>         struct-or-union identifier
> ```
>
> or
>
> ```c
>         enum identifier
> ```
>
> occurs other than as part of one of the above forms, and a declaration of the
> identifier as a tag is visible, then it specifies the same type as that other
> declaration, and does not redeclare the tag.

At line X a declaration of `fred` as a tag is visible, so this line specifies
the same type as that other declaration, even though this uses `struct` and that
uses `union` !

It has been further pointed out to me that nothing in the Standard actually says
that `union x` is a union type as opposed to a structure type, and vice versa.

### Suggested Technical Corrigendum

Append to 6.7.2.1#6:

> The keywords `struct` and `union` indicate that the type being specified is,
> respectively, a structure type or a union type.

Add a new paragraph following 6.7.2.3#1:

> \[#1a] Where two declarations that use the same tag declare the same type, they
> shall both use the same choice of `struct`, `union`, or `enum`.

---

Comment from WG14 on 2006-03-29:

### Committee Discussion

The Committee is inclined to accept the suggested TC, but the issue is still
being debated.

### Technical Corrigendum

Append to 6.7.2.1#6:

> The keywords `struct` and `union` indicate that the type being specified is,
> respectively, a structure type or a union type.

Add a new paragraph following 6.7.2.3#1:

> \[#1a] Where two declarations that use the same tag declare the same type, they
> shall both use the same choice of `struct`, `union`, or `enum`.
