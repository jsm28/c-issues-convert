## Issue 0278: lacuna in character encodings

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_278.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_278.htm)

### Problem

Defect Report 091 discussed a multibyte character encoding where some
single-byte characters are proper prefixes of two-byte characters. For example,
single-byte characters have codes 1 to 127 while two-byte characters consist of
such a code followed by a code from 128 to 255\. At the time WG14 stated that
such an encoding was legitimate.

Now 5.2.1.2 states, inter alia:

> * The basic character set shall be present and each character shall be encoded as a single byte.
> * A byte with all bits zero shall be interpreted as a null character independent of shift state.
> * A byte with all bits zero shall not occur in the second or subsequent bytes of a multibyte character.

Nothing in this wording forbids a two-byte character from having a first byte
that is zero. By the logic of DR091, just as the sequences 0x12 and 0x12 0x9A
are both valid, but different, characters, so would the sequences 0x00 and 0x00
0x9A; the first would be the null character and the second would be something
else. Note that there are no shift states, and so the wording "independent of
shift state" is irrelevant.

This interpretation is undesirable for obvious reasons, and so it ought to be
outlawed.

### Suggested Technical Corrigendum

Replace the current last two bullets with a single one:

> * A byte with all bits zero shall be interpreted as a null character independent of shift state. Such a byte shall not occur as part of any other multibyte character.

---

Comment from WG14 on 2002-03-07:

### Technical Corrigendum

Replace the current last two bullets in 5.2.1.2 with a single bullet:

> * A byte with all bits zero shall be interpreted as a null character independent of shift state. Such a byte shall not occur as part of any other multibyte character.
