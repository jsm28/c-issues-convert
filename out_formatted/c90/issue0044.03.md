## Issue 0044.03: Does expanding `offsetof` result in a non-strictly conforming program?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Steve M. Hoxey, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-010  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_044.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_044.html)

Assuming (b) is the correct interpretation of Question 1, if a particular
implementation expands `offsetof` into an expression which contains operands
and/or operators which result in a violation of the definition of “integral
constant expression” from subclause 6.4, page 55, lines 17-21, does this
situation constitute:

a. a constraint violation since the expansion presented for further translation
is not an “integer constant expression?”

or

b. undefined behavior since the definition of “integral constant expression”
appears in a “shall” requirement in the semantic description of subclause 6.4
**Constant expressions**?

---

Comment from WG14 on 1997-09-23:

### Response

The response to Question 1 makes this a moot question.
