## Issue 0297: May `FE_*` floating-point exception flags have bits in common?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred Tydeman (USA)  
Date: 2003-11-29  
Reference document: [N1045](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1045.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_297.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_297.htm)

### Summary

May the floating-point exception flags of 7.6 Floating-point environment
`<fenv.h>`, paragraph 5, have bits in common, e.g., the AND between two of the
`FE_*` macros be nonzero?

**Details from C99\+TC1**

Suppose that the floating-point exception flags of 7.6 Floating-point
environment `<fenv.h>` are defined as follows:

```c
 #define FE_INVALID   0x8001
  #define FE_DIVBYZERO 0x8002
  #define FE_OVERFLOW  0x8004
  #define FE_UNDERFLOW 0x8008
  #define FE_INEXACT   0x8010
```

That is, there is a bit in common to at least two of the macros, in this case,
it is common to all five macros. This is allowed by the current C99 wording.
That bit here could mean: any floating-point exception is raised.

Clive Feather scanned through Annex B, and concluded that this is really the
only case of flags being allowed to have common bits, which could be why we
haven't spotted this condition before now.

Does this cause any problems?

Yes. Consider the example code in 7.6.2.5:

```c
if (set_excepts & FE_INVALID) f();
  if (set_excepts & FE_OVERFLOW) g();
```

Suppose that just `FE_DIVBYZERO` is raised, e.g., set\_excepts is 0x8002. Then,
both of the above tests would report true (which is wrong), and both `f()` and
`g()` would be called.

I know of two solutions:

1. Require that there be no bits in common to any of these `FE_*` floating-point
   exception macros. One way is to change the last sentence of paragraph 5 of 7.6
   to be:

   > The defined macros expand to integer constant expressions with values such that
   > bitwise ORs of all combinations of the macros result in distinct values, and
   > furthermore, bitwise ANDs of all combinations of the macros result in zero.

   In addition, we could add a footnote to that sentance along the lines of:

   > The macros should be distinct powers of two.

   Possible problem: This could break existing implementations. Anyone know of an
   implementation that would break?

   All feedback I have received says this is what we "designed" and is the only
   sane solution; it is also what people expect.
2. Add another macro, such as `FE_EXP_MASK`, that is the OR of all these macros,
   but without any of the bits in common. In this case, it would be 0x001f. If we
   choose this solution, then we will need to redo the examples that test the
   floating-point exception flags. For example, in 7.6.2.5, the tests would become:

   ```c
   if (set_excepts & FE_INVALID & FE_EXP_MASK) f();
     if (set_excepts & FE_OVERFLOW & FE_EXP_MASK) g();
   ```

   Possible problem: This would require existing user programs to be recoded.

   Many of us do not like this solution, and if it were allowed, would be very bad
   news.

### Suggested Technical Corrigendum

Change the last sentence of paragraph 5 of 7.6 Floating-point environment
`<fenv.h>` to be:

> The defined macros expand to integer constant expressions with values such that
> bitwise ORs of all combinations of the macros result in distinct values, and
> furthermore, bitwise ANDs of all combinations of the macros result in zero.

In addition, add a footnote to that sentance along the lines of:

> The macros should be distinct powers of two.

---

Comment from WG14 on 2004-09-28:

### Technical Corrigendum

Change the last sentence of paragraph 5 of 7.6 Floating-point environment
`<fenv.h>` to be:

> The defined macros expand to integer constant expressions with values such that
> bitwise ORs of all combinations of the macros result in distinct values, and
> furthermore, bitwise ANDs of all combinations of the macros result in zero.

In addition, add a footnote to that sentance along the lines of:

> The macros should be distinct powers of two.
