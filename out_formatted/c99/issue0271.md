## Issue 0271: lacuna in `iswctype` and `towctrans`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_271.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_271.htm)

### Problem

Consider the calls:

```c
   iswctype (c, wctype (property))
    towctrans (c, wctrans (property))
```

where property is not valid in the current locale. The `wctype` and `wctrans`
functions return zero, but the behaviour of `iswctype` and `towctrans` is not
specified.

I believe it would be useful \- and considered natural \- for them to return 0
("`c` does not have this property") and `c` ("`c` is unaffected by this
mapping") respectively.

### Suggested Technical Corrigendum

Append to 7.25.2.2.1#4:

> If `desc` is zero, the `iswctype` function returns zero (false).

Append to 7.25.3.2.1#4:

> If `desc` is zero, the `towctrans` function returns the value of `wc`.

---

Comment from WG14 on 2002-05-15:

### Committee Response

Since no behavior is specified when `desc` is zero, for either `iswctype()` or
`towctrans()`, the behavior is undefined. We do not believe it would be
appropriate to add new requirements here.

### Committee Discussion

The Committee believes this should be considered for a future revision of the
Standard.
