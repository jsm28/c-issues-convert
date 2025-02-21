## Issue 0072: What is the definition of an object?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0044.01](../c90/issue0044.01.md), [0051](../c90/issue0051.md), [0073](../c90/issue0073.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_072.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_072.html)

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

Now, [Defect Report #051](../c90/issue0051.md) has established that the assignment on
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

---

Comment from WG14 on 1997-09-23:

### Response

a) [Defect Report #051](../c90/issue0051.md) provides the rationale for why Line A
results in undefined behavior. The same rules also apply to the assignment to
`pt`; thus Line B results in undefined behavior

b) Not applicable given the answer to question (a).

c) Assignment causes the base address of the structure to be assigned to `pc`.
The response to [Defect Report #044, question 1](../c90/issue0044.01.md), states that use
of the `offsetof` macro does not result in undefined behavior. The second line
causes `pc` to point to member `data`. Line C does not contain any construct
that would result in the program not being strictly conforming.

d) Line D results in undefined behavior. See answer (a) for rationale.

e) Not applicable given answers (c) and (d).

f) Subclause 6.3 contains additional restrictions, not permissions.

g) The answers to questions (a)-(e) are not affected if `T` has `char` type.
