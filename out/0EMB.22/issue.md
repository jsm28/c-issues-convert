Problem: the bitwise integer to fixed-point functions (in 7.18a.6.6) do not use
the int\_*fx*\_t and uint\_*fx*\_t integer types; the text in 4.1.7.5 is already
correct.

Solution:

* change the Synopsis section of 7.18a.6.6 to read:
  ```c
  #include <stdfix.h>
  short fract hrbits(int_hr_t n);
  fract rbits(int_r_t n);
  long fract lrbits(int_lr_t n);
  short accum hkbits(int_hk_t n);
  accum kbits(int_k_t n);
  long accum lkbits(int_lk_t n);
  unsigned short fract uhrbits(uint_uhr_t n);
  unsigned fract urbits(uint_ur_t n);
  unsigned long fract ulrbits(uint_ulr_t n);
  unsigned short accum uhkbits(uint_uhk_t n);
  unsigned accum ukbits(uint_uk_t n);
  unsigned long accum ulkbits(uint_ulk_t n);
  ```
* remove from the of 7.18a.2 the words 'as return types'
* change in 7.18a.2 the first sentence after the list to read:
  
  The integer types **int\_*fx*\_t** and **uint\_*fx*\_t** are the return types of
  the corresponding **bits*fx*** functions and are chosen so that the return value
  can hold all the necessary bits; the ***fx*****bits** functions use these
  integer types as types for their parameters.
