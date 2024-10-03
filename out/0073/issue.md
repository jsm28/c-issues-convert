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
 	array [1].real [0] = x;				/* Line A /*
 	array [1].real [1] = x;				/* Line B /*
 	array [1].imag = x;					/* Line C /*
 	pc = array + 1;					/* Line D /*
 	pc = array + 2;					/* Line E /*
 	pd = &(array [1].real [0]);			/* Line F /*
 	pd = &(array [1].real [1]);			/* Line G /*
 	pd = &(array [1].imag);				/* Line H /*
 	pd = &(array [0].real [0]) + D_PER_C;		/* Line I /*
 	pd = &(array [0].real [1]) + D_PER_C;		/* Line J /*
 	pd = &(array [0].imag) + D_PER_C;		/* Line K /*
 	pd = &(array [0].real [0]) + D_PER_C * 2; 		/* Line L /*
 	pd = &(array [0].real [0]) + D_PER_C + 1; 		/* Line M /*
 	pd = &(array [0].real [0]) + D_PER_C + 2; 		/* Line N /*
        return array;
        }
```

Subscripting is strictly conforming if the array is “large enough” (subclause
6.3.6). For each of the marked lines, is the assignment strictly conforming?
