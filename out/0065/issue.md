Item 2 \- locales

Consider the program:

```c
#include <stdio.h>
 #include <stdlib.h>
 #include <locale.h>

 int main (void)
        {
        int i;
        char *loc [] = { "English", "En_UK", "Loglan", "" };

        for (i = 0; ; i++)
                if (setlocale (LC_ALL, loc [i]) != NULL)
                        {
                        /*
                         *  We must eventually get here,
                         *  because setlocale("") can't yield NULL.
                         /*
                        printf ("Decimal point = '%s'\n",
                        localeconv ()->decimal_point);
                        exit (0);
                        }
        }
```

The valid locales are implementation-defined (subclause 7.4.1.1). Nevertheless,
the output produced depends only on the locale, not any other
implementation-defined behavior. Is the program strictly conforming?
