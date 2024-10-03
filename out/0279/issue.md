### Summary

Standard C requires `('x' == L'x')` to hold true if `x` is a member of the basic
character set. This restricts the implementation's choice of `wchar_t` encoding.
The restriction makes it very difficult, if not impossible, for EBCDIC based
system to use Unicode as the `wchar_t` encoding.

Note: For the purpose of this DR, we will call this restriction the *wchar\_t
restriction*.

### Details

C99 7.17 paragraph 2 specifies in part:

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

Since the code value of the basic characters in UCS-2 and UCS-4 are based on
ASCII, EBCDIC systems cannot conform to the last sentence of the above if the
encoding of `wchar_t` is UCS-2 or UCS-4. This makes it unnecessarily difficult
for EBCDIC systems to use Unicode with the C language.

A program knows the type of characters (wide or normal) it is processing.
Therefore the appropriate character literal can always be used in an expression.
In situations where a program does need to mix normal and wide character code
values, the `btowc` and `wctob` functions should be used (7.24.6.1 and .2).
Facilitating such mixing were the original reason for imposing the wchar\_t
restriction in C90. With the introduction of these two functions in Amendment 1,
this restriction can be relaxed with little practical impact to the programmer.

### Suggested Technical Corrigendum

Suggestion 1

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

Suggestion 2

This change removes the restriction altogether.

Change the last part of 7.17 paragraph 2 as follows:

> "...
> 
> ```c
>    wchar_t
> ```
> 
> which is an integer type whose range of values can represent distinct codes for
> all members of the largest extended character set specified among the supported
> locales; the null character shall have the code value zero."

Suggestion 3

This change reverses the meaning of the macro in suggestion 1 and combine with
the text in suggestion 2\. An implementation can assert conformance to the
wchar\_t restriction by defining the macro `__STDC_BTOWC_EQ_WCTOB__`.

Note: Despite what the macro name suggests, `btowc` and `wctob` may not be the
same disregard of the mapping of the basic character set because of
`EOF`/`WEOF`.

Change the last part of 7.17 paragraph 2 as follows:

> "...
> 
> ```c
>    wchar_t
> ```
> 
> which is an integer type whose range of values can represent distinct codesfor
> all members of the largest extended character set specified among thesupported
> locales; the null character shall have the code value zero."

Add the following paragraph to 7.24.1 after #3.

> "The macro `__STDC_BTOWC_EQ_WCTOB__` is defined if the implementation intends to
> assert that for each member of the basic character set the `wchar_t` encoding
> has a code value equal to its value when used as the lone character in an
> integer character constant."
