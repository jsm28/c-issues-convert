## Issue 0161: Is the wording of subclause 7.13 unclear?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_161.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_161.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 009: Details of reserved symbols

The wording of subclause 7.13 is unclear.

Does the term *any combination* in subclause 7.13 include the empty combination?
In other words, are names like `E2`, `tom`, `LC_X`, and `memo` reserved?

---

Comment from WG14 on 1997-09-23:

### Response

Yes, the term "any combination" does include the empty combination so names such
as those cited are reserved. We believe that having the "any combination"
language in parenthetical remarks rather than as part of the main text makes is
sufficiently clear that it is just the prefix that is important in determining
whether a name is reserved or not.
