Item 13 \- pointers to the end of arrays

Consider the following code extracts:

```c
int a [10];
        int *p;
        /* ... */
        p = &a[10];
```

and

```c
int *n = NULL;
        int *p
        /* ... */
        p = &*n;
```

In the first extract, is the assignment strictly conforming (with `p` being set
to the expression `a + 10`), or is the constraint in subclause 6.3.3.2 violated
because `a[10]` is not an object? Note that this expression is often seen in the
idiom:

> ```c
> for (p = &a[0]; p &lt; &a[10]; p++)
>                 /* ... */
> ```

In the second extract, is the assignment strictly conforming (with `p` being set
to a null pointer), or is the constraint in subclause 6.3.3.2 violated because
`*n` is not an object?

If only one assignment is strictly conforming, what distinguishes the two cases?
If either assignment is strictly conforming, what distinguishes it from the
situation described in the following extract from the response to [Defect Report
#012](issue:0012)?

> Given the following declaration:
>
> ```c
> void *p;
> ```
>
> the expression `&*p` is invalid. This is because `*p` is of type `void` and so
> is not an lvalue, as discussed in the quote from subclause 6.2.2.1 above.
> Therefore, as discussed in the quote from subclause 6.3.3.2 above, the operand
> of the `&` operator in the expression `&*p` is invalid because it is neither a
> function designator nor an lvalue.
>
> This is a constraint violation and the translator must issue a diagnostic
> message.
