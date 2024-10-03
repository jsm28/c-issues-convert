### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14282:

> C11 specifies that the usual arithmetic conversions on the pair of types (`long
> double`, `double`) produces a result of type `long double`.
> 
> Suppose `long double` and `double` have the same set of values.  TS 18661-3
> rewrites the rules for usual arithmetic conversions so that the case "if both
> operands are floating types and the sets of values of their corresponding real
> types are equivalent" prefers interchange types to standard types to extended
> types.  But this leaves the case of (`long double`, `double`) unspecified as to
> which type is chosen, unlike in C11, as those are both standard types.
> 
> I think this is a defect in TS 18661-3, and it should say that if both are
> standard types with the same set of values then `long double` is preferred to
> `double` which is preferred to `float`, as in C11.
> 
> A similar issue could arise if two of the extended types have equivalent sets of
> values.  I'm not aware of anything to prohibit that, although it seems less
> likely in practice.  I think the natural fix would be to say that `_Float128x`
> is preferred to `_Float64x` which is preferred to `_Float32x`.
> 
> I think such an issue would also arise for `<tgmath.h>` (if `_Float64x` and
> `_Float128x` have the same set of values, the choice doesn't seem to be
> specified).  It also seems possible for the `<tgmath.h>` rules for purely
> floating-point arguments to produce a different result from the usual arithmetic
> conversions (consider the case where `_Float32x` is wider than `long double`,
> and `<tgmath.h>` chooses `long double`), and since rules that are the same in
> most cases but subtly different in obscure cases tend to be confusing, I wonder
> if it might be better to specify much simpler rules for `<tgmath.h>`: take the
> type resulting from the usual arithmetic conversions\[\*], where integer
> arguments are replaced by `_Decimal64` if there are any decimal arguments and
> `double` otherwise.  (That's different from the present rules for e.g.
> (`_Float32x`, `int`), but it's a lot simpler, and seems unlikely in practice to
> choose a type with a different set of values from the present choice.)
> 
> \[\*] Meaningful for more than two arguments as long as the usual arithmetic
> conversions are commutative and associative as an operation on pairs of types.

Though substantive, the suggested change to the usual arithmetic conversions is
consistent with the intention in TS 18661-3 to specify all the cases (except
where neither format is a subset of the other and the formats are not the same).
The missing cases were an oversight. The suggested preferences of `long double`
over `double` over `float` and `_Float128x` over `_Float64x` over `_Float32x`
are the obvious choices.

Joseph Myers notes that the `<tgmath.h>` specification is incomplete in the same
way as the usual arithmetic conversions. He argues for simplifying the
specification by referring to the usual arithmetic conversions specification,
rather than mostly repeating it, as the current specification does. The
suggested Technical Corrigendum below follows this new approach. Though a
substantive change to TS 18661-3, the effects on implementations and users are
expected to be minimal – worth the simplification.

The suggested Technical Corrigendum below also restores footnote number 62,
which is lost in the current TS 18661-3.

### Suggested Technical Corrigendum

In clause 8, change the replacement text for 6.3.1.8#1:

> If one operand has decimal floating type, the other operand shall not have
> standard floating type, binary floating type, complex type, or imaginary type.
> 
> If both operands have floating types and neither of the sets of values of their
> corresponding real types is a subset of (or equivalent to) the other, the
> behavior is undefined.
> 
> Otherwise, if both operands are floating types and the sets of values of their
> corresponding real types are equivalent, then the following rules are applied:
> 
> > If both operands have the same corresponding real type, no further conversion is
> > needed.
> > 
> > Otherwise, if the corresponding real type of either operand is an interchange
> > floating type, the other operand is converted, without change of type domain, to
> > a type whose corresponding real type is that same interchange floating type.
> > 
> > Otherwise, if the corresponding real type of either operand is a standard
> > floating type, the other operand is converted, without change of type domain, to
> > a type whose corresponding real type is that same standard floating type.
> 
> Otherwise, if both operands have floating types, the operand, whose set of
> values of its corresponding real type is a (proper) subset of the set of values
> of the corresponding real type of the other operand, is converted, without
> change of type domain, to a type with the corresponding real type of that other
> operand.
> 
> Otherwise, if one operand has a floating type, the other operand is converted to
> the corresponding real type of the operand of floating type.
> 
> Otherwise, the integer promotions are performed on both operands. Then the
> following rules are applied to the promoted operands:
> 
> > . . .

