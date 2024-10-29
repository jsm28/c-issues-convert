*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 020: Relational and equality operators

The descriptions of these operators with pointer operands contain several
defects.

**Part 1**

Consider the following code:

```c
char *s = "a string";
 if (s  = NULL)
 	/* ... */
```

Subclause 6.3.8, Semantics reads in part:

If the objects pointed to are not members of the same aggregate or union object,
the result is undefined

This implies that the comparison causes undefined behavior.

Subclause 6.2.2.1 reads in part:

Such a pointer, called a null pointer, is guaranteed to compare unequal to a
pointer to any object or function.

This implies that the comparison is guaranteed to yield *false.*

This is a direct contradiction.

**Part 2**

Subclause 6.3.9, Semantics reads in part:

Where the operands have types and values suitable for the relational operators,
the semantics detailed in subclause 6.3.8 apply.

This can reasonably be read as meaning that, whenever the constraints of
subclause 6.3.8 apply, its definitions should be used, even if that would result
in undefined behavior. (The phrase *and values* can reasonably be read as
requiring only that the pointers both be to objects; it does not necessarily
mean that the result of the comparison must be defined.)

It further reads:

If two pointers to object or incomplete types are both null pointers, they
compare equal. If two pointers to object or incomplete types compare equal, they
both are null pointers, or both point to the same object, or both point one past
the last element of the same array object.

This says nothing about the comparison of any other pointers. Now, subclause
3.16 reads in part:

Undefined behavior is otherwise indicated ... by the omission of any explicit
definition of behavior.

Thus, in:

```c
int a, b;
 &a == &b
```

the comparison causes undefined behavior!

**Part 3**

The above citation does not allow for the case where one pointer is to an
object, and the other is one past the last element of an array object. If an
implementation places two independent objects in adjacent memory locations, a
pointer to one would equal a pointer to just past the other on many common
implementations.

If these pointers are not to be viewed as identical, then the wording is
defective.

### Suggested Technical Corrigendum

In subclause 6.2.2.1, replace the cited text by:

Such a pointer is called a null pointer.

In subclause 6.3.9, replace the first paragraph of the semantics by:

The operators `==` (equal to) and `!=` (not equal to) shall yield 1 if the
specified relation is true and 0 if it is false. If the operands have types
suitable for those of a relational operator and values that would not cause
undefined behavior if used with a relational operator, then the result of the
comparison, either greater than or less than (both implying not equal to) or
equal to, is the same as with a relational operator.

Insert at the start of the second paragraph:

Otherwise the operands are pointers, and they shall compare either equal or not
equal.

If part 3 is viewed as an issue, then in the same paragraph change:

or both point one past the last element of the same array object.

to:

both point one past the last element of the same array object, or one points one
past the last element of some array object and the other points to the first
element of a different array object.