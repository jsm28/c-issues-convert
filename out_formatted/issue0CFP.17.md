## Issue 0CFP.17: P3: incommensurate arguments for comparison macros

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, C Floating Point Group  
Date: 2018-02-11  
Reference document: [N2203](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2203.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This DR addresses a problem noted by Joseph Myers in email SC22WG14.14885:

> The usual arithmetic conversions in TS 18661-3 include "If both operands have
> floating types and neither of the sets of values of their corresponding real
> types is a subset of (or equivalent to) the other, the behavior is undefined.".  
>
> Thus, for example, if neither of long double and \_Float128 has a set of values
> that is a subset of the other, given  
>
> long double a;  
> \_Float128 b;  
>
> it's undefined to have the expression "a \< b".  
>
> Now what about the expression "isless (a, b)"?  By analogy with the
> direct comparison, it would seem natural for it to be undefined.  But
> while 18661-2 explicitly disallows using those macros with one decimal and
> one non-decimal argument, I see nothing to disallow the case where neither
> set of values is a subset of the other, and the definition of these
> macros doesn't actually include the usual arithmetic conversions.

It was an oversight to not disallow argument types neither of which is a subset
(or equivalent to) the other.

### Suggested Technical Corrigendum

In TS 18661-3, at the end of clause 12 (just before 12.1), insert:

> To 7.12.14#1, append:
>
> > If neither of the sets of values of the argument formats is a subset of (or
> > equivalent to) the other, the behavior is undefined.

---

Comment from WG14 on 2018-10-18:

Apr 2018 meeting

### Committee Discussion

> The committee accepted the Suggested Technical Corrigendum as the Proposed
> Change (using our new terminology).

### Proposed Change

In TS 18661-3, at the end of clause 12 (just before 12.1), insert:

> To 7.12.14#1, append:
>
> > If neither of the sets of values of the argument formats is a subset of (or
> > equivalent to) the other, the behavior is undefined.
