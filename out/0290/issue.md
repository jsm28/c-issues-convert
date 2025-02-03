### Summary

`FLT_EVAL_METHOD` says that *all* floating-point operations and operands are
evaluated to a format whose range and precision may be greater than required by
the type. This contradicts descriptions of assignment and cast. It may
contradict return. It may contradict argument passing. It may contradict
register variables.

**Details from C99\+TC1**

5.2.4.2.2 Characteristics of floating types \<float.h\>

> 7 The values of operations with floating operands and values subject to the
> usual arithmetic conversions and of floating constants are evaluated to a format
> whose range and precision may be greater than required by the type. The use of
> evaluation formats is characterized by the implementation-defined value of
> `FLT_EVAL_METHOD`:<sup>19\)</sup>
>
> -1 indeterminable;
>
> 0 evaluate all operations and constants just to the range and precision of the
> type;
>
> 1 evaluate operations and constants of type float and double to the range and
> precision of the double type, evaluate long double operations and constants to
> the range and precision of the long double type;
>
> 2 evaluate all operations and constants to the range and precision of the long
> double type.
>
> All other negative values for `FLT_EVAL_METHOD` characterize
> implementation-defined behavior.
>
> 19\) The evaluation method determines evaluation formats of expressions
> involving all floating types, not just real types. For example, if
> `FLT_EVAL_METHOD` is `1`, then the product of two `float _Complex` operands is
> represented in the `double _Complex` format, and its parts are evaluated to
> `double`.

5.1.2.3 Program Execution

> 12 EXAMPLE 4 Implementations employing wide registers have to take care to honor
> appropriate semantics. Values are independent of whether they are represented in
> a register or in memory. For example, an implicit spilling of a register is not
> permitted to alter the value. Also, an explicit store and load is required to
> round to the precision of the storage type. In particular, casts and assignments
> are required to perform their specified conversion. For the fragment

```c
                double d1, d2;
                float f;
                d1 = f = expression;
                d2 = (float)expressions;
```

> the values assigned to `d1` and `d2` are required to have been converted to
> `float`.

6.3 Conversions

> 1 Several operators convert operand values from one type to another
> automatically. This subclause specifies the result required from such an
> implicit conversion, as well as those that result from a cast operation (an
> explicit conversion). The list in 6.3.1.8 summarizes the conversions performed
> by most ordinary operators; it is supplemented as required by the discussion of
> each operator in 6.5.

6.3.1.5 Real floating types

> 1 When a `float` is promoted to `double` or `long double`, or a `double` is
> promoted to `long double`, its value is unchanged.
>
> 2 When a `double` is demoted to `float`, a `long double` is demoted to `double`
> or `float`, or a value being represented in greater precision and range than
> required by its semantic type (see 6.3.1.8) is explicitly converted to its
> semantic type, if the value being converted can be represented exactly in the
> new type, it is unchanged. If the value being converted is in the range of
> values that can be represented but cannot be represented exactly, the result is
> either the nearest higher or nearest lower representable value, chosen in an
> implementation-defined manner. If the value being converted is outside the range
> of values that can be represented, the behavior is undefined.

6.3.1.8 Usual Arithmetic Conversions

> 2 The values of floating operands and of the results of floating expressions may
> be represented in greater precision and range than that required by the type;
> the types are not changed thereby.<sup>52\)</sup>
>
> 52\) The cast and assignment operators are still required to perform their
> specified conversions as described in 6.3.1.4 and 6.3.1.5.

6.5.4 Cast operators

Semantics

> 4 Preceding an expression by a parenthesized type name converts the value of the
> expression to the named type. This construction is called a cast.<sup>85\)</sup>
> A cast that specifies no conversion has no effect on the type or value of an
> expression.<sup>86\)</sup>
>
> 86\) If the value of the expression is represented with greater precision or
> range than required by the type named by the cast (6.3.1.8), then the cast
> specifies a conversion even if the type of the expression is the same as the
> named type.

6.5.2.2 Function calls

Semantics

> 4 An argument may be an expression of any object type. In preparing for the call
> to a function, the arguments are evaluated, and each parameter is assigned the
> value of the corresponding argument.<sup>78\)</sup>

6.9.1 Function definitions

Semantics

> 10 On entry to the function, the size expressions of each variably modified
> parameter are evaluated and the value of each argument expression is converted
> to the type of the corresponding parameter as if by assignment. (Array
> expressions and function designators as arguments were converted to pointers
> before the call.)

6.8.6.4 The return statement

Semantics

> 3 If a return statement with an expression is executed, the value of the
> expression is returned to the caller as the value of the function call
> expression. If the expression has a type different from the return type of the
> function in which it appears, the value is converted as if by assignment to an
> object having the return type of the function.<sup>136\)</sup>
>
> 136\) The return statement is not an assignment. The overlap restriction of
> subclause 6.5.16.1 does not apply to the case of function return.

6.7.1 Storage-class specifiers

Semantics

> 4 A declaration of an identifier for an object with storage-class specifier
> register suggests that access to the object be as fast as possible. The extent
> to which such suggestions are effective is
> implementation-defined.<sup>100\)</sup>
>
> 100\) The implementation may treat any register declaration simply as an auto
> declaration. However, whether or not addressable storage is actually used, the
> address of any part of an object declared with storage-class specifier register
> cannot be computed, either explicitly (by use of the unary \& operator as
> discussed in 6.5.3.2) or implicitly (by converting an array name to a pointer as
> discussed in 6.3.2.1). Thus, the only operator that can be applied to an array
> declared with storage-class specifier register is `sizeof`.

### Suggested Technical Corrigendum

In 5.2.4.2.2 Characteristics of floating types \<float.h\>, change paragraph 7
to:

> Except for assignment and cast (which remove all extra range and precision), the
> values of operations with floating operands and values subject to the usual
> arithmetic conversions and of floating constants are evaluated to a format whose
> range and precision may be greater than required by the type. The use of
> evaluation formats is characterized by the implementation-defined value of
> `FLT_EVAL_METHOD`:<sup>19\)</sup>

In 6.8.6.4 The return statement, add to footnote 136:

> The representation of floating-point values may have wider range or precision
> and is determined by `FLT_EVAL_METHOD`. A cast may be used to remove this extra
> range and precision.

In 5.1.2.3 Program Execution, paragraph 12, change the second sentence to:

> Implementation created intermediate values are independent of whether they are
> represented in a register or in memory.

In 6.7.1 Storage-class specifiers, add to paragraph 4:

> A floating object with storage-class register may have greater range or
> precision than an auto object of the same type.
