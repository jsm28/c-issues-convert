## Issue 0501: Can **DECIMAL\_DIG** be larger than necessary?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C23  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14285:

> C11 defines `DECIMAL_DIG` as "number of decimal digits, *n*, such that any
> floating-point number in the widest supported floating type with
> *p<sub>max</sub>* radix *b* digits can be rounded to a floating-point number
> with *n* decimal digits and back again without change to the value," and then
> gives a formula.
>
> Is it OK for the value of `DECIMAL_DIG` to be larger than given by the formula?
>  Such a value would still seem to meet the textual description, though being
> suboptimal.
>
> This is an issue for implementing TS 18661-3 when that involves types wider than
> `long double`.  In C11, "real floating type" means `float`, `double` or `long
> double` (6.2.5#10) (and then those types plus the three complex types are
> defined to be the floating types).  TS 18661-3 is supposed to be compatible with
> C11, so that an implementation can conform to both simultaneously.  The
> definition of `DECIMAL_DIG` in TS 18661-3 covers all supported floating types
> and non-arithmetic encodings.  And that's not conditional on
> `__STDC_WANT_IEC_60559_TYPES_EXT__`.  So in an implementation of TS 18661-3 that
> supports `_Float128`, `DECIMAL_DIG` must be big enough for `_Float128`, even if
> `__STDC_WANT_IEC_60559_TYPES_EXT__` is not defined when `<float.h>` is included.
>  And that's only compatible with C11 (if `long double` is narrower than
> `_Float128`) if C11 allows `DECIMAL_DIG` to be larger than given by the formula.

Agreed. The current specification for `DECIMAL_DIG` in TS 18661-3 is
incompatible with C11, as explained.

The suggested Technical Corrigendum below allows `DECIMAL_DIG` to be larger than
the value of the given formula. Thus an implementation that supports a floating
type wider than `long double`, for example a wide type in TS 18661-3, could
define `DECIMAL_DIG` to be large enough for its widest type and still conform as
a C implementation without extensions.

Where `DECIMAL_DIG` is used to determine a sufficient number of digits, this
change might lead to conversions with more digits than needed and with more
digits than would have been used without the change. However, programs wishing
the minimal sufficient number of digit are better served by the type-specific
macros `FLT_DECIMAL_DIG`, etc.

We considered the alternative of changing TS 198661-3 to make `DECIMAL_DIG`
dependent on `__STDC_WANT_IEC_60559_TYPES_EXT__`.  But this could lead to errors
resulting from separately compiled parts of a program using inconsistent values
of `DECIMAL_DIG`.

### Suggested Technical Corrigendum

In 5.2.4.2.2#11, change the bullet defining `DECIMAL_DIG` from:

> —      number of decimal digits, *n*, such that any floating-point number in the
> widest supported floating type with *p<sub>max</sub>* radix *b* digits can be
> rounded to a floating-point number with n decimal digits and back again without
> change to the value,
>
> > \< … formula … \>

to:

> —      number of decimal digits, *n*, such that any floating-point number in the
> widest supported floating type with *p<sub>max</sub>* radix *b* digits can be
> rounded to a floating-point number with n decimal digits and back again without
> change to the value, at least
>
> > \< … formula … \>

---

Comment from WG14 on 2019-05-03:

Oct 2016 meeting

### Committee Discussion

> The committee agrees with the recommendation. The following example was
> solicited and provided for a committee response.
>
> (The committee’s Proposed Committee Response and Proposed Technical Corrigendum
> have been superceded)

Apr 2017 meeting

### Committee Discussion

> The committee’s Proposed Committee Response and Proposed Technical Corrigendum
> from the last meeting was discussed and a new paper
> [N2108](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2108.pdf) by the WG14
> Floating Point study group was written and discussed at some length. After due
> consideration the committee agreed with their conclusion that `DECIMAL_DIG`
> could not in fact be implemented properly, and adopted their Suggested Technical
> Corrigendum below. For reference, the committee's previous direction can be
> found in [N2109](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2109.htm) and
> has been elided in this document.

