ANSI/ISO C Defect report #rfg7:

Subclause 6.6.6.4 **The `return`** statement says:

> If the expression has a type different from that of the function in which it
> appears, it is converted as if it were assigned to an object of that type.

This is nonsensical. The type of the containing function is a function type, and
that's different from an object type. I believe that should be changed to read:

> If the expression has a type different from that of the return type of the
> function in which it appears, it is converted as if it were assigned to an
> object having the same type as the return type of the containing function.
