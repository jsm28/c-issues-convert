Subclause 7.11.6.2 **The `strerror` function**, page 168, reads:

> The `strerror` function maps the error number in `errnum` to an error message
> string.

However, “error number” is an undefined term. Must `strerror` provide a valid
message for every value of type `int`, or can some values be a domain error,
allowing it to return garbage or a null pointer? If the latter, then what are
the values that must generate a valid string? Must the following generate a
valid string:

zero

`EDOM` and `ERANGE`

the value of any other symbol defined in `<errno.h>`

any value that a library routine might set `errno` to
