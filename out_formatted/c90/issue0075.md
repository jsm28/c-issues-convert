## Issue 0075: What is the alignment of allocated memory?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_075.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_075.html)

Item 12 \- alignment of allocated memory

Is a piece of memory allocated by `malloc` required to be aligned suitably for
any type, or only for those types that will fit into the space? For example,
following the assignment:

```c
void *vp = malloc (1);
```

is it required that `(void *)(int *)vp` compare equal to `vp` (assuming that
`sizeof(int) > 1`), or is it permissible for `vp` to be a value not suitably
aligned to point to an `int`?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.10.3 requires allocated memory to be suitably aligned for *any*
type, so they must compare equal.
