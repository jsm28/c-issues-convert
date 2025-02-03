Must there exist a user-accessible integral type for every pointer? If an
implementation provides 48-bit pointers, must there be an integral type, such as
`long` or `int`, that is at least 48 bits? Parts of the C Standard that may help
answer the question follow:

Subclause 6.3.4, **Cast operators**, page 45, lines 30-34 and Footnote 45:

> A pointer may be converted to an integral type. The size of integer required and
> the result are implementation-defined. If the space provided is not long enough,
> the behavior is undefined.
>
> An arbitrary integer may be converted to a pointer. The result is
> implementation-defined.**45** \[Footnote 45: The mapping functions for
> converting a pointer to an integer or an integer to a pointer are intended to be
> consistent with the addressing structure of the execution environment.]
