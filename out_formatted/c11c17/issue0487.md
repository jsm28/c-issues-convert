## Issue 0487: `timespec` vs. `tm`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman  
Date: 2015-11-22  
Reference document: [N1987](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1987.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The standard appears to be inconsistent on `timespec` structure versus `tm`
structure with respect to normative requirements. Both have: The semantics of
the members and their normal ranges are expressed in the comments. But, for
`timespec`, it appears as a footnote, while for `tm`, it appears in the body of
the standard.

### Suggested Technical Corrigendum

Move that sentence from footnote 317 in 7.27.1#4 to be in paragraph 4

---

Comment from WG14 on 2017-11-03:

Apr 2016 meeting

### Committee Discussion

> The committee spent considerable time understanding the change requested and
> accepted it as The Proposed Technical Corrigendum below.

### Proposed Technical Corrigendum

Change §7.27.1p4 sentence 2 and footnote 317 from:

> The `timespec` structure shall contain at least the following members, in any
> order.<sup>317\)</sup>
>
> <sup>317\)</sup> The `tv_sec` member is a linear count of seconds and may not
> have the normal semantics of a `time_t`. The semantics of the members and their
> normal ranges are expressed in the comments.

to:

> The `timespec` structure shall contain at least the following members, in any
> order, where the semantics of the members and their normal ranges are expressed
> in the comments.
>
> <sup>317\)</sup> The `tv_sec` member is a linear count of seconds and may not
> have the normal semantics of a `time_t`.
