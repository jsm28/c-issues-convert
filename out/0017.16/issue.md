Pointer to multidimensional array

Given the declaration:

```c
char a[3][4], (*p)[4]=a[1];
```

Does the behavior become undefined when:

1. `p` no longer points within the slice of the array, or
2. `p` no longer points within the object `a`?

This case should be explicitly stated.

Arguments for/against:

The standard refers to a pointed-to object. There does not appear to be any
concept of a slice of an array being an independent object.
