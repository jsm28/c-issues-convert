### Summary

Three 'equivalent' phrases are used:

```c
    effective rounding
    current rounding
    rounding mode characterized by the value of FLT_ROUNDS
```

when C99 should be using just one.

Six 'equivalent' phrases are used:

```c
    rounding direction mode
    rounding direction
    rounding mode
    directed-rounding control mode
    directed rounding mode
    rounding control mode
```

when C99 should be using just one.

### Details

3.9 correctly rounded result: representation in the result format that is
nearest in value, subject to the effective rounding mode, to what the result
would be given unlimited range and precision

5.2.4.2.2 Characteristics of floating types \<float.h\>: Paragraph 6: The
rounding mode for floating-point addition is characterized by the
implementation-defined value of `FLT_ROUNDS`:18)

18\) Evaluation of `FLT_ROUNDS` correctly reflects any execution-time change of
rounding mode through the function `fesetround` in \<fenv.h\>.

7.6 Floating-point environment \<fenv.h\>:

Paragraph 1: The header \<fenv.h\> declares two types and several macros and
functions to provide access to the floating-point environment. The
floating-point environment refers collectively to any floating-point status
flags and control modes supported by the implementation.173)

173\) This header is designed to support the floating-point exception status
flags and directed-rounding control modes required by IEC 60559, and other
similar floating-point state information.

Paragraph 7 Each of the macros: `FE_DOWNWARD`, `FE_TONEAREST`, `FE_TOWARDZERO`,
`FE_UPWARD`; is defined if and only if the implementation supports getting and
setting the represented rounding direction by means of the `fegetround` and
`fesetround` functions.

7.6.3 Rounding: Paragraph 1 The `fegetround` and `fesetround` functions provide
control of rounding direction modes.

7.12.9.3 The `nearbyint` functions: Paragraph 2: The `nearbyint` functions round
their argument to an integer value in floating-point format, using the current
rounding direction and without raising the inexact floating-point exception.

7.12.9.5 The `lrint` and `llrint` functions: Paragraph 2: The `lrint` and
`llrint` functions round their argument to the nearest integer value, rounding
according to the current rounding direction.

7.12.9.6 The `round` functions: Paragraph 2: The `round` functions round their
argument to the nearest integer value in floating-point format, rounding halfway
cases away from zero, regardless of the current rounding direction.

7.12.9.7 The `lround` and `llround` functions: Paragraph 2: The `lround` and
`llround` functions round their argument to the nearest integer value, rounding
halfway cases away from zero, regardless of the current rounding direction.

Footnote 203\) When y !\= 0, the remainder r \= x REM y is defined regardless of
the rounding mode ...

7.12.13.1 The `fma` functions: Paragraph 2: The `fma` functions compute
(x\*y)\+z, rounded as one ternary operation: they compute the value (as if) to
infinite precision and round once to the result format, according to the
rounding mode characterized by the value of `FLT_ROUNDS`.

7.19.6.1 The `fprintf` function:

Paragraph 12: ... error should have a correct sign for the current rounding
direction.

Paragraph 13: ... error should have a correct sign for the current rounding
direction.

7.20.1.3 The `strtod`, `strtof`, and `strtold` functions:

Paragraph 8: ... error should have a correct sign for the current rounding
direction.

Paragraph 9: ... according to the current rounding direction, ... ... should
have a correct sign for the current rounding direction.

7.24.2.1 The `fwprintf` function:

Paragraph 12: ... error should have a correct sign for the current rounding
direction.

Paragraph 13: ... the error should have a correct sign for the current rounding
direction.

7.24.4.1.1 The `wcstod`, `wcstof`, and `wcstold` functions:

Paragraph 8: ... the error should have a correct sign for the current rounding
direction.

Paragraph 9: ... according to the current rounding direction, with the extra
stipulation that the error with respect to D should have a correct sign for the
current rounding direction.

Annex F.3 Operators and functions: Paragraph 1: The `fegetround` and
`fesetround` functions in \<fenv.h\> provide the facility to select among the
IEC 60559 directed rounding modes represented by the rounding direction macros
in \<fenv.h\> (`FE_TONEAREST`, `FE_UPWARD`, `FE_DOWNWARD`, `FE_TOWARDZERO`) and
the values 0, 1, 2, and 3 of `FLT_ROUNDS` are the IEC 60559 directed rounding
modes.

