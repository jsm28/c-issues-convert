## Issue 0017.04: Do numeric escape sequences map from source to execution character sets?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Mapping of escape sequences

Refer to subclause 6.1.3.4, page 29, line 12 and line 16\. Are these values the
values in the source or execution character set?

When subclause 6.1.3.4, page 29, line 24 says: “The value of an ...,” is this
“value” the value in the source character set of the escape sequence or the
value of the mapped escape sequence? I would have said that the “value” is the
value in the execution environment since in the source environment `\x123` is
part of a token.

It might be argued that characters in the source character set do not have
values and thus no misinterpretation of “value” can occur. Subclause 5.2.1, page
10, lines 25-26 refer to the value of a character in the source basic character
set.

---

Comment from WG14 on 1997-09-23:

### Response

The values of octal or hexadecimal escape sequences are well defined and not
mapped. For instance, the value of the constant `'\x12'` is always 18, while the
value of the constant `'\34'` is always 28\.

The mapping described in subclause 6.1.3.4 on page 28, lines 35-39 only applies
to members of the source character set, of which octal and hexadecimal escape
sequences clearly are not members.
