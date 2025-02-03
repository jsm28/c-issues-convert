### Summary

Exactly WHERE are the MEANINGS of any of the FE\_\* macros defined in cases
where \<fenv.h\> applies to an environment that is not IEEE-754 (IEC 60559)?

### Details

5.1.2.3p2 Program execution says:

> Accessing a volatile object, modifying an object, modifying a file, or calling a
> function that does any of those operations are all side effects,<sup>11\)</sup>
> which are changes in the state of the execution environment. Evaluation of an
> expression may produce side effects.
>
> 11\) The IEC 60559 standard for binary floating-point arithmetic requires
> certain user-accessible status flags and control modes. Floating-point
> operations implicitly set the status flags; modes affect result values of
> floating-point operations. Implementations that support such floating-point
> state are required to regard changes to it as side effects see annex F for
> details. The floating-point environment library \<fenv.h\> provides a
> programming facility for indicating when these side effects matter, freeing the
> implementations in other cases.

The above footnote is the closest I can find to a requirement that there is any
relationship between floating-point operations, status flags, and modes. But, it
is a footnote, and only for IEC 60559\.

5.2.4.2.2p6 Characteristics of floating types \<float.h\> has:

> The rounding mode for floating-point addition is characterized by the
> implementation-defined value of FLT\_ROUNDS:<sup>18\)</sup>
>
> ```c
>  -1 indeterminable
>   0 toward zero
>   1 to nearest
>   2 toward positive infinity
>   3 toward negative infinity
> ```
>
> All other values for FLT\_ROUNDS characterize implementation-defined rounding
> behavior.
>
> 18\) Evaluation of FLT\_ROUNDS correctly reflects any execution-time change of
> rounding mode through the function fesetround in \<fenv.h\>.

The above mentions, but does not define, some rounding modes.

7.6p5 Floating-point environment \<fenv.h\> has:

> Each of the macros
>
> ```c
>    FE_DIVBYZERO
>    FE_INEXACT
>    FE_INVALID
>    FE_OVERFLOW
>    FE_UNDERFLOW
> ```
>
> is defined if and only if the implementation supports the floating-point
> exception by means of the functions in 7.6.2. <sup>175\)</sup> Additional
> implementation-defined floating-point exceptions, with macro definitions
> beginning with FE\_ and an uppercase letter, may also be specified by the
> implementation.
>
> 175\) The implementation supports an exception if there are circumstances where
> a call to at least one of the functions in 7.6.2, using the macro as the
> appropriate argument, will succeed. It is not necessary for all the functions to
> succeed all the time.

The above mentions, but does not define, some floating-point exceptions.

If an implementation defines a new floating-point exception, FE\_BLUEMOON, such
that:

* `feraiseexcept(FE_BLUEMOON)` succeeds,
* `fetestexcept(FE_BLUEMOON)` returns the current status of that "exception",
* `feclearexcept(FE_BLUEMOON)` succeeds,

but FE\_BLUEMOON is NOT tied to any floating-point operation, is this valid
"support"?

7.6p7 Floating-point environment \<fenv.h\> has:

> Each of the macros
>
> ```c
>    FE_DOWNWARD
>    FE_TONEAREST
>    FE_TOWARDZERO
>    FE_UPWARD
> ```
>
> is defined if and only if the implementation supports getting and setting the
> represented rounding direction by means of the fegetround and fesetround
> functions. Additional implementation-defined rounding directions, with macro
> definitions beginning with FE\_ and an uppercase letter, may also be specified
> by the implementation. The defined macros expand to integer constant expressions
> whose values are distinct nonnegative values.<sup>176\)</sup>
>
> 176\) Even though the rounding direction macros may expand to constants
> corresponding to the values of FLT\_ROUNDS, they are not required to do so.

The above mentions, but does not define, some rounding modes.

F.8.1p1 Global transformations says:

> Floating-point arithmetic operations and external function calls may entail side
> effects which optimization shall honor, at least where the state of the
> FENV\_ACCESS pragma is "on". The flags and modes in the floating-point
> environment may be regarded as global variables; floating-point operations (\+,
> \*, etc.) implicitly read the modes and write the flags.