to:

> If one operand has decimal floating type, the other operand shall not have
> standard floating type, binary floating type, complex type, or imaginary type.
> 
> If both operands have floating types and neither of the sets of values of their
> corresponding real types is a subset of (or equivalent to) the other, the
> behavior is undefined.
> 
> If both operands have the same corresponding real type, no further conversion is
> needed.
> 
> Otherwise, if both operands are floating types and the sets of values of their
> corresponding real types are equivalent, then the following rules are applied:
> 
> > If the corresponding real type of either operand is an interchange floating
> > type, the other operand is converted, without change of type domain, to a type
> > whose corresponding real type is that same interchange floating type.
> > 
> > Otherwise, if the corresponding real type of either operand is `long double`,
> > the other operand is converted, without change of type domain, to a type whose
> > corresponding real type is `long double`.
> > 
> > Otherwise, if the corresponding real type of either operand is `double`, the
> > other operand is converted, without change of type domain, to a type whose
> > corresponding real type is `double`.
> > 
> > (All cases where `float` might have the same format as another type are covered
> > above.)
> > 
> > Otherwise, if the corresponding real type of either operand is `_Float128x` or
> > `_Decimal128x`, the other operand is converted, without change of type domain,
> > to a type whose corresponding real type is `_Float128x` or `_Decimal128x`,
> > respectively.
> > 
> > Otherwise, if the corresponding real type of either operand
> > is `_Float64x` or `_Decimal64x`, the other operand is converted, without change
> > of type domain, to a type whose corresponding real type
> > is `_Float64x` or `_Decimal64x`, respectively.
> 
> Otherwise, if both operands have floating types, the operand, whose set of
> values of its corresponding real type is a (proper) subset of the set of values
> of the corresponding real type of the other operand, is converted, without
> change of type domain62), to a type with the corresponding real type of that
> other operand.
> 
> Otherwise, if one operand has a floating type, the other operand is converted to
> the corresponding real type of the operand of floating type.
> 
> Otherwise, the integer promotions are performed on both operands. Then the
> following rules are applied to the promoted operands:
> 
> . . .

In clause 15, replace:

