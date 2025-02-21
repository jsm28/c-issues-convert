## Issue 0047: Can an array parameter have elements of incomplete type?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Randall Meyers, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-040  
Submitted against: C90  
Status: Closed  
Cross-references: [0017.07](../c90/issue0017.07.md), [0110](../c90/issue0110.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_047.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_047.html)

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
Question 10](../c90/issue0017.07.md), the Committee took the position that a declaration
like that of `es1` was strictly conforming, since the size of `es1` is not
needed for an external reference, and thus was similar to the cases described in
Footnote 63 in subclause 6.5.2.3 on page 62\.

The declaration of `es2` also does not require its size to be known. However, it
appears that the rule from subclause 6.1.2.5, page 23, lines 23-24 that
prohibits an incomplete array element type makes `es2` not strictly conforming.

---

Comment from WG14 on 1997-09-23:

### Response

First of all, no constraints are violated. Therefore, no diagnostics are
required.

Declarations 1, 2, and 5 are strictly conforming. Declarations 3, 4, and 6 are
not, and therefore cause undefined behavior.

The struct `S` is an incomplete type (subclause 6.5.2.3, page 62, lines 25-28).
Also, an array of unknown size is an incomplete type (subclause 6.5.4.2, page
67, lines 9-10). Therefore, arrays of either of the above are not strictly
conforming (subclause 6.1.2.5, page 23, lines 23-24). This makes declarations 3,
4, and 6 not strictly conforming. (But an implementation could get it right.)

As an aside, array parameters are adjusted to pointer type (subclause 6.7.1,
page 82, lines 23-24). However, there is nothing to suggest that a
not-strictly-conforming array type can magically be transformed into a strictly
conforming pointer parameter via this rule.

The types in question can be interpreted two different ways. (Array to pointer
conversion can happen as soon as possible or as late as possible.) Hence a
program that uses such a form has undefined behavior.
