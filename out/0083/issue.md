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
