ANSI/ISO C Defect Report #rfg26:

Subject: Initialization of multi-dimensional array objects.

a) Is a diagnostic required for the following declaration?

b) Is the following declaration strictly conforming or not?

```c
static int array[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9  } };
```

Background:

Subclause 6.5.7 (**Semantics**):

> If an array of unknown size is initialized, its size is determined by the number
> of initializers provided for its elements.

Subclause 6.5.7 (**Semantics**):

> If the aggregate contains members that are aggregates or unions, or if the first
> member of a union is an aggregate or union, the rules apply recursively to the
> subaggregates or contained unions.

On the basis of the above quoted rules, one might conclude that the code example
given above is strictly conforming. (Many existing implementations seem to
disagree, however.)
