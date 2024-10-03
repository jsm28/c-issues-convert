### Summary

The standard does not require translation-time expression evaluation to produce
"obvious" values. For example, there is no requirement that `static const double
d = 1.23/4.56 - 1.23/4.56;` be zero.

### Details

5.2.4.2.2p7 discusses `FLT_EVAL_FORMAT`, range and precision of floating-point
constants and operations.

6.4.4.2p5 discusses translation time conversion of floating-point constants to
internal format.

6.6p5 discusses translation time evaluation of floating-point constant
expressions.

F.7.2p2 and footnote 306 discusses conversion of floating-point constants to
internal representation.

F.7.5p3 discusses initialization and internal representation of floating-point
constants.

Currently, if `FLT_EVAL_METHOD` is negative, there is no requirement that the
first 1.23 and the second 1.23 convert to the same internal representation; one
could have more precision than the other. While the same range and precision is
a requirement when `FLT_EVAL_METHOD` is 0, 1, or 2, there is no requirement that
those two identical constants convert to the same value.

Currently, if `FLT_EVAL_METHOD` is negative, there is no requirement that the
first '/' produce a result with the same precision as the second '/' (for the
same operands). This is a requirement when `FLT_EVAL_METHOD` is 0, 1, or 2\.

Without these two requirements, the best one can do to try to get zero is:
`static const double d = (double)((double)1.23/(double)4.56) -
(double)((double)1.23/(double)4.56);` and even that could fail if the first 1.23
and the second 1.23 convert to different values.

For translation-time expression evaluation to produce the "obvious" value, two
requirments must be met: the same decimal constants must result in the same
value and internal representation, and operators must use the same precision.

### Suggested Technical Corrigendum

6.4.4.2 Floating constants: Add to paragraph 5: All floating-constants of the
same source form in the same translation unit shall convert to the same internal
format with the same value. Footnote: 1.23, 1.230, 123e-2, 123e-02, 1.23L are
all different source forms, so need not convert to the same internal format and
value.

Add to 6.4.4.2p7, All floating-constants with the same mathematical value and
type in the same translation unit should convert to the same internal format and
value. Footnote: 1.23, 1.230, 123e-2 and 123e-02 have the same mathematical
value, so should convert to the same internal format and value.

6.6: Constant expression: Add a 12th paragraph: All operators with the same
type(s) of floating-point operand(s) in the same translation unit shall use the
same precision.
