Subclause 7.1.6, page 98, lines 24-30 describe the macro

```c
offsetof(type, member_designator)
```

“which expands to an integral constant expression that has type `size_t`, ...”

How is this statement to be interpreted? The expansion of the macro `offsetof`
is

a. an expression which can be evaluated during translation, the value of which
is in the range representable by a `size_t` type.

Or

b. an expression as (a) above, but further constrained to be an “integral
constant expression” as defined in subclause 6.4, page 55, lines 17-21.
