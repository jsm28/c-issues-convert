## Issue 0264: graphic characters

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_264.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_264.htm)

### Problem

The Standard uses the terms "printing character", "graphic character", and
"nongraphic character". The first is discussed in 5.2.2#1 and defined formally
in 7.4#3:

> \[#3] The term printing character refers to a member of a locale-specific set of
> characters, each of which occupies one printing position on a display device;

A "nongraphic character" is clearly a character which is not a graphic
character, but "graphic character" is nowhere defined. It is used only in
5.2.1#3, which requires "the following 29 graphic characters" to be part of the
basic character sets, while "nongraphic character" is used in 5.2.2#2 and
6.4.4.4#8 when discussing the `\a \b \f \n \r \t` and `\v` escape sequences.

The key questions are:

1. Are the 29 enumerated graphic characters required to be printing characters ?
2. Are `isalnum()` and `isspace()` required to be false for them ?
3. Is `ispunct()` required to be true for them ?

In addition, given that the seven characters corresponding to the escape
sequences above are required to be control characters (see 5.2.1#3):

4. Should "nongraphic character" be replaced by "control character" ?

I believe that the answers should be:

1. yes
2. yes;
3. yes in the C locale, but not otherwise;
4. yes.

However, it is not clear that these answers can be derived from the Standard
(though if (1) and (2) are "yes", (3) must at least be "yes in the C locale").

### Suggested Technical Corrigendum

To address (1): in 5.2.1#3, replace "29 graphic characters" with "29 printing
characters".

To address (4): in 5.2.2#2 and 6.4.4.4#8 replace "nongraphic" with "control".

To address (2): append to 5.2.1#4:

> A *graphical mark character* is one of the 29 other printing characters listed
> above.

in 7.4.1.2#2, insert between the two sentences:

> The `isalpha` function returns false for all graphical mark characters.

and in 7.4.1.10#2, change "characters for which" to "characters which are not
graphical mark characters and for which".

Given the above changes, (3) can be derived from the modified Standard.

---

Comment from WG14 on 2002-03-07:

### Committee Response

The referenced sections in the standard only use the term "non-graphic
character" in the context of backslash-escape sequences, for which the standard
is clear enough, and no changes are needed.
