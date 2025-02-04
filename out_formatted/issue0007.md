## Issue 0007: Are declarations of the form `struct` *`tag`* permitted after *`tag`* has already been declared?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Paul Eggert, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-043  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_007.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_007.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

The declaration

```c
struct s;
```

declares the tag `s`. It need not be the first or only declaration of the tag
`s` within a given scope to qualify as a declaration of `s`, just as

```c
int i;
```

declares `i` however often it is repeated. The applicable constraint is in
subclause 6.5: “A declaration shall declare at least a declarator, a tag, or the
members of an enumeration.” Clearly,

```c
struct s;
```

declares the tag `s`.

Subclause 6.5.2.3, in the examples, characterizes a declaration of this form as
“otherwise vacuous” in the draft you read. The words “otherwise vacuous” were an
editorial comment that was omitted from the International Standard. These words
were intended to mean “other than declaring `s2` to be an (incomplete) struct
type,” and should not be read as saying that the declaration fails to declare
the tag.

We believe that this interpretation is consistent with the intent of the
Committee, and that a reasonable reading of the standard supports this
interpretation.
