## Issue 0134: Is *error number* an undefined term?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, Project Editor (P.J. Plauger)  
Date: 1994-01-31  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_134.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_134.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

The `strerror` function must provide a valid message for the error numbers
`EDOM`, `ERANGE`, and any other value a library function might store in `errno`.
For all other values, the behavior is undefined.
