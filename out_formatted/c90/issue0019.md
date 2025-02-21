## Issue 0019: Are printing characters implementation defined?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Richard Wiersma, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-014  
Submitted against: C90  
Status: Closed  
Cross-references: [0132](../c90/issue0132.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_019.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_019.html)

Background:

Subclause 7.3.1.5 states that “the `isgraph` function tests for any printing
character except space.” Subclause 7.3.1.7 states that “the `isprint` function
tests for any printing character including space.”

The third paragraph of subclause 7.3 defines the term *printing character* as “a
member of an implementation-defined set of characters, each of which occupies
one printing position on a display device.”

Subclause 5.2.1 defines the source and execution character sets and provides a
list of characters which must be contained in both sets.

Question for interpretation: Are the `isprint` and `isgraph` functions required
to return a non-zero value for all of the characters defined in subclause 5.2.1?

A scenario for use of `isprint`/`isgraph` that depends on the interpretation is:
A developer may wish to use these functions to determine whether a particular
character can be displayed as itself (e.g., whether a square bracket is actually
displayed as a square bracket). This could be useful for formatting output in a
device-independent manner, since the application could substitute some other
character for ones that do not print “correctly.”

If `isprint` and `isgraph` are required to return non-zero for all characters in
subclause 5.2.1, developers cannot use them for this purpose.

This problem has occurred in a real implementation. The most commonly used
terminals and printers for IBM System/370 computers do not support all of the
characters listed in subclause 5.2.1. For example, most IBM printers and
terminals do not print the square brackets.

The SAS/C implementation of `isprint` and `isgraph` assumes that subclause 7.3
controls the behavior of these functions, and returns non-zero only for those
characters that print “correctly.” The Plum Hall test suite, however, assumes
that `isprint` and `isgraph` return non-zero for all characters listed in
subclause 5.2.1.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.3, page 102, line 8 says that *printing character* is
implementation-defined. In particular, the value (zero or non-zero) of
`isprint('[')` is implementation-defined, *even in the* `"C"` *`locale.`*
