### Summary

The definition of variable length array type is in 6.7.5.2p4 (Array
declarators), but it is not italicized:

> If the size is \* instead of being an expression, the array  
> type is a variable length array type of unspecified size,  
> which can only be used in declarations with function prototype  
> scope; such arrays are nonetheless complete types. If the size  
> is an integer constant expression and the element type has a  
> known constant size, the array type is not a variable length  
> array type; otherwise, the array type is a variable length  
> array type.

The way that the term appears in the text is not in a form where there is a
single occurrence that gives the complete definition, but it would still
probably be better to italicize it than not.

Or perhaps both the 1st and 3rd occurrence of it in the above should get
italics?  It would not make sense to italicize the 2nd occurrence.  Re-writing
the text to create a single occurrence that provides a complete definition does
not seem worthwhile.

Also, variable length array types are mentioned several times prior to this
definition.  The following sections should probably have a forward reference
"variable length array type (6.7.5.2)":  6.2.4, 6.2.7, 6.5.3.4

Similarly, a forward reference "variably modified type (6.7.5)" is desirable in 
6.7.2.1.

### Suggested Technical Corrigendum

1\. Change first sentence of 6.7.5.2p4 (adding italics) from::

> > If the size is \* instead of being an expression, the array type is a variable
> > length array type of unspecified size, which can only be used in declarations
> > with function prototype scope; such arrays are nonetheless complete types.
>
> to
>
> > If the size is \* instead of being an expression, the array type is a *variable
> > length array type* of unspecified size, which can only be used in declarations
> > with function prototype scope; such arrays are nonetheless complete types.

     It might also be desirable to change the second sentence (adding italics)
from:

> > If the size is an integer constant expression and the element type has a known
> > constant size, the array type is not a variable length array type; otherwise,
> > the array type is a variable length array type.
>
> to
>
> > If the size is an integer constant expression and the element type has a known
> > constant size, the array type is not a variable length array type; otherwise,
> > the array type is a *variable length array type.*

2\. Change list of Forward references following 6.2.4p6 from

> **Forward references:** statements (6.8), function calls (6.5.2.2), declarators
> (6.7.5), array declarators (6.7.5.2), initialization (6.7.8).

    to

> **Forward references:** statements (6.8), function calls (6.5.2.2), declarators
> (6.7.5), array declarators (6.7.5.2), variable length array type (6.7.5.2),
> initialization (6.7.8).

3\. Add forward reference section following 6.2.7p5:

> **Forward references:** variable length array type (6.7.5.2).

4\. Change list of Forward references following 6.5.3.4p7 from:

> **Forward references:** common definitions `<stddef.h>` (7.17), declarations
> (6.7), structure and union specifiers (6.7.2.1), type names (6.7.6), array
> declarators (6.7.5.2).

    to

> **Forward references:** common definitions `<stddef.h>` (7.17), declarations
> (6.7), structure and union specifiers (6.7.2.1), type names (6.7.6), array
> declarators (6.7.5.2), variable length array type (6.7.5.2).

5\. Change list of Forward references following 6.7.2.1p22 from:

> **Forward references:** tags (6.7.2.3).

    to

> **Forward references:** tags (6.7.2.3), variably modified type (6.7.5).
