## Issue 0EMB.01: Name conflict for strtok

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [188](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/188), [189](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/189), [190](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/190), [191](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/191), [192](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/192), [194](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/194), [196](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/196), [198](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/198), [200](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/200), [201](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/201), [203](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/203), [204](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/204), [207](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/207)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: by selecting the letter 'k' as suffix for the accum type, the the
function to convert a string to an accum type gets the name strtok; this name is
already in use in the C standard. Possible solutions:

* use a different letter
  + 'q' as proposed originally, conflicts with quadruple precision format
  + 'y' the only reasonable choice of the 'free' letters (others are 'b', 'm', 'v' and 'w');
* change the names of all "strto" functions to "strto\_"; that is: "strtok" becomes "strto\_k", "strtoht" becomes "strto\_hr", etc. Easy to do but a little bit inconsistent with the C library;
* use the letter 'q' only for the functionnames, leave the 'k' everywhere else.

---

Comment from WG14 on 2004-11-15:

Problem: Using the suffix 'k' to stand for 'accum' with the base 'strto' for
numeric conversion functions yields a conflict with the existing C function
'strtok'.

Solution: Rename the fixed-point numeric conversion functions to have a base of
'strtofx' instead of 'strto'. The new names will be 'strtofxhr', 'strtofxr',
'strtofxlr', 'strtofxhk', 'strtofxk', 'strtofxlk', 'strtofxuhr', 'strtofxur',
'strtofxulr', 'strtofxuhk', 'strtofxuk', and 'strtofxulk'.

Affected sections in TR18037: 4.1.7 (2 times), 4.1.9, replacement text for
7.18a.6.8 (many times), replacement text for 7.19.6.2 para 12\.
