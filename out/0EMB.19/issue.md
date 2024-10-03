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
