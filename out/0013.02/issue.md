“Compatible” not defined for recursive types

The term “compatible” is not completely defined. Consider the following two
file-scope declarations in *separate* translation units:

```c
extern struct a { struct a *p; } x;
 struct a { struct a *p; } x;
```

Are these two declarations of `x` compatible? Obviously they should be, but
subclause 6.1.2.6 does not say so.

Because subclause 6.1.2.6 does not say how to terminate the recursion in testing
for compatibility of two recursive types, either interpretation is possible. In
other words, it is consistent with the rules in subclause 6.1.2.6 to decide that
the two declarations are compatible; but it is also consistent to decide that
they are incompatible.

We can solve the problem roughly as follows: append the following draft sentence
to the first paragraph of subclause 6.1.2.6 (page 25, line 8):

> If two types declared in separate translation units admit the possibility of
> being either compatible or incompatible, the two types shall be
> compatible.**\*** \[Footnote \*: This case occurs with recursive types.\]

This sentence is not satisfactory; perhaps another Committee member can state
this rule better.
