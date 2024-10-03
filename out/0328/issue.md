### Summary

6.5.2.5 Compound literals, paragraph 3 in ISO/IEC 9899:1999 C Standard says:

> If the compound literal occurs outside the body of a function, the initializer
> list shall consist of constant expressions.

This is to say a string literal, which is neither a constant nor a constant
expression, can not be taken to initialize a compound literal with static
storage duration. However, this is not the fact.

String literals can not be constants because they are not among constants
(defined in Section 6.4.4). When a string literal is used to initialize a
compound literal (in the case an array type), the array-to-pointer conversion
does not occur (6.3.2.1 Lvalues, arrays, and function designators, paragraph 3),
and hence the string literal can not be an address constant, which is the only
chance to become a constant expression.

Obviously string literals should be mentioned together with constant
expressions. It should be:

> If the compound literal occurs outside the body of a function, the initializer
> list shall consist of constant expressions or string literals.

The following paragraph excerpted from Page 125, 6.7.8-4 seems to support the
above correction:

> All the expressions in an initializer for an object that has static storage
> duration shall be constant expressions or string literals.

### Suggested Technical Corrigendum

Change 6.5.2.5, paragraph 3, to:

> If the compound literal occurs outside the body of a function, the initializer
> list shall consist of constant expressions or string literals.
