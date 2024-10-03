Under subclause 6.8.3.1 **Argument substitution**, the C Standard states on page
90, lines 12-14:

> Before being substituted, each argument's preprocessing tokens are completely
> macro replaced as if they form the rest of the translation unit; no other
> preprocessing tokens are available.

It is not clear to us what should happen if, after the first replacement, the
argument is a valid preprocessing number. Consider the following example:

```c
#define X 0x000E
 #define Y 0x0100
 #define FOO(a) a
 FOO(X+Y)
```

After `X` is replaced, `FOO(X+Y)` becomes `FOO(0x000E+Y)`. At this point, should
the macro replacement continue and expand `Y` to be 0x0100 with the final result
being `FOO(0x000E+0x0100)`; or should the expansion stop since `0x000E+Y` is a
syntactically valid preprocessing number?

In other words, should `FOO(X+Y)` be expanded into `FOO(0x000E+0x0100)`, or
should it be `FOO(0x000E+Y)`?
