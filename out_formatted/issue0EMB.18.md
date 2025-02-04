## Issue 0EMB.18: \[Embedded C 2004 DR#18]

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-11-15  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: In 6.5, the first sentence of the replacement text for the description
section of 7.8a.4.6 lists a number of functions. The second sentence of the same
paragraph has a similar list of functions that should be in the same order as in
the first sentence, but which is not.

Solution: Reorder the list in the second sentence.

Change: Change in 6.5 (detailed changes for the Basic I/O Hardware Addressing)
the second sentence of the description section in 7.8a.4.6 to start with: ' The
functions are equivalent to ioand, ioor, ioxor, ioandl, ioorl, and ioxorl,
respectively, ...'.
