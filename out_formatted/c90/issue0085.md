## Issue 0085: Is the return from `main` equivalent to calling `exit`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_085.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_085.html)

Item 22 \- returning from `main`

Consider the following program:

```c
#include <stdlib.h>
 #include <stdio.h>

 int *pi;

 void handler (void)
        {
        printf ("Value is %d\n", *pi);
        }

 int main (void)
        {
        int i;

        atexit (handler);
        i = 42;
        pi = &i;
        return 0;
        }
```

Return from `main` is defined to be equivalent to calling `exit` (subclause
5.1.2.2.3). If the `return` statement was replaced by the equivalent call, the
program would be strictly conforming. Is it strictly conforming without this
replacement?

Note that if the answer is “yes,” special processing will be required for return
from `main,` which will depend on whether the call being returned from is the
initial call or a recursive one.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 5.1.2.2.3, page 7, add at the end of the first sentence the
footnote:***

In accordance with subclause 6.1.2.4, objects with automatic storage duration
declared in `main` will no longer have storage guaranteed to be reserved in the
former case even where they would in the latter.
