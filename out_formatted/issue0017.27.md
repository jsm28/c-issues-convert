## Issue 0017.27: Does the `#` flag alter zero stripping of `%g` in `fprintf`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Cross-references: [0040.09](issue0040.09.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

`g` conversions

Subclause 7.9.6.1 says on page 132, lines 42: “For `g` and `G` conversions,
trailing zeros will *not* be removed ...,” whereas on page 133, lines 37-38 it
says: “Trailing zeros are removed ...”

It has been suggested that the italics on page 132, lines 42 gives this rule
precedence. I don't mind which rule wins as long as the text says so. Do we add
text to describe the italics rule or change the conflicting lines?

---

Comment from WG14 on 1997-09-23:

### Response

In the collision between the description of the `#` flag and the `g` and `G`
conversion specifiers to `fprintf,` which takes precedence?

The `#` flag takes precedence. Subclause 7.9.6.1, page 132, line 1 says, “Zero
or more *flags* (in any order) ... modify the meaning of the conversion
specification.”
