## Issue 0246: completion of declarators

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_246.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_246.htm)

### Problem

6.2.1#7 reads in part:

> Any other identifier has scope that begins just after the completion of its
> declarator.

However, nothing says when a declarator is completed. While it seems obvious to
experienced people that this means the syntactic end of the declarator, the term
"complete" has other meanings when discussing declarations and objects, and
therefore it's a bad term to use.

### Suggested Technical Corrigendum

Change the quoted text to:

> Any other identifier has scope that begins just after the end of the full
> declarator it appears in.

---

Comment from WG14 on 2002-03-06:

### Committee Response

The suggested words don't appear to be an improvement; the current phrasing is
clear enough.
