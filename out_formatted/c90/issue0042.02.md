## Issue 0042.02: If so, how big is the object defined by `memcpy`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Tom MacDonald, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-001  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_042.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_042.html)

For the purposes of the description of `memcpy`, can a contiguous sequence of
elements within an array be regarded as an object in its own right? If so, are
the objects in the description of `memcpy` the smallest contiguous sequences of
bytes that can be construed as the objects into which the arguments point?

In Example 2:

```c
void f2(void) {
        extern char b[2*N];
        memcpy(b+N, b, N);
        }
```

can each of the first and last half of array `b` be regarded as an object in its
own right, so that the behavior of the call of `memcpy` is defined? (Although
they are not declared as separate objects, each half does seem to satisfy the
definition of object quoted above.) Or is the behavior undefined, since both
arguments point into the same array object `b`?

In Example 3:

```c
void f3(void) {
        void *p = malloc(2*N);  /* Allocate an object. */
        {
        char (*q)[N] = p;       /* The object pointed to by p may
                                                        be interpreted as having type
                                                        (char [2][N]) when referenced
                                                        through q. */
        /* ... */
        memcpy(q[1], q[0], N);
        /* ... */
        }
        {
        char *r = p;            /* The object pointed to by p may
                                                        be interpreted as having type
                                                        (char [2*N]) when referenced
                                                        through r. */
        /* ... */
        memcpy(r+N, r, N);
        /* ... */
        }
 }
```

the types of the objects are inferred from the pointers, and the underlying
storage is dynamically allocated. Is the behavior of each call of `memcpy`
defined?

Since the relationship between the values of the arguments presented to `memcpy`
is the same in all the above calls, it seems reasonable to expect that either
all these calls of `memcpy` give defined behavior, or none do. But which is it?

---

Comment from WG14 on 1997-09-23:

### Response

a. Yes, for `memcpy`, a contiguous sequence of elements within an array can be
regarded as an object in its own right.

b. The objects are not the smallest contiguous sequence of bytes that can be
construed; they are exactly the regions of data storage starting at the pointer
and of `N` bytes in length.

c. Yes, the non-overlapping halves of array `b` can be regarded as objects in
their own rights.

d. The behavior (in Example 2\) is defined.

e. The definition of object is independent of the *method* of storage
allocation. The array length is determined by “various methods.” So, yes, the
behavior of each call of `memcpy` is well-defined.

f. All of the calls of `memcpy` (in Example 3\) give defined behavior.
