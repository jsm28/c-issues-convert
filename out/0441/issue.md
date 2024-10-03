### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 2: Definition of FLT\_ROUNDS

The C11 definition of FLT\_ROUNDS is inadequate in that it refers to
floating-point addition but does not say addition of what type. If long double
is not an IEC 60559 type, it may not fully support all rounding modes even
though they are supported by other types. (This is an actual issue with real
implementations using non-IEC 60559 types for long double.) A suitable fix would
be:

> In 5.2.4.2.2#8, insert "for type float" after "floating-point addition". At the
> end of F.2#1, insert "The value of FLT\_ROUNDS applies to all IEC 60559 types
> supported by the implementation, but may not apply to non-IEC 60559 types.".
