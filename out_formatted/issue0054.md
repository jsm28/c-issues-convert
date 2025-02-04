## Issue 0054: What is the behavior of various string functions with a specified length of zero?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1993-04-01  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0042.01](issue0042.01.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_054.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_054.html)

Are the string handling functions defined in subclause 7.11 that have an
explicit length specification (`memcpy`, `memmove`, `strncpy`, `strncat`,
`memcmp`, `strncmp`, `strxfrm`, `memchr`, and `memset`) well-defined when the
length is specified as zero?

Taking `memcpy` as an example, the description in subclause 7.11.2.1 states:

> The `memcpy` function copies `n` characters from the object pointed to by `s2`
> into the object pointed to by `s1`. If copying takes place between objects that
> overlap, the behavior is undefined.

The response to [Defect Report #042 Question 1](issue0042.01.md) indicates that:

> ... the “objects” referred to by subclause 7.11.2.1 are exactly the regions of
> data storage pointed to by the pointers and dynamically determined to be of `N`
> bytes in length (i.e. treated as an array of `N` elements of character type).

Since, by definition, objects consist of at least one byte, this would imply
that `s1` and `s2` are not pointing to objects when `N` is zero and thus are
outside the domain of the function leading to undefined behavior.

I do not recall whether this was the Committee's intent or not, but it would
seem that some clarification is in order.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 7.11.1, page 162:***

Where an argument declared as `size_t n` specifies the length of the array for a
function, `n` can have the value zero on a call to that function. Unless
explicitly stated otherwise in the description of a particular function in this
subclause, pointer arguments on such a call must still have valid values, as
described in subclause 7.1.7. On such a call, a function that locates a
character finds no occurrence, a function that compares two character sequences
returns zero, and a function that copies characters copies zero characters.
