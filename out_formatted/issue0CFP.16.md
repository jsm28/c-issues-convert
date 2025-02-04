## Issue 0CFP.16: P1: tgmath cbrt macro

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas  
Date: 2017-10-25  
Reference document: [N2178](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2178.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
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
