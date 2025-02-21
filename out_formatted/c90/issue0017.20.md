## Issue 0017.20: Is the scope of macro parameters defined in the right place?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Scope of macro parameters

Refer to subclause 6.8.3 on page 89, line 16; the scope of macro parameters
should be defined in the section on scope.

The idea is to enable all references to the scope of names to be under one
heading. This is not really a significant issue.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.1.2 on page 20, line 5, states “Macro names and macro parameters are
not considered further here.” This approach was intentionally adopted to avoid
explicitly having to mention exceptions of using identifiers, for example in the
sections on scope, linkage, name spaces, and storage durations, none of which
applies to macros. The proposed change does *not* clarify the standard and may
even obscure it.
