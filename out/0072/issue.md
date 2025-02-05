Item 9 \- definition of object

Consider the following translation unit:

```c
#include <stdlib.h>

 typedef double T;
 struct hacked
        {
        int size;
        T data [1];
        };

 struct hacked *f (void);
        {
        T *pt;
        struct hacked *a;
        char *pc;

        a = malloc (sizeof (struct hacked) + 20 * sizeof (T));
        if (a == NULL)
                return NULL;
        a->size = 20;

        /* Method 1 /*
        a->data [8] = 42;                                    /* Line A /*

        /* Method 2 /*
        pt = a->data;
        pt += 8;                                                        /* Line B /*
        *pt = 42;

        /* Method 3 /*
        pc = (char *) a;
        pc += offsetof (struct hacked, data);
        pt = (T *) pc;                                          /* Line C /*
        pt += 8;                                                        /* Line D /*
        *pt = 6 * 9;
        return a;
        }
```

Now, [Defect Report #051](issue:0051) has established that the assignment on
line A involves undefined behavior.

a. Is the addition on line B strictly conforming?

If the answer to (a) is “yes,” are the three statements forming “method 2” a
valid way of implementing the `struct hacked`?

b. Is the cast of line C strictly conforming?

c. Is the addition on line D strictly conforming?

d. If the answer to (c) and (d) are “yes,” are the five statements forming
“method 3” a valid way of implementing the `struct hacked`?

Now suppose that the definition of type `T` is changed to `char`. This means
that the last bullet in subclause 6.3 (“an object shall have its stored value
accessed only by ... a character type”) now applies, and furthermore it means
that the location accessed is an integral multiple of `sizeof(T)` bytes from the
start of the `malloc`ed object, and so constitutes an element of that object
when viewed as an array of `T`.

e. Is the assignment on line A now strictly conforming?

f. What are the answers to questions (a) to (e) with this change?
