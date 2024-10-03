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
