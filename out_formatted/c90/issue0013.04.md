## Issue 0013.04: When is a struct type complete?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

When a structure is incomplete

Reference subclause 6.5.2.3, page 62, lines 25-28:

> If a type specifier of the form
>
> ```c
> struct-or-union  identifier
> ```
>
> occurs prior to the declaration that defines the content, the structure or union
> is an incomplete type.

In the following example, neither the second nor the third occurrence of `struct
foo` seem adequately covered by this sentence:

```c
struct foo {
         struct foo *p;
 } a[sizeof(struct foo)];
```

In the second occurrence `foo` is incomplete, but since the occurrence is within
“the declaration that defines the content,” it cannot be said to be “prior” that
declaration. In the third occurrence `foo` is complete, but again, the
occurrence is within the declaration.

To fix the problem, change the phrase “prior to the declaration” to “prior to
the end of the `struct-declaration-list` or `enumerator-list`.”

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.2.3, page 62, line 27, change:***

occurs prior to the declaration that defines the content

***to:***

occurs prior to the `}` following the `struct-declaration-li st` that defines
the content
