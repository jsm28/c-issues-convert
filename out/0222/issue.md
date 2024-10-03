### Summary

Consider the code extract:

```c
   struct listheader
     {
         struct item *head;
         struct item *tail;
     };
     // The following is at block scope    struct listheader h1;
     h1.head = NULL;
     struct listheader h2;
     h2 = h1;
```

The value of `h1.tail` is indeterminate throughout, but provided that the code
never accesses it this is not a problem. However, if it holds a trap
representation, the assignment to `h2` involves assigning a trap representation,
which is undefined behaviour.

There are two possible resolutions I can think of:

1. Say that the code is defined. Any implementation that uses memberwise copying of structures now has to explicitly disable detection of trap values.
2. Say that the code is undefined. This is going to surprise a number of people. In particular, it becomes impossible to assign any structure where the complete list of fields is unknown (e.g. any structure defined in a Standard header).
