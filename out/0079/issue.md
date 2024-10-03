Item 16 \- constancy of system library function addresses

(These questions approach the same problem from three slightly different
directions.)

a. If a pointer to a given standard library function (say `strlen`) is evaluated
in two different translation units, and the pointers compared, must they compare
equal?

b. Can a conforming implementation declare a standard library function as having
internal linkage, or must the identifiers with file scope declared in standard
headers have external linkage?

c. If the contents of the header `<string.h>` include the following definition
of `strlen`, is the implementation conforming?

```c
static size_t strlen (const char *__s)
        {
        size_t __len = 0;

        while (*__s++)
              __len++;
        return __len;
        }
```
