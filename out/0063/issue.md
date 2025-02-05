\[This is Defect Report #056, resubmitted for administrative reasons.\]

The following requirement is implied in several places, but not explicitly
stated. It should be explicitly affirmed, or alternative wording adopted.

The representation of floating-point values (such as floating-point constants,
the results of floating-point expressions, and floating-point values returned by
library functions) shall be accurate to one unit in the last position, as
defined in the implementation's `<float.h>` header.

Discussion: The values in `<float.h>` aren't required to document the underlying
bitwise representations. If you want to know how many bits, or bytes, a
floating-point values occupies, use `sizeof`. The `<float.h>` values document
the mathematical properties of the representation, the behaviors that the
programmer can count upon in analyzing algorithms.

It is a quality-of-implementation question as to whether the implementation
delivers accurate bits throughout the bitwise representation, or alternatively,
delivers considerably less accuracy. The point being clarified is that
`<float.h>` documents the delivered precision, not the theoretically possible
precision.
