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
