ANSI/ISO C Defect Report #rfg28:

Subject: Conversions of pointer values to integral types.

Subclause 6.3.4 (**Semantics**):

> A pointer may be converted to an integral type. The size of integer required and
> the result are implementation-defined. If the space provided is not long enough,
> the behavior is undefined.

This passage is worded rather ambiguously.

In the first place, it talks about “The size of the integer required....”
Required by whom? Required by what? I can't tell.

Also, I get the feeling that the way this passage reads, an implementation might
permit conversions of pointers to types `char`, `short`, and `int` (with
implementation defined semantics) while *disallowing* conversions of pointers to
type `long`! (Of course that would be highly counterintuitive.)

Here is a suggested replacement for the above passage:

The value of any pointer expression whose `sizeof`, if computed, would be *N,*
may be converted (via a cast) to any integral type whose `sizeof` is *N* or
greater. The values resulting from such conversions are implementation-defined.

If an attempt is made to convert (via a cast) the value of a pointer expression
whose `sizeof`, if computed, would be *N,* to some integral type whose `sizeof`
is less than *N,* the behavior is undefined.

This is simply a more precise (and accurate) way of saying exactly what was
(obviously) intended.
