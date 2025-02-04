## Issue 0310: Add non-corner case example of trigraphs

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG21, WG21  
Date: 2004-10-26  
Reference document: [ISO/IEC WG14 N1068](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1068.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_310.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_310.htm)

### Summary

The existing corner case example is a good one. For some reason it was removed
from C\+\+, and I will propose that it be restored. But in general there are
very few cases where the **only** example presented is a corner case. If
trigraphs make any sense at all, then perhaps it would make sense to present a
more realistic example (possibly even more realistic than this example).

### Suggested Technical Corrigendum

Add new example paragraph before 5.2.1.1p2:

> EXAMPLE 1:
>
> > ```c
> > ??=define arraycheck(a,b) a??(b??) ??!??! b??(a??)
> > ```
>
> becomes
>
> > ```c
> > #define arraycheck(a,b) a[b] || b[a]
> > ```

---

Comment from WG14 on 2006-03-05:

### Technical Corrigendum

Add new example paragraph before 5.2.1.1p2:

> EXAMPLE 1:
>
> > ```c
> > ??=define arraycheck(a,b) a??(b??) ??!??! b??(a??)
> > ```
>
> becomes
>
> > ```c
> > #define arraycheck(a,b) a[b] || b[a]
> > ```
