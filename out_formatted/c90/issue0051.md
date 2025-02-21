## Issue 0051: Can one index beyond the declared end of an array if space is allocated for the extra elements?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Andrew R. Koenig, Project Editor (P.J. Plauger)  
Date: 1993-03-08  
Submitted against: C90  
Status: Closed  
Cross-references: [0072](../c90/issue0072.md), [0178](../c90/issue0178.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_051.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_051.html)

I'll give you the short form first. I can haul out lots of related material if
it becomes necessary, but perhaps the bare question is enough. Is the following
program strictly conforming?

```c
#include <stdlib.h>

 struct A {
        char x[1];
        };

 main()
        {
        struct A *p = (struct A *) malloc(sizeof(struct A) + 100);
        p->x[5] = '?';               /* This is the key line */
        return 0;
        }
```

If I remember correctly from reading the C Standard, pointer arithmetic is
illegal if it results in an address outside the object to which the original
pointer refers. The question here is essentially whether the “object” is all the
memory returned by `malloc` or the single `char` denoted by `p->x[0]`.

I do not believe there is any language in the C Standard that clearly answers
this question. I understand that this particular programming technique is quite
common, but that is more likely to affect whether a program is “conforming” than
whether it is “strictly conforming.”

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.3.2.1 describes limitations on pointer arithmetic, in connection
with array subscripting. (See also subclause 6.3.6.) Basically, it permits an
implementation to tailor how it *represents pointers* to the size of the objects
they point at. Thus, the expression `p->x[5]` may fail to designate the expected
byte, even though the `malloc` call ensures that the byte is present. The idiom,
while common, is *not* strictly conforming.

A safer idiom is:

```c
#include <stdlib.h>
 #define HUGE_ARR       10000   /* largest desired array */

 struct A {
        char x[HUGE_ARR];
        };

 main()
        {
        struct A *p = (struct A *) malloc(sizeof(struct A)
                - HUGE_ARR + 100);      /* want x[100] this time */
        p->x[5] = '?';               /* now strictly conforming */
        return 0;
        }
```
