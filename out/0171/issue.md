*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 019: Ranges of integral types

It appears to be possible to create implementations with unreasonable
arrangements of integral types.

Subclause 6.1.2.5 states various rules which allow the following deductions to
be made:

> ```c
> SCHAR_MAX  = SHRT_MAX
>  SHRT_MAX   = INT_MAX
>  INT_MAX    = LONG_MAX
>  SCHAR_MIN  = SHRT_MIN
>  SHRT_MIN   = INT_MIN
>  INT_MIN    = LONG_MIN
>  SCHAR_MAX  = UCHAR_MAX
>  SHRT_MAX   = USHRT_MAX
>  INT_MAX    = UINT_MAX
>  LONG_MAX   = ULONG_MAX
> ```

and, depending on the interpretation of the term *the same amount of storage:*

> ```c
> sizeof (unsigned short) == sizeof (short)
>  sizeof (unsigned int)   == sizeof (int)
>  sizeof (unsigned long)  == sizeof (long)
> ```

However, (based on the preliminary discussions of [Defect Report
#069](issue:0069), which allow padding bits in integral types) there does not
appear to be any requirement for the following:

> ```c
> UCHAR_MAX  = USHRT_MAX
>  USHRT_MAX  = UINT_MAX
>  UINT_MAX   = ULONG_MAX
>  sizeof (short)  = sizeof (int)
>  sizeof (int)    = sizeof (long)
>  UCHAR_MAX  = INT_MAX
> ```

The first five of these are necessary to allow reasonable deductions to be made
about the behavior of types in the presence of padding bits (for example, that
unsigned long can hold any value representable in any integral type). The sixth
is necessary to allow the `<ctype.h>` functions to behave sensibly (it is also
assumed by example 2 of subclause 5.1.2.3).

### Suggested Technical Corrigendum

In subclause 6.1.2.5, change in the fourth paragraph:

> In the list of signed integer types above, the range of values of each type is a
> subrange of the values of the next type in the list

. to:

> In the list of signed integer types above, the range of values of each type is a
> subrange of the values of the next type in the list, and the size of an object
> of each type is not greater than the size of an object of the next type in the
> list.

Add to the fifth paragraph:

> The range of values of each unsigned integer type is a subrange of the next type
> (in the list `unsigned char`, `unsigned short`, `unsigned int`, `unsigned
> long`).

Add to the fifth or eighth paragraph:

> The range of values of the type `unsigned char` is a subrange of the values of
> the type `int`.
