### Summary

Originally, Standard C required `('x' == L'x')` to hold true when `x` is a
member of the basic character set. This restricted the implementation's choice
of `wchar_t` encoding, and the changes made in response to DR 279 removed this
restriction (published as change #58, on page 11 of TC2). However, there is a
vast body of existing application code that relies on this formerly normative
requirement for portability.

DR 279 suggested methods to relax the restriction that would make it easier for
applications to continue to rely on the relationship between basic characters
and their wide character equivalents. The POSIX community strongly urges WG14 to
reconsider the change introduced in ISO/IEC 9899:1999 Technical Corrigendum 2 in
response to DR 279\.

### Details

C99 7.17 paragraph 2 specified (before TC2) in part:

> "...
>
> ```c
>    wchar_t
> ```
>
> which is an integer type whose range of values can represent distinct codes for
> all members of the largest extended character set specified among the supported
> locales; the null character shall have the code value zero and each member of
> the basic character set shall have a code value equal to its value when used as
> the lone character in an integer character constant."

TC2 altered this text, removing the phrase:

> " and each member of the basic character set shall have a code value equal to
> its value when used as the lone character in an integer character constant"

In the committee discussion for TC2, an alternative approach was proposed:

> "...
>
> ```c
>    wchar_t
> ```
>
> which is an integer type whose range of values can represent distinct codes for
> all members of the largest extended character set specified among the supported
> locales; the null character shall have the code value zero. Each member of the
> basic character set shall have a code value equal to its value when used as the
> lone character in an integer character constant if an implementation does not
> define `__STDC_BTOWC_NEQ_WCTOB__`."

The POSIX community, as represented by the Austin Group, would have preferred
this solution. Without any method to determine if the restriction applies or
not, all applications would be required to make changes that may have
performance and efficiency impacts in order to maintain portability. The ISO/IEC
9945:2004 POSIX standard contains words derived from the ISO/IEC 9899:1999
standard:

> **wchar\_t**
>
> Integer type whose range of values can represent distinct wide-character codes
> for all members of the largest character set specified among the locales
> supported by the compilation environment: the null character has the code value
> 0 and each member of the portable character set has a code value equal to its
> value when used as the lone character in an integer character constant.

In order to align with TC2, the Austin Group is proposing to change this to:

> **wchar\_t**
>
> Integer type whose range of values can represent distinct wide-character codes
> for all members of the largest character set specified among the locales
> supported by the compilation environment: the null character has the code value
> 0 and each member of the portable character set has a code value equal to its
> value when used as the lone character in an integer character constant if an
> implementation does not define `__POSIX_BTOWC_NEQ_WCTOB__`."

However, the Austin Group also feels that such a change would be beneficial to
all C language users, and not just to the POSIX community, and therefore
respectfully suggests that if a future revision or technical corrigendum to
ISO/IEC 9899 were to be published, a similar change (using
`__STDC_BTOWC_NEQ_WCTOB__` as the macro name) would help application developers
understand when and where the restriction applies.

### Suggested Technical Corrigendum

Suggestion 1 from DR279:

This change allows an implementation to deviate from the last part of 7.17
paragraph 2 if the macro `__STDC_BTOWC_NEQ_WCTOB__` is predefined. This would
not affect ASCII based systems, but would provide leeway for EBCDIC systems to
process Unicode using C.

Change the last part of 7.17 paragraph 2 as follows:

> "...
>
> ```c
>    wchar_t
> ```
>
> which is an integer type whose range of values can represent distinct codes for
> all members of the largest extended character set specified among the supported
> locales; the null character shall have the code value zero. Each member of the
> basic character set shall have a code value equal to its value when used as the
> lone character in an integer character constant if an implementation does not
> define `__STDC_BTOWC_NEQ_WCTOB__`."

A program that requires the wchar\_t restriction can check for the macro and
cause the translator to put out a diagnostic if the implementation does not
support the restriction. This at least would help diagnose porting problems.
