## Issue 0203: C locale conflict with ISO/IEC 9945-2

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG15, Project Editor (Larry Jones)  
Date: 1999-08-18  
Reference document: [ISO/IEC WG14 N888](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n888.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_203.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_203.htm)

### Summary

In subclause 7.23.3.5p7, the specifications for the `strftime %c`, `%p`, and`%x`
conversion specifiers in the C locale conflict with the specifications in
ISO/IEC 9945-2 for the POSIX locale.  As the POSIX and C locales have always
been intended to be compatible, we strongly suggest changing these
specifications to match the pre-existing POSIX specifications.

### Suggested Correction

In subclause 7.23.3.5, paragraph 7, page 345, change the definitions of `%c`,
`%p`, and `%x` to:

> `%c`
>
> > equivalent to "`%a %b %e %T %Y`".
>
> `%p`
>
> > one of "`AM`" or "`PM`".
>
> `%x`
>
> > equivalent to "`%m/%d/%y`".

---

Comment from WG14 on 2000-04-18:

### Committee Response

Changes were incorporated into the Standard just before printing. This was
considered an editorial change by the Committee.
