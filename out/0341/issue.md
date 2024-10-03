### Summary

6.7.5.2#4 says that `*` as an array size "can only be used in declarations with
function prototype scope", and paragraph 5 says "If the size is an expression
that is not an integer constant expression: if it occurs in a declaration at
function prototype scope, it is treated as if it were replaced by `*`".

But is a type name in a function prototype a declaration, and does it have
function prototype scope? Scopes are only defined in 6.2.1 for identifiers, and
such type names do not declare identifiers. The presence of `[*]` in the syntax
for abstract declarators suggests that

```c
    void f(int (*)[*]);
```

was intended to be valid and `void f(int (*)[a]);` was intended to be equivalent
to it, but there are no declarations at function prototype scope involved.

Similarly, what is "in" such a declaration? Is the following valid?

```c
    void f(int (*)[sizeof(int (*)[*])]);
```

Although the `[*]` lies within a parameter declaration, it's within an
expression inside it; not one of the declarators involved in declaring the
identifier with function prototype scope.

### Suggested Technical Corrigendum

6.7.5.2 paragraph 4, change "declarations with function prototype scope" to "the
nested sequence of declarators or abstract declarators for a function parameter
in a function declaration that is not a definition"; remove the footnote.
Paragraph 5, change "declaration at function prototype scope" to "the nested
sequence of declarators or abstract declarators for a function parameter in a
function declaration that is not a definition".
