### Summary

C99 6.7.2#2 lists the valid combinations of type specifiers. 6.7.2#5 says:

> \[#5\] Each of the comma-separated sets designates the same type, except that
> for bit-fields, it is implementation-defined whether the specifier `int`
> designates the same type as `signed int` or the same type as `unsigned int`.

6.7.2.1#4 says:

> \[#4\] A bit-field shall have a type that is a qualified or unqualified version
> of `_Bool`, `signed int`, `unsigned int`, or some other implementation-defined
> type.

Some problems arise with use of an "other implementation-defined type", a new
addition in C99.

1\. Suppose an implementation supports bit-fields of types `char`, `short`,
`long` and `long long`. Bit-fields of type `int` may be unsigned on that
implementation. Must bit-fields of type `char` nevertheless have the same
signedness as ordinary objects of type `char`, and similarly for those of types
`short` (or `short int`), `long` (or `long int`), `long long` (or `long long
int`)? The practice in C\+\+ is that all these are implementation-defined
(except that C\+\+ does not include `long long`); it seems an oversight in the
addition of implementation-defined bit-field types in C99 not to make such
provision for `char`, `short`, `long` and `long long` bit-fields as is made for
`int` bit-fields. (It might still be appropriate to ensure, for example, that
`short` and `short int` have the same signedness as bit-field types, although
that might be unsigned and so differ from the signedness of `signed short` and
`signed short int`.) Footnote 104, reiterating that `int` as a bit-field type
may be signed or unsigned, would also need amendment.

2\. Suppose an implementation has 32-bit `int` (with no padding bits) and
permits `unsigned long long` as an implementation-defined bit-field type.
Consider the code:

```c
  struct s { unsigned long long a : 37, b : 37; } x;
  // ...
  sizeof(x.a + x.b);
```

`x.a` and `x.b` have 37-bit unsigned integer types, by 6.7.2.1#9. Such types
have an integer conversion rank greater than that of `int`, so are unchanged by
the integer promotions. (That all the bit-field types have integer conversion
ranks, and may need to be documented by implementations as extended integer
types, is a consequence of the standard that may not be intended and may be
surprising to some, but it is a logical consequence of the text of the
standard.) Whether or not `x.a` and `x.b` have the same 37-bit type, `(x.a +
x.b)` also has a 37-bit unsigned integer type. However, `(x.a + x.b)` does not
designate a bit-field member, so it does not violate the constraints on
`sizeof`. But what should `sizeof(x.a + x.b)` evaluate to, when `(x.a + x.b)`
has such a bit-field type which does not occupy an integer number of bytes? Must
an implementation define representations occupying an integer number of bytes
(with some padding bits) for all such types, although such representations would
have no use other than to define the result of `sizeof`?

Changing the promotion rules for bit-fields wider than int to avoid such
expressions of bit-field type would create an odd inconsistency in the type
system about which types are promoted, although it would be consistent with
C\+\+ where bit-fields have narrow representation but are considered to have the
declared type rather than a special narrow type and would allow implementations
to support bit-fields wider than `int` without needing special support for
arithmetic on such types (alternatively, it could be argued that if an
implementor wishes to support bit-fields wider than `int` it is up to them to
implement arithmetic on all bit-field types wider than `int` as a consequence of
their decision); changing the C definition of bit-field types to follow the
C\+\+ one would be more radical and probably not suitable for a TC. (C\+\+ then
has a special rule so that `unsigned int` bit-fields promote to `int` if
narrower than `int`.) The alternative is to be more explicit about the nature of
bit-field types and to define when an expression has such a type, and to make
the constraint on `sizeof` apply to expressions with such types and not just to
bit-fields themselves.

### Suggested Technical Corrigendum
