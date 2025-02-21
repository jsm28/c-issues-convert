## Issue 0017.05: When are character constants implementation defined?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Example of value of character constants

Refer to subclause 6.1.3.4, page 29, lines 24-25 and page 30, lines 9-10. Both
of these statements cannot be true.

1. If the constraint is violated, end of story. There is no implementation-defined value.
2. The implementation-defined behavior may be referring to the mapping of the escape sequence to the basic character set, in which case subclause 6.1.3.4, page 29, lines 24-25 should be changed to mention that it will violate a constraint if the mapped value is outside the range of representable values for the type `unsigned char`.

---

Comment from WG14 on 1997-09-23:

### Response

The values of octal or hexadecimal escape sequences are well defined and not
mapped. For instance, the value of the constant `'\x123'` has the value 291\.

The mapping described in subclause 6.1.3.4 on page 28, lines 35-39 applies only
to members of the source character set, of which octal and hexadecimal escape
sequences clearly are not members.

The constraint in subclause 6.1.3.4 on page 29, lines 24-25 will be violated
only if the implementation uses characters of eight bits.

The text of the example in subclause 6.1.3.4 on page 30, lines 8-10 is slightly
opaque, but the parenthesized comment is meant to be subject to the words “Even
if eight bits are used ...” The value is implementation-defined only in that the
implementation specifies how many bits are used for characters and whether type
`char` is signed or not.

This example could be worded a little more clearly to indicate what is
implementation-defined about the constant, and that it “violates the above
constraint” only if eight bits are used for objects that have type `char`, but
we believe that this interpretation is consistent with the intent of the
Committee, and that a reasonable reading of the standard supports this
interpretation.
