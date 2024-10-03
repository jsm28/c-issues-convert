ANSI/ISO C Defect Report #rfg33:

Subject: What does “synonym” mean with respect to typedef names?

Given the declarations:

```c
typedef int *IP;
 const IP object;
```

what is the type of `object`?

Background:

Subclause 6.5.6 says:

> A `typedef` declaration does not introduce a new type, only a synonym for the
> type so specified.

At least one person has wondered aloud about the true meaning of this rule.

Note that if the name `IP` in the above example is expanded as if it were a mere
macro, then the type of `object` would be `(const int *)`. But essentially all
existing implementations act as if there were some sort of magical parsing
precedence (or extra parenthesization) which causes the `IP` (when used in the
second line of the example above) to be treated as a single type, to which the
`const` qualifier is applied (after the fact) thus resulting in `object` having
type `(int * const)` rather than `(const int *)`.

While this treatment is well known to experienced implementors and users, it
appears that the C Standard doesn't really explain it very well (or very
precisely). I consider this to be a defect in the C Standard, worthy of the
Committee's attention.
