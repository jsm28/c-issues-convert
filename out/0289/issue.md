### Summary

6.7.6 (direct-abstract-declarator) is inconsistent with 6.7.5
(direct-declarator) with respect to omitting an identifier from a declaration to
form a type name.

Here is a specific example that shows the problem.

```c
 int lio_listio(int, struct aiocb *restrict const[restrict]);
```

is invalid and appears to have to be done as:

```c
 int lio_listio(int, struct aiocb *restrict const __FOO[restrict]);
```

6.7.6 Type names, paragraph 2 has:

> In several contexts, it is necessary to specify a type. This is accomplished
> using a type name, which is syntactically a declaration for a function or an
> object of that type that omits the identifier.

So you would think that if

```c
  struct aiocb *restrict const __FOO[restrict]
```

is a valid declaration of the object `__FOO`, then it should follow from the
above statement that

```c
  struct aiocb *restrict const [restrict]
```

must be a valid type name.
