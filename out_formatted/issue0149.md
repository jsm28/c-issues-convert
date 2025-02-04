## Issue 0149: Is the term *variable* defiend?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_149.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_149.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 033: The term "variable"

*\[BSI characterize this issue as minor.]*

The term "variable" is used in subclause 7.7.1.1, but is never defined in the C
Standard.

### Suggested Technical Corrigendum:

In subclause 7.7.1.1, change:

... or refers to any object with static storage duration other than by assigning
a value to a static storage duration variable of type `volatile sig_atomic_t`.

to:

... or refers to any object with static storage duration other than by assigning
a value to an object declared as `volatile sig_atomic_t`.

---

Comment from WG14 on 1997-09-23:

### Response

The next revision of the C Standard will use the term "object" instead of
"variable" uniformly.
