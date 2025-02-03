When a structure is incomplete

Reference subclause 6.5.2.3, page 62, lines 25-28:

> If a type specifier of the form
>
> ```c
> struct-or-union  identifier
> ```
>
> occurs prior to the declaration that defines the content, the structure or union
> is an incomplete type.

In the following example, neither the second nor the third occurrence of `struct
foo` seem adequately covered by this sentence:

```c
struct foo {
         struct foo *p;
 } a[sizeof(struct foo)];
```

In the second occurrence `foo` is incomplete, but since the occurrence is within
“the declaration that defines the content,” it cannot be said to be “prior” that
declaration. In the third occurrence `foo` is complete, but again, the
occurrence is within the declaration.

To fix the problem, change the phrase “prior to the declaration” to “prior to
the end of the `struct-declaration-list` or `enumerator-list`.”
