### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 4: Floating-point state not being an object

The description of the floating-point environment in C11 fails to make
sufficiently clear what is or is not an object (C11 footnote 205 is not
normative, and so cannot be used to that effect); it uses terms such as "system
variable" without saying what that is. Simply moving that footnote to normative
text would fix this issue:

> Move the contents of footnote 205 (C11 subclause 7.6) to the end of 5.1.2.3#2.
