Item 18 \- left shift operator

The result of the left shift operator `E1 < E2`, when `E1` is signed, is defined
(subclause 6.3.7) as `E1` left-shifted by `E2` bits, with vacated bits filled
with zeros. But what exactly does this mean?

The C Standard defines a bit (subclause 3.3) only as a unit of data storage.
Bits are related to the value of an object only in subclause 6.1.2.5, which
specifies the representation of certain types. It may therefore be claimed that
the left shift operator must act on representations, which are of fixed length.
In this interpretation, the left `E2` bits (including the sign bit) are lost, as
they would be if `E1` was unsigned; the sign bit of the result is taken from a
bit in `E1`, `E2` places to the right of the sign bit and, provided that the
resultant bit pattern actually represents a value of the result type, an
exception is impossible.

On the other hand, it may also be claimed that the whole of subclause 6.3
specifies the meaning of operations in abstract mathematical terms, subject to
the general note about exceptions. In this view, the bit sequence representing
the non-sign part of a signed integer is converted by the shift operation to a
bit sequence of indefinite length, and, to avoid an exception due to overflow,
this bit sequence must fit back in the non-sign part without the loss at the
left of anything but copies of the sign bit.

a. Which of these two views is correct?

b. If the answer to (a) is the first view, does undefined behavior occur if the
resulting bit pattern is not the representation of an integer?

The following questions apply only if the answer to (a) is that the second view
is correct.

c. If `E1` is positive, and `E1` times 2 to the power `E2` is less than or equal
to `INT_MAX` (or `LONG_MAX`), is the result always `E1` times 2 to the power
`E2`?

d. Under what circumstances is the result undefined?
