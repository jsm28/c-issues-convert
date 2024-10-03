May floating-point constants be represented with more precision than implied by
its type? Consider the following code fragment:

```c
float f;
 double d;
 long double ld;
 ld = ld + 0.1; /* add a long double and a double */
 ld = ld + 1.0 / 10.0; /* expression with "same" value */
 d = f + 0.1f; /* "+" is allowed to be double precision */
```

In the above example, the decimal number `0.1`, when converted to binary, is a
non-terminating repeating binary number; so the more bits used to represent the
number, the closer it will be to its true value. Hence, if `double`s are 64 bits
and `long double`s are 80 bits, the `long double` will be more accurate. So in
essence, may `0.1` (a `double`) be represented with more precision, e.g. as
`0.1L` (a `long double`)?

Parts of the C Standard that may help answer the question follow.

Subclause 5.1.2.3 **Program execution**, page 7, line 36:

> In the abstract machine, all expressions are evaluated as specified by the
> semantics.

I believe that this is the “as if” rule that applies to this case.

Subclause 5.1.2.3 **Program execution**, page 8, lines 44-45:

> Alternatively, an operation involving only `int`s or `float`s may be executed
> using double-precision operations if neither range nor precision is lost
> thereby.

Clearly, `d = f + 0.1F` may be done using a double-precision add. But may `0.1f`
be represented as the `double 0.1`?

Subclause 6.1.3.1 **Floating constants**, page 26, lines 32-35:

> If the scaled value is in the range of representable values (for its type) the
> result is either the nearest representable value, or the larger or smaller
> representable value immediately adjacent to the nearest representable value,
> chosen in an implementation-defined manner.

I believe that the above does not require that the result be the nearest
representable value (for its type).

Subclause 6.2.1.5 **Usual arithmetic conversions**, page 35, lines 38-39:

> The values of floating operands and of the results of floating expressions may
> be represented in greater precision and range than that required by the type;
> the types are not changed thereby.

I believe that a floating constant is a floating operand, so is allowed greater
precision. Clearly, the expression `1.0 / 10.0` is allowed greater precision
than just `double`, so it would make sense to allow an equivalent constant
(`0.1`) to have greater precision.

Subclause 6.4 **Constant expressions**, page 55, lines 14-16:

> If a floating expression is evaluated in the translation environment, the
> arithmetic precision and range shall be at least as great as if the expression
> were being evaluated in the execution environment.
