## Issue 0CFP.13: P3: Type-generic macros for functions that round result to narrower type

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas  
Date: 2017-03-04  
Reference document: [N2125](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2125.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This is about an issue raised by Joseph Myers in SC22WG14.14561:

> TS 18661-1 and -2 define type-generic macros for the functions that round
>
> result to a narrower type.  In part 1 these are, for example, fadd and
>
> dadd for addition; in part 2, for example, d32add and d64add.
>
> Part 3 does not seem to make any changes or additions to those macros, and
>
> consequences of that seem nonobvious.  It defines new functions for the
>
> new types: fMaddfN, fMaddfNx, fMxaddfN, fMxaddfNx (where M \< N, or M \<\= N
>
> in the fMaddfNx case), and likewise for decimal types.  But the
>
> type-generic macros remain as defined in 7.25#6a after the changes from
>
> parts 1 and 2 are applied (part 3 does not contain the string "6a").
>
> That is, it's valid to pass the \_FloatN and \_FloatNx types to the fadd and
>
> dadd macros, and valid to pass the new \_DecimalN and \_DecimalNx types from
>
> part 3 to the d32add and d64add types.
>
> (a) 7.25#6a says "If the macro prefix is d32 or d64, use of an argument of
>
> standard floating type results in undefined behavior.".  Other places get
>
> amended in part 3 to say "floating type of radix 2" in addition to
>
> "standard floating type".  But it appears it fails to make it undefined to
>
> pass \_FloatN or \_FloatNx arguments to d32add, d64add etc. type-generic
>
> macros \- although clearly it should be undefined.
>
> (b) Passing \_Decimal128 to d32add would result in the d32addd128 function
>
> being called, as expected.  But say you pass a \_Decimal128x argument.  A
>
> function d32addd128x exists but the specification would seem to result in
>
> d32addd64 being called, which seems unintuitive.  Similar issues apply
>
> with \_FloatN and \_FloatNx types \- calling fadd on them would always call
>
> the fadd function not faddl.  (But in that case there \*are\* no functions
>
> defined that take \_FloatN / \_FloatNx arguments and return float or double.
>
> So the right thing to do is less obvious.)

The following addresses these issues by filling in the missing specification in
part 3\.

### Suggested Technical Corrigendum

In clause 15, after the change to 7.25#6, add:

> Change 7.25#6a from:
>
> > \[6a\] The functions that round result to a narrower type have type-generic
> > macros whose names are obtained by omitting any suffix from the function names.
> > Thus, the macros with `f` or `d` prefix are:
> >
> > > ```c
> > > fadd              fmul                 ffma
> > >
> > > dadd              dmul                 dfma
> > >
> > > fsub              fdiv                 fsqrt
> > >
> > > dsub              ddiv                 dsqrt
> > > ```
>
> and the macros with `d32` or `d64` prefix are:
>
> > ```c
> > d32add            d32mul               d32fma
> >
> > d64add            d64mul               d64fma
> >
> > d32sub            d32div               d32sqrt
> >
> > d64sub            d64div               d64sqrt
> > ```
> >
> > All arguments are generic. If any argument is not real, use of the macro results
> > in undefined behavior. If the macro prefix is `f` or `d`, use of an argument of
> > decimal floating type results in undefined behavior. If the macro prefix is
> > `d32` or `d64`, use of an argument of standard floating type results in
> > undefined behavior. The function invoked is determined as follows:
> >
> > > —    If any argument has type `_Decimal128`, or if the macro prefix is `d64`,
> > > the function invoked has the name of the macro, with a `d128` suffix.
> > >
> > > —    Otherwise, if the macro prefix is `d32`, the function invoked has the name
> > > of the macro, with a `d64` suffix.
> > >
> > > —    Otherwise, if any argument has type `long double`, or if the macro prefix
> > > is `d`, the function invoked has the name of the macro, with an `l` suffix.
> > >
> > > —    Otherwise, the function invoked has the name of the macro (with no suffix).
>
>  to:
>
> > \[6a\] The functions that round result to a narrower type have type-generic
> > macros whose names are obtained by omitting any suffix from the function names.
> > Thus, the macros with `f` or `d` prefix are:
> >
> > > ```c
> > > fadd              fmul                 ffma
> > >
> > > dadd              dmul                 dfma
> > >
> > > fsub              fdiv                 fsqrt
> > >
> > > dsub              ddiv                 dsqrt
> > > ```
>
> and the macros with `f`*M*, `f`*M*`x`, `d`*M*, or `d`*M*`x` prefix are:
>
> > `f`*M*`add             f`*`M`*`xmul              d`*`M`*`fma`
> >
> > `f`*M*`sub             f`*`M`*`xdiv              d`*`M`*`sqrt`
> >
> > `f`*M*`mul             f`*`M`*`xfma              d`*`M`*`xadd`
> >
> > `f`*M*`div             f`*`M`*`xsqrt             d`*`M`*`xsub`
> >
> > `f`*M*`fma             d`*`M`*`add               d`*`M`*`xmul`
> >
> > `f`*M*`sqrt            d`*`M`*`sub               d`*`M`*`xdiv`
> >
> > `f`*M*`xadd            d`*`M`*`mul               d`*`M`*`xfma`
> >
> > `f`*M*`xsub            d`*`M`*`div               d`*`M`*`xsqrt`
>
> All arguments are generic. If any argument is not real, use of the macro results
> in undefined behavior. If the macro prefix is `f`, `d`, `f`*M*, or `f`*M*`x`,
> use of an argument of decimal floating type results in undefined behavior. If
> the macro prefix is `d`M or `d`*M*`x`, use of an argument of standard or binary
> floating type results in undefined behavior. The function invoked is determined
> as follows:
>
> > —    Arguments that have integer type are regarded as having type `_Decimal64`
> > if any argument has decimal floating type, and as having type `double`
> > otherwise.
> >
> > —    The unsuffixed name of the function is the name of the macro, and its
> > suffix, if any, corresponds to the parameter type which may be any type with at
> > least the range and precision of the argument types.

In clause 15, at the end of the text appended to the table in 7.25#7, further
append:

> `f32xadd(d, f32x)`                any `f32xaddf`*N* or `f32xaddf`*N*`x` such
> that *N* \> 32 and the suffix type, `_Float`*`N`* or `_Float`*`N`*`x`, is at
> least as wide as `double` and `_Float32x`

---

Comment from WG14 on 2019-05-03:

Apr 2017 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

Apr 2018 meeting

### Committee Discussion

> After extensive discussion on the mailing list several documents were proposed
> with new and revised change suggestions. The following revised proposed change
> is largely drawn from
> [N2213](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2213.pdf) with further
> changes reviewed at the meeting.

### Proposed Change

In clause 15, after the change to 7.25#6, add:

> Change 7.25#6a from:
>
> > \[6a\] The functions that round result to a narrower type have type-generic
> > macros whose names are obtained by omitting any suffix from the function names.
> > Thus, the macros with `f` or `d` prefix are:
> >
> > > ```c
> > > fadd              fmul                 ffma
> > >
> > > dadd              dmul                 dfma
> > >
> > > fsub              fdiv                 fsqrt
> > >
> > > dsub              ddiv                 dsqrt
> > > ```
>
> and the macros with `d32` or `d64` prefix are:
>
> > ```c
> > d32add            d32mul               d32fma
> >
> > d64add            d64mul               d64fma
> >
> > d32sub            d32div               d32sqrt
> >
> > d64sub            d64div               d64sqrt
> > ```
> >
> > All arguments are generic. If any argument is not real, use of the macro results
> > in undefined behavior. If the macro prefix is `f` or `d`, use of an argument of
> > decimal floating type results in undefined behavior. If the macro prefix is
> > `d32` or `d64`, use of an argument of standard floating type results in
> > undefined behavior. The function invoked is determined as follows:
> >
> > > —    If any argument has type `_Decimal128`, or if the macro prefix is `d64`,
> > > the function invoked has the name of the macro, with a `d128` suffix.
> > >
> > > —    Otherwise, if the macro prefix is `d32`, the function invoked has the name
> > > of the macro, with a `d64` suffix.
> > >
> > > —    Otherwise, if any argument has type `long double`, or if the macro prefix
> > > is `d`, the function invoked has the name of the macro, with an `l` suffix.
> > >
> > > —    Otherwise, the function invoked has the name of the macro (with no suffix).
>
>  to:
>
> > \[6a\] The functions that round result to a narrower type have type-generic
> > macros whose names are obtained by omitting any suffix from the function names.
> > Thus, the macros with `f` or `d` prefix are:
> >
> > > ```c
> > > fadd              fmul                 ffma
> > >
> > > dadd              dmul                 dfma
> > >
> > > fsub              fdiv                 fsqrt
> > >
> > > dsub              ddiv                 dsqrt
> > > ```
>
> and the macros with `f`*M*, `f`*M*`x`, `d`*M*, or `d`*M*`x` prefix are:
>
> > `f`*M*`add             f`*`M`*`xmul              d`*`M`*`fma`
> >
> > `f`*M*`sub             f`*`M`*`xdiv              d`*`M`*`sqrt`
> >
> > `f`*M*`mul             f`*`M`*`xfma              d`*`M`*`xadd`
> >
> > `f`*M*`div             f`*`M`*`xsqrt             d`*`M`*`xsub`
> >
> > `f`*M*`fma             d`*`M`*`add               d`*`M`*`xmul`
> >
> > `f`*M*`sqrt            d`*`M`*`sub               d`*`M`*`xdiv`
> >
> > `f`*M*`xadd            d`*`M`*`mul               d`*`M`*`xfma`
> >
> > `f`*M*`xsub            d`*`M`*`div               d`*`M`*`xsqrt`
>
> All arguments are generic. If any argument is not real, use of the macro results
> in undefined behavior. If the macro prefix is `f` or `d`, use of an argument of
> interchange or extended floating type results in undefined behavior. If the
> macro prefix is `f`*M*, or `f`*M*`x`, use of an argument of standard or decimal
> floating type results in undefined behavior. If the macro prefix is `d`*M* or
> `d`*M*`x`, use of an argument of standard or binary floating type results in
> undefined behavior.  The function invoked is determined as follows:
>
> > —  Arguments that have integer type are regarded as having type `double` if the
> > macro prefix is `f` or `d`, as having type `_Float64` if the macro prefix is
> > `f`*M* or `f`*M*`x`, and as having type `_Decimal64` if the macro prefix is
> > `d`*M* or `d`*M*`x`.
>
> —  If the function has exactly one generic parameter, the type determined is the
> type of the argument.
>
> —  If the function has exactly two generic parameters, the type determined
> is the type determined by the usual arithmetic conversions (6.3.1.8) applied to
> the arguments.
>
> —  If the function has three generic parameters, the type determined is the type
> determined by applying the usual arithmetic conversions twice, first to the
> first two arguments, then to that result type and the third argument.
>
> —  If no function with the given prefix has the parameter type determined above,
> the parameter type is determined from the prefix as follows:

|  |  |
| --- | --- |
| ```c f ``` | ```c double ``` |
| ```c d ``` | ```c long double ``` |
| `f`*M* | `_Float`*`N`* for minimum *N* \> *M* if supported, else `_Float`*`M`*`x` |
| `f`*M*`x` | `_Float`*`N`*`x` for minimum *N* \> *M* if supported, else `_Float`*`N`* for minimum *N* \> *M* |
| `d`*M* | `_Decimal`*`N`* for minimum *N* \> *M* if supported, else `_Decimal`*`M`*`x` |
| `d`*M*`x` | `_Decimal`*`N`*`x` for minimum *N* \> *M* if supported, else `_Decimal`*`N`* for minimum *N* \> *M* |

> In clause 15, at the end of the text appended to the table in 7.25#7, further
> append:
>
> > ```c
> > fsub(d, ld)          fsubl
> >
> > f32add(f64x, f64)     f32addf64x
> >
> > d32xsqrt(n)          d32xsqrtd64
> > ```
> >
> > `f32mul(f128, f32x)    f32mulf128` if `_Float128` is at least as wide as
> > `_Float32x`, or `f32mulf32x` if `_Float32x` is wider than `_Float128`
> >
> > `f32fma(f32x, n, f32x)  f32fmaf64` if `_Float64` is at least as wide as
> > `_Float32x,` or `f32fmaf32x` if `_Float32x` is wider than `_Float64`
> >
> > `ddiv(ld, f128)`                 undefined
> >
> > `f32fma(f64, d, f64)`      undefined
> >
> > `fmul(dc, d)`                        undefined
>
> ```c
> f32add(f32, f32)             f32addf64(f32, f32)
> ```
>
> `f32xsqrt(f32)                   f32xsqrtf64x(f32)` if `_Float64x` is
>
> > supported, else `f32xsqrtf64`
>
> ```c
> f64div(f32x, f32x)        f64divf128(f32x, f32x)
> ```
