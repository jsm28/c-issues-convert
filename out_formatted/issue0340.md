## Issue 0340: Composite types for variable-length arrays

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Joseph Myers \<joseph@codesourcery.com\>, Joseph Myers (UK)  
Date: 2007-03-24  
Reference document: [ISO/IEC WG14 N1221](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1221.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Cross-references: [0342](issue0342.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_340.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_340.htm)

### Summary

The definition of composite types in 6.2.7#3 says "If one type is an array of
known constant size, the composite type is an array of that size; otherwise, if
one type is a variable length array, the composite type is that type." and also
"These rules apply recursively to the types from which the two types are
derived.". Which of these wins for variable length array types? Are the element
types composed recursively, or is the element type of the variable length array
type taken even though it may have less information than the other element type?
(That loss of information in the composite type would mean some sequences of
three or more declarations of the same function are constraint violations for
some orderings of the declarations and undefined behavior for other orderings.)

See reflector messages 11145-11147 for discussion.

### Suggested Technical Corrigendum

6.2.7 paragraph 3, change "is that type" to "is an array of that size; in either
case, the element type of the composite type is the composite type of the two
element types".

---

Comment from WG14 on 2008-09-10:

### Committee Discussion

The element types are composed. Suggested TC is close, but not quite right. The
example from 11145 should be included here.

Also see [N1238](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1238.htm) and
WG14 e-mail SC22WG14.11145.

#### Fall 2007

No consensus was reached on the words from
[N1238](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1238.htm).

#### Spring 2008

It appears that the current implementations differ in this area. Some compilers
works one way (as described), while others do not. Probably best solution is to
make this undefined behavior.

### Proposed Technical Corrigendum

In subclause 6.2.7, paragraph 3, change the first bullet to the following.

> – If both types are array types, the following rules are applied:
>
> > If one type is an array of known constant size, the composite type is an array
> > of that size.  
> > Otherwise, if one type is a variable length array whose size is specified by an
> > expression that is not evaluated, the behavior is undefined.  
> > Otherwise, if one type is a variable length array whose size is specified, the
> > composite type is a variable length array of that size.  
> > Otherwise, if one type is a variable length array of unspecified size, the
> > composite type is a variable length array of unspecified size.  
> > Otherwise, both types are arrays of unknown size, and the composite type is an
> > array of unknown size.  
> > The element type of the composite type is the composite type of the two element
> > types.
>
> In subclause J.2, paragraph 1, insert the following bullet in order.
>
> > – A program requires the formation of a composite type from a variable length
> > array type whose size is specified by an expression that is not evaluated
> > (6.2.7).
