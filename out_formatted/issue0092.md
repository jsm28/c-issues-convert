## Issue 0092: Are the remaining elements in a partially initalized string guaranteed to be zero?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0060](issue0060.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_092.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_092.html)

Item 29 \- partial initialization of strings

Consider the following program:

```c
#include <stdio.h>

 int main (void)
        {
        char s [10] = "Hello";

        printf ("s [9] is %d\n", s [9]);
        return 0;
        }
```

Is this program strictly conforming? If so, is the value of `s[9]` guaranteed to
be zero? Subclause 6.5.7 states:

> If there are fewer initializers in a brace-enclosed list than there are members
> of an aggregate, the remainder of the aggregate shall be initialized the same as
> objects that have static storage duration.

However, the initializer is not brace-enclosed, so this clause does not apply.

---

Comment from WG14 on 1997-09-23:

### Response

See the response to [Defect Report #060](issue0060.md).
