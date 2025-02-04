## Issue 0070: Can non-compatible types be used interchangeabily for function arguments?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_070.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_070.html)

Item 7 \- interchangeability of function arguments

Consider the following program:

```c
#include <stdio.h>

 void output (c)
        int c;
        {
        printf("C == %d\n", c);
        }
 int main (void)
        {
        output(6);
        output(6U);
        return 0;
        }
```

The constant `6` has type `int`, and `6U` has type `unsigned int` (subclause
6.1.3.2), and they have the same representation (subclause 6.1.2.5). Footnote
16, which is not a part of the C Standard, states that this implies that they
are interchangable as arguments. However, `int` and `unsigned int` are not
compatible types, and so subclause 6.3.2.2 makes the second call undefined.

Is the program strictly conforming?

Note that similar issues arise in connection with the other cases mentioned in
Footnote 16 (function return values and union members).

---

Comment from WG14 on 1997-09-23:

### Response

The program is not strictly conforming. Since many pre-existing programs assume
that objects with the same representation are interchangeable in these contexts,
the C Standard encourages implementors to allow such code to work, but does not
require it.
