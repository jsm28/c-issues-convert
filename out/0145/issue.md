*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 029: Constant expressions

There is a confusion of contextual levels in subclause 6.4. Subclause 6.4 lists
four possible forms for a constant expression in an initializer:

> Such a constant expression shall evaluate to one of the following:
> 
> an arithmetic constant expression,
> 
> a null pointer constant,
> 
> an address constant, or
> 
> an address constant for an object type plus or minus an integral constant
> expression.

The first two of these are syntactic forms, not something that a syntactic form
would evaluate to. The third is the result of an evaluation, and the fourth is a
compound of the two types of entity.

This confusion makes it unclear whether expressions like:

```c
(int *)0
```

which is not a null pointer constant, or

```c
x[5] - x[2]
```

which is clearly a constant, are permitted in initializers.

### Suggested Technical Corrigendum:

Replace the quoted text with:

> Such a constant expression shall be either an arithmetic constant expression, a
> null pointer constant, or an address constant expression.

In the second subsequent paragraph, change:

> An address constant is a pointer to an lvalue designating an object of static
> storage duration, or to a function designator; it shall be created explicitly,
> using the unary \& operator, or implicitly ...

to:

> An address constant expression shall have pointer type, and shall evaluate to:
> 
> a null pointer,
> 
> the address of a function, or
> 
> the address of an object of static storage duration plus or minus some integer.
> 
> The address may be created explicitly, using the unary `&` operator, or
> implicitly ...