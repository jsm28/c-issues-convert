ANSI/ISO C Defect Report #rfg22:

Subject: Member declarators as declarators.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
 struct { int mbr; };   /* ? */
 union  { int mbr; };   /* ? */
```

Background:

Subclause 6.5 (**Constraints**):

> A declaration shall declare at least a declarator, a tag, or the members of an
> enumeration.

It is not entirely clear what it means to “declare” a declarator. Neither is it
clear whether or not a declarator for a member should be considered to satisfy
the constraint quoted above. (Many existing implementations behave as if member
declarators *do not* satisfy the constraint.)
