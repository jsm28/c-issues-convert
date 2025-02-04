## Issue 0409: `f(inf)` is `inf` being a range error

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred J. Tydeman (USA)  
Date: 2012-01-11  
Reference document: [N1593](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1593.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Several of the functions in `<math.h>` that compute infinity for `f(infinity)`
have the phrase (or something similar):

> A range error occurs if the magnitude of x is too large.

Since infinity is 'too large', one might conclude that `f(infinity)` is a range
error for those functions.

However, 7.12.1#5 has:

> A floating result overflows if the magnitude of the mathematical result is
> finite but so large that the mathematical result cannot be represented without
> extraordinary roundoff error ...

The key word being 'finite'. So, one could conclude f(infinity) being infinity
is not overflow (and therefore, not a range error).

To me, this appears to be a contradiction. I have encountered both kinds of
implementations; some treat this case as a range error, and others that do not.

For both LIA and IEEE-754, f(infinity) being infinity is not considered an
error.

### Suggested Change

1. 7.12.5.4 The cosh functions

   Change to: A range error occurs if the magnitude of finite x is too large.
2. 7.12.5.5 The sinh functions

   Change to: A range error occurs if the magnitude of finite x is too large.
3. 7.12.6.1 The exp functions

   Change to: A range error occurs if the magnitude of finite x is too large.
4. 7.12.6.2 The exp2 functions

   Change to: A range error occurs if the magnitude of finite x is too large.
5. 7.12.6.3 The expm1 functions

   Change to: A range error occurs if the magnitude of finite x is too large.
6. 7.12.6.6 The ldexp functions

   Change to: A range error may occur for finite arguments.
7. 7.12.6.13 The scalbn and scalbln functions

   Change to: A range error may occur for finite arguments.
8. 7.12.7.3 The hypot functions

   Change to: A range error may occur for finite arguments.
9. 7.12.7.4 The pow functions

   Change to: A range error may occur for finite arguments.
10. 7.12.8.2 The erfc functions

    Change to: A range error occurs if finite x is too large.
11. 7.12.8.3 The lgamma functions

    Change to: A range error occurs if finite x is too large.
12. 7.12.8.4 The tgamma functions

    Change to: A range error occurs if the magnitude of finite x is too large and
    may occur if the magnitude of x is too small.
13. 7.12.12.1 The fdim functions

    Change to: A range error may occur for finite arguments.
14. 7.12.13.1 The fma functions

    Change to: A range error may occur for finite arguments.

---

Comment from WG14 on 2016-10-21:

Feb 2012 meeting

### Committee Discussion

> * The committee rejected the Suggested Change in the main body of this defect report.
> * The committee considered the following, but rejected it (as just being a restatement of 7.12.1 paragraphs 4 and 5).
>   > If the result overflows, a range error shall occur.
> * A question arose as to why these range error cases are listed in the individual functions (instead of just being covered by the blanket 7.12.1 paragraphs 4, 5, and 6\)
>
>   7.12.1 paragraph 1 has the answer:
>
>   > The behavior of each of the functions in \<math.h\> is specified for all
>   > representable values of its input arguments, except where stated otherwise.
> * Several other approaches were discussed, without any consensus reached
>   1. Add a footnote to 7.12.1 paragraph 5, first sentence:
>      > In an implementation that supports infinities, a range error may happen for
>      > functions that map an infinity argument into an exact infinity or exact zero
>      > result.
>   2. Add to end of 7.12.1 paragraph 4:
>      > Recommended practice
>      >
>      > In an implementation that supports infinities, a range error should not happen
>      > for functions that map an infinity argument into an exact infinity or exact zero
>      > result.
>   3. Add to 7.12.1 paragraph 4:
>      > An implementation may define additional range errors, provided that such errors
>      > are consistent with the mathematical definition of the function.

Oct 2012 meeting

### Committee Discussion

> * Fred wrote a paper [N1629](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1629.htm) discussing "Fixing a contradiction" and "Taking care of infinity".
> * The definition of range error, however, in 7.12.1 paragraph 4 indicates infinity is excluded (since it has a representation), and as such no change is required.

Oct 2015 meeting

### Committee Discussion

> Fred presented another paper
> [N1979](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1979.htm) noting an
> error in the October 2012 committee response, and after discussion, the proposed
> clarification was adopted, and is as follows

### Proposed Committee Response

The definition of range error in 7.12.1 paragraph 4 excludes infinity.

For example, `exp(+infinity)` is `+infinity`. Since the input `+infinity` is
representable, then the output `+infinity` is representable in an object of the
specified type. By, 7.12.1 paragraph 4, a range error has not happened. Also, by
7.12.1 paragraph 5, since the result is not finite, overflow has not happened.
