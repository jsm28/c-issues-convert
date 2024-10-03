### Summary

It has been noted that the descriptions for 7.24.2.1 `memcpy`, 7.24.2.2
`memmove` and 7.24.4.1 `memcmp` are written using the term *character* which is
inconsistent with their design as *memory* functions. Moreover, if one then
reads 3.7.2 as allowing character to mean multibyte character, it is thought
that confusion could arise as to whether the number of multibyte characters
should be supplied rather than the number of bytes.

Although it is clear by 7.24.1 *String function conventions* paragraph 3

> For all functions in this sub clause, each character shall be interpreted as if
> it had the type `unsigned char`

that the number of bytes to be used corresponds to the size of a `unsigned
char`, one has to reference 6.2.6 *Representation of types* to learn that
`unsigned char` is in fact a single byte (consisting of `CHAR_BIT` bits).

It would be simpler and more to the point if the three memory functions describe
their count parameter `n` in terms of bytes.

### Suggested Technical Corrigendum

**memcpy**

Change 7.24.2.1 p 2 first sentence from

> The `memcpy` function copies `n` <u>characters</u> from the object pointed to by
> `s2` into the object pointed to by `s1`.

to

> The `memcpy` function copies `n` <u>bytes</u> from the object pointed to by `s2`
> into the object pointed to by `s1`.

**memmove**

Change 7.24.2.2 p 2 from

> The `memmove` function copies `n` <u>characters</u> from the object pointed to
> by `s2` into the object pointed to by `s1`. Copying takes place as if the `n`
> <u>characters</u> from the object pointed to by `s2` are first copied into a
> temporary array of `n` <u>characters</u> that does not overlap the objects
> pointed to by `s1` and `s2`, and then the `n` <u>characters</u> from the
> temporary array are copied into the object pointed to by `s1`.

to

> The `memmove` function copies `n` <u>bytes</u> from the object pointed to by
> `s2` into the object pointed to by `s1`. Copying takes place as if the `n`
> <u>bytes</u> from the object pointed to by `s2` are first copied into a
> temporary array of `n` <u>bytes</u> that does not overlap the objects pointed to
> by `s1` and `s2`, and then the `n` <u>bytes</u> from the temporary array are
> copied into the object pointed to by `s1`.

**memcmp**

Change 7.24.4.1 p 2 from

> The `memcmp` function compares the first `n` <u>characters</u> of the object
> pointed to by `s1` to the first `n` <u>characters</u> of the object pointed to
> by `s2`.

to

> The `memcmp` function compares the first `n` <u>bytes</u> of the object pointed
> to by `s1` to the first `n` <u>bytes</u> of the object pointed to by `s2`.
