## Issue 0041: Are `'A'` through `'Z'` always `isupper` in all locales?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Andrew Josey, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-076  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_041.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_041.html)

Does the description in subclause 7.3.1 imply that the characters defined in
subclause 5.2.1 are always classified as implied by subclause 5.2.1 regardless
of the locale specified?

In particular, do the characters `'a'` through `'z'` and `'A'` through `'Z'`
have to be classified as “lower case and “upper case,” respectively, in every
locale?

The specific lines needing interpretation are lines 20-21 in subclause 7.3.1.6,
page 103, and lines 16-17 in subclause 7.3.1.10, page 104\. The word “or” can be
interpreted to require a superset of the characters specified as lower/upper
case in subclause 5.2.1 or to allow an implementation-defined set of characters
(which might contain none of the subclause 5.2.1 designated lower/upper case
characters).

---

Comment from WG14 on 1997-09-23:

### Response

Does the description in subclause 7.3.1 imply that the characters defined in
subclause 5.2.1 are always classified as implied by subclause 5.2.1 regardless
of the locale specified?

Answer: By subclause 7.3.1.6 **The `islower` function** and subclause 7.3.1.10
**The `isupper` function** which refer to lower- and upper-case letters,
respectively, and by subclause 5.2.1: “basic source and basic execution
character sets shall have at least ... upper-case letters of the English
alphabet” (with example) ... “lower-case letters of the English alphabet” (with
example), and by subclause 5.2.1.2 “The single-byte characters defined in
subclause 5.2.1 shall be present,” which refers to multibyte characters,
therefore, yes, the characters defined in subclause 5.2.1 are always classified
as implied by subclause 5.2.1 regardless of the locale specified.

Do the characters `'a'` through `'z'`, and `'A'` through `'Z'`, have to be
classified as “lower case” and “upper case,” respectively, in every locale?

Answer: Yes, the characters `'a'` through `'z'`, and `'A'` through `'Z'`, have
to be classified as “lower case” and “upper case,” respectively, in every locale
(following the citations above).