Annex F.5 Binary-decimal conversion:

Paragraph 2: Conversions involving IEC 60559 formats follow all pertinent
recommended practice. In particular, conversion between any supported IEC 60559
format and decimal with `DECIMAL_DIG` or fewer significant digits is correctly
rounded, which assures that conversion from the widest supported IEC 60559
format to decimal with `DECIMAL_DIG` digits and back is the identity function.

Paragraph 3: 3 Functions such as `strtod` that convert character sequences to
floating types honor the rounding direction. Hence, if the rounding direction
might be upward or downward, the implementation cannot convert a minus-signed
sequence by negating the converted unsigned sequence.

Annex F.6 Contracted expressions: Paragraph 1: A contracted expression treats
infinities, NaNs, signed zeros, subnormals, and the rounding directions in a
manner consistent with the basic arithmetic operations covered by IEC 60559\.

Annex F.7 Floating-point environment: Paragraph 1: The floating-point
environment defined in \<fenv.h\> includes the IEC 60559 floating-point
exception status flags and directed-rounding control modes.

Annex F.7.1 Environment management: Paragraph 1: IEC 60559 requires that
floating-point operations implicitly raise floating-point exception status
flags, and that rounding control modes can be set explicitly to affect result
values of floating-point operations.

Annex F.7.2 Translation: Paragraph 1: During translation the IEC 60559 default
modes are in effect: The rounding direction mode is rounding to nearest.

Footnote 306\) As floating constants are converted to appropriate internal
representations at translation time, their conversion is subject to default
rounding modes ...

Annex F.7.3 Execution: Paragraph 1: At program startup the floating-point
environment is initialized as prescribed by IEC 60559: All floating-point
exception status flags are cleared. The rounding direction mode is rounding to
nearest.

Footnote 307\) Where the state for the `FENV_ACCESS` pragma is "on", results of
inexact expressions like 1.0/3.0 are affected by rounding modes set at execution
time, ...

Annex F.8.2 Expression transformations: has in several places: default rounding
direction.

Annex F.8.4 Constant arithmetic: Paragraph 1: ... changing the rounding
direction to downward ...

Footnote 311\) 0-0 yields -0 instead of \+0 just when the rounding direction is
downward.

Annex F.9 Mathematics \<math.h\>:

Paragraph 6: ... rounding direction, ...

Paragraph 10: Whether the functions honor the rounding direction mode is
implementation-defined.

Annex F.9.6.3 The `nearbyint` functions: Paragraph 1: The `nearbyint` functions
use IEC 60559 rounding according to the current rounding direction.

Annex F.9.6.5 The `lrint` and `llrint` functions: Paragraph 1: The `lrint` and
`llrint` functions provide floating-to-integer conversion as prescribed by IEC
60559\. They round according to the current rounding direction.

Annex F.9.6.7 The `lround` and `llround` functions: Paragraph 1: The `lround`
and `llround` functions differ from the `lrint` and `llrint` functions with the
default rounding direction ...

Annex F.9.6.8 The `trunc` functions: Paragraph 1: The `trunc` functions use IEC
60559 rounding toward zero (regardless of the current rounding direction).

Annex J.3.6 Floating point: Paragraph 1: Additional floating-point exceptions,
rounding modes, environments, and classifications, and their macro names (7.6,
7.12).

Annex J.3.12 Library functions: Whether the functions in \<math.h\> honor the
rounding direction mode in an IEC 60559 conformant implementation (F.9).

Index:

correctly rounded result, 3.9

floating-point rounding mode, 5.2.4.2.2

rounding mode, floating point, 5.2.4.2.2

### Suggested Technical Corrigendum

Of the six 'equivalent' phrases that involve 'rounding', 'direction', 'control',
and 'mode', pick one ('rounding mode' is the submitter's choice) and change the
others to it thruout the C99 standard.

Change 3.9 'effective rounding mode' to 'current rounding mode'.

Change 7.12.13.1 The `fma` functions: '... the rounding mode characterized by
the value of `FLT_ROUNDS`' to '... the current rounding mode'.

Change Annex F.5 Binary-decimal conversion: Paragraph 2: 'correctly rounded' to
'correctly rounded (which honors the current rounding mode)'. Note: Once
'effective rounding mode' is changed to 'current rounding mode', is this change
really needed (since correctly rounded implies honors the current rounding
mode)?
