Example of value of character constants

Refer to subclause 6.1.3.4, page 29, lines 24-25 and page 30, lines 9-10. Both
of these statements cannot be true.

1. If the constraint is violated, end of story. There is no implementation-defined value.
2. The implementation-defined behavior may be referring to the mapping of the escape sequence to the basic character set, in which case subclause 6.1.3.4, page 29, lines 24-25 should be changed to mention that it will violate a constraint if the mapped value is outside the range of representable values for the type `unsigned char`.
