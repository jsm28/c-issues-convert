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
