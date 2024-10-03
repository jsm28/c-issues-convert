*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 003: Zero-sized allocations

The use of the word "unique" in subclause 7.10.3 is ambiguous, and the handling
of zero size allocations is incomplete.

**Part 1**

Subclause 7.10.3 reads

If the size of the space requested is zero, the behavior is
implementation-defined; the value returned shall be either a null pointer or a
unique pointer.

Does the term "unique" mean "different every time," or does it mean "there is a
single pointer returned by all calls with size zero" (as might be presumed from
the ordinary dictionary definition of "unique") ?

In other words, if `malloc(0)` does not return a null pointer, is the following
expression:

```c
malloc(0) == malloc(0)
```

always zero, always non-zero, or implementation-defined ?

**Part 2**

If unique means "there is a single pointer," what is the result of attempting to
free that pointer? How does the wording of 7.10.3 apply:

The value of a pointer that refers to freed space is indeterminate.

Possibly nothing happens, because the pointer does not really point to a block
of memory. In that case, is the following code strictly conforming?

```c
#include <stdlib.h>
 /* ..... */
 void *p = malloc(0);
 if (p != NULL)
 {
 free (p); /* Line A */
free (p); /* Line B */
}
```

What is the behavior if each of lines A and B are reached?

**Part 3**

If "unique" means "different every time," then each such call still consumes
address space, even though no storage actually needs to be allocated, and
therefore the call can fail due to exhaustion of memory. Thus `malloc(0)` can
return a null pointer, while the C Standard seems to suggest that an
implementation can return either null pointers or unique pointers, but not both.
This is a defect in the existing wording.

### Suggested Technical Corrigendum:

If "unique" means "there is a single pointer," then change the penultimate
sentence of 7.10.3 from:

If the size of the space requested is zero, the behavior is
implementation-defined; the value returned shall be either a null pointer or a
unique pointer.

to:

If the size of the space requested is zero, the behavior is
implementation-defined; the value returned shall be either a null pointer or a
unique pointer. The values returned by two zero-length allocations shall compare
equal. Freeing the value returned by a zero-length allocation shall have no
effect. If that value is used as an operand of the unary `*` operator, or of a
`+` or `-` operator except one whose other operand has integral type and value
zero, the behavior is undefined.

If "unique" means "different every time," then change it to:

If the size of the space requested is zero, the behavior is
implementation-defined; either a null pointer is always returned, or the
behavior is as if the size were some unspecified non-zero value. In the latter
case, if the returned pointer is not a null pointer and is used as an operand of
the unary `*` operator, or of a `+` or `-` operator except one whose other
operand has integral type and value zero, the behavior is undefined.

\[See also [Defect Report #158](issue:0158).]
