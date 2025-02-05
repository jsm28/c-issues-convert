### Summary

6.5 reads:

> \[#6\] \[...\] If a value is copied into an object having no declared type using
> `memcpy` or `memmove`, or is copied as an array of character type, then the
> effective type of the modified object for that access and for subsequent
> accesses that do not modify the value is the effective type of the object from
> which the value is copied, if it has one. For all other accesses to an object
> having no declared type, the effective type of the object is simply the type of
> the lvalue used for the access.

Now consider the code extract:

```c
 struct s { char c; int i; long l; double d; } s = { 1, 2, 3, 4 };
     size_t len1 = sizeof (int);
     size_t len2 = offsetof (s, d) - offsetof (s, i));
     void *p1 = malloc (len1); assert (p1);
     void *p2 = malloc (len2); assert (p2);
     memcpy (p1, (char *)&s + offsetof (s, i), len1);
     memcpy (p2, (char *)&s + offsetof (s, i), len2);
```

What are the effective types of `p1` and `p2` ? The cited text would imply that
they are both `struct s`, even though this is patently nonsense.
