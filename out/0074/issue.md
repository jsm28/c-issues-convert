Item 11 \- alignment and structure padding

The existence of structure padding (subclause 6.5.2.1) can be detected by a
strictly conforming program by use of the `sizeof` operator and the `offsetof`
macro.

a. If a structure has a field of type `t`, can the alignment requirements of the
field be different from the alignment requirements of objects of the same type
that are not members of structures?

If the answer to (a) is “yes,” then where applicable the remaining questions
should be assumed to have been asked for both objects within structures and
objects outside structures.

b. If an array has a component type of `t`, can the alignment requirements of
the elements of the array be different from those of independent variables of
type `t`?

The alignment requirement of a type is that addresses of objects of that type
must be multiples of some constant (subclause 3.1); for some type `t`, this is
written `A(t)` in this Defect Report.

c. For any type `t`, can the expression `sizeof (t) % A(t)` be non-zero (in
other words, can `A(t)` be a value other than 1, `sizeof (t)`, or a factor of
`sizeof (t)`)? It would appear not, because otherwise adjacent elements of an
array of objects of type `t` would either not be correctly aligned, or else
would not be contiguously allocated.

d. Can `A(struct foo)` be greater than the least common multiple of `A(type_1)`,
`A(type_2)`, ..., `A(type_n)`, where `type_1` to `type_n` are the types of the
elements of `struct foo`? In particular, if a structure holds exactly one
element, can `A(structure type)` be different from `A(element type)`? (In each
case, if the answer to (a) is “yes,” `A(type)` should be interpreted
appropriately.)

e. If, at any point in a structure or union (obviously excluding the start),
there is more than one size of padding that can satisfy all alignment
requirements, can any size be used, or must the smallest (possibly zero) padding
be used because that is all that is “necessary to achieve the appropriate
alignment?”

f. If a structure type has trailing padding to ensure that its use as an array
element would be correctly aligned, must objects of that type which are not
array elements also have the padding? If not, what is the effect of using
`memcpy` to copy the value of one such object to another thus?

```c
struct fred a, b;
 	/* ... /*
        memcpy(&a, &b, sizeof (struct fred));
```

It appears from subclause 6.3.3.4 (“the size is determined from the type of the
operand”) that `sizeof a` must equal `sizeof (struct fred)`. Is this correct?

g. When an element of a structure is in turn a structure, can trailing padding
of the inner structure be reused to hold other elements of the enclosing
structure? For example, in:

```c
struct outer
        {
        struct inner { long a; char b; } inner;
        char c;
        };
```

is it permitted for `offsetof (struct outer, c)` to be less than `sizeof (struct
inner)`?
