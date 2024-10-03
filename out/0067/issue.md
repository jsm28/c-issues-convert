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
 	int : N	 /* i.e. bitfield of size N /*
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
