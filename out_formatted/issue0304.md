## Issue 0304: Clarifying illegal tokens in `#if` directives

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG21, WG21  
Date: 2004-10-26  
Reference document: [ISO/IEC WG14 N1068](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1068.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_304.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_304.htm)

### Summary

According to 6.10.1p3, "each preprocessing token \[in a #if directive] is
converted into a token." But what if, for example, the line contains an
unmatched quote mark, or a preprocessing number like 4hello? How is such a
preprocessing token converted into a token? No indication is given that the
conversion may fail.

### Suggested Technical Corrigendum

Insert new constraint paragraph after 6.10.1p1:

> Each preprocessing token that remains after all macro replacements have occurred
> shall be in the lexical form of a token (6.4).

---

Comment from WG14 on 2006-04-04:

### Technical Corrigendum

Insert new constraint paragraph after 6.10.1p1:

> Each preprocessing token that remains after all macro replacements have occurred
> shall be in the lexical form of a token (6.4).
