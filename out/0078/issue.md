Item 15 \- uniqueness of addresses

Consider the following translation unit:

```c
#include <string.h>

 unsigned int f (unsigned int a)
        {
        unsigned int x, y;

        x = a;
        x = x * x + a;
        if (x > 100)
 		return x;	/* Returned value must be > 100 */
        if (&x == &y)
              return 0;
        y = a + 1;
        y = y * y + 17;
 	return y;		/* Returned value must be > 0 */
        }

 unsigned int g1 (void) { return 0; };
 unsigned int g2 (void) { return 0; };

 unsigned int g (void)
        {
        return g1 != g2;
        }

 unsigned int h (void)
        {
        return memcpy != memmove;
        }

 const int j1 = 1;
 const int j2 = 1;

 unsigned int j (void)
        {
        return &j1 != &j2;
        }
```

a. Can `f` ever return zero? An aggressive optimizer could notice that `x` and
`y` are never used at the same time, and assign them the same memory location.
(The optimizer could be designed to conceal the fact that `x` and `y` are
sharing storage, for example by forcing the comparison to be unequal. Such an
application of the “as if” rule (subclause 5.1.2.3) would become increasingly
difficult to implement in the presence of operations such as writing out `&x` to
a file (using `fwrite` or the `fprintf %p` conversion specification) and then
reading it back in later in the same run of the program. However, this is
irrelevant; the issue is whether or not the implementation is required to
conceal it in the first place.)

b. Can `g` ever return zero? A optimizer using an intermediate form can easily
determine that the two functions have identical effects.

c. Can `h` ever return zero? The library function `memmove` (subclause 7.11.2.2)
completely meets the requirements for `memcpy` (subclause 7.11.2.1) and so they
could be implemented using the same code (even if the answer to (b) is no, this
could happen if the system library is not implemented in C).

d. Can `j` ever return zero? Since the two variables are constants, code which
uses `j1` instead of `j2` anywhere except in an address comparison cannot
distinguish them.
