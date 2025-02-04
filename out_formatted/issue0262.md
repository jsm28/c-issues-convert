## Issue 0262: maximum size of bit fields

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Cross-references: [0335](issue0335.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_262.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_262.htm)

### Problem

6.7.2.1#3 reads, in part:

> \[#3] The expression that specifies the width of a bit-field shall be an integer
> constant expression that has nonnegative value that shall not exceed the number
> of bits in an object of the type that is specified if the colon and expression
> are omitted.

Is "the number of bits of the type ..." the width or is it the number of bits in
the object representation ?

Since it might not be practical to make use of padding bits in such an object,
the former would be more sensible.

### Suggested Technical Corrigendum

Change the cited text to read:

> \[#3] The expression that specifies the width of a bit-field shall be an integer
> constant expression that has nonnegative value that shall not exceed **the width
> of an object** of the type that is specified if the colon and expression are
> omitted.

(bold type shows the changed words)

---

Comment from WG14 on 2002-03-07:

### Technical Corrigendum

Change 6.7.2.1#3 to read:

> The expression that specifies the width of a bit-field shall be an integer
> constant expression that has nonnegative value that shall not exceed the width
> of an object of the type that is specified if the colon and expression are
> omitted.
