## Issue 0017.16: Are subarrays of arrays distinct objects?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Pointer to multidimensional array

Given the declaration:

```c
char a[3][4], (*p)[4]=a[1];
```

Does the behavior become undefined when:

1. `p` no longer points within the slice of the array, or
2. `p` no longer points within the object `a`?

This case should be explicitly stated.

Arguments for/against:

The standard refers to a pointed-to object. There does not appear to be any
concept of a slice of an array being an independent object.

---

Comment from WG14 on 1997-09-23:

### Response

For an array of arrays, the permitted pointer arithmetic in subclause 6.3.6,
page 47, lines 12-40 is to be understood by interpreting the use of the word
“object” as denoting the specific object determined directly by the pointer's
type and value, *not* other objects related to that one by contiguity.
Therefore, if an expression exceeds these permissions, the behavior is
undefined. For example, the following code has undefined behavior:

```c
int a[4][5];

 a[1][7] = 0;    /* undefined */
```

Some conforming implementations may choose to diagnose an “array bounds
violation,” while others may choose to interpret such attempted accesses
successfully with the “obvious” extended semantics.

### Correction

***Add to subclause G.2, page 201:***

\- An array subscript is out of range, even if an object is apparently
accessible with the given subscript (as in the lvalue expression `a[1][7]` given
the declaration `int a[4][5]`) (6.3.6).
