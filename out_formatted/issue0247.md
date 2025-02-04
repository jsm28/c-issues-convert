## Issue 0247: are values a form of behaviour ?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_247.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_247.htm)

### Problem

I can see nothing that says or implies that production of an unspecified value
is a form of unspecified behaviour, and similarly for implementation-defined
values. It is therefore arguable that a program is strictly-conforming even if
its output depends on an unspecified value.

### Suggested Technical Corrigendum

Add a new paragraph 4#2a after 4#2:

> \[#2a] An evaluation that makes use of an unspecified or implementation-defined
> value is a form of unspecified or implementation-defined behaviour respectively.

---

Comment from WG14 on 2002-03-06:

### Technical Corrigendum

In section 3.4.4, prepend

> "Use of an unspecified value, or other ..." before "behavior where".
