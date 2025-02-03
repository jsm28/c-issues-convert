For the case of converting a large finite value to an integer value, lrint and
lround have one set of requirements, while ilogb has another set. This is
inconsistent.

Both 7.12.9.5 The lrint and llrint functions and 7.12.9.7 The lround and llround
functions have:

> If the rounded value is outside the range of the return type, the numeric result
> is unspecified and a domain error or range error may occur.

While 7.12.6.5 The ilogb functions has:

> If the correct value is outside the range of the return type, the numeric result
> is unspecified.

I believe that the following changes to C11 should be done.

1. 7.12.6.5 The ilogb functions:

   Change to: If the correct value is outside the range of the return type, the
   numeric result is unspecified and a domain error or range error may occur.
