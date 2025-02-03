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
