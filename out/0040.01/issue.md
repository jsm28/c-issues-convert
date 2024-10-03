Composite type

Rule for function parameter compatibility, subclause 6.7,1, page 82, lines
24-25:

```c
void f(const int);
 void f(int a)
 {
 a = 4;
 }
```

In the above case what is the composite type of `f`? The legality of the
assignment to `a` depends on the answer.

```c
int f(int a[4]);
 int f(int a[5]);
```

The parameters are compatible because they are converted to *pointer to* ...,
but what is the composite type?
