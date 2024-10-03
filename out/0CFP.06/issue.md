### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14328:

> TS 18661-1 says, for `fetestexceptflag`, "The value of `*flagp` shall have been
> set by a previous call to `fegetexceptflag`.".
> 
> This contrasts with the C11 wording for `fesetexceptflag`, "The value of
> `*flagp` shall have been set by a previous call to `fegetexceptflag` whose
> second argument represented at least those floating-point exceptions represented
> by the argument `excepts`.".  So what happens if more exceptions are specified
> in the call to `fetestexceptflag` than were specified in the call to
> `fegetexceptflag`?  Then `fegetexceptflag` may or may not have stored any
> meaningful representation of the state of the extra exceptions being tested.
> 
> I think `fetestexceptflag` should have the same wording for this issue as
> `fesetexceptflag`: "whose second argument represented at least those
> floating-point exceptions represented by the argument `excepts`".

`fesetexceptflag` sets global state, typically a hardware register, whereas
`fetestexceptflag` just reads a variable. It seems more important to avoid
spurious data in the former.

Still, there’s no utility in testing spurious flag settings, and placing the
same restrictions on `fetestexceptflag` as on `fesetexceptflag` might be less
error prone.

### Suggested Technical Corrigendum

In 15.2, in the new text for C 7.6.2.4a#2, change:

> The value of `*flagp` shall have been set by a previous call to
> `fegetexceptflag`.

to:

> The value of `*flagp` shall have been set by a previous call to
> `fegetexceptflag` whose second argument represented at least those
> floating-point exceptions represented by the argument `excepts`.
