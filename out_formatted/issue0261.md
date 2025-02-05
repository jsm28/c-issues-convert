## Issue 0261: constant expressions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_261.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_261.htm)

### Problem

When is an expression a constant expression ?

Consider the code (at block scope):

```c
 enum e1 { ex1 = INT_MAX + 1 };        // Line E1  enum e2 { ex2 = INT_MAX + (0, 1) };   // Line E2  char *p1 = (1 - 1);                   // Line P1  char *p2 = (42, 1 - 1);               // Line P2  short s1 = 42 + (0, 1);               // Line S1  p1 = (42, 1 - 1);                     // Line X1  s1 = (42, 69);                        // Line X2  p2 = 0;                               // Line X3  p2 = 1 - 1;                           // Line X4
```

On line E1 the syntax says that `INT_MAX + 1` is a constant-expr. Therefore this
is a constant expression, the requirements of 6.6 apply, and line E2 violates
the constraint in 6.6#3.

On the remaining lines the syntax says that the code following the \= sign is an
assignment-expr; at no point in the parse does a constant-expr occur. So are
these constant expressions ?

For line P1 to be legitimate, the expression `(1 - 1)` must be an integer
constant expression (6.3.2.3#3). This implies that any expression comprised
entirely of constants is an integer constant expression. So line P2 violates the
constraint in 6.6#3 and, rather more worryingly, so does line S1.

If a generic initializer can be a constant expression, then, surely, so can any
other expression. This means that lines X1 and X2 violate the constraint in
6.6#3. On the other hand, if they are not constant expressions, then the right
hand sides on lines X3 and X4 do not include a null pointer constant; nor does
line P1.

Consider also:

```c
static int v = sizeof (int [(2, 2)]);
```

This is legitimate if, and only if, `(2, 2)` is a constant expression.

It would appear that the term "constant expression" actually has four subtly
different meanings.

1. An object in the syntax. Where the syntax tree contains constant-expr the resulting code must meet the constraints and semantics of 6.6. An example is 6.7.2.2, where explicit values for enumeration constants must be constant-exprs.
2. A requirement on the program that a given construct must, in context, be a constant expression even though in other contexts the expression need not be constant. An example is 6.7.8#4: if the object has static storage duration, the initializer is subject to the constraints and semantics of 6.6, but if it has automatic storage duration there is no such requirement.
3. A requirement on the implementation that an entity must be a constant expression. For example, this applies to macros in standard headers. The implementation is not conforming if the definition does not meet the syntax, constraints, and semantic requirements of 6.6.
4. A test that distinguishes two cases. An example is 6.3.2.3#3, where a certain subset of integer expressions (those that are constant-exprs and have a value of 0\) are also null pointer constants. It is not clear whether expressions that break the constraints or semantic requirements are erroneous or are simply not constant expressions.

The Standard needs to make clear when each of these four cases applies.

On further examination, cases (1) and (2) appear to always be obvious from the
text of the Standard. Case (3) appears only to apply to macros defined in
standard headers or predefined. Case (4) is harder to identify, but I believe
that there are only two situations:

> \- null pointer constants;  
> \- determining whether a type is variably modified.

### Suggested Technical Corrigendum

Replace 6.6#2 with the following:

> \[#2\] A constant expression is one which is evaluated during translation rather
> than runtime, usually because the precise value will affect the translation in
> some way.
>
> \[#2a\] Where the implementation is required to provide a constant expression,
> that expression shall be one that, if included in the appropriate context, would
> meet the requirements of this subclause and whose evaluation would not involve
> undefined behaviour.
>
> \[#2b\] An expression has a *translation-time value* if it meets the
> requirements of this subclause and evaluation would not involve undefined
> behaviour. If the expression fails to meet these requirements (for example, an
> integer expression includes a comma operator or a cast to a floating type), the
> expression does not have a translation-time value but nevertheless is not
> necessarily invalid.

Change 6.3.2.3#3 to begin:

> \[#3\] An integer expression with the translation-time value 0, or such an
> expression cast to type `void *`, is called a *null pointer constant*.55)

Change 6.7.5.2#1 to read, in part:

> \[...\] an integer type. If the expression has a translation-time value, it
> shall be greater than zero. The element type \[...\]

the last part of #4 to read:

> If the size is an integer expression with a translation-time value and the
> element type has a known constant size, the array type is not a variable length
> array type; otherwise, the array type is a variable length array type.

#5 to begin:

> \[#5\] If the size is an expression that does not have a translation-time value:
> if it occurs \[...\]

#6 to begin:

> \[#6\] For two array types to be compatible, both shall have compatible element
> types, and if both size specifiers are present and have translation-time values,
> then both size specifiers shall have the same value.

and add a new example:

> \[#11\] EXAMPLE 5: an expression that contains only constants but breaks one or
> more of the rules of 6.6 does not have a translation-time value. Therefore, in:
>
> ```c
>      int fla [5];       // not a VLA, "5" has a translation-time value      int vla [(0, 5)];  // VLA, 6.6 forbids comma operators
> ```
>
> This can be used to force an array to have a constant size but still be variably
> modified.

---

Comment from WG14 on 2003-10-06:

**Committee Discussion** (for history only)  
The semantics and grammar overlap.  
The grammar says "this is an expression".  
The semantics says "this is a constant expression"

### Committee Response

> The Committee agrees with your analysis of "constant expression" and the
> division into four categories.
>
> We agree that line P1 is legitimate because "(1-1)" is a constant expression.
> Lines P2 and S1 do not include constant expressions because:
>
> * they contain a comma operator (forbidden by 6.6#3)
> * there is a valid interpretation of the code that uses a non-constant expression.
>
> Line S1 is legitimate, while line P2 violates the constraints of 6.5.16.1#3 (the
> right hand side must either have pointer to character or pointer to void type,
> or must be a null pointer constant). Line X1 violates the same constraint for
> the same reason (this was also addressed in DR 064).
>
> Line X2 is legitimate because there is no requirement for the right hand side to
> be a constant expression. Lines X3 and X4 are legitimate because the expressions
> are constant expressions with value `0` and therefore null pointer constants.
>
> The Committee also agrees that:
>
> ```c
>     int fla [(0+5)];     // is a normal array, not variably modified
>     int vla [(0,5)];     // is a variable length array
> ```
>
> In general, the interpretation of an expression for constantness is context
> sensitive. For any expression which contains only constants:
>
> * If the syntax or context only permits a constant expression, the constraints of 6.6#3 and 6.6#4 shall apply.
> * Otherwise, if the expression meets the requirements of 6.6 (including any form accepted in accordance with 6.6#10), it is a constant expression.
> * Otherwise it is not a constant expression.
>
> In summary, provided the above points are taken account of, the Committee does
> not believe the Standard is ambiguous nor that it is necessary to modify it to
> make this clearer.
