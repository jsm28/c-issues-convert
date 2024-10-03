### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 3: Floating-point exceptions and 6.5#5

C11 6.5#5 says "If an exceptional condition occurs during the evaluation of an
expression (that is, if the result is not mathematically defined or not in the
range of representable values for its type), the behavior is undefined.". When
the Annex F bindings are in effect, it must be intended that floating-point
exceptions do not produce such undefined behavior (instead, behavior such as
evaluating to a NaN must be defined). But no normative text actually says that.

A suitable fix would be:

> Append to 6.5#5: For implementations defining \_\_STDC\_IEC\_559\_\_, this does
> not apply to exceptional conditions where the behavior (such as raising a
> floating-point exception and returning a NaN) is defined by Annex F, directly or
> by reference to IEC 60559\.
