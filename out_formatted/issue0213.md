## Issue 0213: Lacuna in `mbrtowc`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather  
Date: 1999-10-20  
Reference document: [ISO/IEC WG14 N900](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n900.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_213.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_213.htm)

### Summary

The description of the result of `mbrtowc` uses the term "positive" to
distinguish one case from others. Unfortunately some of the other cases are also
positive, because they are negative numbers cast to the (unsigned) type
`size_t`.

The actual return value in this case is always between 1 and the value of the
parameter `n` (inclusive): positive if the next *n* or fewer bytes complete a
valid multibyte character (which is the value stored); the value returned is the
number of bytes that complete the multibyte character.

---

Comment from WG14 on 2000-11-02:

### Technical Corrigendum

In 7.24.6.3.2 paragraph 4, change the label of the case "positive" to "between 1
and `n` inclusive".
