## Issue 0472: Introduction to complex arithmetic in 7.3.1p3 wrong due to CMPLX

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman  
Date: 2015-01-07  
Reference document: [N1902](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1902.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The introduction to complex arithmetic in 7.3.1p3 is wrong on several counts,
all due to CMPLX.

The text in question is:

> Each synopsis specifies a family of functions consisting of a principal function
> with one or more **double complex** parameters and a **double complex** or
> **double** return value; and other functions with the same name but with **f**
> and **l** suffixes which are corresponding functions with **float** and **long
> double** parameters and return values.

The items that are wrong are:

* CMPLX is a macro (not a function).
* CMPLX takes **double** parameters (not **double complex**).
* CMPLX has **F** and **L** suffixes (not **f** and **l**).

### Suggested Technical Corrigendum

---

Comment from WG14 on 2017-11-03:

Apr 2015 meeting

### Committee Discussion

> The following Proposed Technical Corrigendum was presented, discussed, and
> accepted.

### Proposed Technical Corrigendum

In 7.3.1#3, change:

> Each synopsis specifies a family of functions

to

> Each synopsis other than the CMPLX macros specifies a family of functions
>
> (add forward reference to 7.3.9.3)
