*This Defect Report was prepared with considerable help from Mark Brader, Clive
Feather, Ronald Guilmette, and a person whose employment conditions require
anonymity.*

DIN-001:

According to the current C Standard, programs containing

```c
char array[] = "Hello, World";
```

are not strictly conforming.

A **Constraint** in subclause 6.5.7 **Initialization**, demands that:

All the expressions in an initializer for an object that has static storage
duration or in an initializer list for an object that has aggregate or union
type shall be constant expressions.

Subclause 6.4 **Constant expressions**, defines various kinds of constant
expression. In its **Semantics** it states that a constant expression in an
initializer evaluates to one of the following:

\- an arithmetic constant expression

\- a null pointer constant,

\- an address constant, or

\- an address constant for an object type plus or minus an integral constant
expression.

String literals are neither. A string literal used to initialize a character
array does not decay to a pointer to its first element, according to Subclause
6.2.2.1:

Except when it is the operand of the `sizeof` operator or the unary `&`
operator, or is a character string literal used to initialize an array of
character type, or is a wide string literal used to initialize an array with
element type compatible with `wchar_t`, an lvalue that has type "array of
*type*" is converted to an expression that has type "pointer to *type*" that
points to the initial element of the array object and is not an lvalue.

and hence is not an address constant.

### Suggested Technical Corrigendum:

In subclause 6.5.7, change:

All the expressions in an initializer for an object that has static storage
duration or in an initializer list for an object that has aggregate or union
type shall be constant expressions.

to:

All the expressions in an initializer for an object that has static storage
duration or in an initializer list for an object that has aggregate or union
type shall be constant expressions or string literals.
