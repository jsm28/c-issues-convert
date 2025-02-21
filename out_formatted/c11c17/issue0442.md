## Issue 0442: Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 3

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Joseph Myers  
Date: 2013-07-21  
Reference document: [N1730](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1730.pdf)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 3: Floating-point exceptions and 6.5#5

C11 6.5#5 says "If an exceptional condition occurs during the evaluation of an
expression (that is, if the result is not mathematically defined or not in the
range of representable values for its type), the behavior is undefined.". When
the Annex F bindings are in effect, it must be intended that floating-point
exceptions do not produce such undefined behavior (instead, behavior such as
evaluating to a NaN must be defined). But no normative text actually says that.

A suitable fix would be:

> Append to 6.5#5: For implementations defining \_\_STDC\_IEC\_559\_\_, this does
> not apply to exceptional conditions where the behavior (such as raising a
> floating-point exception and returning a NaN) is defined by Annex F, directly or
> by reference to IEC 60559\.

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

### Committee Discussion

* The following words were discussed extensively and thought appropriate as appropriate for inclusion in F.3, rather than a new F.4:
  > If an exceptional condition occurs during the evaluation of an expression (that
  > is, if the result is not mathematically defined or not in the range of
  > representable values for its type), and the behaviour is not defined in this
  > annex or by reference to IEC 60559, 6.5p5 applies and the behaviour is
  > undefined.
* The committee also suggested adding an example or footnote suggesting that this would apply to a non-IEC 60550 `long double`.

Apr 2014 meeting

### Committee Discussion

> Further correspondence with the author and excerpted in
> [N1804](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1804.htm) has
> identified the core issue as being a simple misunderstanding of the
> applicability of normative annexes to the standard.

### Proposed Committee Response

> WG14 treats normative annexes such as Annex F as if they were linear extensions
> of the standard itself. When Annex F is requested via definition of
> `__STDC_IEC_559__` then 6.5#5 is superseded and floating point exceptions become
> well defined.
