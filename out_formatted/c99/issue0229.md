## Issue 0229: `localeconv() *_sep_by_space` table entries issues

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Project Editor (Larry Jones)  
Date: 2000-04-10  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_229.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_229.htm)

### Summary

The `int_n_sep_by_space` and `int_p_sep_by_space` table entries in 7.11.1.1#10
are incorrect.

The `n_sep_by_space` entry for the Netherlands should be a 2\.

---

Comment from WG14 on 2001-09-18:

### Technical Corrigendum

In 7.11.2.1 paragraph 9:

* remove the word "the" from the first sentence (to indicate that the example is not definitive)
* replace the names of the countries Finland, Italy, Netherlands and Switzerland with Country1, Country2, Country3 and Country4 respectively.

In 7.11.2.1 paragraph 10:

* replace the word "are" with the words "could be" in the first sentence
* replace the names of the countries Finland, Italy, Netherlands and Switzerland with Country1, Country2, Country3 and Country4 respectively
* change the `n_sep_by_space` table entry for Country3 from `1` to `2`
* change all the `int_p_sep_by_space` table entries from `0` to `1`
* Change the `int_n_sep_by_space` table entries for Country1 and Country3 from `0` to `2` and for Country2 and Country3 from `0` to `1`.
