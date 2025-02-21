## Issue 0121: What is ment by *size required* when convering a ponter value to an integral type?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_121.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_121.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

The “size required” is that required by the implementation. The words “If the
space provided is not long enough” make it clear that it is the size of the type
that is relevant, and means that any type that is at least as long as the type
of the “size required” is also acceptable. The size required need not be related
to the result of `sizeof` applied to the expression.
