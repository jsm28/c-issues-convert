## Issue 0225: `strtod`, `strtof` and `strtold` expected form of the subject sequence

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Bill Plauger (US)  
Date: 2000-04-10  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_225.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_225.htm)

### Summary

In `<stdlib.h>`, functions `strtod`, `strtof`, and `strtold` should permit an
implementation to recognize either `inf` or `infinity`, and either `nan` or
`nan(`*n-char-sequence<sub>opt</sub>* `)`, not just one of each.

### Suggested Technical Corrigendum

In 7.20.1.3 replace:

> * one of `INF` or `INFINITY`, ignoring case
> * one of `NAN` or `NAN(`*n-char-sequence<sub>opt</sub>* `)`, ignoring case in the `NAN` part, where:

with:

> * either `INF` not followed by `I`, or `INFINITY`, ignoring case
> * either `NAN` not followed by a left parenthesis, or `NAN(`*n-char-sequence<sub>opt</sub>* `)`, ignoring case in the `NAN` part, where:

---

Comment from WG14 on 2001-09-18:

### Committee Discussion (for history only)

For the functions `strtod`, `strtof` and `strtold`, should the implementation
allow `INFI` to work as `INF` and leave the pointer at the next `I`, or should
it reject a sequence such as `INFINF` as an invalid sequence, that failed at the
second `F`.

The issue concerns what degree of pushback is necessary. But these are string
functions, not input functions, so they do not need push back. Furthermore,
7.19.6.2¶9 and the associated footnote, clearly indicates that there is no
requirement for the `strto*` functions to retain symmetric functionality with
fscanf, indeed that is noted as being explicitly different.

It was noted that while symmetry with `scanf` may have some attractiveness, that
the `strto*` functions cannot report that the input string did not match (no
error mechanism exists) and that it would just return ZERO. With scanf the error
is reported.

However, the issue in the DR really reduces to the use of the term *one of* on
the bullets in 7.20.1.3¶3. The discussion indicated we were in agreement with
Clive Feather's comments on this DR.

It was also observed that these changes also apply to the `wcsto*` functions in
7.24.4.1

---

Comment from WG14 on 2001-09-18:

### Technical Corrigendum

Remove the words 'one of' from the third and fourth bullets of 7.20.1.3¶3.

Remove the words 'one of' from the third and fourth bullets of 7.24.4.1¶3.