> In 7.25#3c, replace the bullets:
> 
> > … bullets …
> 
> with:
> 
> > > —  If two arguments have floating types and neither of the sets of values of
> > > their corresponding real types is a subset of (or equivalent to) the other, the
> > > behavior is undefined.
> > > 
> > > —  If any arguments for generic parameters have type `_Decimal`*`M`* where *M* ≥
> > > 64 or `_Decimal`*`N`*`x` where *N* ≥ 32, the type determined is the widest of
> > > the types of these arguments. If `_Decimal`*`M`* and `_Decimal`*`N`*`x` are both
> > > widest types (with equivalent sets of values) of these arguments, the type
> > > determined is `_Decimal`*`M`*.
> > > 
> > > —  Otherwise, if any argument for generic parameters is of integer type and
> > > another argument for generic parameters has type `_Decimal32`, the type
> > > determined is `_Decimal64`.
> > > 
> > > —  Otherwise, if any argument for generic parameters has type `_Decimal32`, the
> > > type determined is `_Decimal32`.
> > > 
> > > —  Otherwise, if the corresponding real type of any argument for generic
> > > parameters has type `long double`, `_Float`*`M`* where *M* ≥ 128, or
> > > `_Float`*`N`*`x` where *N* ≥ 64, the type determined is the widest of the
> > > corresponding real types of these arguments. If `_Float`*`M`* and either
> > > `long double` or `_Float`*`N`*`x` are both widest corresponding real types (with
> > > equivalent sets of values) of these arguments, the type determined is
> > > `_Float`*`M`*. Otherwise, if `long double` and `_Float`*`N`*`x` are both widest
> > > corresponding real types (with equivalent sets of values) of these arguments,
> > > the type determined is `long double`.
> > > 
> > > —  Otherwise, if the corresponding real type of any argument for generic
> > > parameters has type `double`, `_Float64`, or `_Float32x`, the type determined is
> > > the widest of the corresponding real types of these arguments. If `_Float64` and
> > > either `double` or `_Float32x` are both widest corresponding real types (with
> > > equivalent sets of values) of these arguments, the type determined is
> > > `_Float64`. Otherwise, if `double` and `_Float32x` are both widest corresponding
> > > real types (with equivalent sets of values) of these arguments, the type
> > > determined is `double`.
> > > 
> > > —  Otherwise, if any argument for generic parameters is of integer type, the
> > > type determined is `double`.
> > > 
> > > —  Otherwise, if the corresponding real type of any argument for generic
> > > parameters has type `_Float32`, the type determined is `_Float32`.
> > > 
> > > —  Otherwise, the type determined is `float`.
> > 
> > In the second bullet 7.25#3c, attach a footnote to the wording:
> > 
> > the type determined is the widest
> > 
> > where the footnote is:
> > 
> > \*) The term widest here refers to a type whose set of values is a superset of
> > (or equivalent to) the sets of values of the other types.

with:

> In 7.25#3c, replace the first sentence and bullets:
> 
> > \[3c] Except for the macros for functions that round result to a narrower type
> > (7.12.13a), use of a type-generic macro invokes a function whose generic
> > parameters have the corresponding real type determined by the corresponding real
> > types of the arguments as follows:
> > 
> > > —    First, if any argument for generic parameters has type `_Decimal128`, the
> > > type determined is `_Decimal128`.
> > > 
> > > —    Otherwise, if any argument for generic parameters has type `_Decimal64`, or
> > > if any argument for generic parameters is of integer type and another argument
> > > for generic parameters has type `_Decimal32`, the type determined is
> > > `_Decimal64`.
> > > 
> > > —    Otherwise, if any argument for generic parameters has type `_Decimal32`,
> > > the type determined is `_Decimal32`.
> > > 
> > > —    Otherwise, if the corresponding real type of any argument for generic
> > > parameters is `long double`, the type determined is `long double`.
> > > 
> > > —    Otherwise, if the corresponding real type of any argument for generic
> > > parameters is `double` or is of integer type, the type determined is `double`.
> > > 
> > > —    Otherwise, if any argument for generic parameters is of integer type, the
> > > type determined is `double`.
> > > 
> > > —    Otherwise, the type determined is `float`.
> 
> with:
> 
> > \[3c] Except for the macros for functions that round result to a narrower type
> > (7.12.13a), use of a type-generic macro invokes a function whose generic
> > parameters have the corresponding real type determined by the types of the
> > arguments for the generic parameters as follows:
> > 
> > > —  Arguments of integer type are regarded as having type `_Decimal64` if any
> > > argument has decimal floating type, and as having type `double` otherwise.
> > > 
> > > —  If the function has exactly one generic parameter, the type determined is
> > > the corresponding real type of the argument for the generic parameter.
> > > 
> > > —  If the function has exactly two generic parameters, the type determined is
> > > the corresponding real type determined by the usual arithmetic conversions
> > > (6.3.1.8) applied to the arguments for the generic parameters.
> > > 
> > > —  If the function has more than two generic parameters, the type determined is
> > > the corresponding real type determined by repeatedly applying the usual
> > > arithmetic conversions, first to the first two arguments for generic parameters,
> > > then to that result type and the next argument for a generic parameter, and so
> > > forth until the usual arithmetic conversions have been applied to the last
> > > argument for a generic parameter.
