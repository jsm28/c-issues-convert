Is the following conforming?

```c
  struct x
                 {
                 char y[1];
                  };
         struct x *z;

         z = (struct x *) malloc(sizeof (*z) + 100);
         z- y[5] = '?';
```

[Defect Report #051](issue:0051) states that this isn't conforming behavior
because the pointer arithmetic for the larger structure might not be compatible
with a smaller structure. Thus, it recommends the *safer* idiom:

```c
#define HUGE_ARR  1000    /* or bigger than ever needed */
         struct x
                 {
                 char y[HUGE_ARR];
                 };
         struct x *z;

         z = (struct x *) malloc(sizeof (*z) + 100);
         z- y[5] = '?';
```

However, [Defect Report #073](issue:0073) states that the *safer* idiom is
undefined behavior because it is possible to implement the operator `-` as first
fetching all of `*z`, then selecting `y[5]` from it. This approach would cause
access to unallocated memory. Thus, the operation produces undefined behavior.

These responses are inconsistent. At the Oct 95 meeting in Nashua NH, WG14
indicated that it wanted to designate this as undefined behavior.
