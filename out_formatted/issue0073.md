## Issue 0073: Another definition of an object question

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0072](issue0072.md), [0178](issue0178.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_073.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_073.html)

Item 10 \- definition of object

Consider the following translation unit:

```c
#include <stdlib.h>
 struct complex
        {
        double real [2];
        double imag;
        }
 #define D_PER_C (sizeof (struct complex) / sizeof (double))
 struct complex *f (double x)
        {
        struct complex *array = malloc(sizeof (struct complex) +
                sizeof (double));
        struct complex *pc;
        double *pd;

        if (array == NULL)
                return NULL;
        array [1].real [0] = x;                         /* Line A /*
        array [1].real [1] = x;                         /* Line B /*
        array [1].imag = x;                                     /* Line C /*
        pc = array + 1;                                 /* Line D /*
        pc = array + 2;                                 /* Line E /*
        pd = &(array [1].real [0]);                 /* Line F /*
        pd = &(array [1].real [1]);                 /* Line G /*
        pd = &(array [1].imag);                             /* Line H /*
        pd = &(array [0].real [0]) + D_PER_C;               /* Line I /*
        pd = &(array [0].real [1]) + D_PER_C;               /* Line J /*
        pd = &(array [0].imag) + D_PER_C;           /* Line K /*
        pd = &(array [0].real [0]) + D_PER_C * 2;           /* Line L /*
        pd = &(array [0].real [0]) + D_PER_C + 1;           /* Line M /*
        pd = &(array [0].real [0]) + D_PER_C + 2;           /* Line N /*
        return array;
        }
```

Subscripting is strictly conforming if the array is “large enough” (subclause
6.3.6). For each of the marked lines, is the assignment strictly conforming?

---

Comment from WG14 on 1997-09-23:

### Response

Lines A, B, C. The identifier `array` points to an object that is not large
enough to hold two `struct complex` objects. The dot selection operator is at
liberty to require the complete structure denoted by its left hand side to be
accessed. Such an access would result in undefined behavior.

Line D. If `array` is regarded as pointing to a single structure then creating a
pointer to one past the end of that object is permitted.

Line E. If `array` is regarded as pointing to a single structure then creating a
pointer two past the end of that object is not permitted. Since there is
insufficient storage allocated to create a second `struct complex` object, it is
not permitted to point one past this partial `struct complex` object.

Lines F, G, H. Same analysis as Lines A, B, C.

Lines I, J, K, L, M, N. All of these calculations will result in pointers that
point outside the original object (arrays or structures) and result in undefined
behavior.
