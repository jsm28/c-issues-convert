## Issue 0415: Missing divide by zero entry in Annex J.2

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Seacord (PL22.11)  
Date: 2012-06-02  
Reference document: [N1617](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1617.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The undefined behavior defined in paragraph 6 of 6.5.5 is missing in J.2 and
should be added.

### Suggested Technical Corrigendum

Add a bullet with the following text to J.2 after bullet 45

> If the quotient `a/b` is not representable, the behavior of both `a/b` and `a%b`
> is undefined (6.5.5).

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Committee Discussion

Adopt the Suggested Technical Corregendum as proposed.

### Proposed Technical Corrigendum

Add a bullet with the following text to J.2 after bullet 45

> If the quotient `a/b` is not representable, the behavior of both `a/b` and `a%b`
> is undefined (6.5.5).
