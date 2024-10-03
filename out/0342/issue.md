### Summary

Consider the code:

```c
    int a, b;
    void *p1(void), *p2(void);
    int c1(void);
    int d1(void);
    int z1(void), z2(void);

    int
    h(void)
    {
      int r = (c1()
               ? (z1(), (int (*)[d1()])p1())
               : (z2(), (int (*)[])p2()))[a][b];
      return r;
    }
```

The type of the conditional expression involves the size expression `d1()`
that's only evaluated in one part of the expression, and this information is
needed to evaluate the array reference even when `c1()` returns false.

For a more complicated example and discussion see reflector messages
10731-10754. The validity of that more complicated example depends on the
interpretation of composite type rules as in [DR 340](issue:0340), so this
example has been simplified to avoid that problem.

### Suggested Technical Corrigendum

6.7.5.2 paragraph 6 at end add "or one of the size specifiers (including the
case of a single size specifier where the other array type does not include a
size specifier) is not an integer constant expression and is not evaluated
during the flow of execution." with a footnote "This case arises where a
conditional expression involves a cast to variably modified type or a compound
literal of variably modified type."
