### Summary

> The majority of bounds checking functions are specified to set the first element
> of the destination buffer, `s[0]`, to the NUL character when a constraint
> violation occurs and the `s` pointer is non-null and the size of the buffer is
> greater than zero and less than or equal to `SIZE_MAX`.
>
> However, the `tmpnam_s` function sets `s[0]` to NUL even when `maxsize` is
> greater than `RSIZE_MAX`, making its behavior on constraint violation
> inconsistent with the rest.

#### Suggested Technical Corrigendum:

> Change paragraph 8 in the Returns section of tmpnam\_s to read:
>
> * If no suitable string can be generated, or if there is a runtime-constraint violation and `s` is not null and `maxsize` is greater than zero and not greater than `RSIZE_MAX`, the `tmpnam_s` function sets `s[0]` to the null character and returns a nonzero value.
