## Issue 0219: Effective types

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 2000-04-04  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_219.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_219.htm)

### Summary

6.5 reads:

> \[#6\] \[...\] If a value is copied into an object having no declared type using
> `memcpy` or `memmove`, or is copied as an array of character type, then the
> effective type of the modified object for that access and for subsequent
> accesses that do not modify the value is the effective type of the object from
> which the value is copied, if it has one. For all other accesses to an object
> having no declared type, the effective type of the object is simply the type of
> the lvalue used for the access.

Now consider the code extract:

```c
 struct s { char c; int i; long l; double d; } s = { 1, 2, 3, 4 };
     size_t len1 = sizeof (int);
     size_t len2 = offsetof (s, d) - offsetof (s, i));
     void *p1 = malloc (len1); assert (p1);
     void *p2 = malloc (len2); assert (p2);
     memcpy (p1, (char *)&s + offsetof (s, i), len1);
     memcpy (p2, (char *)&s + offsetof (s, i), len2);
```

What are the effective types of `p1` and `p2` ? The cited text would imply that
they are both `struct s`, even though this is patently nonsense.

---

Comment from WG14 on 2006-04-04:

### Committee Discussion

Consider:

> 1\. `struct s { char c; int i; long l; double d; } s = { 1, 2, 3, 4 };`  
> 2\. `size_t len1 = sizeof (int);`  
> 3\. `size_t len2 = offsetof (s, d) - offsetof (s, i));`  
> 4\. `void *p1 = malloc (len1); assert (p1);`  
> 5\. `void *p2 = malloc (len2); assert (p2);`  
> 6\. `memcpy (p1, (char *)&s + offsetof (s, i), len1);`  
> 7\. `memcpy (p2, (char *)&s + offsetof (s, i), len2);`

In lines 6 and 7, the type of the source object in the `memcpy` is an array of
`char` because the dereference of `(char *)&s + ...` is a `char`. This is
inferred by:

> \- "`(`*some\_type*`*)x`" has the type "pointer to *some\_type*"  
> \- the dereference of "pointer to *some\_type*" has the type "*some\_type*"

In other words, "`(char *)&s + offsetof (s,i)`" has type "pointer to `char`" and
its dereference has type "`char`", i.e., the type of the source object. In the
following examples:

> 8\. `memcpy (p1, &s.i, len1);`  
> 9\. `memcpy (p1, (char *) &s.i, len1);`  
> 10\. `memcpy (p1, (float *) &s.i, len1);`

the source types are, respectively, array of `int`, `char`, and `float`.

In lines 6 and 7, the effective type of the source arguments to `memcpy` is an
array of `char`, based on the following sentence from 6.5P6:

> "For all other accesses to an object having no declared type, the effective type
> of the object is simply the type of the lvalue used for the access."

Based on the following sentence again from 6.5P6:

> "If a value is copied into an object having no declared type using `memcpy` or
> `memmove`, or is copied as an array of character type, then the effective type
> of the modified object for that access and for subsequent accesses that do not
> modify the value is the effective type of the object from which the value is
> copied, if it has one."

The object being copied into has no declared type (because it was an allocated
object), thus "the effective type of the modified object for that access ... is
the effective type of the object from which the value is copied ...". The object
from which it was copied is array of `char`. The effective type for `p1` and
`p2` in lines 6 and 7 is: array of `char`.

### Committee Response

The effective types of `*p1` and `*p2` are not `struct S` because not all of the
bytes of `struct S` are copied.

However, the memcpy calls do copy pieces of `s`. Those pieces contain objects
with declared types.

`memcpy (p1, (char *)&s + offsetof (s, i), len1);` copies all of the bytes of
`s.i` to an alignment suitable for an object of type int. The effective type of
the resulting copy can be treated as having effective type `int`.

`memcpy (p2, (char *)&s + offsetof (s, i), len2);` copies all of the bytes of
`s.i` and `s.l`. The memcpy also might copy bytes corresponding to padding
before and after `s.l`.

The `int` object from `s.i` is copied to an alignment suitable for an object of
type `int`. The object starting at `*p2` extending for `sizeof (int)` bytes can
be treated as having effective type `int`.

Because of alignment requirements and padding rules that vary from
implementation to implementation, the long object from `s.l` might or might not
be copied to an alignment suitable for an object of type long. If it is aligned
properly, the object starting at `*((char *) p2 + (offsetof (s, l) - offsetof
(s, i)))` extending for `sizeof (long)` bytes can be treated as having effective
type long.

The objects resulting from the calls to memcpy may also be accessed by other
types (primarily given by Subclause 6.5 paragraph 7).
