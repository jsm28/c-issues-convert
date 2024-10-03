Also consider:

```c
void g(c)
 enum m{q, r} c;
 {
 }
```

What is the scope of `m`, `q`, and `r`?

Subclause 6.1.2.1 says on page 20, lines 28-29 “... appears outside of any block
or list of parameters, the identifier has *file scope,* ...”

It says on page 20, lines 30-31 “... appears inside a block or within the list
of parameter declarations in a function definition, the identifier has *block
scope,* ...”

Now the above three identifiers appear outside of any block or list of
parameters but they are within the list of parameter declarations.

Who wins?
