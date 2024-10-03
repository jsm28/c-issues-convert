Ambiguous parsing of typedefs in prototypes

On page 67 in subclause 6.5.4.3, an ambiguity needs resolving in the parsing of
the following:

a. `int x(T (U));`

b. `int x(T (U (int a, char b)));`

In (a) `U` is the type of the parameter to a function returning type `T`. From
subclause 6.5.4.3, page 68, line 2:

> In a parameter declaration, a single typedef name in parentheses is taken to be
> an abstract declarator that specifies a function with a single parameter, not as
> redundant parentheses around the identifier for a declarator.

Thus in the case of (b):

1. `U` could be a redundantly parenthesized name of a function which takes a *`parameter-type-list`* and returns type `T`, or
2. `U` could be the type returned by a function which takes a *`parameter-type-list`*, which in turn is the single parameter of a function returning type `T`.
