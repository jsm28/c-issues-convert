### Summary

When `FLT_EVAL_METHOD` is 2, the 0.1f is represented to the precision of `long
double`, while the type remains as `float`. Then, when the cast to `double` is
done, contradictory requirements are specified by the standard. One part of the
standard requires that when a float is promoted to a double, the value is
unchanged. While another part of the standard requires that extra precision be
removed by the cast conversion.

### Details

5.2.4.2.2 Characteristics of floating types \<float.h\>; Paragraph 7 \[after DR
290\]

> Except for assignment and cast (which remove all extra range and precision), the
> values of operations with floating operands and values subject to the usual
> arithmetic conversions and of floating constants are evaluated to a format whose
> range and precision may be greater than required by the type. The use of
> evaluation formats is characterized by the implementation-defined value of
> `FLT_EVAL_METHOD`:<sup>19\)</sup>
>
> **2** evaluate all operations and constants to the range and precision of `long
> double` type.

6.3.1.5 Real floating types; Paragraphs 1 and 2

> When a `float` is promoted to `double` or `long double`, or a `double` is
> promoted to `long double`, its value is unchanged.
>
> When a `double` is demoted to `float`, a `long double` is demoted to `double` or
> `float`, or a value being represented in greater precision and range than
> required by its semantic type (see 6.3.1.8) is explicitly converted to its
> semantic type, if the value being converted can be represented exactly in the
> new type, it is unchanged. If the value being converted is in the range of
> values that can be represented but cannot be represented exactly, the result is
> either the nearest higher or nearest lower representable value, chosen in an
> implementation-defined manner. If the value being converted is outside the range
> of values that can be represented, the behavior is undefined.

6.3.1.8 Usual arithmetic conversions; Paragraph 2

> The values of floating operands and of the results of floating expressions may
> be represented in greater precision and range than that required by the type;
> the types are not changed thereby. <sup>52\)</sup>
>
> 52\) The cast and assignment operators are still required to perform their
> specified conversions as described in 6.3.1.4 and 6.3.1.5.

6.5.4 Cast operators; Paragraph 4

> ... A cast that specifies no conversion has no effect on the type or value of an
> expression. <sup>86\)</sup>
>
> 86\) If the value of the expression is represented with greater precision or
> range than required by the type named by the cast (6.3.1.8), then the cast
> specifies a conversion even if the type of the expression is the same as the
> named type.

### Suggested Technical Corrigendum

Add to 6.3.1.5, the end of paragraph 1: "(if the source value is represented in
the precision and range of its type)".

Change in 6.3.1.5, paragraph 2, "explicitly converted to its semantic type" to
"explicitly converted (including to its own type)".

Move the text of footnote 86 to normative text in 6.5.4.

An alternative (not liked by the author) is to add a footnote to 6.3.1.5 along
the lines of: To force a floating-point value to have no more precision than a
given type requires two casts to that type, e.g., `(double)(double)0.1f`
assuredly has no more precision than `(double)`. The rightmost cast changes the
type, but not the representation, while the leftmost cast changes the
representation (throws away any extra precision or range).
