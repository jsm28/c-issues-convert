## Issue 0083: A use of library functions question

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_083.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_083.html)

Item 20 \- use of library functions

Consider the following program:

```c
#include <stdio.h>

 int main (void)
        {
        printf ("%d\n", 42.0);
        return 0;
        }
```

This program clearly should have undefined behavior, but I can find no wording
which states so.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.1.7, page 99, insert after the words in parentheses in the
second sentence of the first paragraph:***

or a type (after promotion) not expected by a function with variable number of
arguments
