## Issue 0305: 6.10.1p3: Clarifying handling of keywords in `#if` directives

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG21, WG21  
Date: 2004-10-26  
Reference document: [ISO/IEC WG14 N1068](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1068.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_305.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_305.htm)

### Summary

This just clarifies that keywords are not treated specially in `#if` directives.
(In C\+\+, the keywords `true` and `false` **are** treated specially in this
regard; I suspect that someone didn't want the sentence to read, "... all
remaining identifiers, except for `true` and `false`, are replaced ...", for
reasons which seem fairly obvious to me.)

### Suggested Technical Corrigendum

Change the following sentence in 6.10.1p3:

> After all replacements due to macro expansion and the `defined` unary operator
> have been performed, all remaining identifiers <ins>and keywords</ins> are
> replaced with the pp-number `0`, and then each preprocessing token is converted
> into a token.

---

Comment from WG14 on 2006-03-05:

### Committee Response

It is clear from the standard (in particular, the phases of translation) that
there are not yet any keywords at the point in question.

### Technical Corrigendum

Change the following sentence in 6.10.1p3:

> After all replacements due to macro expansion and the `defined` unary operator
> have been performed, all remaining identifiers <ins>(including those lexically
> identical to keywords)</ins> are replaced with the pp-number `0`, and then each
> preprocessing token is converted into a token.
