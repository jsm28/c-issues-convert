Are declarations of the form `struct-or-union identifier ;` permitted after the
`identifier` tag has already been declared? Here are some examples of the
problem:

```c
/*1*/ struct s;
 /*2*/ struct s;
 /*3*/ struct s {int a;};
 /*4*/ struct s;
 /*5*/ struct t {int a;};
/*6*/ struct t;
```

Subclause 6.5 says “A declaration shall declare at least a declarator, a tag, or
the members of an enumeration.” In this sense, does `/*`*`2`*`*/` also declare
the tag `s`? If so, then surely all of the above lines are conforming. But if
not, then in what sense does `/*`*`3`*`*/` declare a tag and thus satisfy
subclause 6.5's constraint?

The example at the end of subclause 6.5.2.3 says “To eliminate this context
sensitivity, the otherwise vacuous declaration `struct s2;` may be inserted ...”
This seems to imply that `/*`*`2`*`*/`, `/*`*`4`*`*/`, and `/*`*`6`*`*/` are not
conforming, because the y are vacuous. But how can this be reconciled with the
above argument?
