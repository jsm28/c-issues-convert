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
