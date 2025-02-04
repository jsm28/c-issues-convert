## Issue 0060: When an array of `char` (or `wchar_t`) is initialized with a string literal that contains fewer characters than the array, are the remaining elements of the array initialized?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1993-07-19  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Cross-references: [0092](issue0092.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_060.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_060.html)

When an array of `char` (or `wchar_t`) is initialized with a string literal that
contains fewer characters than the array, are the remaining elements of the
array initialized?

Subclause 6.5.7 **Initialization**, page 72, only says (emphasis mine):

> If there are fewer initializers in a *brace-enclosed list* than there are
> members of an aggregate, the remainder of the aggregate shall be initialized
> implicitly the same as objects that have static storage duration.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.7, page 72, the penultimate paragraph of Semantics (before
Examples), add after the comma:***

or fewer characters in a string literal or wide string literal used to
initialize an array of known size, and elements of character or `wchar_t` type
