## Issue 0017.39: Are header names tokens outside include directives?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0040.04](issue0040.04.md), [0146](issue0146.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Header name tokenization

There is an inconsistency between subclause 6.1.7, page 33, line 8 and the
description of the creation of header name preprocessing tokens.

The “shall” on page 32, line 33 does not limit the creation of header name
preprocessing tokens to within `#include` directives. It simply states that they
would cause a constraint error in this context.

Subclause 6.1.7, page 33, line 8 should read {`0x3`}{`<1/a.h>`}{`1e2`}, or extra
text needs to be added to subclause 6.1.7.

I have not met anybody who expects `if (a<b || c>d)` to parse as {`if`} {`(`}
{`a`} {`<b || c>`} {`d`} {`)`}.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.1, page 18 (Semantics):***

A header name preprocessing token is only recognized within a `#include`
preprocessing directive, and within such a directive, a sequence of characters
that could be either a header name or a string literal is recognized as the
former.

***Add to subclause 6.1.2, page 20 (Semantics):***

When preprocessing tokens are converted to tokens during translation phase 7, if
a preprocessing token could be converted to either a keyword or an identifier,
it is converted to a keyword.

***In subclause 6.1.7, page 32, lines 32-34, delete:***

**Constraint**

Header name preprocessing tokens shall only appear within a `#include`
preprocessing directive.

***Add to subclause 6.1.7, page 32 (Semantics):***

A header name preprocessing token is recognized only within a `#include`
preprocessing directive.
