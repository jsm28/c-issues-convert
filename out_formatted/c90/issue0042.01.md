## Issue 0042.01: Does `memcpy` define a (sub)object?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Tom MacDonald, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-001  
Submitted against: C90  
Status: Closed  
Cross-references: [0054](../c90/issue0054.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_042.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_042.html)

The description of `memcpy` in subclause 7.11.2.1 says:

> ```c
> void *memcpy(void *s1, const void *s2, size_t n);
> ```
>
> The `memcpy` function copies `n` characters from the object pointed to by `s2`
> to the object pointed to by `s1`. If copying takes place between objects that
> overlap, the behavior is undefined.

The definition of the term *object* in subclause 3.14 is:

> **object** \- A region of data storage in the execution environment, the
> contents of which can represent values. Except for bit-fields, objects are
> composed of contiguous sequences of one or more bytes, the number, order, and
> encoding of which are either explicitly specified or implementation-defined.
> When referenced, an object may be interpreted as having a particular type...

Are the objects in the description of `memcpy` the largest objects into which
the arguments can be construed as pointing?

In particular, is the behavior of the call of `memcpy` in Example 1 defined:

```c
void f1(void) {
        extern char a[2][N];
        memcpy(a[1], a[0], N);
        }
```

because the arguments point into the disjoint array objects, `a[1]` and `a[0]`?
Or is the behavior undefined because the arguments both point into the same
array object, `a`?

---

Comment from WG14 on 1997-09-23:

### Response

From subclause 3.14, an object is “a region of data storage ... Except for
bit-fields, objects are composed of contiguous sequences of one or more bytes,
the number, order, and encoding of which are either explicitly specified or
implementation-defined ...” From subclause 7.11.1, “the header `<string.h>`
declares one type and several functions, and defines one macro useful for
manipulating arrays of character type and other objects treated as arrays of
character type.” “Various methods are used for determining the lengths of the
arrays...” From subclause 7.11.2.1, description of `memcpy`, “if copying takes
place between objects that overlap, the behavior is undefined.” Therefore, the
“objects” referred to by subclause 7.11.2.1 are exactly the regions of data
storage pointed to by the pointers and dynamically determined to be of `N` bytes
in length (i.e. treated as an array of `N` elements of character type).

a. So, no, the objects are not “the largest objects into which the arguments can
be construed as pointing.”

b. In Example 1, the call to `memcpy` has defined behavior.

c. The behavior is defined because the pointers point into different
(non-overlapping) objects.
