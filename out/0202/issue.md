### Summary

Change the return type of various functions in 7.6.2 from `void` to `int` so
that they can fail.

**Urgency**  
These functions are new in C99. Once the function prototypes have been published
it will not be practical to change them. The only solution will be to produce
new parallel functions with a return value; because of the way these functions
are defined, this will involve significantly more change than just that.

**Rationale**  
The functions in question are to do with the floating-point exception and
environment flags. The former will do as an example.

The wording of the FDIS assumes that either:

* the implementation has full control over the flags, or
* the implementation has no control over the flags.

In the first case it defines various `FE_` macros such as `FE_DIVBYZERO` for the
flags. The Standard then assumes that it is always possible to set or clear the
flag or to raise the exception. In the second case the macros are not defined
and so there are no valid argument values for the functions (other than zero).

However, there are implementations that can do some things with the flags but
not others. For example, it may be possible to raise exceptions but not to clear
flags. This case is not allowed in the present draft.

The two alternative proposed changes are:

> 1. Change the return types of the functions to `int`. For now the functions always return zero (success) but a later Amendment can alter this. This is the minimum to "future-proof".
> 2. Change the definitions properly to allow them to fail. This is more complex but solves the problem once and for all.

Option 2 contains an extra item to make`fesetround` more consistent with the
other changes. This change may be omitted if it will increase consensus.

**Proposed solutions  
Option A** \- placeholder change

For each of the following functions:

> ```c
> feclearexcept
> fegetexceptflag
> feraiseexcept
> fesetexceptflag
> fegetenv
> fesetenv
> feupdateenv
> ```

change the return type to `int` and add the following:

> **Returns**
> 
> This function always returns zero. \[\*]
> 
> \[\*] This may change in a future revision of this Standard, in which case a
> zero return will mean success and a non-zero return will mean failure of some
> kind.

Add to the Future Directions clause:

> The fact that various functions in 7.6.2 and 7.6.4 always return zero is an
> obsolescent feature.

**Option B** \- full change

In 7.6 paragraph 5, attach a footnote to the wording:

> if and only if the implementation supports the floating-point exception by means
> of the functions in 7.6.2.

where the footnote is:

> \[\*] The implementation supports an exception if there are circumstances where
> a call to at least one of the functions in 7.6.2, using the macro as the
> appropriate argument, will succeed. It is not necessary for all the functions to
> succeed all the time.

For each of the following functions:

> ```c
> feclearexcept
> fegetexceptflag
> feraiseexcept
> fesetexceptflag
> fegetenv
> fesetenv
> feupdateenv
> ```

make changes equivalent to the following (which shows the wording changes for
7.6.2.1).

In paragraph 2, replace "clears" with "attempt to clear".

Add a new heading and paragraph 3:

> **Returns**
> 
> \[3] The `feclearexcept` function returns zero if the excepts argument is zero
> or if all the specified exceptions were successfully cleared. Otherwise it
> returns a nonzero value.

Optional additional change: replace 7.6.3.2p3 by:

> \[3] The `fesetround` function returns zero if and only if the requested
> rounding direction was established.