Oct 2017 meeting

> A proposed change was adopted.

Apr 2018 meeting

### Committee Discussion

> Alternative input to the Proposed Change was presented in paper
> [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.htm) by the C
> Floating Point working group.
>
> These changes were, however, not reviewed by the Committee.

Oct 2018 meeting

### Committee Discussion

> Alternative input to the Proposed Change was presented in paper
> [N2211](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2211.htm) by the C
> Floating Point working group.
>
> N2108 suggested obsolescing `DECIMAL_DIG`, as part of the resolution of CR 501\.
> This document updates the suggested CR in N2108 to eliminate references in C11
> to `DECIMAL_DIG`, and to clarify. Changes below (along with changes to TS
> 18661\) were identified in N2211.
>
> The Floating Point Study Group was requested to extract the changes for C from
> N2211 and present them separately. This was done and presented (without change)
> in paper [N2253](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2253.pdf) and
> these changes were accepted by the committee as the proposed resolution to this
> issue.

### Proposed Change

In 7.31, add a subclause:

> **7.31.x Mathematics** `<math.h>`
>
> Use of the `DECIMAL_DIG` macro is an obsolescent feature. A similar
> type-specific macro, such as `LDBL_DECIMAL_DIG` can be used instead.

In 5.2.4.2.2#11, in the bullet defining `DECIMAL_DIG`, attach a footnote to the
wording:

> ```c
> DECIMAL_DIG
> ```

where the footnote is:

> \*) See ‘‘future library directions’’ (7.31.x).

In 5.2.4.2.2#14, change:

>  \[14\] Conversion from (at least) `double` to decimal with `DECIMAL_DIG` digits
> and back should be the identity function.

to:

> \[14\] Conversion between real floating type and decimal character sequence with
> at most *T*`_DECIMAL_DIG` digits should be correctly rounded, where *T* is the
> macro prefix for the type. This assures conversion from real floating type to
> decimal character sequence with *T*`_DECIMAL_DIG` digits and back, using
> to-nearest rounding, is the identity function.

In 5.2.4.2.2#16, in the list of macro values in EXAMPLE 2, omit:

> ```c
> DECIMAL_DIG          17
> ```

In 5.2.4.2.2#16, at the end of EXAMPLE 2, omit:

> If a type wider than `double` were supported, then `DECIMAL_DIG` would be
> greater than 17\. For example, if the widest type were to use the minimal-width
> IEC 60559 double-extended format (64 bits of precision), then `DECIMAL_DIG`
> would be 21\.

In 7.21.6.1#13 and 7.29.2.1#13, change:

> \[13\] For `e`, `E`, `f`, `F`, `g`, and `G` conversions, if the number of
> significant decimal digits is at most `DECIMAL_DIG`, then the result should be
> correctly rounded.283) If the number of significant decimal digits is more than
> `DECIMAL_DIG` but the source value is exactly representable with `DECIMAL_DIG`
> digits, then the result should be an exact representation with trailing zeros.
> Otherwise, the source value is bounded by two adjacent decimal strings *L* \<
> *U*, both having `DECIMAL_DIG` significant digits; the value of the resultant
> decimal string *D* should satisfy *L* ≤ *D* ≤ *U*, with the extra stipulation
> that the error should have a correct sign for the current rounding direction.

to:

> \[13\] For `e`, `E`, `f`, `F`, `g`, and `G` conversions, if the number of
> significant decimal digits is at most the maximum value *M* of the
> *T*`_DECIMAL_DIG` macros (defined in `<float.h>`), then the result should be
> correctly rounded.283) If the number of significant decimal digits is more than
> *M* but the source value is exactly representable with *M* digits, then the
> result should be an exact representation with trailing zeros. Otherwise, the
> source value is bounded by two adjacent decimal strings *L* \< *U*, both having
> *M* significant digits; the value of the resultant decimal string *D* should
> satisfy *L* ≤ *D* ≤ *U*, with the extra stipulation that the error should have a
> correct sign for the current rounding direction.

