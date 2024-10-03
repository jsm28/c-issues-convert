Ordering of conversion of arrays to pointers

In subclause 6.5.4.3 on page 68, line 22 there is a sentence in parentheses.
Does the sentence refer to the whole paragraph or just the preceding sentence?

```c
int f(int a[4]);
 int f(int a[5]);
 int f(int *a);
```

1. It refers to the whole paragraph. This makes all of the above three declarations compatible.
2. It does not refer to the whole paragraph. This makes all three declarations incompatible.
