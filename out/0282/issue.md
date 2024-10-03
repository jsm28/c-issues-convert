### Summary

6.7.2.1 Structure and union specifiers, paragraphs 15 and 16 require that any
padding for  
alignment of a structure containing a flexible array member must preceed the
flexible  
array member.  This contradicts existing implementations.  We do not believe
this was the intent of the C99 specification.

### Details

If a struct contains a flexible array member and also requires padding for
alignment, then the current C99 specification requires the implementation to put
this padding **before** the flexible array member.  However, existing
implementations, including at least GNU C, Compaq C, and Sun C, put the padding
**after** the flexible array member.

The layout used by existing implementations can be more efficient. Furthermore,
requiring these existing implementations to change their layout would break
binary backwards compatibility with previous versions.

### Suggested Technical Corrigendum

Change the wording such that it is implementation defined as to whether the
padding is before or after the flexible array member.
