Are the following declarations strictly conforming?

```c
/* 1 */ struct S;
 /* 2 */        struct S *f(struct S *p) {return p; }
 /* 3 */        struct S *g(struct S a[]) {return a; }
 /* 4 */        int *h(int a2[][]) {return *a2; }
 /* 5 */        extern struct S es1;
 /* 6 */        extern struct S es2[1];
```

The declaration of struct tag `S` introduces an incomplete type (subclause
6.5.2.3, page 62, lines 25-29) that may only be used when the size of the type
is not needed.

The function `f` therefore is a fairly common and non-controversial use of an
incomplete pointer type by a function. It is strictly conforming.

The function `g` is more interesting. A parameter of type array is adjusted to
pointer type (subclause 6.7.1, page 82, lines 23-26). (Note that is an
adjustment of the type of the parameter definition. It is not a conversion, as
is what happens when an argument of type array is passed to a function.) Thus,
the type of parameter `a` is pointer to struct `S`. This would seem to make the
function `g` the same case as function `f`. However, subclause 6.1.2.5, page 23,
lines 23-24 (also Footnote 17\) disallow array types from having an incomplete
element type (like struct `S`). This raises the question, is function `g`
strictly conforming because the type of `a` is really pointer, or is function
`g` not strictly conforming because `a` had an invalid array type before the
compiler in effect rewrote the declaration?

The function `h` is similar to function `g`. The type of `a2` after adjustment
is pointer to array of unknown size of `int`, which does not violate any rules.
However, before adjustment, the type of `a2` is illegal because it is an array
whose element type is array of unknown size, which is an incomplete type.

In previous Committee discussion that occurred concerning [Defect Report #017
Question 10](issue:0017.07), the Committee took the position that a declaration
like that of `es1` was strictly conforming, since the size of `es1` is not
needed for an external reference, and thus was similar to the cases described in
Footnote 63 in subclause 6.5.2.3 on page 62\.

The declaration of `es2` also does not require its size to be known. However, it
appears that the rule from subclause 6.1.2.5, page 23, lines 23-24 that
prohibits an incomplete array element type makes `es2` not strictly conforming.
