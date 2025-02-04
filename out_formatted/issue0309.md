## Issue 0309: Clarifying trigraph substitution

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG21, WG21  
Date: 2004-10-26  
Reference document: [ISO/IEC WG14 N1068](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1068.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_309.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_309.htm)

### Summary

Obviously, "before any other processing" is already implied by the phases of
translation, but it doesn't hurt to point out the implication here. And in
general, a distributive description ("each" with singular) tends to be less
ambiguous than a collective one ("all" with plural). The motivation for deleting
the phrase "in a source file" is, as far as I can see, weak at best.

### Suggested Technical Corrigendum

Change 5.2.1.1p1:

> ~~All occurrences in a source file~~ <u>Before any other processing takes place,
> each occurrence of one</u> of the following sequences of three characters
> (called *trigraph sequences*<sup>12\)</sup>) ~~are~~ <u>is</u> replaced with the
> corresponding single character.

---

Comment from WG14 on 2006-03-05:

### Technical Corrigendum

Change 5.2.1.1p1:

> ~~All occurrences in a source file~~ <u>Before any other processing takes place,
> each occurrence of one</u> of the following sequences of three characters
> (called *trigraph sequences*<sup>12\)</sup>) ~~are~~ <u>is</u> replaced with the
> corresponding single character.
