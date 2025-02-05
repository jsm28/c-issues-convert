### Summary

Does "known constant size" mean something different from "not a VLA"? The phrase
is used in the definition of composite types, 6.2.7#3:

> \-- If one type is an array of known constant size, the composite type is an
> array of that size; otherwise, if one type is a variable length array, the
> composite type is that type.

and in an example in 6.5.6#11 (where it doesn't cause problems), and in
6.7.5.2#4 to define VLAs:

> \[#4\] If the size is not present, the array type is an incomplete type. If the
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
