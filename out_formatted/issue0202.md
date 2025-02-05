## Issue 0202: Change return type of certain `<fenv.h>` functions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 1999-07-06  
Reference document: [ISO/IEC WG14 N883](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n883.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_202.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_202.htm)

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
> This function always returns zero. \[\*\]
>
> \[\*\] This may change in a future revision of this Standard, in which case a
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

> \[\*\] The implementation supports an exception if there are circumstances where
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
> \[3\] The `feclearexcept` function returns zero if the excepts argument is zero
> or if all the specified exceptions were successfully cleared. Otherwise it
> returns a nonzero value.

Optional additional change: replace 7.6.3.2p3 by:

> \[3\] The `fesetround` function returns zero if and only if the requested
> rounding direction was established.

---

Comment from WG14 on 2001-01-22:

### Technical Corrigendum

In 7.6 paragraph 5, attach a footnote to the wording:

> if and only if the implementation supports the floating-point exception by means
> of the functions in 7.6.2.

where the footnote is:

> \[\*\] The implementation supports an exception if there are circumstances where
> a call to at least one of the functions in 7.6.2, using the macro as the
> appropriate argument, will succeed. It is not necessary for all the functions to
> succeed all the time.

In 7.6.2.1 paragraph 1, change the result type from `void` to `int`.

In 7.6.2.1 paragraph 2, replace "clears" with "attempts to clear".

In 7.6.2.1 add a new heading and paragraph 3:

> **Returns**
>
> \[#3\] The `feclearexcept` function returns zero if the excepts argument is zero
> or if all the specified exceptions were successfully cleared. Otherwise it
> returns a nonzero value.

In 7.6.2.2 paragraph 1, change the result type from `void` to `int`.

In 7.6.2.2 paragraph 2, replace "stores" with "attempts to store".

In 7.6.2.2 add a new heading and paragraph 3:

> **Returns**
>
> \[#3\] The `fegetexceptflag` function returns zero if the representation was
> successfully stored. Otherwise it returns a nonzero value.

In 7.6.2.3 paragraph 1, change the result type from `void` to `int`.

In 7.6.2.3 paragraph 2, replace "raises" with "attempts to raise".

In 7.6.2.3 add a new heading and paragraph 3:

> **Returns**
>
> \[#3\] The `feraiseexcept` function returns zero if the excepts argument is zero
> or if all the specified exceptions were successfully raised. Otherwise it
> returns a nonzero value.

In 7.6.2.4 paragraph 1, change the result type from `void` to `int`.

In 7.6.2.4 paragraph 2, replace "sets" with "attempts to set".

In 7.6.2.4 add a new heading and paragraph 3:

> **Returns**
>
> \[#3\] The `fesetexceptflag` function returns zero if the excepts argument is
> zero or if all the specified flags were successfully set to the appropriate
> state. Otherwise it returns a nonzero value.

In 7.6.3.2 replace paragraph 3 by:

> \[#3\] The `fesetround` function returns zero if and only if the requested
> rounding direction was established.

In 7.6.4.1 paragraph 1, change the result type from `void` to `int`.

In 7.6.4.1 paragraph 2, replace "stores" with "attempts to store".

In 7.6.4.1 add a new heading and paragraph 3:

> **Returns**
>
> \[#3\] The `fegetenv` function returns zero if representation was successfully
> stored. Otherwise it returns a nonzero value.

In 7.6.4.3 paragraph 1, change the result type from `void` to `int`.

In 7.6.4.3 paragraph 2, replace "establishes" with "attempts to establish".

In 7.6.4.3 add a new heading and paragraph 3:

> **Returns**
>
> \[#3\] The `fesetenv` function returns zero if the environment was successfully
> established. Otherwise it returns a nonzero value.

In 7.6.4.4 paragraph 1, change the result type from `void` to `int`.

In 7.6.4.4 paragraph 2, replace "saves" with "attempts to save", replace
"installs" by "install", and replace "raises" by "raise".

In 7.6.4.4 add a new heading and paragraph 3:

> **Returns**
>
> \[#3\] The `feupdateenv` function returns zero if all the actions were
> successfully carried out. Otherwise it returns a nonzero value.

In 7.6.4.4 change to existing paragraph 3, also renumbering it as 4:

> \[#3\] EXAMPLE Hide spurious underflow floating-point exceptions:

```c
       #include <fenv.h>
         double f(double x)
         {
             #pragma STDC FENV_ACCESS ON
             double result;
             fenv_t save_env;
             if (feholdexcept(&save_env))
                 return /* indication of an environmental problem*/;
             // compute result           if (/* test spurious underflow*/)
                 if (feclearexcept(FE_UNDERFLOW))
                     return /* indication of an environmental problem */;
             if (feupdateenv(&save_env))
                 return /* indication of an environmental problem*/;
             return result;
         }
```

In Annex B change the return types for the following to `int`.

> ```c
> feclearexcept
> fegetexceptflag
> feraiseexcept
> fesetexceptflag
> fegetenv
> fesetenv
> feupdateenv
> ```
