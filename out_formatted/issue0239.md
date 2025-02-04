## Issue 0239: Annex F `nexttoward` description is inconsistent with 7.12.11.4. and F.9.8.3

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman (US)  
Date: 2001-02-25  
Reference document: [ISO/IEC WG14 N943](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n943.txt)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_239.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_239.htm)

### Summary

> The description for `nexttoward()` in Annex F should be changed to reference
> `nextafter` to be consistent with 7.12.11.4. and F.9.8.3.

### Details

> Currently, F.9.8.4 has: No additional requirements. From that, one could
> conclude that there is no required underflow or overflow for `nexttoward` by
> annex F. But, F.9.8.3 has two explicit error conditions on `nextafter` and
> 7.12.11.4 says `nexttoward` is similar to `nextafter`. We need to make it clear
> that `nextafter` and `nexttoward` have the same requirements with respect to
> range errors in annex F.

### Suggested Technical Corrigendum

In F.9.8.4 `nexttoward` change:

> No additional requirements.

to

> No additional requirements beyond `nextafter`.

---

Comment from WG14 on 2001-10-16:

### Technical Corrigendum

In F.9.8.4 `nexttoward` change:

> No additional requirements.

to

> No additional requirements beyond those on `nextafter`.
