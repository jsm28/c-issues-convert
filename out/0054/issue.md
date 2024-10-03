Are the string handling functions defined in subclause 7.11 that have an
explicit length specification (`memcpy`, `memmove`, `strncpy`, `strncat`,
`memcmp`, `strncmp`, `strxfrm`, `memchr`, and `memset`) well-defined when the
length is specified as zero?

Taking `memcpy` as an example, the description in subclause 7.11.2.1 states:

> The `memcpy` function copies `n` characters from the object pointed to by `s2`
> into the object pointed to by `s1`. If copying takes place between objects that
> overlap, the behavior is undefined.

The response to [Defect Report #042 Question 1](issue:0042.01) indicates that:

> ... the “objects” referred to by subclause 7.11.2.1 are exactly the regions of
> data storage pointed to by the pointers and dynamically determined to be of `N`
> bytes in length (i.e. treated as an array of `N` elements of character type).

Since, by definition, objects consist of at least one byte, this would imply
that `s1` and `s2` are not pointing to objects when `N` is zero and thus are
outside the domain of the function leading to undefined behavior.

I do not recall whether this was the Committee's intent or not, but it would
seem that some clarification is in order.
