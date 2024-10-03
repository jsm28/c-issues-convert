```c
void f(a, b)
 int a(enum b {x, y});
 int b;
 {
 }
```

Now this example is perverse because a prototype declaration is used to declare
the parameter of an old-style function declaration. But anyway ...

Is the declaration of the parameter `a` legal or a constraint error?

Now `a(...)` is a declarator.

Subclause 6.7.1 says on page 82, lines 7-8:

> ... each declaration in the declaration list shall have at least one declarator,
> and those declarators shall declare only identifiers from the identifier list.

The identifier list contains `a` and `b`.

The declarator for parameter `a` declares the identifiers `a`, `b`, `x`, and
`y`.

`b` is in the identifier list, so that is okay. But `x` and `y` are not.
Constraint error (methinks so)?

See subclause 6.1.2, page 19 for a definition of an identifier.
