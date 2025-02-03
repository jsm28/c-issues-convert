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
