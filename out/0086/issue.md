Item 23 \- object-like macros in system headers

Consider an implementation where `<string.h>` defines the macro `strlen` thus:

```c
#define strlen  __internal_fast_strlen
```

and declares functions (defined elsewhere) called `__internal_fast_strlen` and
`strlen`, both with the functionality of `strlen` in subclause 7.11.6.3. Is such
an implementation conforming with respect to the rules of subclause 7.1.7?

Note that a strictly conforming application can detect this situation by
comparing the value of the expression `strlen` taken before and after a
`#undef`.
