### Problem

7.21.2.1#2 defines the operation of `memcpy` as:

> \[#2] The `memcpy` function copies n characters from the object pointed to by
> `s2` into the object pointed to by `s1`.

7.21.2.3#2 defines the operation of `strcpy` as:

> \[#2] The `strcpy` function copies the string pointed to by `s2` (including the
> terminating null character) into the array pointed to by `s1`.

Other functions in 7.21 refer to either a string or a set of characters in the
same way. The definition of "string" is in 7.1.1#1:

> \[#1] A *string* is a contiguous sequence of characters terminated by and
> including the first null character.

and that of "character" is in 3.7:

> 3.7 \[#1] character  
> \<abstract\> member of a set of elements used for the organization, control, or
> representation of data
>
> 3.7.1 \[#1] character single-byte character  
> \<C\> bit representation that fits in a byte

However, none of this makes it clear whether "character" is to be interpreted as
having type `char`, `signed char`, or `unsigned char`. This matters because
`signed char` need not have the same sized range of values as `unsigned char`
(for example, `SCHAR_MIN` could be -127, or on a 10 bit byte system signed
`char`s could have a padding bit, with `SCHAR_MAX` equal to 255 but `UCHAR_MAX`
equal to 1023).

It would be very unfortunate if the `mem`\* functions could not copy every
possible byte value. The `str`\* functions probably ought to access the values
as if they were plain `char`.

### Suggested Technical Corrigendum

Append a new paragraph to 7.21.1:

> \[#3] Where a block of characters is accessed through a parameter of type `void
> *`, each character shall be interpreted as if it had type `unsigned char` (and
> therefore every object representation is valid and has a different value). Where
> it is accessed through a parameter of type `char *`, each character shall be
> interpreted as if it had type `char` (and therefore, if `CHAR_MAX - CHAR_MIN +
> 1` is less than `UCHAR_MAX`, some byte values may be trap representations or be
> treated as equal to other values).
