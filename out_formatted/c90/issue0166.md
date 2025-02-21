## Issue 0166: Do constraints that require something to be an lvalue place an unacceptable burden on the implementation?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Cross-references: [0076](../c90/issue0076.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_166.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_166.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 014: Meaning of lvalue

Constraints that require something to be an lvalue place an unacceptable burden
on the implementation.

Subclause 6.2.2.1 states in part:

An lvalue is an expression (with an object type or an incomplete type other than
`void`) that designates an object.

Given the declaration

```c
int a[10], i;
```

the expression `a[i]` designates an object, and is thus an lvalue, if and only
if `i` has a value between 0 and 9 inclusive (see [Defect Report
#076](../c90/issue0076.md) for further details). Now consider the Constraint in subclause
6.3.3.2:

The operand of the unary `&` operator shall be either a function designator or
an lvalue that designates an object ...

This means that the expression `&a[i]` is a constraint violation whenever `i`
has a value outside the range 0 to 9 inclusive, and that therefore a diagnostic
is required, at run-time!

The defect is that the operand of the unary `&` operator does not need to be an
lvalue that designates an object, but rather an lvalue which, if evaluated with
its operands having suitable values, could designate an object.

There are probably other parts of the C Standard with the same problem, such as
subclauses 6.3.2.4, 6.3.3.1, and 6.3.16.
