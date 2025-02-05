### Summary

Require that `size_t` be no wider than `unsigned long` and `ptrdiff_t` be no
wider than `signed long`.

**Urgency**  
If this change is not made now, there will be a window of opportunity \- of at
least two years \- when implementations can make `size_t` be wider than
`unsigned long`. By the time any future Amendment is ready it will be
impractical to re-impose the restriction. If the change **is** made now, it can
always be relaxed if it becomes necessary.

**Rationale**  
Various types in the Standard are defined as integer types. Two of these
`size_t` and `ptrdiff_t` \- are frequently manipulated and on many
implementations need to hold values of the same order as `[un]signed long`. In
C89 there are various programming idioms that involve these types but also need
a standard integer type. For example:

> ```c
> printf ("%lu", (unsigned long) sizeof X);
> ```

or:

> ```c
> int *P1, *P2;
> ... /* make P1 and P2 point into the same array*/
> malloc (sizeof (int) * labs (P1 - P2));
> ```

If these types are allowed to become wider than long, these idioms will stop
working. More importantly, this might not happen when the code is compiled but
rather when large values first get used by a previously working program. This is
clearly a Quiet Change.

There do not appear to be any implementations which would be affected by this
proposal, and it eliminates the vast majority of potential problems with these
two types. While there are other types that theoretically meet these criteria,
such as `sig_atomic_t`, in practice they are unlikely to be larger than long and
no action is needed. There are also types in POSIX and other standards, such as
`off_t`, which are similarly affected, but they are outside the scope of C9X;
the recommended practice section would assist them.

### Suggested Technical Corrigendum

Append a new paragraph to 7.18.3:

> The value of `SIZE_MAX` shall be no greater than that of `ULONG_MAX`. The
> absolute values of `PTRDIFF_MIN` and `PTRDIFF_MAX` shall be no greater than
> those of `LONG_MIN` and`LONG_MAX` respectively.

or change the first part of 7.17 paragraph 2 to:

> \[#2\] The types are `ptrdiff_t` which is the signed integer type of the result
> of subtracting two pointers (the width of `ptrdiff_t` shall be no greater than
> that of `signed long`);
>
> > ```c
> > size_t
> > ```
>
> which is the unsigned integer type of the result of the `sizeof` operator (the
> width of `size_t` shall be no greater than that of unsigned long); or both (the
> changes are equivalent in effect).

Possibly also add the following paragraph somewhere (perhaps in 6.3.1.3):

> Recommended practice
>
> Implementations should provide a mode which will warn of conversions (including
> those involving an explicit cast) where:
>
> * the original value was taken from an object whose type is derived from a typedef defined in a header provided by the implementation;
> * that type has a conversion rank greater than that of signed long;
> * the result type has a conversion rank equal to that of signed long.
>
> (Headers provided by the implementation are not limited to those defined by this
> Standard, but explicitly excludes \<`stdint.h>`.)
