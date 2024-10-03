`register` on aggregates

```c
void f(void)
 {
 register union{int i;} v;
 &v      /* Constraint error */
 &(v.i);  /*  Constraint error or undefined? */
 }
```

In subclause 6.3.3.2 on page 43, lines 37-38 in a constraint clause, it says
“... and is not declared with the `register` storage-class specifier.” But in
the above, the field `i` is not declared with the `register` storage-class
specifier.

Footnote 58, on page 58, states that “... the address of any part of an object
declared with storage-class specifier `register` may not be computed ...”
Although the reference to this footnote is in a constraints clause I think that
it is still classed as undefined behavior.

Various people have tried to find clauses in the standard that tie the storage
class of an aggregate to its members. I would not use the standard to show this
point. Rather I would use simple logic to show that if an object has a given
storage class then any of its constituent parts must have the same storage
class. Also the use of storage classes on members is syntactically illegal.

The question is not whether such a construction is legal but the status of its
illegality. Is it a constraint error or undefined behavior?

It might be argued that although `register` does not appear on the field `i`,
its presence is still felt. I would point out that the standard does go to some
pains to state that in the case of `const union{...}` the `const` does apply to
the fields. The fact that there is no such wording for `register` implies that
`register` does not follow the `const` rule.
