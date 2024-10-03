Item 21 \- incomplete type in function declaration

Consider the following declarations:

```c
struct tag;
 extern void (*f) (struct tag);
```

At the point of the declaration of `f`, the type of the parameter is incomplete.
Now a parameter is an object (subclause 3.15) with no linkage (subclause
6.1.2.2), but it is unclear whether this is a declaration of the parameter. If
it is, then the declaration of `f` is forbidden by subclause 6.5. If it is not,
then the declaration is strictly conforming. Which is the case?

If the type `struct tag` is completed before a call to `f`, is the call strictly
conforming? Alternatively, since the declaration of `f` includes an incomplete
type, is it possible to make a call to it at all?
