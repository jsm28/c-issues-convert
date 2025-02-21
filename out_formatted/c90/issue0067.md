## Issue 0067: Are the definitions of types clear?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0071](../c90/issue0071.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_067.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_067.html)

Item 4 \- definitions of types

The terms “signed integer type,” “unsigned integer type,” and “integral type”
are defined in subclause 6.1.2.5. The C Standard also uses the terms “integer
type,” “signed integral type,” and “unsigned integral type” without defining
them. Integer-valued bitfields are also introduced in subclause 6.5.2.

a. For each of the following types, which if any of the six categories above do
they belong to?

```c
char
        signed char
        unsigned char
        signed short
        unsigned short
        signed int
        unsigned int
        signed long
        unsigned long
        int : N  /* i.e. bitfield of size N /*
        signed int : N
        unsigned int : N
        enumerated type
```

b. For each of these categories, do the `const` and/or `volatile` qualified
versions of the types belonging to the category also belong to the category?

c. Can an implementation extension add other types defined by the C Standard to
any of these six categories?

d. Can an implementation define other types (e.g. `__very long`) which belong to
any of these six categories?

e. If the answer to (c) or (d), or both, is yes, can `size_t` and `ptrdiff_t` be
one of these other types, or must it be a type in the above list?

---

Comment from WG14 on 1997-09-23:

### Response

a) “Signed integer type”, “unsigned integer type”, and plain “integer type” are
used interchangeably with “signed integral type”, “unsigned integral type”, and
“integral type” in the C Standard. This observation makes it easy to categorize
the types in your list.

b) Yes, see subclause 6.1.2.5.

c) No, the list in the C Standard is meant to be exhaustive. For example,
`float` cannot be defined as an integer type.

d) No strictly conforming program could contain an instance of such a type. The
treatment of such types is beyond the scope of the C Standard.

e) No, it must be a type in the list. For example, `size_t` cannot be defined as
`unsigned __int24`.
