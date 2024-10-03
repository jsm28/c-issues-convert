Is an “environmental constraint” a constraint?

In subclause 7.6.1.1, page 118, lines 22-30, we have a set of environmental
constraints on where `setjmp` may occur.

Does violating these rules require a constraint error to be flagged, or is it
undefined behavior?

Some examples:

```c
i = setjmp(a);
 if (setjmp(a) == i)
 ...
```
