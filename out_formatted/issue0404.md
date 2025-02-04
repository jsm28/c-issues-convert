## Issue 0404: joke fragment remains in a footnote

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 seems to have inherited part of a joke from C\+\+, which ought to be removed
or made whole and annotated as such. Originally, C\+\+0x had the footnotes:

> "Atomic objects are neither active nor radioactive" and "Among other
> implications, atomic variables shall not decay".

The first is pretty clearly a joke, but it's not obvious that the second doesn't
have some technical meaning, and that is the one that remains in C11 in
7.17.3p13.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee discussion

> * It is not clear that rewording will make the footnote useful.

Feb 2012

### Proposed Technical Corrigendum

> In 7.17.3 Paragraph 13, remove footnote 256\.
