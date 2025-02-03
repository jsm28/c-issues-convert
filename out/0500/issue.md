### Summary

5.2.4.2.2#9:

> Except for assignment and cast (which remove all extra range and precision), the
> values yielded by operators with floating operands and values subject to the
> usual arithmetic conversions and of floating constants are evaluated to a format
> whose range and precision may be greater than required by the type. The use of
> evaluation formats is characterized by the implementation-defined value
> of `FLT_EVAL_METHOD`:
>
> `-1` indeterminable;
>
> `0` evaluate all operations and constants just to the range and precision of the
> type;
>
> `1` evaluate operations and constants of type `float` and `double` to the range
> and precision of the `double` type, evaluate `long double` operations and
> constants to the range and precision of the `long double` type;
>
> `2` evaluate all operations and constants to the range and precision of the
> `long double` type.
>
> All other negative values for `FLT_EVAL_METHOD` characterize
> implementation-defined behavior

Do the words:

> the values yielded by operators with floating operands and values subject to the
> usual arithmetic conversions

in the first sentence mean the same as:

> Interpretation 1: the values yielded by operators with: (a) floating operands
> and (b) values subject to the usual arithmetic conversions

or:

> Interpretation 2: (a) the values yielded by operators with floating operands and
> (b) the values subject to the usual arithmetic conversions?

Interpretation 2 is problematic because the evaluation methods pertain only to
operators that return a value of floating type, not to, for example, the
relational operators with floating operands. Nor do they apply to all values
subject to the usual arithmetic conversions, and so (b) doesn’t add anything.
Thus, reasonableness suggests Interpretation 1\. However, the mention of
assignment and cast (which are not subject to the usual arithmetic conversions)
suggests Interpretation 2\.

Interpretation 2, unlike Interpretation 1, implies that values yielded by unary
operators are widened to the evaluation format. In some cases whether a unary
operator is widened matters. Widening a signaling NaN operand raises the
“invalid” floating-point exception. Widening an operand with a non-canonical
encoding canonicalizes the encoding.

The IEC 60559 *copy* and *negate* operations are bit manipulation operations
that affect at most the sign. C operations bound to these IEC 60559 operations
are expected to behave accordingly, but won’t if they entail widening.

Widening unary operators would introduce conversions that might affect
performance but which have no benefit.

According to personal notes, this issue came up at the WG14 meeting in Chicago
in 2013, but was not resolved and did not result in an action item.

Recently, this issue came up again as underlying the issue raised by Joseph
Myers in email SC22WG14.14278:

> Suppose that with an implementation of C11 \+ TS 18661-1, that defines
>
> `FLT_EVAL_METHOD` to `2`, you have:
>
> > ```c
> > static volatile double x = SNAN;
> >
> > (void) x;
> > ```
>
> Suppose also that the implementation defines the "`(void) x;`" statement to
>
> constitute an access to volatile-qualified `x`.
>
> May the implementation define that access to convert `x` from the format of
>
> `double` to the format of `long double`, with greater range and precision,
>
> that format being used to represent `double` operands in accordance with the
>
> setting of `FLT_EVAL_METHOD`, and thereby to raise the "invalid" exception?
>
> That is, may a convertFormat operation be applied as part of
>
> lvalue-to-rvalue conversion where `FLT_EVAL_METHOD` implies that a wider
>
> evaluation format is in use?
>
> Even without signaling NaNs, the issue can apply to the case of exact
>
> underflow, which can be detected using pragmas from TS 18661-5, if the
>
> wider format has extra precision but not extra range and so exact underflow
> occurs on converting a subnormal value to the wider format.

The following suggested Technical Corrigendum is intended to clarify the wording
in favor of Interpretation 1, which excludes widening unary operators to the
evaluation format.

### Suggested Technical Corrigendum

In 5.2.4.2.2#9, replace:

> Except for assignment and cast (which remove all extra range and precision), the
> values yielded by operators with floating operands and values subject to the
> usual arithmetic conversions and of floating constants are evaluated to a format
> whose range and precision may be greater than required by the type.

with:

> The values of floating type yielded by operators subject to the usual
> arithmetic conversions and the values of floating constants are evaluated to a
> format whose range and precision may be greater than required by the type. In
> all cases, assignment and cast remove all extra range and precision.
