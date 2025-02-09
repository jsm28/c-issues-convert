## Issue 0323: Potential problems with TC2 #34, #35, and #36

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Josey (US)  
Date: 2005-09-28  
Reference document: [N1138](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1138.pdf)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_323.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_323.htm)

**Summary:** The imaginary macro is missing in the normative text.

I think there may be a problem here with C99 (as amended by TC2). As far as I
can see there is no longer any mention of the imaginary macro in normative text,
which means implementations are not allowed to define it (because it is not
reserved for use by the implementation). Yet in Annex G it still recommends (in
informative text) that implementations which define `__STDC_IEC_559_COMPLEX__`
should define the imaginary macro. It also recommends that these implementations
should define `I` "to be `_Imaginary_I` (not `_Complex_I` as stated in 7.3)".
Yet implementations that do so would not comply with the normative text in 7.3
which requires I to be defined as `_Complex_I`.

Assuming that the intention was to allow implementations to follow the
recommendations in Annex G, but by an oversight the necessary normative text to
allow them to do so was omitted from TC2, perhaps in POSIX we should keep the
current text but mark some of it CX?

### Suggested Technical Corrigendum

---

Comment from WG14 on 2006-10-25:

### Committee Discussion (for history only)

#### Fall 2005 discussion

It was pointed out that implementing Annex G causes nonconforming changes to the
normative text in C99. Exact instances were not given or known. The implications
of NOT allowing 'I' to expand to '\_Imaginary\_I' are not readily clear.

#### Spring 2006 discussion

We did not fully realize the repercusions of the changes that DR 207 would do
(implementing Annex G and

* setting **I** to **\_Imaginary\_I**, as per G.6, would contradict 7.3.1p3,
* defining the **imaginary** macro would violate the user's name space

make the implementation non-conforming; our intent was to allow implementations
to do Annex G and still conform) and agree that (some of) the effects of DR 207
should be undone. There are three possible levels of undo that could be done.

1. The smallest one is back out parts of DR 207 so that C99 allows Annex G implementators to define the **imaginary** macro and have **I** to **\_Imaginary\_I** and still conform.
2. The middle one is restore C99 back to the state before DR 207 was applied.
3. The hardest one is to re-process DR 207 and look at the suggested alternate changes it has (and even other imaginary issues identified).

Some members of the committee had hoped that imaginary would be ignored and go
away. However, at least one vendor has shipped an implementation that supports
imaginary and Annex G. This vendor has indicated that it would not be hard to
modify its implementation so that it passes strict conformance with one command
line switch and offer a default implementation with imaginary without that
switch.

One problem with **I** being imaginary versus complex is f(**I**) is either
passed one double or two doubles. However, this only matters to a few type
generic math functions and no user functions (since users have no means to
define their own type generic functions). One such type generic math function is
**cosh()**, i.e., **cosh(I\*y)** is the real **cos(y)** if **I** is imaginary,
but is the complex **cosh(z)** if **I** is complex.

It has been observed that the relational operators (\<, \<\=, \>\=, \>) of 6.5.8
and comparison macros of 7.12.14 (isless, ...) should be allowed to be used with
imaginary types when both operands are imaginary; this was an oversite in the
original C99 specification.

The mimimal changes to restore back to C99 w.r.t. to DR 207 is restore
paragraphs 3, 4, and 5 of 7.3.1 of C99; this is a subset of the changes done by
DR 207 in TC2.

### Technical Corrigendum

In 7.3.1 of C99\+TC1\+TC2, replace paragraphs 3 and 4 with:

> \[#3\] The macros
>
> > ```c
> > imaginary
> > ```
>
> and
>
> > ```c
> > _Imaginary_I
> > ```
>
> are defined if and only if the implementation supports imaginary
> types;<sup>165</sup> if defined, they expand to `_Imaginary` and a constant
> expression of type `const float _Imaginary` with the value of the imaginary
> unit.
>
> \[#4\] The macro
>
> > ```c
> > I
> > ```
>
> expands to `_Imaginary_I` or `_Complex_I`. If `_Imaginary_I` is not defined, `I`
> shall expand to `_Complex_I`.
>
> \[#5\] Notwithstanding the provisions of subclause 7.1.3, a program may undefine
> and perhaps then redefine the macros `complex`, `imaginary` and `I`.
>
> <sup>165</sup>A specification for imaginary types is in informative annex G.
