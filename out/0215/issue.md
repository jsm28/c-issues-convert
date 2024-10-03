### Summary

When discussing the comparison operators, 6.5.8 says:

> \[#4] For the purposes of these operators, a pointer to an object that is not an
> element of an array behaves the same as a pointer to the first element of an
> array of length one with the type of the object as its element type.

Given that the restrictions on the arguments for pointer comparison and pointer
equality are very different, it would be advisable to repeat this wording in
6.5.9. The only wording that implies that this applies to equality operators is
the bit about "analogous" in 6.5.9#3. Since other restrictions (e.g. that the
pointers must be in the same array) do *not* apply to equality operators, it is
at best ambiguous whether this text applies. Therefore for clarity it should be
repeated.
