### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 1: Choice of long double in Annex F

Annex F provides various choices for the long double type (which may or may not
be an IEC 60559 type), but no method is provided for an application to determine
which choice has been made.

If a macro is provided to say whether the type is an IEC 60559 type, all the
other properties can be determined from the existing \<float.h\> macros. So, a
sufficient fix would be:

> In 5.2.4.2.2, insert a new paragraph after paragraph 10: Whether a type matches
> an IEC 60559 type is characterized by the implementation-defined values of
> FLT\_IS\_IEC\_60559, DBL\_IS\_IEC\_60559, and LDBL\_IS\_IEC\_60559:
> 
> * 0 type does not match an IEC 60559 format
> * 1 type's values and operations are those of an IEC 60559 basic, interchange or extended type
