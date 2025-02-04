## Issue 0417: Annex J not updated with necessary `aligned_alloc` entries

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, John Benito  
Date: 2012-10-22  
Reference document: [N1628](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1628.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The following unspecified behaviors are incomplete in Annex J.1,
`aligned_alloc()` is missing in both entries.

> — The order and contiguity of storage allocated by successive calls to the
> `calloc`, `malloc`, and `realloc` functions (7.22.3).   
>
> — The amount of storage allocated by a successful call to the `calloc`,
> `malloc`, or `realloc` function when 0 bytes was requested (7.22.3).

The following undefined behavior bullet is incomplete in Annex J.2,
`aligned_alloc()` is missing.

> — A non-null pointer returned by a call to the `calloc`, `malloc`, or `realloc`
> function with a zero requested size is used to access an object (7.22.3).

The following implementation-defined behavior bullet is incomplete in Annex
J.3.12, `aligned_alloc()` is missing.

> — Whether the `calloc`, `malloc`, and `realloc` functions return a null pointer
> or a pointer to an allocated object when the size requested is zero (7.22.3).

### Suggested Technical Corrigendum

Change bullet 42 of J.1 to:

> — The order and contiguity of storage allocated by successive calls to the
> `calloc`, `malloc`, `realloc`, and `aligned_alloc` functions (7.22.3).

Change bullet 43 of J.1 to:

> — The amount of storage allocated by a successful call to the `calloc`,
> `malloc`, `realloc`, or `aligned_alloc` function when 0 bytes was requested
> (7.22.3).

Change bullet 166 of J.2 to

> — A non-null pointer returned by a call to the `calloc`, `malloc`, `realloc`, or
> `aligned_alloc` function with a zero requested size is used to access an object
> (7.22.3).

Change bullet 37 of J.3.12 to

> — Whether the `calloc`, `malloc`, `realloc` and `aligned_alloc` functions return
> a null pointer or a pointer to an allocated object when the size requested is
> zero (7.22.3).

---

Comment from WG14 on 2017-11-03:

Oct 2012 meeting

### Committee Discussion

Adopt as proposed the Suggested Technical Corrigendum.

### Proposed Technical Corrigendum

Change bullet 42 of J.1 to:

> — The order and contiguity of storage allocated by successive calls to the
> `calloc`, `malloc`, `realloc`, and `aligned_alloc` functions (7.22.3).

Change bullet 43 of J.1 to:

> — The amount of storage allocated by a successful call to the `calloc`,
> `malloc`, `realloc`, or `aligned_alloc` function when 0 bytes was requested
> (7.22.3).

Change bullet 166 of J.2 to

> — A non-null pointer returned by a call to the `calloc`, `malloc`, `realloc`, or
> `aligned_alloc` function with a zero requested size is used to access an object
> (7.22.3).

Change bullet 37 of J.3.12 to

> — Whether the `calloc`, `malloc`, `realloc` and `aligned_alloc` functions return
> a null pointer or a pointer to an allocated object when the size requested is
> zero (7.22.3).
