## Issue 0CFP.06: Part 1: **fetestexceptflag** and exceptions passed to **fegetexceptflag**

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

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

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In 15.2, in the new text for C 7.6.2.4a#2, change:

> The value of `*flagp` shall have been set by a previous call to
> `fegetexceptflag`.

to:

> The value of `*flagp` shall have been set by a previous call to
> `fegetexceptflag` whose second argument represented at least those
> floating-point exceptions represented by the argument `excepts`.
