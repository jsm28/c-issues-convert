Item 12 \- alignment of allocated memory

Is a piece of memory allocated by `malloc` required to be aligned suitably for
any type, or only for those types that will fit into the space? For example,
following the assignment:

```c
void *vp = malloc (1);
```

is it required that `(void *)(int *)vp` compare equal to `vp` (assuming that
`sizeof(int) > 1`), or is it permissible for `vp` to be a value not suitably
aligned to point to an `int`?
