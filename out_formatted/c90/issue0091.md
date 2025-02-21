## Issue 0091: Does a locale with multibye characters conform?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_091.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_091.html)

Item 28 \- multibyte encodings

Does a locale with the following encoding of multibyte characters conform to the
C Standard?

The 99 characters of the basic execution character set have codes 1 to 99, in
the order mentioned in subclause 5.2.1.1 (so `'A' == 1`, `'a' == 27`, `'0' ==
53`, `'!' == 63`, `'\n' == 99`).

The extended execution character set consists of 16,256 (127 `*` 128\) two-byte
characters. For each two-byte character, the first byte is between 1 and 127
inclusive, and the second byte is between 128 and 255 inclusive.

Note that any sequence of bytes can unambiguously be broken into multibyte
characters, but the basic characters are prefixes of other characters.

---

Comment from WG14 on 1997-09-23:

### Response

The hypothetical locale described does conform to the C Standard because the
specified encoding does not violate the requirements imposed on multibyte
characters by subclause 5.2.1.2. No additional requirements are needed.
