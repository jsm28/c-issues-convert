## Issue 0401: "happens before" cannot be cyclic

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C\+\+11 forbids "happens before" from being cyclic, but this change has not made
its way into C11. In order to fix this, the following sentence (taken from C\+\+
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf),
1.10p12) should be added to 5.1.2.4p18:

> The implementation shall ensure that no program execution demonstrates a cycle
> in the "happens before" relation.  
>
> NOTE: This cycle would otherwise be possible only through the use of consume
> operations.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee Discussion

> * Seems as if C\+\+ made this change at the last minute and WG 14 had already voted a document for ballot.
> * There seems to be consensus to make a change along this line.

Feb 2012 meeting

### Proposed Technical Corrigendum

> Add to 5.1.2.4p18:
>
> > The implementation shall ensure that no program execution demonstrates a cycle
> > in the "happens before" relation.  
> >
> > NOTE: This cycle would otherwise be possible only through the use of consume
> > operations.
