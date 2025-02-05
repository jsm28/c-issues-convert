Item 19 \- multiple varargs

Consider the following translation unit:

```c
#include <stdarg.h>
 #include <stdio.h>

 extern int is_final_arg (int);

 void f1 (int n, ...)
        {
        va_list ap1, ap2;

        va_start (ap1, n);
        va_start (ap2, n);
        while (va_arg (ap1, int) != 0)
                printf ("Value is %d\n", va_arg (ap2, int));
        va_end (ap1);
        va_end (ap2);
        }

 void f2 (int n, ...)
        {
        va_list ap;

        va_start (ap, n);
        for (;;)
                {
                n = va_arg (ap, int);
                if (is_final_arg (n))
                        {
                        va_end (ap);
                        return;
                        }
                printf ("Value is %d\n", n);
                }
        }

 void f3 (int n, ...)
        {
        va_list ap;

        va_start (ap, n);
        while (n = va_arg (ap, int), n != 0)
                printf ("Value is %d\n", n);
        va_start (ap, n);
        while (n = va_arg (ap, int), n != 0)
                printf ("Value is still %d\n", n);
        va_end (ap);
        }

 void f4a (va_list *pap)
        {
        int n;

        while (n = va_arg (*pap, int), n != 0)
                printf ("Value is %d\n", n);
        }

 void f4 (int n, ...)
        {
        va_list ap;

        va_start (ap, n);
        f4a (&ap);
        va_end (ap);
        }

 void f5a (va_list apc)
        {
        int n;

        while (n = va_arg (apc, int), n != 0)
                printf ("Value is %d\n", n);
        }

 void f5 (int n, ...)
        {
        va_list ap;

        va_start (ap, n);
        f5a (ap);
        va_end (ap);
        }
```

a. Is each function in this translation unit strictly conforming? Note in
particular:

in `f1`, the use of simultaneous `va_lists` in `f1`;

in `f2`, `va_start` and `va_end` are in different scopes;

in `f3`, there are two `va_start`s and one `va_end`;

in `f4`, the address of an object of type `va_list` is taken;

in `f4a` and `f5a`, `va_arg` is called with a first parameter which is not “the
same as the `va_list ap` initialized by `va_start`” (subclause 7.8.1.2).

b. Is the following implementation conforming?

`va_start` allocates a block of memory with `malloc`;

a `va_list` is a pointer to the block;

`va_end` frees the same block;

c. Is there any portable method to copy the current state of a `va_list`, for
example in order that the remaining arguments can be scanned twice without
knowledge of the `va_arg` calls made previous to that point? If the answer to
(b) is “yes,” I believe the answer to (c) must be “no.”
