## Issue 0303: 6.10p2: Breaking up the very long sentence describing preprocessing directive

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG21, WG21  
Date: 2004-10-26  
Reference document: [ISO/IEC WG14 N1068](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1068.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Cross-references: [0250](issue0250.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_303.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_303.htm)

### Summary

The sentence describing a preprocessing directive is fearsomely long.

### Suggested Technical Corrigendum

Change 6.10p2:

> A preprocessing directive consists of a sequence of preprocessing tokens ~~that
> begins with~~ <u>. The first token in the sequence is</u> a `#` preprocessing
> token that (at the start of translation phase 4\) is either the first character
> in the source file (optionally after white space containing no new-line
> characters) or that follows white space containing at least one new-line
> character~~, and is ended by the next~~ <u>. The last token in the sequence is
> the first</u> new-line character <u>that follows the first token in the
> sequence</u>.<sup>140\)</sup> A new-line character ends the preprocessing
> directive even if it occurs within what would otherwise be an invocation of a
> function-like macro.

---

Comment from WG14 on 2006-03-05:

### Committee Response

TC2 (and specifically [DR 250](issue0250.md)) changed that sentence into a
definition.

### Technical Corrigendum

Change 6.10p2:

> A *preprocessing directive* consists of a sequence of preprocessing tokens
> ~~that begins with~~ <u>that satisfies the following constraints. The first
> token in the sequence is</u> a `#` preprocessing token that (at the start of
> translation phase 4\) is either the first character in the source file
> (optionally after white space containing no new-line characters) or that follows
> white space containing at least one new-line character~~, and is ended by the
> next~~ <u>. The last token in the sequence is the first</u> new-line character
> <u>that follows the first token in the sequence</u>.<sup>140\)</sup> A new-line
> character ends the preprocessing directive even if it occurs within what would
> otherwise be an invocation of a function-like macro.
