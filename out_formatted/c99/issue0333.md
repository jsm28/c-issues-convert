## Issue 0333: Missing Predefined Macro Name

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Austin Group, Nick Stoughton (US)  
Date: 2006-10-24  
Reference document: [DR\_321](../c99/issue0321.md),  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Cross-references: [0321](../c99/issue0321.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_333.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_333.htm)

### Summary

Defect report [DR\_321](../c99/issue0321.md) introduced a new pre-defined macro name,
\_\_STDC\_MB\_MIGHT\_NEQ\_WC\_\_ that is conditionally defined by the
implementation. However, this new macro is not in the list of macros that may be
conditionally defined by the implementation in 6.10.8, para 2\.

### Suggested Technical Corrigendum

Add, in proper alphabetic order in the list in 6.10.8 para 2:

> `__STDC_MB_MIGHT_NEQ_WC__` The integer constant `1`, intended to indicate that
> there might be some character *`x`* in the basic character set, such that
> `'`*`x`*`'` need not be equal to `L'`*`x`*`'`.

---

Comment from WG14 on 2007-09-06:

### Technical Corrigendum

Add, in proper alphabetic order in the list in 6.10.8 paragraph 2:

> `__STDC_MB_MIGHT_NEQ_WC__` The integer constant `1`, intended to indicate that,
> in the encoding for `wchar_t`, a member of the basic character set need not have
> a code value equal to its value when used as the lone character in an integer
> character constant.
