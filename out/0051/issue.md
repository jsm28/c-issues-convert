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
