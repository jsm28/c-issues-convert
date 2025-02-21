## Issue 0293: Typo in Standard \- `double complex` instead of `complex` in an example

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Tydeman (US)  
Date: 2003-10-24  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_293.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_293.htm)

### Summary

> 6.7.8, paragraph 24, example 1\.
>
> > ```c
> > complex c = 5 + 3 * I
> > ```
>
> should changed to
>
> > ```c
> > double complex c = 5 + 3 * I
> > ```

### Suggested Technical Corrigendum

Change `complex` to `double complex` in the example.

---

Comment from WG14 on 2004-03-01:

### Technical Corrigendum

> 6.7.8, paragraph 24, example 1\.
>
> > ```c
> > complex c = 5 + 3 * I
> > ```
>
> changed to
>
> > ```c
> > double complex c = 5 + 3 * I
> > ```
