ANSI/ISO C Defect report #rfg19:

Subject: Null pointer constants and relational comparisons.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
void test (void *vp)
        {
        (vp > (void*)0);     /* ? */
        }
```

Background:

Subclause 6.2.2.3:

> An integral constant expression with the value 0, or such an expression cast to
> type `void *`, is called a *null pointer constant.* If a null pointer constant
> is assigned to or compared for equality to a pointer, the constant is converted
> to a pointer of that type.

This last paragraph of subclause 6.2.2.3 seems to suggest that zero-valued
integral constant expressions which are cast to `void *` (and then called null
pointer constants) can *only* be used in assignments and/or equality
comparisons, but not in relational comparisons.

(It was probably the Committee's intent to permit such expression to be used in
all ways, and in all contexts where any other kind of `void *` non-lvalued
expressions can be used, but the current wording of subclause 6.2.2.3 does not
make that fact altogether apparent and unambiguous.)
