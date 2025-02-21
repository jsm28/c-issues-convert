## Issue 0414: Typos in 6.27 Threads `<threads.h>`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Tom Plum  
Date: 2012-03-20  
Reference document: [N1614](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1614.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Cross-references: [0469](../c11c17/issue0469.md), [0493](../c11c17/issue0493.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

In 7.26.1 paragraph 5

> The enumeration constants are
>
> > ```c
> > mtx_plain
> > ```
>
> which is passed to `mtx_init` to create a mutex object that supports neither
> timeout nor test and return;

the "test and return" is referring to `try_lock`, `try_lock` is not optional,
therefore the "test and return" should be removed.   

In 7.26.4.2 paragraph 2

> The `mtx_init` function creates a mutex object with properties indicated by
> `type`,   
> which must have one of the six values:  
> `mtx_plain` for a simple non-recursive mutex,  
> `mtx_timed` for a non-recursive mutex that supports timeout,  
> `mtx_plain | mtx_recursive` for a simple recursive mutex, or   
> `mtx_timed | mtx_recursive` for a recursive mutex that supports timeout.

There are not **six** values listed, "six" should be changed to "these".

### Suggested Technical Corrigendum

Change 7.26.1 paragraph 5 to

> The enumeration constants are
>
> > ```c
> > mtx_plain
> > ```
>
> which is passed to `mtx_init` to create a mutex object that does not support
> timeout;

Change 7.26.4.2 paragraph 2 to

> The `mtx_init` function creates a mutex object with properties indicated by
> `type`,   
> which must have one of these values:

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Committee Discussion

Adopt the Suggested Technical Corregendum as proposed.

### Proposed Technical Corrigendum

Change 7.26.1 paragraph 5 to

> The enumeration constants are
>
> > ```c
> > mtx_plain
> > ```
>
> which is passed to `mtx_init` to create a mutex object that does not support
> timeout;

Change 7.26.4.2 paragraph 2 to

> The `mtx_init` function creates a mutex object with properties indicated by
> `type`,   
> which must have one of the these values:
