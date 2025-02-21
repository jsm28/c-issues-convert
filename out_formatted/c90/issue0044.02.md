## Issue 0044.02: Must the expansion of a standard header be a strictly conforming program?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Steve M. Hoxey, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-010  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_044.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_044.html)

Subclause 5.1.1.1, page 5, lines 11-20 define a “translation unit” to be
equivalent to the sequence of preprocessing tokens and white-space characters
which exists at the end of translation phase 4 (subclause 5.1.1.2). Later in
translation phases 5, 6, 7, these preprocessing tokens are converted to tokens
and syntactically and semantically analyzed and translated.

Therefore, must a conforming implementation provide strictly conforming
expansions of macros defined by the standard headers, such that any use of the
resulting preprocessing token sequence, and ultimately the token sequence,
beyond phase 4 does not alter the behavior of an otherwise strictly conforming
program? See also clause 4 **Compliance**, page 4, lines 24-26.

---

Comment from WG14 on 1997-09-23:

### Response

A conforming implementation need not provide strictly conforming expansion of
macros defined by the standard headers.
