## Issue 0057: Must there exist a user-accessible integral type for every pointer?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman, Project Editor (P.J. Plauger)  
Date: 1993-06-07  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_057.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_057.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

Integral types and pointer types are incommensurate. An implementation need not
provide an integral type that can accept the conversion from a pointer type
without loss of information.