The above is a clear description of how modes and flags interact with
operations, but it applies only to IEEE-754.

### Suggested Technical Corrigendum

7.6 Floating-point environment \<fenv.h\>: Add to paragraph 5:

> A necessary condition for an implementation to support a given FE\_\* exception
> is that it implicitly occur as a side effect of at least one floating-point
> operation. Just having `feraiseexcept()`, `fetestexcept()` and `feclearexcept()`
> succeed for a given FE\_\* exception is not sufficient.
>
> `FE_INVALID` should be a side-effect of:
>
> * operations on signaling NaN or trap representation,
> * adding infinities with different signs,
> * subtracting infinities with the same signs,
> * multipling zero by infinity,
> * dividing zero by zero and infinity by infinity,
> * remainder (x REM y), where x is infinite or y is zero,
> * square root of a negative number (excluding -0.0),
> * converting a too large to represent floating value to an integer \[both signed and unsigned], e.g., int i \= INFINITY; unsigned int ui \= -1.0;
> * comparison with a relational operator (\<, \<\=, \>\=, \>) when (at least) one of the operands is a NaN.
>
> `FE_DIVBYZERO` should be a side-effect of dividing a non-zero finite number by
> zero, e.g., 1.0/0.0. There should be no exception when dividing an infinity by
> zero, nor when dividing a NaN by zero.
>
> It is implementation defined as to whether FE\_INVALID, FE\_DIVBYZERO, or no
> exception is raised for zero / zero.
>
> `FE_OVERFLOW` should be a side-effect of producing a rounded floating-point
> result (assuming an unbounded exponent range) larger in magnitude than the
> largest finite number.
>
> `FE_UNDERFLOW` should be a side-effect of producing a rounded floating-point
> result (assuming an unbounded exponent range) smaller in magnitude than the
> smallest non-zero finite number, or an inexact denormal number smaller than the
> smallest non-zero normalized number.
>
> `FE_INEXACT` should be a side-effect of producing a rounded floating-point
> result that differs from the mathematical (or infinitely precise) result.

Also in 7.6, change footnote 175 from "The implementation supports an exception
if ..." to "The implementation supports an exception if that exception happens
as a side-effect of at least one floating-point operation and if ..."

5.2.4.2.2 Characteristics of floating types \<float.h\>: Add to paragraph 6:

> See 7.6 Floating-point environment paragraph 7 for meaning of these rounding
> modes.

7.6 Floating-point environment \<fenv.h\>: Add to paragraph 7:

> A necessary condition for an implementation to support these rounding control
> modes is that they can be set explicitly and that they affect result values of
> floating-point operations. Just having `fegetround()` and `fesetround()` succeed
> for a given FE\_\* rounding direction is not sufficient.
>
> `FE_TOWARDZERO` means the result shall be the format's value closest to and no
> greater in magnitude than the infinitely precise result. For example, if
> rounding to integer value in floating-point format, \+3.7 rounds to \+3.0 and
> -3.7 rounds to -3.0.
>
> `FE_UPWARD` means the result shall be the format's value closest to and no less
> than the infinitely precise result. For example, if rounding to integer value in
> floating-point format, \+3.1 rounds to \+4.0 and -3.7 rounds to -3.0.
>
> `FE_DOWNWARD` means the result shall be the format's value closest to and no
> greater than the infinitely precise result. For example, if rounding to integer
> value in floating-point format, \+3.7 rounds to \+3.0 and -3.1 rounds to -4.0.
>
> `FE_TONEAREST` means the result shall be the format's value closest to the
> infinitely precise result. It is implementation defined as to what happens when
> the two nearest representable values are equally near. For example, if rounding
> to integer value in floating-point format, \+3.1 rounds to \+3.0 and \+3.7
> rounds to \+4.0, and \+3.5 rounds to either \+3.0 or \+4.0.

Add to J.3.6 Floating point:

> \-- to nearest rounding result when the two nearest representable values are
> equally near.
>
> \-- whether FE\_INVALID, FE\_DIVBYZERO, or no exception is raised for zero /
> zero.

Add 7.6 to the index entry for floating-point rounding mode.
