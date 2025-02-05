## Issue 0EMB.19: \[Embedded C 2004 DR#19\]

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2005-03-03  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1096.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1096.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: Sec 7.18a.2 introduces a set of typedefs, and describes a convention
for the return type of bits'*fx*': either int\_*fx*\_t, or uint\_*fx*\_t.

Sec 7.18a.6.5 lists the 12 functions for bits'*fx*', all of which make use of
the form 'int\_*fx*\_t'. According to 7.18a.2 the last six should be of the form
'uint\_*fx*\_t'.

Solution: change the last 6 function prototypes in the Synopsis of 7.18a.6.5 to:

```c
uint_uhr_t bitsuhr(unsigned short fract f);
uint_ur_t bitsur(unsigned fract f);
uint_ulr_t bitsulr(unsigned long fract f);
uint_uhk_t bitsuhk(unsigned short accum f);
uint_uk_t bitsuk(unsigned accum f);
uint_ulk_t bitsulk(unsigned long accum f);
```
