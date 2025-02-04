## Issue 0312: Meaning of "known constant size"

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Joseph Myers \<joseph@codesourcery.com\>, UK C Panel  
Date: 2005-03-04  
Reference document: [ISO/IEC WG14 N1100](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1100.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_312.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_312.htm)

### Summary

Does "known constant size" mean something different from "not a VLA"? The phrase
is used in the definition of composite types, 6.2.7#3:

> \-- If one type is an array of known constant size, the composite type is an
> array of that size; otherwise, if one type is a variable length array, the
> composite type is that type.

and in an example in 6.5.6#11 (where it doesn't cause problems), and in
6.7.5.2#4 to define VLAs:

> \[#4] If the size is not present, the array type is an incomplete type. If the
> size is `*` instead of being an expression, the array type is a variable length
> array type of unspecified size, which can only be used in declarations with
> function prototype scope;122) such arrays are nonetheless complete types. If the
> size is an integer constant expression and the element type has a known constant
> size, the array type is not a variable length array type; otherwise, the array
> type is a variable length array type.

Suppose the implementation does not accept any non-standard forms of constant
expressions under 6.6#10, so that `(int)+1.0` is an arithmetic constant
expression but not an integer constant expression. Thus `int[(int)+1.0]` is a
VLA type. But is `int[1][(int)+1.0]` a VLA type? The element type is a VLA type,
but the element size is a known constant. If "known constant size" is
interpreted to include some VLA cases, this also means further indeterminacy of
composite types in such cases; is "an array of that size" a VLA of that size, or
a non-VLA of that size, and may cases involving compatible array types with
different known constant sizes (which would yield undefined behavior if
executed) be rejected at translation time?

### Suggested Technical Corrigendum

---

Comment from WG14 on 2006-04-04:

### Committee Discussion (for history only)

The statement, "Suppose the implementation does not accept any non-standard
forms of constant expressions under 6.6#10, so that `(int)+1.0` is an arithmetic
constant expression but not an integer constant expression." , implies an
interpretation of the standard that the implementation can extend the meaning of
what constitutes an integer constant expression. For example, that `(int)+1.0`
is an integer constant expression.

The committee does not believe that it does. Even if an implementation accepts
other forms of constant expressions, paragraph 6.6#10 does not change the
definition of an integer constant expression given by paragraph 6.6#6, and
`int[(int)+1.0]` is still a VLA.

Paragraph 6.6#10 cannot be used to get around issuing diagnostics for constraint
violations where integer constant expressions are required. Which we believe is
what the first paragraph of the introductory text is implying

### Technical Corrigendum

Add to 6.2.5, after Paragraph 22

> A type has *known constant size* if the type is not incomplete and is not a
> variable length array type.
