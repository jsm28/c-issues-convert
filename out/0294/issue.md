### Summary

I have a question on section 6.7.3.1 of the C99 spec.

Paragraph 4 is where this seems to get complicated.

Question 1\)

> "...Every other lvalue used to access the value of X shall also have its address
> based on P".

Consider the following example:

```c
        #include <stdlib.h>
        char * restrict a, * restrict b;

        void copy(char * restrict dest, char * restrict source)
        {
         int i;
        for (i = 0; i < 10; i++)
            dest[i] = source[i];
        }

        int main()
        {
         a = calloc(10);
         b = calloc(10);
         copy(a, b);
         return 0;
        }
```

Is this a legal program? If so, could you explain the following? From the
standpoint of `main()`, the memory in `a` is modified through the call to
`copy()`. However, it seems to me that based on the definition of *based on*,
the writes that modify `*a` are not *based on* the pointer `a`, but instead
they're based on `dest`. Doesn't this violate the guarantee above?

Question 2\)

> "Every access that modifies X shall be considered also to modify P, for the
> purposes of this subclause." \- Why is this necessary?

Question 3\)

> The same question for the rules on the copying of `restrict` pointers ("If P is
> assigned the value of a pointer expression E that is based on another restrict
> pointer object P2, associated with block B2, then either the execution of B2
> shall begin before the execution of B, or the execution of B2 shall end prior to
> the assignment."). Why is this necessary?