In 7.22.1.3#9 and 7.29.4.1.1#9, change:

> \[9\] If the subject sequence has the decimal form and at most `DECIMAL_DIG`
> (defined in `<float.h>`) significant digits, the result should be correctly
> rounded. If the subject sequence *D* has the decimal form and more than
> `DECIMAL_DIG` significant digits, consider the two bounding, adjacent decimal
> strings *L* and *U*, both having `DECIMAL_DIG` significant digits, such that the
> values of *L*, *D*, and *U* satisfy *L* ≤ *D* ≤ *U*. The result should be one of
> the (equal or adjacent) values that would be obtained by correctly rounding *L*
> and *U* according to the current rounding direction, with the extra stipulation
> that the error with respect to *D* should have a correct sign for the current
> rounding direction.294)

to:

> \[9\] If the subject sequence has the decimal form and at most *M* significant
> digits, where *M* is the maximum value of the *T*`_DECIMAL_DIG` macros (defined
> in `<float.h>`), the result should be correctly rounded. If the subject sequence
> *D* has the decimal form and more than *M* digits, consider the two bounding,
> adjacent decimal strings *L* and *U*, both having *M* significant digits, such
> that the values of *L*, *D*, and *U* satisfy *L* ≤ *D* ≤ *U*. The result should
> be one of the (equal or adjacent) values that would be obtained by correctly
> rounding *L* and *U* according to the current rounding direction, with the extra
> stipulation that the error with respect to *D* should have a correct sign for
> the current rounding direction.294)

In 7.22.1.3 footnote 294 and 7.29.4.1.1 footnote 345, change:

> `DECIMAL_DIG`, defined in `<float.h>`, should be sufficiently large that *L* and
> *U* will usually round to the same internal floating value, but if not will
> round to adjacent values.

to:

> *M* is sufficiently large that *L* and *U* will usually correctly round to the
> same internal floating value, but if not will correctly round to adjacent
> values.

In F.5, omit footnote 361:

> If the minimum-width IEC 60559 extended format (64 bits of precision) is
> supported, `DECIMAL_DIG` shall be at least 21\. If IEC 60559 double (53 bits of
> precision) is the widest IEC 60559 format supported, then `DECIMAL_DIG` shall be
> at least 17\. (By contrast, `LDBL_DIG` and `DBL_DIG` are 18 and 15,
> respectively, for these formats.)

The following change is needed only if TS 18661-1 (with CR 20\) is not
incorporated into C.

In F.5, replace::

> \[1\] Conversion from the widest supported IEC 60559 format to decimal with
> **DECIMAL\_DIG** digits and back is the identity function.361)
>
> \[2\] Conversions involving IEC 60559 formats follow all pertinent recommended
> practice. In particular, conversion between any supported IEC 60559 format and
> decimal with `DECIMAL_DIG` or fewer significant digits is correctly rounded
> (honoring the current rounding mode), which assures that conversion from the
> widest supported IEC 60559 format to decimal with `DECIMAL_DIG` digits and back
> is the identity function.

with:

> \[1\] Conversions involving IEC 60559 formats follow all pertinent recommended
> practice. Conversion between any supported IEC 60559 format and decimal
> character sequence with *M* or fewer significant digits is correctly rounded
> (honoring the current rounding mode), where *M* is the maximum value of the
> *T*`_DECIMAL_DIG` macros (defined in `<float.h>`). Conversion from any supported
> IEC 60559 format to decimal character sequence with at least *T*`_DECIMAL_DIG`
> digits (for the corresponding *type*) and back, using to-nearest rounding, is
> the identity function.

and renumber the subsequent paragraph.
