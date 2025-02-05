# Floating-point TS 18661 (C11 version): issue log

**This issue log has been automatically converted from the original issue lists and some formatting may not have been preserved.**

|Issue|Summary|Status|
|-|-|-|
|0CFP.01|[Part 1: Typos](log_cfp-c11.md#issue0CFP.01)|Fixed in C23|
|0CFP.02|[Part 1: Functions that round result to narrower type don't always](log_cfp-c11.md#issue0CFP.02)|Fixed in C23|
|0CFP.03|[Part 1: feature macros and header file inclusions](log_cfp-c11.md#issue0CFP.03)|Fixed in C23|
|0CFP.04|[Part 3: Error in function name](log_cfp-c11.md#issue0CFP.04)|Fixed in C23|
|0CFP.05|[Part 1: Is return of same type convertFormat or copy?](log_cfp-c11.md#issue0CFP.05)|Fixed in C23|
|0CFP.06|[Part 1: **fetestexceptflag** and exceptions passed to **fegetexceptflag**](log_cfp-c11.md#issue0CFP.06)|Fixed in C23|
|0CFP.07|[Part 1: Editorial changes](log_cfp-c11.md#issue0CFP.07)|Fixed in C23|
|0CFP.08|[Part 2: Editorial clarification about number digits in the coefficient](log_cfp-c11.md#issue0CFP.08)|Fixed in C23|
|0CFP.09|[Part 2,3: Missing specification for usual arithmetic conversions, tgmath](log_cfp-c11.md#issue0CFP.09)|Fixed in C23|
|0CFP.10|[Part 1: wrong type for **fesetmode** parameter](log_cfp-c11.md#issue0CFP.10)|Fixed in C23|
|0CFP.11|[Part 2: a-style formatting not IEC 60559 conformant](log_cfp-c11.md#issue0CFP.11)|Fixed in C23|
|0CFP.12|[P1: Zero payloads and `set payload` function](log_cfp-c11.md#issue0CFP.12)|Fixed in C23|
|0CFP.13|[P3: Type-generic macros for functions that round result to narrower type](log_cfp-c11.md#issue0CFP.13)|Fixed in C23|
|0CFP.14|[P2: Effect of `%a` vs `%A` conversion specifiers](log_cfp-c11.md#issue0CFP.14)|Fixed in C23|
|0CFP.15|[P3: Characteristic macros for non-arithmetic formats](log_cfp-c11.md#issue0CFP.15)|Fixed in C23|
|0CFP.16|[P1: tgmath cbrt macro](log_cfp-c11.md#issue0CFP.16)|Fixed in C23|
|0CFP.17|[P3: incommensurate arguments for comparison macros](log_cfp-c11.md#issue0CFP.17)|Fixed in C23|
|0CFP.18|[P4: missing specification of preferred quantum exponents](log_cfp-c11.md#issue0CFP.18)|Fixed in C23, Floating-point TS 18661-4:2025|
|0CFP.19|[P1: updating underflow definition](log_cfp-c11.md#issue0CFP.19)|Fixed in C23|
|0CFP.20|[P1: changes for obsolescing DECIMAL\_DIG](log_cfp-c11.md#issue0CFP.20)|Fixed in C23|
|0CFP.21|[P1: printf of one-digit character string](log_cfp-c11.md#issue0CFP.21)|Fixed in C23|
|0CFP.22|[P3: changes for obsolescing DECIMAL\_DIG](log_cfp-c11.md#issue0CFP.22)|Fixed in C23|
|0CFP.23|[P2: llquantexp invalid case](log_cfp-c11.md#issue0CFP.23)|Fixed in C23|
|0CFP.24|[P1 remainder NaN case](log_cfp-c11.md#issue0CFP.24)|Fixed in C23|
|0CFP.25|[P1 totalorder parameters](log_cfp-c11.md#issue0CFP.25)|Fixed in C23|

---

<div id="issue0CFP.01">

## Issue 0CFP.01: Part 1: Typos

Authors: WG14, Jim Thomas et al.  
Date: 2016-03-19  
Reference document: [N2029](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2029.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

1. Page 18: In C 7.6.1a#4, the last sentence, “functon” should be “function”.
2. Page 48: In C 7.6.2.4a#3, “The **fetestexcept** function returns ...” should be “The **fetestexceptflag** function returns ...”.

### Suggested Technical Corrigendum

1. Page 18: In C 7.6.1a, paragraph 4, the last sentence, change “functon” to “function”
2. Page 48: In C 7.6.2.4a#3, change “**fetestexcept**” to “**fetestexceptflag**”.

---

Comment from WG14 on 2018-10-18:

Apr 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

1. Page 18: In C 7.6.1a, paragraph 4, the last sentence, change “functon” to “function”
2. Page 48: In C 7.6.2.4a#3, change “**fetestexcept**” to “**fetestexceptflag**”.


</div>


---

---

<div id="issue0CFP.02">

## Issue 0CFP.02: Part 1: Functions that round result to narrower type don't always

Authors: WG14, Jim Thomas et al.  
Date: 2016-03-19  
Reference document: [N2029](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2029.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

### Summary

Page 38: The C 7.12.13a subclause heading is “Functions that round result to
narrower type” and this is the way the functions in the subclause are referred
to throughout the TS. In some cases, the functions in the subclause round their
result to a type that isn’t really narrower than the parameter types. For
example, this is true for the functions **daddl**, **dsubl**, etc. if the **long
double** and **double** types have the same width (as is allowed). (With the
extended types introduced in TS 18661-3, the destination type might be wider, as
it might for **f32xaddf64**.)

The current way of referencing these functions reflects the usual situation, and
is perhaps a helpful way of think about them generally. With a note about the
uncharacteristic cases, it seems unlike to cause significant confusion. Also,
changing all the references to these functions would be a large editorial
undertaking, spanning multiple parts of the TS. Confusion could easily arise
from having an inconsistent set of documents.

### Suggested Technical Corrigendum

Page 38: After the C 7.12.13a subclause heading, insert the following paragraph:

> \[1] The functions in this subclause round their results to a type typically
> narrower than the parameter types.

Page 40: After the change to C ending with “7.12.13a.6 Square root rounded to
narrower type ... \[3] These functions return the square root of x, rounded to
the type of the function.”, insert the following:

> In 7.12.13a #1, attach a footnote to the wording:
>
> > typically narrower
>
> where the footnote is:
>
> > \*) In some cases the destination type might not be narrower than the parameter
> > types. For example, **double** might not be narrower than **long double**.

---

Comment from WG14 on 2018-10-18:

Apr 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

Page 38: After the C 7.12.13a subclause heading, insert the following paragraph:

> \[1] The functions in this subclause round their results to a type typically
> narrower than the parameter types.

Page 40: After the change to C ending with “7.12.13a.6 Square root rounded to
narrower type ... \[3] These functions return the square root of x, rounded to
the type of the function.”, insert the following:

> In 7.12.13a #1, attach a footnote to the wording:
>
> > typically narrower
>
> where the footnote is:
>
> > \*) In some cases the destination type might not be narrower than the parameter
> > types. For example, **double** might not be narrower than **long double**.


</div>


---

---

<div id="issue0CFP.03">

## Issue 0CFP.03: Part 1: feature macros and header file inclusions

Authors: WG14, Jim Thomas et al.  
Date: 2016-03-19  
Reference document: [N2029](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2029.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

ISO/IEC TS 18661-1 subclause 5.3 specifies interfaces that are defined or
declared “only if **\_\_STDC\_WANT\_IEC\_60559\_BFP\_EXT\_\_** is defined as a
macro at the point in the source file where the header for the interface is
first included.” C 7.12#1 says **\<tgmath.h\>** includes **\<math.h\>** and
**\<complex.h\>**.

So for

> ```c
> #include <math.h>
> #define __STDC_WANT_IEC_60559_BFP_EXT__
> #include <tgmath.h>
> float f(float x) { return nextup(x); }
> ```

the **nextup** functions in **\<math.h\>** are not declared and the **nextup**
macro in **\<tgmath.h\>** is defined. Since x has type float, the function
determined by the **nextup** macro in **\<tgmath.h\>** is **nextupf**. But is
this function available to be called? Another example. For

> ```c
> #include <limits.h>
> #define __STDC_WANT_IEC_60559_BFP_EXT__
> #include <math.h>
> ...
> ```

the **fromfp** functions in **\<math.h\>** are declared, but the **WIDTH**
macros in **\<limits.h\>**, which are needed for portable use of the **fromfp**
functions, are not defined. In these examples, interfaces provided by one header
are related to interfaces that are not provided by another header, because of
the placement of the **WANT** macros. This leads to ambiguous cases (as in the
first example above) and incomplete feature sets. Later parts of the TS have
their own WANT macros, which compounds the problem. See also Joseph Myers’s
\<[http://www.open-std.org/jtc1/sc22/wg14/13831](https://www.open-std.org/jtc1/sc22/wg14/13831)\>.

The suggested corrigendum below specifies that the same set of **WANT** macros
must be defined at the points in the code where the relevant headers are first
included. This results in fewer combinations of interfaces and provides one sets
of interfaces that is consistent and complete with respect to a given set of
WANT macros.

### Suggested Technical Corrigendum

Page 5: At the end of 5.3, insert:

> After 7.1.2#4, insert:
>
> > \[4a] Some standard headers define or declare identifiers contingent on whether
> > certain macros whose names begin with **\_STDC\_WANT\_IEC\_60559\_** and end
> > with **\_EXT\_** are defined (by the user) at the point in the code where the
> > header is first included. Within a preprocessing translation unit, the same set
> > of such macros shall be defined for the first inclusion of all such headers.

---

Comment from WG14 on 2018-10-18:

Apr 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

Page 5: At the end of 5.3, insert:

> After 7.1.2#4, insert:
>
> > \[4a] Some standard headers define or declare identifiers contingent on whether
> > certain macros whose names begin with **\_STDC\_WANT\_IEC\_60559\_** and end
> > with **\_EXT\_** are defined (by the user) at the point in the code where the
> > header is first included. Within a preprocessing translation unit, the same set
> > of such macros shall be defined for the first inclusion of all such headers.


</div>


---

---

<div id="issue0CFP.04">

## Issue 0CFP.04: Part 3: Error in function name

Authors: WG14, Jim Thomas et al.  
Date: 2016-03-19  
Reference document: [N2029](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2029.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

Page 32: In 12.3, the function name is written as “**scoshdNx**”, instead of
“**coshdNx**” as intended. Although correcting the mistake could be seen as a
substantive change, it is clear from the context that this function is in the
family of **cosh** functions. It is extremely unlikely that any implementer
would not have recognized the mistake and provided the function with the
erroneous name.

### Suggested Technical Corrigendum

Page 32: In 12.3, change “**scoshdNx**” to “**coshdNx**”.

---

Comment from WG14 on 2018-10-18:

Apr 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

Page 32: In 12.3, change “**scoshdNx**” to “**coshdNx**”.


</div>


---

---

<div id="issue0CFP.05">

## Issue 0CFP.05: Part 1: Is return of same type convertFormat or copy?

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14280:

> TS 18661-1 says "Whether C assignment (6.5.16) (and conversion as if by
> assignment) to the same format is an IEC 60559 convertFormat or copy operation
> is implementation-defined, even if `<fenv.h>` defines the macro
>
> `FE_SNANS_ALWAYS_SIGNAL` (F.2.1).".
>
> Does this apply to function return, where the return type of the function is the
> same as the type of the expression passed to the return statement and no wider
> evaluation format is in use \- that is, may this act as either convertFormat or
> copy?  C11 F.6 clearly envisages that such a return statement may do a
> conversion to the same type in the case of wider evaluation formats.  But
> 6.8.6.4#3 only refers to conversions "If the expression has a type different
> from the return type of the function in which it appears".

The specification, from F.3#3, quoted above is incomplete in that it doesn’t
cover function returns, which are not assignments or conversions as if by
assignment. As currently written, C11 \+ TS18661-1 might be read to exclude the
possibility of using convertFormat in this case. A statement should be added to
say that the implementation has the option to apply convertFormat to the return
value. The change does not break existing implementations.

The effect of convertFormat would be that signaling NaNs would signal and
noncanonical representations would be canonicalized. It is extremely unlikely
that a program would depend on convertFormat not being used.

### Suggested Technical Corrigendum

In Clause 8, to the text for C F.3#3:

> \[3] Whether C assignment (6.5.16) (and conversion as if by assignment) to the
> same format is an IEC 60559 convertFormat or copy operation is
> implementation-defined, even if `<fenv.h>` defines the macro
> `FE_SNANS_ALWAYS_SIGNAL` (F.2.1).

append the sentence:

> If the return expression of a `return` statement is evaluated to the
> floating-point format of the return type, it is implementation-defined whether a
> convertFormat operation is applied to the result of the return expression.”

At the end of Clause 8, add:

> In F.3#3, attach a footnote to the wording:
>
> > Whether C assignment (6.5.16) (and conversion as if by assignment) to the same
> > format is an IEC 60559 convertFormat or copy operation
>
> where the footnote is:
>
> \*) Where the source and destination formats are the same, convertFormat
> operations differ from copy operations in that convertFormat operations raise
> the “invalid” floating-point exception on signaling NaN inputs and do not
> propagate non-canonical encodings.

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In Clause 8, to the text for C F.3#3:

> \[3] Whether C assignment (6.5.16) (and conversion as if by assignment) to the
> same format is an IEC 60559 convertFormat or copy operation is
> implementation-defined, even if `<fenv.h>` defines the macro
> `FE_SNANS_ALWAYS_SIGNAL` (F.2.1).

append the sentence:

> If the return expression of a `return` statement is evaluated to the
> floating-point format of the return type, it is implementation-defined whether a
> convertFormat operation is applied to the result of the return expression.”

At the end of Clause 8, add:

> In F.3#3, attach a footnote to the wording:
>
> > Whether C assignment (6.5.16) (and conversion as if by assignment) to the same
> > format is an IEC 60559 convertFormat or copy operation
>
> where the footnote is:
>
> \*) Where the source and destination formats are the same, convertFormat
> operations differ from copy operations in that convertFormat operations raise
> the “invalid” floating-point exception on signaling NaN inputs and do not
> propagate non-canonical encodings.


</div>


---

---

<div id="issue0CFP.06">

## Issue 0CFP.06: Part 1: **fetestexceptflag** and exceptions passed to **fegetexceptflag**

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14328:

> TS 18661-1 says, for `fetestexceptflag`, "The value of `*flagp` shall have been
> set by a previous call to `fegetexceptflag`.".
>
> This contrasts with the C11 wording for `fesetexceptflag`, "The value of
> `*flagp` shall have been set by a previous call to `fegetexceptflag` whose
> second argument represented at least those floating-point exceptions represented
> by the argument `excepts`.".  So what happens if more exceptions are specified
> in the call to `fetestexceptflag` than were specified in the call to
> `fegetexceptflag`?  Then `fegetexceptflag` may or may not have stored any
> meaningful representation of the state of the extra exceptions being tested.
>
> I think `fetestexceptflag` should have the same wording for this issue as
> `fesetexceptflag`: "whose second argument represented at least those
> floating-point exceptions represented by the argument `excepts`".

`fesetexceptflag` sets global state, typically a hardware register, whereas
`fetestexceptflag` just reads a variable. It seems more important to avoid
spurious data in the former.

Still, there’s no utility in testing spurious flag settings, and placing the
same restrictions on `fetestexceptflag` as on `fesetexceptflag` might be less
error prone.

### Suggested Technical Corrigendum

In 15.2, in the new text for C 7.6.2.4a#2, change:

> The value of `*flagp` shall have been set by a previous call to
> `fegetexceptflag`.

to:

> The value of `*flagp` shall have been set by a previous call to
> `fegetexceptflag` whose second argument represented at least those
> floating-point exceptions represented by the argument `excepts`.

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In 15.2, in the new text for C 7.6.2.4a#2, change:

> The value of `*flagp` shall have been set by a previous call to
> `fegetexceptflag`.

to:

> The value of `*flagp` shall have been set by a previous call to
> `fegetexceptflag` whose second argument represented at least those
> floating-point exceptions represented by the argument `excepts`.


</div>


---

---

<div id="issue0CFP.07">

## Issue 0CFP.07: Part 1: Editorial changes

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

### Summary

In CFP email, Fred Tydeman noted:

> Searching for "infinite precision" in part 1, most of them have "(as if) to"
> before it. Except, `ffma`, `ffmal`, `dfmal` which is missing the "(as if)".

Right. In particular, all the functions that round result to narrower type have
“(as if)”, except for the `fma` family.

### Suggested Technical Corrigendum

In 14.5, in the new text for C 7.12.13a.5#2, insert “(as if)” before “to
infinite precision”.

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In 14.5, in the new text for C 7.12.13a.5#2, insert “(as if)” before “to
infinite precision”.


</div>


---

---

<div id="issue0CFP.08">

## Issue 0CFP.08: Part 2: Editorial clarification about number digits in the coefficient

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

### Summary

In 12.5, n is defined to be “the number of digits in the coefficient *c*”, where
the decimal floating-point argument is represented by the triple (*s*, *c*,
*q*). The intention is that *n* is the number of digits in the coefficient of
the particular argument, i.e., the number of significant digits, not the maximum
number of digits in the coefficient for the type. This might be misread,
particularly since 5.2.4.2.2a says

> number of digits in the coefficient
>
> ```c
> DEC32_MANT_DIG                 7
> ```

```c
DEC64_MANT_DIG                 16
```

> ```c
> DEC128_MANT_DIG                34
> ```

This part of 5.2.4.2.2a is in the context of characterizing the type, so clearly
refers to the type and not any particular representation.

### Suggested Technical Corrigendum

In 12.5, change:

> where *n* is the number of digits in the coefficient *c*

to:

> where *n* is the number of significant digits in the coefficient *c*

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In 12.5, change:

> where *n* is the number of digits in the coefficient *c*

to:

> where *n* is the number of significant digits in the coefficient *c*


</div>


---

---

<div id="issue0CFP.09">

## Issue 0CFP.09: Part 2,3: Missing specification for usual arithmetic conversions, tgmath

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

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

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

Apr 2017 meeting

### Committee Discussion

A new paper [N2127](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2127.pdf)
was presented which offers a simplified Technical Corrigendum. From that paper:

> The TC in DR 501 includes two changes to TS 18661-3, one for the usual
> arithmetic conversions, the other for type-generic math. The first change fills
> in missing conversions for new types in TS 18661-3. The second change simplifies
> type-generic math by referencing the usual arithmetic conversions, and thereby
> also fills in missing type-generic math rules for arguments of the new types.
>
> This is a proposal for an alternative change to type-generic math. The original
> change was proposed for TS 18661-3, where the new types where introduced.
> However, the change can be made in TS 18661-2, where it is easier to understand
> and leads to a simplification in TS 18661-3.

The committee accepts the proposed modification as reflected below.

### Proposed Technical Corrigendum

In TS 18662-3

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

In TS 18661-2

In 12.9, change the introduced \[3c] from:

> \[3c] Except for the macros for functions that round result to a narrower type
> (7.12.13a), use of a type-generic macro invokes a function whose generic
> parameters have the corresponding real type determined by the corresponding real
> types of the arguments as follows:
>
> > —    First, if any argument for generic parameters has type `_Decimal128`, the
> > type determined is `_Decimal128`.
> >
> > —    Otherwise, if any argument for generic parameters has type `_Decimal64`, or
> > if any argument for generic parameters is of integer type and another argument
> > for generic parameters has type `_Decimal32`, the type determined is
> > `_Decimal64`.
> >
> > —    Otherwise, if any argument for generic parameters has type `_Decimal32`,
> > the type determined is `_Decimal32`.
> >
> > —    Otherwise, if the corresponding real type of any argument for generic
> > parameters is `long double`, the type determined is `long double`.
> >
> > —    Otherwise, if the corresponding real type of any argument for generic
> > parameters is `double` or is of integer type, the type determined is `double`.
> >
> > —    Otherwise, if any argument for generic parameters is of integer type, the
> > type determined is `double`.
> >
> > —    Otherwise, the type determined is `float`.

to:

> \[3c] Except for the macros for functions that round result to a narrower type
> (7.12.13a), use of a type-generic macro invokes a function whose generic
> parameters have the corresponding real type determined by the types of the
> arguments for the generic parameters as follows:
>
> > —    Arguments of integer type are regarded as having type `_Decimal64` if any
> > argument has decimal floating type, and as having type `double` otherwise.
> >
> > —     If the function has exactly one generic parameter, the type determined
> > is the corresponding real type of the argument for the generic parameter.
> >
> > —    If the function has exactly two generic parameters, the type determined
> > is the corresponding real type determined by the usual arithmetic conversions
> > (6.3.1.8) applied to the arguments for the generic parameters.
> >
> > —    If the function has more than two generic parameters, the type determined
> > is the corresponding real type determined by repeatedly applying the usual
> > arithmetic conversions, first to the first two arguments for generic parameters,
> > then to that result type and the next argument for a generic parameter, and so
> > forth until the usual arithmetic conversions have been applied to the last
> > argument for a generic parameter.


</div>


---

---

<div id="issue0CFP.10">

## Issue 0CFP.10: Part 1: wrong type for **fesetmode** parameter

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14358:

> TS 18661-1 gives the declaration of `fesetmode` as:
>
> ```c
> int fesetmode(const fenv_t *modep);
> ```
>
> The argument should be of type `const femode_t *`, not `const fenv_t *`.
>
> \--

This was an editorial cut-and-past error. The Description says the argument
`modep` shall point to an objet set by a call to `fegetmode`, which sets objects
of type `femode_t`. It’s unlikely the function would be implemented with the
erroneous type.

### Suggested Technical Corrigendum

In 15.3, in the new text for C 7.6.3.1a#1, change:

```c
          int fesetmode(const fenv_t *modep);
```

to:

```c
          int fesetmode(const femode_t *modep);
```

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In 15.3, in the new text for C 7.6.3.1a#1, change:

```c
          int fesetmode(const fenv_t *modep);
```

to:

```c
          int fesetmode(const femode_t *modep);
```


</div>


---

---

<div id="issue0CFP.11">

## Issue 0CFP.11: Part 2: a-style formatting not IEC 60559 conformant

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The `a`-style formatting specified in subclause 12.5 of TS 18661-2 is not an IEC
60559 conversion for cases where the formatting precision is less than the
length of the coefficient of the input. The specification entails an
intermediate rounding to the floating type of the input, which might overflow
resulting in a character sequence representation of infinity. IEC 60559
conversions to character sequences do not overflow, unless the language
over-restricts the exponent range for character sequence output, which C does
not.

Another undesirable aspect of the current specification is that in certain cases
it produces results with more precision than given by a width modifier.

Here are some examples, showing the result of the intermediate conversion, with
different behaviors for the current spec (“old”) and the spec in the suggested
Technical Corrigendum below (“new”):

For `_Decimal32` input *x* with representation (1, 9512345, 90\) and specifier
...

```c
%.3Ha
```

old:                           *x*                -\>             (1, 9510000,
90\)                -\>             `9.510000e96`

new:                         *x*                -\>             (1, 951,
94\)                            -\>             `9.51e96`

```c
%.2Ha
```

old:                           *x*                -\>             (1, 9500000,
90\)                -\>             `9.500000e96`

new:                         *x*                -\>             (1, 95,
95\)                               -\>             `9.5e96`

```c
%.1Ha
```

old:                           *x*                -\>            
Inf                                                -\>             `inf`

new:                         *x*                -\>             (1, 1,
97\)                                  -\>             `1e97`

Here’s another example:

For `_Decimal32` input x with representation (1, 9512345, 86\) and specifier ...

```c
%.2Ha
```

old:                           *x*                -\>             (1, 950,
90\)                            -\>             `9.50e92`

new:                         *x*                -\>             (1, 95,
91\)                               -\>             `9.5e92`

The examples use a to-nearest rounding.

As the examples illustrate, the problematic cases for the current “old” spec
occur because of the exponent range limitation of the format used for the
intermediate conversion.

The suggested Technical Corrigendum below specifies formatting that is IEC 60559
conformant and which honors a width modifier. It does not change the numerical
value of the result, except in overflow cases.

### Suggested Technical Corrigendum

In 12.5, in the addition to 7.21.6.1#8 and 7.29.2.1#8, under `a`,`A` conversion
specifiers, change:

> If the precision is present (in the conversion specification) and is zero or at
> least as large as the precision *p* (5.2.4.2.2) of the decimal floating type,
> the conversion is as if the precision were missing. If the precision is present
> (and nonzero) and less than the precision *p* of the decimal floating type, the
> conversion first obtains an intermediate result by rounding the input in the
> type, according to the current rounding direction for decimal floating-point
> operations, to the number of digits specified by the precision, then converts
> the intermediate result as if the precision were missing. The length of the
> coefficient of the intermediate result is the smallest number, at least as large
> as the formatting precision, for which the quantum exponent is within the
> quantum exponent range of the type (see 5.2.4.2.2a). The intermediate rounding
> may overflow.

to:

> If the precision *P* is present (in the conversion specification) and is zero or
> at least as large as the precision *p* (5.2.4.2.2) of the decimal floating type,
> the conversion is as if the precision were missing. If the precision *P* is
> present (and nonzero) and less than the precision *p* of the decimal floating
> type, the conversion first obtains an intermediate result as follows, where *n*
> is the number of significant digits in the coefficient:
>
> > If *n* \<\= *P*, set the intermediate result to the input.
> >
> > If *n* \> *P*, round the input value, according to the current rounding
> > direction for decimal floating-point operations, to *P* decimal digits, with
> > unbounded exponent range, representing the result with a *P*-digit integer
> > coefficient when in the form (*s*, *c*, *q*).
>
> Convert the intermediate result in the manner described above for the case where
> the precision is missing.

In 12.5, in the addition to 7.21.6.1#8 and 7.29.2.1#8, in EXAMPLE 3, change the
results:

> ```c
> 9.54321e+93
>
> 9.5432e+93
>
> 9.543e+93
>
> 9.540e+93
>
> 9.500e+93
>
> 1.0000e+94
>
> inf
> ```

to:

> ```c
> 9.54321e+93
>
> 9.5432e+93
>
> 9.543e+93
>
> 9.54e+93
>
> 9.5e+93
>
> 1e+94
>
> 1e+97
> ```

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

Apr 2017 meeting

### Committee Discussion

The paper [N2126](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2126.htm)
provides an example that illustrates this change, and the committee agreed to
accept this as an addendum to the Proposed Technical Corrigendum.

However, the committee is concerned that `%a` behavior differs from binary
floating point and more review is needed. In particular, there were concerns
that for the decimal floating point types now the %a format specifier given with
a precision is the total number of significant digits, not the number of digits
after the decimal point as it has been for other data types.

### Proposed Technical Corrigendum

In 12.5, in the addition to 7.21.6.1#8 and 7.29.2.1#8, under `a`,`A` conversion
specifiers, change:

> If the precision is present (in the conversion specification) and is zero or at
> least as large as the precision *p* (5.2.4.2.2) of the decimal floating type,
> the conversion is as if the precision were missing. If the precision is present
> (and nonzero) and less than the precision *p* of the decimal floating type, the
> conversion first obtains an intermediate result by rounding the input in the
> type, according to the current rounding direction for decimal floating-point
> operations, to the number of digits specified by the precision, then converts
> the intermediate result as if the precision were missing. The length of the
> coefficient of the intermediate result is the smallest number, at least as large
> as the formatting precision, for which the quantum exponent is within the
> quantum exponent range of the type (see 5.2.4.2.2a). The intermediate rounding
> may overflow.

to:

> If the precision *P* is present (in the conversion specification) and is zero or
> at least as large as the precision *p* (5.2.4.2.2) of the decimal floating type,
> the conversion is as if the precision were missing. If the precision *P* is
> present (and nonzero) and less than the precision *p* of the decimal floating
> type, the conversion first obtains an intermediate result as follows, where *n*
> is the number of significant digits in the coefficient:
>
> > If *n* \<\= *P*, set the intermediate result to the input.
> >
> > If *n* \> *P*, round the input value, according to the current rounding
> > direction for decimal floating-point operations, to *P* decimal digits, with
> > unbounded exponent range, representing the result with a *P*-digit integer
> > coefficient when in the form (*s*, *c*, *q*).
>
> Convert the intermediate result in the manner described above for the case where
> the precision is missing.

In 12.5, in the addition to 7.21.6.1#8 and 7.29.2.1#8, in EXAMPLE 3, change the
results:

> ```c
> 9.54321e+93
>
> 9.5432e+93
>
> 9.543e+93
>
> 9.540e+93
>
> 9.500e+93
>
> 1.0000e+94
>
> inf
> ```

to:

> ```c
> 9.54321e+93
>
> 9.5432e+93
>
> 9.543e+93
>
> 9.54e+93
>
> 9.5e+93
>
> 1e+94
>
> 1e+97
> ```

Add, as a new EXAMPLE,

```c
#include <stdio.h>

int main(void) {
  _Decimal32 x = 9512345e90df;
  _Decimal32 x2 = 9512345e86df;

  printf("%.3Ha\n", x); // New expected output: 9.51e96
  printf("%.2Ha\n", x); // New expected output: 9.5e96
  printf("%.1Ha\n", x); // New expected output: 1e97
  printf("%.2Ha\n", x2); // New expected output: 9.5e92

  return 0;
}
```


</div>


---

---

<div id="issue0CFP.12">

## Issue 0CFP.12: P1: Zero payloads and `set payload` function

Authors: WG14, Jim Thomas  
Date: 2017-03-04  
Reference document: [N2125](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2125.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This is about an issue raised by Joseph Myers in SC22WG14.14450:

> The specification for `setpayload` (and likewise `setpayloadsig`) says "If `pl`
> is not a positive floating-point integer representing a valid payload, `*res` is
> set to positive zero."
>
> Does "positive" as applied to "floating-point integer" here mean "with sign bit
> 0" (the list of definitions in IEEE 754 doesn't include "positive")?  In the
> preferred encodings for binary interchange formats, 0 is a valid payload for
> quiet NaNs.  So should \+0.0 as an argument to `setpayload` result in a quiet
> NaN with payload 0, while -0.0 results in `*res` being set to \+0.0 because -0.0
> isn't positive (and for `setpayloadsig`, both result in `*res` set to \+0.0
> because a payload for a signaling NaN has to be nonzero to avoid all mantissa
> bits being zero)?

A “positive floating-point integer” is a positive integer in the floating-point
format, hence it is greater than zero. So, the current specification for
`setpayload` and `setpayloadsig` is flawed in that it doesn’t allow setting the
payload to zero.

A more basic problem is that TS 18661-1 assumes IEC 60559 interprets payloads as
integers. This is true for decimal formats. IEC 60559 says:

> The payload corresponds to the significand of finite numbers, interpreted as
> an integer with a maximum value of 10^(3×J)−1, …

The significand c interpreted as an integer is assumed throughout to be
non-negative, while the *s* field in (*s*, *q*, *c*) provides the sign. For
decimal, interpreting the bits in the encodings allows the two encoding schemes
to have the same payloads and the payloads to fit conceptually with their
encoding schemes.

However, for binary formats, IEC 60559 says:

> For binary formats, the payload is encoded in the *p*−2 least significant bits
> of the trailing significand field.

Nowhere does it actually interpret the payload for binary formats as an integer.

However, the payload for binary formats has a natural interpretation as an
unsigned integer, so it is reasonable for TS 1866-1 to interpret payloads (for
binary and decimal formats) as such.

The suggested Technical Corrigendum below addresses these problems.

### Suggested Technical Corrigendum

In 14.10, replace the first sentence:

> IEC 60559 defines the payload of a NaN to be a certain part of the NaN’s
> significand interpreted as an integer.

with:

> IEC 60559 defines the payload of a NaN to be a certain part of the NaN’s
> significand. The payload can be interpreted as an unsigned integer.

In 14.10, in the new C subclause F.10.13, replace:

> IEC 60559 defines the *payload* of a quiet or signaling NaN as an integer value
> encoded in the significand.

with:

> IEC 60559 defines the *payload* of a quiet or signaling NaN as information
> encoded in part of the NaN significand. The payload can be interpreted as an
> unsigned integer.

In 14.10, in the new C subclauses F.10.13.2#2 and F.10.13.3#2, change:

> If `pl` is not a positive floating-point integer representing a valid payload,
> `*res` is set to positive zero.

to:

> If `pl` is not a floating-point integer representing a valid payload, `*res` is
> set to positive zero.

---

Comment from WG14 on 2018-10-18:

Apr 2017 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Change

In 14.10, replace the first sentence:

> IEC 60559 defines the payload of a NaN to be a certain part of the NaN’s
> significand interpreted as an integer.

with:

> IEC 60559 defines the payload of a NaN to be a certain part of the NaN’s
> significand. The payload can be interpreted as an unsigned integer.

In 14.10, in the new C subclause F.10.13, replace:

> IEC 60559 defines the *payload* of a quiet or signaling NaN as an integer value
> encoded in the significand.

with:

> IEC 60559 defines the *payload* of a quiet or signaling NaN as information
> encoded in part of the NaN significand. The payload can be interpreted as an
> unsigned integer.

In 14.10, in the new C subclauses F.10.13.2#2 and F.10.13.3#2, change:

> If `pl` is not a positive floating-point integer representing a valid payload,
> `*res` is set to positive zero.

to:

> If `pl` is not a floating-point integer representing a valid payload, `*res` is
> set to positive zero.


</div>


---

---

<div id="issue0CFP.13">

## Issue 0CFP.13: P3: Type-generic macros for functions that round result to narrower type

Authors: WG14, Jim Thomas  
Date: 2017-03-04  
Reference document: [N2125](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2125.pdf)  
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
> > \[6a] The functions that round result to a narrower type have type-generic
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
> to:
>
> > \[6a] The functions that round result to a narrower type have type-generic
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
> > \[6a] The functions that round result to a narrower type have type-generic
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
> to:
>
> > \[6a] The functions that round result to a narrower type have type-generic
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


</div>


---

---

<div id="issue0CFP.14">

## Issue 0CFP.14: P2: Effect of `%a` vs `%A` conversion specifiers

Authors: WG14, Jim Thomas  
Date: 2017-03-04  
Reference document: [N2125](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2125.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The specification in TS 18661-2 for `a`,`A` conversion specifiers for decimal
describes the behavior in terms of  `f` and `e` formatting. The intention was
that the `A` conversion specifier would have the effects of `F` and `E`
formatting. The following Technical Corrigendum corrects this oversight, using
wording similar to that in C11 for the `g`,`G` conversion specifiers.

### Suggested Technical Corrigendum

In 12.5, in the text added to 7.21.6.1#8 and 7.29.2.1#8, under `a`,`A`
conversion specifiers, replace the bullets:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` formatting with formatting precision
> equal to −*q*,
>
> —    otherwise, use style `e` formatting with …

with:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` (or style `F` in the case of an `A`
> conversion specifier) with formatting precision equal to −*q*,
>
> —    otherwise, use style `e` (or style `E` in the case of an `A` conversion
> specifier) with …

---

Comment from WG14 on 2018-10-18:

Apr 2017 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In 12.5, in the text added to 7.21.6.1#8 and 7.29.2.1#8, under `a`,`A`
conversion specifiers, replace the bullets:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` formatting with formatting precision
> equal to −*q*,
>
> —    otherwise, use style `e` formatting with …

with:

> —    if −(*n*\+5) ≤ *q* ≤ 0, use style `f` (or style `F` in the case of an `A`
> conversion specifier) with formatting precision equal to −*q*,
>
> —    otherwise, use style `e` (or style `E` in the case of an `A` conversion
> specifier) with …


</div>


---

---

<div id="issue0CFP.15">

## Issue 0CFP.15: P3: Characteristic macros for non-arithmetic formats

Authors: WG14, Jim Thomas  
Date: 2017-10-25  
Reference document: [N2171](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2171.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This DR addresses an issue related to DR 501 and IEC 60559 non-arithmetic
interchange formats.

TS 18661-3 attempted to change the definition of `DECIMAL_DIG` so that it would
apply to all supported IEC 60559 formats. DR 501 shows that this change is
problematic. After several unsuccessful attempts at a suitable TC, WG 14 and the
CFP group have agreed to obsolesce `DECIMAL_DIG` in favor of the
*type*`_DECIMAL_DIG` macros.

The *type*`_DECIMAL_DIG` macros are helpful in using conversions between binary
floating-point formats and decimal character sequences. TS 18661-3 specifies
such conversions for non-arithmetic binary interchange formats, but neglects to
include the macros for such formats.

Likewise, the *type*`_DIG` macros too are helpful in using conversions between
binary floating-point formats and decimal character sequences, though TS 18661-3
does not specify them for non-arithmetic formats.

The suggested TC below extends the set of `FLT`*N*`_DECIMAL_DIG` and
`FLT`*N*`_DIG` macros to include ones for IEC 60559 non-arithmetic binary
interchange formats.

### Suggested Technical Corrigendum

In TS 18661-3 5.3, in the text for 5.2.4.2.2#6c, after the list for supported
types `_Float`*`N`*, insert:

> for IEC 60559 non-arithmetic binary interchange formats of width *N*:
>
> `FLT`*N*`_DECIMAL_DIG     FLT`*N*`_DIG`

In TS 18661-3 clause 7, in the text for 5.2.4.2.2a#1, change:

> The prefix `FLT`*N*`_` indicates a binary interchange floating type of width
> *N*.

to:

> The prefix `FLT`*N*`_` indicates a binary interchange floating type or a
> non-arithmetic binary interchange format of width *N*.

Change the last sentence of  5.2.4.2.2a#1 from:

> Conversely, for each such type that the implementation does not provide,
> `<float.h>` shall not define the associated macros in the following lists.

to:

> Conversely, for each such type that the implementation does not provide,
> `<float.h>` shall not define the associated macros in the following list,
> except, the implementation shall define the macros `FLT`*N*`_DECIMAL_DIG` and
> `FLT`*N*`_DIG` if it supports IEC 60559 non-arithmetic binary interchange
> formats of width *N* by providing the encoding-to-encoding conversion functions
> in `<math.h>` and the string-to-encoding and string-from-encoding functions in
> `<stdlib.h>`.

---

Comment from WG14 on 2018-10-18:

Oct 2017 meeting

### Committee Discussion

The committee agreed with this issue and its proposed clarification.

**Proposed Technical Clarification**

In TS 18661-3 5.3, in the text for 5.2.4.2.2#6c, after the list for supported
types `_Float`*`N`*, insert:

> for IEC 60559 non-arithmetic binary interchange formats of width *N*:
>
> `FLT`*N*`_DECIMAL_DIG     FLT`*N*`_DIG`

In TS 18661-3 clause 7, in the text for 5.2.4.2.2a#1, change:

> The prefix `FLT`*N*`_` indicates a binary interchange floating type of width
> *N*.

to:

> The prefix `FLT`*N*`_` indicates a binary interchange floating type or a
> non-arithmetic binary interchange format of width *N*.

Change the last sentence of  5.2.4.2.2a#1 from:

> Conversely, for each such type that the implementation does not provide,
> `<float.h>` shall not define the associated macros in the following lists.

to:

> Conversely, for each such type that the implementation does not provide,
> `<float.h>` shall not define the associated macros in the following list,
> except, the implementation shall define the macros `FLT`*N*`_DECIMAL_DIG` and
> `FLT`*N*`_DIG` if it supports IEC 60559 non-arithmetic binary interchange
> formats of width *N* by providing the encoding-to-encoding conversion functions
> in `<math.h>` and the string-to-encoding and string-from-encoding functions in
> `<stdlib.h>`.


</div>


---

---

<div id="issue0CFP.16">

## Issue 0CFP.16: P1: tgmath cbrt macro

Authors: WG14, Jim Thomas  
Date: 2017-10-25  
Reference document: [N2178](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2178.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This DR addresses a problem noted by Joseph Myers in emails SC22WG14.14743 and
14744:

> … the example \[in TS 18661-1 clause 16, for 7.25#6b – see below] implies that
> "#undef cbrtl" before calling the cbrt type-generic macro would mean it's not
> affected by constant rounding modes, but the actual normative text says "is
> affected by constant rounding modes" with no such caveat.

and

> … neither example definition \[in C11 or TS 18661-1] is valid because they might
> call a block-scope cbrtf / cbrtl; they need to avoid such a block-scope
> identifier, or a macro defined by the user, while still depending on whether
> expansion of the    
> standard header cbrtf / cbrtl macros has been suppressed at that point.

The text in question is:

> \[6b] A type-generic macro corresponding to a function indicated in the table in
> 7.6.1a is affected by constant rounding modes (7.6.2). Note that the
> type-generic macro definition in the example in 6.5.1.1 does not conform to this
> specification. A conforming macro could be implemented as follows:
>
> ```c
> #define cbrt(X)     _Generic((X),                  \
>                long double: cbrtl(X),         \
>                default: _Roundwise_cbrt(X),   \
>                float: cbrtf(X)                \
>                )
> ```
>
> where `_Roundwise_cbrt()` is equivalent to `cbrt()` invoked without
> macro-replacement suppression.

The cause of the problems is the use of `cbrtl` and `cbrtf` in the macro
definition. The suggested TC below replaces these uses with `_Roundwise_
prefixed` identifiers similar to `_Roundwise_cbrt`.

### Suggested Technical Corrigendum

In TS 18661-1, clause 16, replace:

> ```c
> #define cbrt(X)     _Generic((X),                  \
>                long double: cbrtl(X),         \
>                default: _Roundwise_cbrt(X),   \
>                float: cbrtf(X)                \
>                )
> ```
>
> where `_Roundwise_cbrt()` is equivalent to `cbrt()` invoked without
> macro-replacement suppression.

with

> ```c
> #define cbrt(X)     _Generic((X),                       \
>                long double: _Roundwise_cbrtl(X),   \
>                default: _Roundwise_cbrt(X),        \
>                float: _Roundwise_cbrtf(X)               \
>                )
> ```
>
> where `_Roundwise_cbrtl()`, `_Roundwise_cbrt()`, and `_Roundwise_cbrtf()` are
> equivalent to `cbrtl()`, `cbrt()`, and `cbrtf()`, respectively, invoked without
> macro-replacement suppression.

---

Comment from WG14 on 2019-05-03:

Oct 2017 meeting

### Committee Discussion

> There was considerable discussion on this issue. The first point is that the
> \_Generic example cited that is proposed to be fixed was not intended to impose
> requirements, yet has elicited two fixes so far, this being a third. The second
> point is that the fix offered would likely elicit numerous compiler errors as
> stated and no longer serves its original intention of illustrating \_Generic
> best practice usage. Lastly, lacking a clear simple example, is there a problem
> here that needs clarification becomes uncertain.

Apr 2018 meeting

### Committee Discussion

> A new document
> [N2212](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2212.pdf) was
> presented with a much simpler proposed change. It was accepted by the committee.

### Proposed Change

In TS 18661-1, clause 16, replace:

```c
       #define cbrt(X) _Generic((X), \
                       long double: cbrtl(X), \
                       default: _Roundwise_cbrt(X), \
                       float: cbrtf(X) \
                       )
```

> where `_Roundwise_cbrt()` is equivalent to `cbrt()` invoked without
> macro-replacement suppression.

with

```c
       #define cbrt(X) _Generic((X), \
                       long double: _Roundwise_cbrtl, \
                       default: _Roundwise_cbrt, \
                       float: _Roundwise_cbrtf \
                       )(X)
```

> where `_Roundwise_cbrtl()`, `_Roundwise_cbrt()`, and `_Roundwise_cbrtf()` are
> equivalent to `cbrtl()`, `cbrt()`, and `cbrtf()`, respectively, invoked without
> macro-replacement suppression.


</div>


---

---

<div id="issue0CFP.17">

## Issue 0CFP.17: P3: incommensurate arguments for comparison macros

Authors: WG14, C Floating Point Group  
Date: 2018-02-11  
Reference document: [N2203](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2203.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This DR addresses a problem noted by Joseph Myers in email SC22WG14.14885:

> The usual arithmetic conversions in TS 18661-3 include "If both operands have
> floating types and neither of the sets of values of their corresponding real
> types is a subset of (or equivalent to) the other, the behavior is undefined.".  
>
> Thus, for example, if neither of long double and \_Float128 has a set of values
> that is a subset of the other, given  
>
> long double a;  
> \_Float128 b;  
>
> it's undefined to have the expression "a \< b".  
>
> Now what about the expression "isless (a, b)"?  By analogy with the
> direct comparison, it would seem natural for it to be undefined.  But
> while 18661-2 explicitly disallows using those macros with one decimal and
> one non-decimal argument, I see nothing to disallow the case where neither
> set of values is a subset of the other, and the definition of these
> macros doesn't actually include the usual arithmetic conversions.

It was an oversight to not disallow argument types neither of which is a subset
(or equivalent to) the other.

### Suggested Technical Corrigendum

In TS 18661-3, at the end of clause 12 (just before 12.1), insert:

> To 7.12.14#1, append:
>
> > If neither of the sets of values of the argument formats is a subset of (or
> > equivalent to) the other, the behavior is undefined.

---

Comment from WG14 on 2018-10-18:

Apr 2018 meeting

### Committee Discussion

> The committee accepted the Suggested Technical Corrigendum as the Proposed
> Change (using our new terminology).

### Proposed Change

In TS 18661-3, at the end of clause 12 (just before 12.1), insert:

> To 7.12.14#1, append:
>
> > If neither of the sets of values of the argument formats is a subset of (or
> > equivalent to) the other, the behavior is undefined.


</div>


---

---

<div id="issue0CFP.18">

## Issue 0CFP.18: P4: missing specification of preferred quantum exponents

Authors: WG14, C Floating Point Group  
Date: 2018-02-22  
Reference document: [N2204](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2204.pdf)  
Status: Fixed  
Fixed in: C23, Floating-point TS 18661-4:2025  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

TS 18661-4 neglected to specify the preferred quantum exponent for its new
functions. This was an oversight. The following suggested TC adds the missing
specification.

### Suggested Technical Corrigendum

In TS 18661-4, at the end of clause 7, append:

In the Preferred Quantum Exponents table in 5.2.4.2.2a#7, insert before the
final row:

|  |  |
| --- | --- |
| ```c rsqrt ``` | −floor(Q(`x`)/2) |
| ```c compoundn ``` | floor(`n` × min(0, Q(`x`))) |
| ```c rootn ``` | floor(Q(`x`)/`n`) |
| ```c pown ``` | floor(`n` × Q(`x`)) |
| ```c powr ``` | floor(`y` × Q(`x`)) |

In TS 18661-4, at the end of clause 8, append:

In the Preferred Exponents Table in 5.2.4.2.2a#7, append:

|  |  |
| --- | --- |
| reduction functions | unspecified |

---

Comment from WG14 on 2018-10-18:

Apr 2018 meeting

### Committee Discussion

> The committee accepted the Suggested Technical Corrigendum as the Proposed
> Change (using our new terminology).

### Proposed Change

In TS 18661-4, at the end of clause 7, append:

In the Preferred Quantum Exponents table in 5.2.4.2.2a#7, insert before the
final row:

|  |  |
| --- | --- |
| ```c rsqrt ``` | −floor(Q(`x`)/2) |
| ```c compoundn ``` | floor(`n` × min(0, Q(`x`))) |
| ```c rootn ``` | floor(Q(`x`)/`n`) |
| ```c pown ``` | floor(`n` × Q(`x`)) |
| ```c powr ``` | floor(`y` × Q(`x`)) |

In TS 18661-4, at the end of clause 8, append:

In the Preferred Exponents Table in 5.2.4.2.2a#7, append:

|  |  |
| --- | --- |
| reduction functions | unspecified |


</div>


---

---

<div id="issue0CFP.19">

## Issue 0CFP.19: P1: updating underflow definition

Authors: WG14, C Floating Point Group  
Date: 2018-03-16  
Reference document: [N2210](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2210.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

C11 7.12.1 says

> The result underflows if the magnitude of the mathematical result is so small
> that the mathematical result cannot be represented, without extraordinary
> roundoff error, in an object of the specified type.232)
>
> 232\) The term underflow here is intended to encompass both ‘‘gradual
> underflow’’ as in IEC 60559 and also ‘‘flush-to-zero’’ underflow

The C definition of underflow doesn’t accomplish its intention as expressed in
footnote 232\. It’s too restrictive to encompass IEC 60559 gradual underflow,
because IEC 60559 underflow can occur without extraordinary roundoff error.

In IEC 60559:2011, the underflow flag is raised (in C terminology, set) if and
only if the result is tiny and inexact, even if the roundoff error is the same
as it would have been if the full (normal) precision of the type were available,
i.e., even if there is no extraordinary roundoff error.

IEC 60559:1989 offered the implementation the option to raise the underflow flag
for tiny results with extraordinary roundoff error, though it also offered the
option to raise the underflow flag for tiny inexact results, which is what most
implementations did. IEC 60559:2011 dropped the option to raise the underflow
flag based on extraordinary roundoff error.

The following suggested TC aims to loosens the C definition of underflow to
encompass IEC 60559:2011 underflow behavior, which is based on tiny inexact
results.

### Suggested Technical Corrigendum

In TS 18661-1, before 14.1, insert:

**14.0 C underflow**

The following change to C11 loosens the C definition of underflow to encompass
IEC 60559 gradual underflow, as is its stated intention (see C11 footnote 232).

**Changes to C11:**

Change the first sentence in 7.12.1#6 from:

> \[6] The result underflows if the magnitude of the mathematical result is so
> small that the mathematical result cannot be represented, without extraordinary
> roundoff error, in an object of the specified type.232) …

to:

> \[6] The result underflows if the magnitude of the mathematical result is
> nonzero and less than the minimum normal number in the type.232) …

---

Comment from WG14 on 2018-10-18:

Apr 2018 meeting

### Committee Discussion

> The committee accepted the Suggested Technical Corrigendum as the Proposed
> Change (using our new terminology).

### Proposed Change

In TS 18661-1, before 14.1, insert:

**14.0 C underflow**

The following change to C11 loosens the C definition of underflow to encompass
IEC 60559 gradual underflow, as is its stated intention (see C11 footnote 232).

**Changes to C11:**

Change the first sentence in 7.12.1#6 from:

> \[6] The result underflows if the magnitude of the mathematical result is so
> small that the mathematical result cannot be represented, without extraordinary
> roundoff error, in an object of the specified type.232) …

to:

> \[6] The result underflows if the magnitude of the mathematical result is
> nonzero and less than the minimum normal number in the type.232) …


</div>


---

---

<div id="issue0CFP.20">

## Issue 0CFP.20: P1: changes for obsolescing DECIMAL\_DIG

Authors: WG14, C Floating Point Group  
Date: 2018-03-16  
Reference document: [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.pdf)  
Status: Fixed  
Fixed in: C23  
Cross-references: [0CFP.22](log_cfp-c11.md#issue0CFP.22)  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

N2211 described changes in C11 and TS 18661 to remove references to
`DECIMAL_DIG`, which CR501 is expected to obsolesce. The changes that apply to
C11 are collected in N2253 as an update to the suggested TC in CR501. The
changes that apply to TS 18661-1 compose the CR in this document. The remaining
change is for TS 18661-3, which will be covered by a CR in a subsequent
document.

### Suggested Technical Corrigendum

In 7.1, omit:

> Change footnote 361\) from:
>
> > 361\)  If the minimum-width IEC60559 extended format (64 bits of precision) is
> > supported, `DECIMAL_DIG` shall be at least 21\. If IEC 60559 double (53 bits of
> > precision) is the widest IEC 60559 format supported, then `DECIMAL_DIG` shall be
> > at least 17\. (By contrast, `LDBL_DIG` and `DBL_DIG` are 18 and 15,
> > respectively, for these formats.)
>
> to:
>
> > 361\)  If the minimum-width IEC 60559 binary64-extended format (64 bits of
> > precision) is supported, `DECIMAL_DIG` shall be at least 21\. If IEC 60559
> > binary64 (53 bits of precision) is the widest IEC 60559 format supported, then
> > `DECIMAL_DIG` shall be at least 17\. (By contrast, `LDBL_DIG` and `DBL_DIG` are
> > 18 and 15, respectively, for these formats.)

In 10.1, change:

> After F.5#2, insert:
>
> > \[2a] The `<float.h>` header defines the macro
> >
> > ```c
> > CR_DECIMAL_DIG
> > ```
> >
> > if and only if `__STDC_WANT_IEC_60559_BFP_EXT__` is defined as a macro at the
> > point in the source file where `<float.h>` is first included. If defined,
> > `CR_DECIMAL_DIG` expands to an integral constant expression suitable for use in
> > `#if` preprocessing directives whose value is a number such that conversions
> > between all supported types with IEC 60559 binary formats and character
> > sequences with at most `CR_DECIMAL_DIG` significant decimal digits are correctly
> > rounded. The value of `CR_DECIMAL_DIG` shall be at least `DECIMAL_DIG` \+ 3\. If
> > the implementation correctly rounds for all numbers of significant decimal
> > digits, then `CR_DECIMAL_DIG` shall have the value of the macro `UINTMAX_MAX`.
> >
> > \[2b] Conversions of types with IEC 60559 binary formats to character sequences
> > with more than `CR_DECIMAL_DIG` significant decimal digits shall correctly round
> > to `CR_DECIMAL_DIG` significant digits and pad zeros on the right.
> >
> > \[2c] Conversions from character sequences with more than `CR_DECIMAL_DIG`
> > significant decimal digits to types with IEC 60559 binary formats shall
> > correctly round to an intermediate character sequence with `CR_DECIMAL_DIG`
> > significant decimal digits, according to the applicable rounding direction, and
> > correctly round the intermediate result (having `CR_DECIMAL_DIG` significant
> > decimal digits) to the destination type. The “inexact” floating-point exception
> > is raised (once) if either conversion is inexact. (The second conversion may
> > raise the “overflow” or “underflow” floating-point exception.)
>
> In F.5#2c, attach a footnote to the wording:
>
> > The “inexact” floating-point exception is raised (once) if either conversion is
> > inexact.
>
> where the footnote is:
>
> > \*) The intermediate conversion is exact only if all input digits after the
> > first `CR_DECIMAL_DIG` digits are `0`**.**
>
> to:
>
> Replace the content of F.5 with:
>
> > \[1] The `<float.h>` header defines the macro
> >
> > ```c
> > CR_DECIMAL_DIG
> > ```
> >
> > if and only if `__STDC_WANT_IEC_60559_BFP_EXT__` is defined as a macro at the
> > point in the source file where `<float.h>` is first included. If defined,
> > `CR_DECIMAL_DIG` expands to an integral constant expression suitable for use in
> > **#if** preprocessing directives whose value is a number such that conversions
> > between all supported IEC 60559 binary formats and character sequences with at
> > most `CR_DECIMAL_DIG` significant decimal digits are correctly rounded. The
> > value of `CR_DECIMAL_DIG` shall be at least *M* \+ 3, where *M* is the maximum
> > value of the *T*`_DECIMAL_DIG` macros for IEC 60559 binary formats. If the
> > implementation correctly rounds for all numbers of significant decimal digits,
> > then `CR_DECIMAL_DIG` shall have the value of the macro `UINTMAX_MAX`.
> >
> > \[2] Conversions of types with IEC 60559 binary formats to character sequences
> > with more than `CR_DECIMAL_DIG` significant decimal digits shall correctly round
> > to `CR_DECIMAL_DIG` significant digits and pad zeros on the right.
> >
> > \[3] Conversions from character sequences with more than `CR_DECIMAL_DIG`
> > significant decimal digits to types with IEC 60559 binary formats shall
> > correctly round to an intermediate character sequence with `CR_DECIMAL_DIG`
> > significant decimal digits, according to the applicable rounding direction, and
> > correctly round the intermediate result (having `CR_DECIMAL_DIG` significant
> > decimal digits) to the destination type. The “inexact” floating-point exception
> > is raised (once) if either conversion is inexact. (The second conversion may
> > raise the “overflow” or “underflow” floating-point exception.)
> >
> > \[4] The specification in this subclause assures conversion between IEC 60559
> > binary format and decimal character sequence follows all pertinent recommended
> > practice. It also assures conversion from IEC 60559 format to decimal character
> > sequence with at least *T*`_DECIMAL_DIG` digits and back, using to-nearest
> > rounding, is the identity function, where *T* is the macro prefix for the
> > format.
> >
> > \[5] Functions such as `strtod` that convert character sequences to floating
> > types honor the rounding direction. Hence, if the rounding direction might be
> > upward or downward, the implementation cannot convert a minus-signed sequence by
> > negating the converted unsigned sequence.
>
> In F.5#3, attach a footnote to the wording:
>
> > The “inexact” floating-point exception is raised (once) if either conversion is
> > inexact.
>
> where the footnote is:
>
> > \*) The intermediate conversion is exact only if all input digits after the
> > first `CR_DECIMAL_DIG` digits are `0`**.**

---

Comment from WG14 on 2019-05-03:

Apr 2018 meeting

### Committee Discussion

> The paper was only briefly discussed.
>
> This resolution is tied to the Floating Point [CR 22](log_cfp-c11.md#issue0CFP.22) as well as
> to the C2x DR 501\.

Oct 2018 meeting

### Committee Discussion

> A new paper [N2254](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2254.pdf)
> was split out from
> [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.pdf) that
> incorporates directly the Suggested Technical Corrigendum already extracted
> above.
>
> The committee accepts the Suggested Technical Corrigendum as the Proposed Change
> to resolve this issue.

### Proposed Change

In 7.1, omit:

> Change footnote 361\) from:
>
> > 361\)  If the minimum-width IEC60559 extended format (64 bits of precision) is
> > supported, `DECIMAL_DIG` shall be at least 21\. If IEC 60559 double (53 bits of
> > precision) is the widest IEC 60559 format supported, then `DECIMAL_DIG` shall be
> > at least 17\. (By contrast, `LDBL_DIG` and `DBL_DIG` are 18 and 15,
> > respectively, for these formats.)
>
> to:
>
> > 361\)  If the minimum-width IEC 60559 binary64-extended format (64 bits of
> > precision) is supported, `DECIMAL_DIG` shall be at least 21\. If IEC 60559
> > binary64 (53 bits of precision) is the widest IEC 60559 format supported, then
> > `DECIMAL_DIG` shall be at least 17\. (By contrast, `LDBL_DIG` and `DBL_DIG` are
> > 18 and 15, respectively, for these formats.)

In 10.1, change:

> After F.5#2, insert:
>
> > \[2a] The `<float.h>` header defines the macro
> >
> > ```c
> > CR_DECIMAL_DIG
> > ```
> >
> > if and only if `__STDC_WANT_IEC_60559_BFP_EXT__` is defined as a macro at the
> > point in the source file where `<float.h>` is first included. If defined,
> > `CR_DECIMAL_DIG` expands to an integral constant expression suitable for use in
> > `#if` preprocessing directives whose value is a number such that conversions
> > between all supported types with IEC 60559 binary formats and character
> > sequences with at most `CR_DECIMAL_DIG` significant decimal digits are correctly
> > rounded. The value of `CR_DECIMAL_DIG` shall be at least `DECIMAL_DIG` \+ 3\. If
> > the implementation correctly rounds for all numbers of significant decimal
> > digits, then `CR_DECIMAL_DIG` shall have the value of the macro `UINTMAX_MAX`.
> >
> > \[2b] Conversions of types with IEC 60559 binary formats to character sequences
> > with more than `CR_DECIMAL_DIG` significant decimal digits shall correctly round
> > to `CR_DECIMAL_DIG` significant digits and pad zeros on the right.
> >
> > \[2c] Conversions from character sequences with more than `CR_DECIMAL_DIG`
> > significant decimal digits to types with IEC 60559 binary formats shall
> > correctly round to an intermediate character sequence with `CR_DECIMAL_DIG`
> > significant decimal digits, according to the applicable rounding direction, and
> > correctly round the intermediate result (having `CR_DECIMAL_DIG` significant
> > decimal digits) to the destination type. The “inexact” floating-point exception
> > is raised (once) if either conversion is inexact. (The second conversion may
> > raise the “overflow” or “underflow” floating-point exception.)
>
> In F.5#2c, attach a footnote to the wording:
>
> > The “inexact” floating-point exception is raised (once) if either conversion is
> > inexact.
>
> where the footnote is:
>
> > \*) The intermediate conversion is exact only if all input digits after the
> > first `CR_DECIMAL_DIG` digits are `0`**.**
>
> to:
>
> Replace the content of F.5 with:
>
> > \[1] The `<float.h>` header defines the macro
> >
> > ```c
> > CR_DECIMAL_DIG
> > ```
> >
> > if and only if `__STDC_WANT_IEC_60559_BFP_EXT__` is defined as a macro at the
> > point in the source file where `<float.h>` is first included. If defined,
> > `CR_DECIMAL_DIG` expands to an integral constant expression suitable for use in
> > **#if** preprocessing directives whose value is a number such that conversions
> > between all supported IEC 60559 binary formats and character sequences with at
> > most `CR_DECIMAL_DIG` significant decimal digits are correctly rounded. The
> > value of `CR_DECIMAL_DIG` shall be at least *M* \+ 3, where *M* is the maximum
> > value of the *T*`_DECIMAL_DIG` macros for IEC 60559 binary formats. If the
> > implementation correctly rounds for all numbers of significant decimal digits,
> > then `CR_DECIMAL_DIG` shall have the value of the macro `UINTMAX_MAX`.
> >
> > \[2] Conversions of types with IEC 60559 binary formats to character sequences
> > with more than `CR_DECIMAL_DIG` significant decimal digits shall correctly round
> > to `CR_DECIMAL_DIG` significant digits and pad zeros on the right.
> >
> > \[3] Conversions from character sequences with more than `CR_DECIMAL_DIG`
> > significant decimal digits to types with IEC 60559 binary formats shall
> > correctly round to an intermediate character sequence with `CR_DECIMAL_DIG`
> > significant decimal digits, according to the applicable rounding direction, and
> > correctly round the intermediate result (having `CR_DECIMAL_DIG` significant
> > decimal digits) to the destination type. The “inexact” floating-point exception
> > is raised (once) if either conversion is inexact. (The second conversion may
> > raise the “overflow” or “underflow” floating-point exception.)
> >
> > \[4] The specification in this subclause assures conversion between IEC 60559
> > binary format and decimal character sequence follows all pertinent recommended
> > practice. It also assures conversion from IEC 60559 format to decimal character
> > sequence with at least *T*`_DECIMAL_DIG` digits and back, using to-nearest
> > rounding, is the identity function, where *T* is the macro prefix for the
> > format.
> >
> > \[5] Functions such as `strtod` that convert character sequences to floating
> > types honor the rounding direction. Hence, if the rounding direction might be
> > upward or downward, the implementation cannot convert a minus-signed sequence by
> > negating the converted unsigned sequence.
>
> In F.5#3, attach a footnote to the wording:
>
> > The “inexact” floating-point exception is raised (once) if either conversion is
> > inexact.
>
> where the footnote is:
>
> > \*) The intermediate conversion is exact only if all input digits after the
> > first `CR_DECIMAL_DIG` digits are `0`**.**


</div>


---

---

<div id="issue0CFP.21">

## Issue 0CFP.21: P1: printf of one-digit character string

Authors: WG14, C Floating Point Group  
Date: 2018-03-24  
Reference document: [N2224](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2224.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

It is possible that a floating-point value, when converted to a one-digit
character string, results in odd numbers no matter which way rounding is done.
For roundTiesToEven, IEC 60559 specifies that the larger magnitude value be
used.

Suggested Technical Corrigendum:

Add the following to TS 18661-1 clause 10.2 Conversions to character sequences:

> Add to F.5 Binary-decimal conversion:
>
> NOTE: IEC 60559 specifies that conversion to one-digit character strings using
> roundTiesToEven when both choices are odd, shall produce the value with the
> larger magnitude. This can happen with 9.5 whose nearest neighbors are 9.e0 and
> 1.e1, both of which are odd.

---

Comment from WG14 on 2019-05-03:

Apr 2018 meeting

### Committee Discussion

> The committee, once it understood the three floating values supplied, agreed
> with the proposed change.
>
> Subsequently, the author supplied revised values making such an understanding
> easier. The committee as a whole has yet to see the tweaked values presented
> below as the Proposed Change.

### Proposed Change

Add the following to TS 18661-1 clause 10.2 Conversions to character sequences:

> Add to F.5 Binary-decimal conversion:
>
> NOTE: IEC 60559 specifies that conversion to one-digit character strings using
> roundTiesToEven when both choices are odd, shall produce the value with the
> larger magnitude. This can happen with 9.5e2 whose nearest neighbors are 9.e2
> and 1.e3, both of which are odd.

Oct 2018 meeting

### Committee Discussion

> A new paper [N2283](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2283.htm)
> was presented with revised words from those suggested above in private
> correspondence.
>
> The committee accepts the Suggested Technical Corrigendum from that paper as the
> Proposed Change to resolve this issue.

### Proposed Change

Add the following to TS 18661-1 clause 10.2 Conversions to character sequences:

> At the end of F.5 Binary-decimal conversion, add:
>
> NOTE IEC 60559 specifies that conversion to one-digit character strings using
> roundTiesToEven when both choices have an odd least significant digit, shall
> produce the value with the larger magnitude. For example, this can happen with
> 9.5e2 whose nearest neighbors are 9.e2 and 1.e3, both of which have a single odd
> digit in the significand part.


</div>


---

---

<div id="issue0CFP.22">

## Issue 0CFP.22: P3: changes for obsolescing DECIMAL\_DIG

Authors: WG14, C Floating Point Group  
Date: 2018-03-16  
Reference document: [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.pdf)  
Status: Fixed  
Fixed in: C23  
Cross-references: [0CFP.20](log_cfp-c11.md#issue0CFP.20)  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

N2211 described changes in C11 and TS 18661 to remove references to
`DECIMAL_DIG`, which CR501 is expected to obsolesce. The changes that apply to
C11 are collected in N2253 as an update to the suggested TC in CR501. The
changes that apply to TS 18661-1 are in the CR in N2254. The remaining change is
for TS 18661-3, which is covered by the CR in this document.

### Suggested Technical Corrigendum

At the end of clause 7, omit:

> With the following change, `DECIMAL_DIG` characterizes conversions of supported
> IEC 60559 encodings, which may be wider than supported floating types.
>
> **Change to C11 \+ TS18661-1 \+ TS18661-2:**
>
> In 5.2.4.2.2#11, change the bullet defining `DECIMAL_DIG` from:
>
> > —  number of decimal digits, *n*, such that any floating-point number in the
> > widest supported floating type with …
>
> to:
>
> > —  number of decimal digits, *n*, such that any floating-point number in the
> > widest of the supported floating types and the supported IEC 60559 encodings
> > with …

---

Comment from WG14 on 2019-05-03:

Apr 2018 meeting

### Committee Discussion

> The paper was only briefly discussed.
>
> This resolution is tied to the Floating Point [CR 20](log_cfp-c11.md#issue0CFP.20) as well as
> to the C2x DR 501\.

Oct 2018 meeting

### Committee Discussion

> A new paper [N2255](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2255.pdf)
> was split out from
> [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.pdf) that
> incorporates directly the Suggested Technical Corrigendum already extracted
> above.
>
> The committee accepts the Suggested Technical Corrigendum as the Proposed Change
> to resolve this issue.

### Proposed Change

At the end of clause 7, omit:

> With the following change, `DECIMAL_DIG` characterizes conversions of supported
> IEC 60559 encodings, which may be wider than supported floating types.
>
> **Change to C11 \+ TS18661-1 \+ TS18661-2:**
>
> In 5.2.4.2.2#11, change the bullet defining `DECIMAL_DIG` from:
>
> > —  number of decimal digits, *n*, such that any floating-point number in the
> > widest supported floating type with …
>
> to:
>
> > —  number of decimal digits, *n*, such that any floating-point number in the
> > widest of the supported floating types and the supported IEC 60559 encodings
> > with …


</div>


---

---

<div id="issue0CFP.23">

## Issue 0CFP.23: P2: llquantexp invalid case

Authors: WG14, C Floating Point Group  
Date: 2018-05-26  
Reference document: [N2262](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2262.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The `llquantexp` functions in 12.4.1 of TS 18661-2 compute the quantum exponent
of a finite argument (of decimal floating type). Infinities and NaNs don’t have
a quantum exponent, so the description in C 7.12.11a.4 says “If `x` is infinite
or NaN, they compute `LLONG_MIN` and a domain error occurs.” In similar cases,
of a function with floating parameters and integer return type, where no return
value is suitable, the “invalid” floating-point exception is raised. Examples in
current C include `ilogb`, `lrint`, and `lround`. However, TS 18661-2 neglects
to specify raising “invalid” for `llquantexp`, which was an oversight.

For the C examples above, the specification of “invalid” is in annex F, because
the functions are not just for IEC 60559 implementations. The `llquantexp`
functions are only for decimal floating types, which C requires to be IEC 60559
conformant. Therefore, the specification for “invalid” can be in the primary
description in 7.12.

CFP has made a similar change for the `quantize` functions. This was done as an
editorial change, because it matches specification for the IEC 60559 quantize
operation, whose specification TS 18661 adopts by reference.

### Suggested Technical Corrigendum

In TS 18661-2 12.4.1, in C 7.12.11a.4#2, change the second sentence from:

> If `x` is infinite or NaN, they compute `LLONG_MIN` and a domain error occurs.

to:

> If `x` is infinite or NaN, they compute `LLONG_MIN`, the “invalid”
> floating-point exception is raised, and a domain error occurs.

---

Comment from WG14 on 2019-05-03:

Oct 2018 meeting

### Committee Discussion

> The committee accepts the Suggested Technical Corrigendum as the Proposed Change
> to resolve this issue.

### Proposed Change

In TS 18661-2 12.4.1, in C 7.12.11a.4#2, change the second sentence from:

> If `x` is infinite or NaN, they compute `LLONG_MIN` and a domain error occurs.

to:

> If `x` is infinite or NaN, they compute `LLONG_MIN`, the “invalid”
> floating-point exception is raised, and a domain error occurs.


</div>


---

---

<div id="issue0CFP.24">

## Issue 0CFP.24: P1 remainder NaN case

Authors: WG14, C Floating Point Group  
Date: 2018-06-26  
Reference document: [N2272](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2272.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The TS 18661-1 specification for remainder in F.10.7.2, says

—             **remainder(***x***,** ±∞**)** returns *x* for *x* not infinite.

For *x* a (quiet) NaN, this specification appears to require that the same NaN
be returned. This unintentionally goes beyond IEC 60559 whose general
specification for NaNs requires only that some (quiet) NaN be returned. The
suggested TC below uses similar words to IEC 60559’s, which allows the general
specification for NaNs to apply.

### Suggested Technical Corrigendum

In TS 18661-1 clause 12, for C F.10.7.2, change the third bullet from:

—             **remainder(***x***,** ±∞**)** returns *x* for *x* not infinite.

to:

—             **remainder(***x***,** ±∞**)** returns *x* for finite *x*.

---

Comment from WG14 on 2019-05-03:

Oct 2018 meeting

### Committee Discussion

> The committee accepts the Suggested Technical Corrigendum as the Proposed Change
> to resolve this issue.

### Proposed Change

In TS 18661-1 clause 12, for C F.10.7.2, change the third bullet from:

—             **remainder(***x***,** ±∞**)** returns *x* for *x* not infinite.

to:

—             **remainder(***x***,** ±∞**)** returns *x* for finite *x*.


</div>


---

---

<div id="issue0CFP.25">

## Issue 0CFP.25: P1 totalorder parameters

Authors: WG14, C Floating Point Group  
Date: 2018-09-05  
Reference document: [N2292](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2292.pdf)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The IEC 60559 totalOrder operation provides a total ordering of the canonical
members of the format, including signaling NaNs. Therefore the binding C
function `totalorder`, specified in TS 18661-1, must be able to accept signaling
NaN inputs. Currently the parameters for `totalorder` have floating type, whose
argument passing may convert a signaling NaN argument into a quiet NaN parameter
value. The following suggested changes use pointers to preserve signaling NaN
inputs.

### Suggested Technical Corrigendum

In F.10.12.1 (TS 18661-1), change:

> ```c
> int totalorder(double x, double y);
> ```

to:

> ```c
> int totalorder(double * x, double * y);
> ```

and similarly for the other prototypes in F.10.12.1 and F.10.12.2.

In F.10.12.1 (TS 18661-1), change:

> **Description**  
>
> \[2] The `totalorder` functions determine whether the total order relationship,
> defined by IEC 60559, is true for the ordered pair of its arguments `x`, `y`.
> These functions are fully specified in IEC 60559\. These functions are
> independent of the current rounding direction mode and raise no floating-point
> exceptions, even if an argument is a signaling NaN.  
>
> **Returns**  
>
> \[3] The `totalorder` functions return nonzero if and only if the total order
> relation is true for the ordered pair of its arguments `x`, `y`.

to:

> **Description**  
>
> \[2] The `totalorder` functions determine whether the total order relationship,
> defined by IEC 60559, is true for the ordered pair `*x`, `*y`. These functions
> are fully specified in IEC 60559\. These functions are independent of the
> current rounding direction mode and raise no floating-point exceptions, even if
> `*x` or `*y` is a signalling NaN.
>
> **Returns**  
>
> \[3] The `totalorder` functions return nonzero if and only if the total order
> relation is true for the ordered pair `*x`, `*y`.

and similarly for F.10.12.2.

---

Comment from WG14 on 2019-05-03:

Oct 2018 meeting

### Committee Discussion

> The committee accepts the Suggested Technical Corrigendum as the Proposed Change
> to resolve this issue.

### Proposed Change

In F.10.12.1 (TS 18661-1), change:

> ```c
> int totalorder(double x, double y);
> ```

to:

> ```c
> int totalorder(double * x, double * y);
> ```

and similarly for the other prototypes in F.10.12.1 and F.10.12.2.

In F.10.12.1 (TS 18661-1), change:

> **Description**  
>
> \[2] The `totalorder` functions determine whether the total order relationship,
> defined by IEC 60559, is true for the ordered pair of its arguments `x`, `y`.
> These functions are fully specified in IEC 60559\. These functions are
> independent of the current rounding direction mode and raise no floating-point
> exceptions, even if an argument is a signaling NaN.  
>
> **Returns**  
>
> \[3] The `totalorder` functions return nonzero if and only if the total order
> relation is true for the ordered pair of its arguments `x`, `y`.

to:

> **Description**  
>
> \[2] The `totalorder` functions determine whether the total order relationship,
> defined by IEC 60559, is true for the ordered pair `*x`, `*y`. These functions
> are fully specified in IEC 60559\. These functions are independent of the
> current rounding direction mode and raise no floating-point exceptions, even if
> `*x` or `*y` is a signalling NaN.
>
> **Returns**  
>
> \[3] The `totalorder` functions return nonzero if and only if the total order
> relation is true for the ordered pair `*x`, `*y`.

and similarly for F.10.12.2.


</div>


---

