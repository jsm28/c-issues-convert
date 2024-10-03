Compatible and composite function types

A fix to both problems Mr. Jones raises in X3J11 Document Number 90-006 is: In
subclause 6.5.4.3 on page 68, lines 23-25, change the two occurrences of “its
type for these comparisons” to “its type for compatibility comparisons, and for
determining a composite type.” This change makes the sentences pretty awkward,
but I think they remain readable.

This change makes all three of Mr. Jones's declarations compatible:

```c
int f(int a[4]);
 int f(int a[5]);
 int f(int *a);
```

This should be the case; it is consistent with the base document's idea of
“rewriting” the parameter type from array to pointer.
