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
