`sizeof` various identifiers (subclause 7.1.6)

a)

```c
void f(int c, char a[sizeof(c)]);
```

b)

```c
int i;
 struct {
 int i;
 char a[sizeof(i)];
 };
```

Now the argument to `sizeof` must be an expression or a type.

In (a) is `c` an expression? I think not because:

expression -\> object -\> has storage in execution environment

and `c` does not have storage allocated to it. So (a) violates a semantic
“shall” and is undefined behavior.

Now in (b) the field `i` is obviously not an expression. But is it visible? Like
the outer `i`, it has file scope. However, it is in a different namespace. There
are no rules for namespace resolution in the `sizeof` subclause.

So is (b) legal or undefined behavior?
