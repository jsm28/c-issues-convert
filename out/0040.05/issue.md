In the constraint for subclause 6.5.2, page 59, lines 2-4: What does the C
Standard mean when it says “set?”

Does it mean that the construct:

```c
int int i;
```

violates a constraint?

It has been suggested that this wording was left vague to allow such constructs
as `long long` (which is supported by some compilers) to fall into the undefined
behavior category.

Would the Committee clarify the situation with regard to duplicate type
specifiers? Do such constructs result in a constraint error or undefined
behavior?

The related case `static static` is explicitly ruled out by the constraints in
the previous subclause.

Additionally, `volatile volatile` is ruled out by the constraint in subclause
6.5.3.
