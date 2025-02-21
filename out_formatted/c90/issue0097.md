## Issue 0097: Can the `type` argument of the `offsetof` macro be an incomplete type?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0040.06](../c90/issue0040.06.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_097.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_097.html)

ANSI/ISO C Defect report #rfg4:

Subclause 7.1.6 fails to contain any constraint which would prohibit the type
argument given in an invocation of the `offsetof` macro from being an incomplete
type. This situation can arise in examples such as the following:

```c
#include <stddef.h>

 struct S
        {
        int member1;
        int member2[1+offsetof(struct S, member1)];
        };
```

I believe that a constraint prohibiting the type argument to `offsetof` from
being an incomplete type is clearly needed.

This problem could be solved by adding an explicit constraint to subclause
7.1.6, such as:

> The type argument given in an invocation of the `offsetof` macro shall be the
> name of a complete structure type or a complete union type. (Note that this way
> of expressing the constraint also makes it completely clear that diagnostics are
> required for cases where the type given in the invocation is, for instance, a
> function type, an array type, an enumerated type, a pointer type, or a built-in
> arithmetic type.)

---

Comment from WG14 on 1997-09-23:

### Response

See the response to [Defect Report #040](../c90/issue0040.06.md), question 6\. This code
is not strictly conforming.
