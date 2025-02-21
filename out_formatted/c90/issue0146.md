## Issue 0146: Does the constraint of 6.1.2 serve a purpose?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Cross-references: [0017.39](../c90/issue0017.39.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_146.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_146.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 030: Nugatory constraint

*\[BSI characterize this issue as minor.\]*

The constraint of 6.1.2 serves no purpose. Subclause 6.1.2 states in part:

**Constraints**

In translation phases 7 and 8, an identifier shall not consist of the same
sequence of characters as a keyword.

**Semantics**

... When preprocessing tokens are converted to tokens during translation phase
7, if a preprocessing token could be converted to either a keyword or an
identifier, it is converted to a keyword.

Given the latter text \[added in Technical Corrigendum 1, reference [DR 017
Q39](../c90/issue0017.39.md)\], the constraint can never be violated.

### Suggested Technical Corrigendum:

Delete the constraint in subclause 6.1.2.

---

Comment from WG14 on 1997-09-23:

### Suggested Future Change

Delete the constraint in subclause 6.1.2.
