## Issue 0495: Part 2: Atomic specifier expression evaluation

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Clark Nelson  
Date: 2016-03-17  
Reference document: [N2027](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2025.htm)  
Submitted against: C11 / C17  
Status: Closed  
Cross-references: [0486](issue0486.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Point D of DR439 (a.k.a. N1729) raises the question of the meaning of a
non-constant expression in an abstract declarator. The other points of that DR
are rather more straightforward, but point D requires more thought. Here I
present some additional analysis I have done on the question.

### Overview

There are three places an abstract declarator or type name can appear and (at
least potentially) not be part of a larger expression:

1. *parameter-declaration*
2. *alignment-specifier*
3. *atomic-type-specifier*

(When this topic comes up, the case of a generic selection is generally raised
as well. However, it should be clearly understood that a type name appearing in
a generic selection is necessarily part of a larger expression, so any
expression therein isn't a full expression, so DR439 does not raise any issues
about it. It's certainly possible that there are issues, but if so, they need to
be spelled out. Once they have been clearly defined, it will hopefully become
clear whether they should be considered along with DR439 or separately.)

So let's consider three file-scope declarations:

1. `void f(int [rand()]);`
2. `_Alignas(int [rand()]) int i;`
3. `_Atomic(int [rand()]) a;`

The first declaration has a clearly defined meaning. According to 6.7.6.2p5, the
expression is “treated as if it were replaced by `*`”. Therefore:

* the expression is not evaluated; and
* the parameter is declared as a VLA of unspecified size.

These are both true even if the declaration appears in a block scope.

For the second and third declarations, the standard today gives no clue how the
expression should be handled. The only thing that is clear (even though the
standard doesn't say so) is that, if the declarations are at file scope, any
answer that requires evaluating the expressions is wrong.

### The atomic type specifier case

`_Atomic`-of-array types are already disallowed; see 6.7.2.4p3. The following
example avoids that restriction, but still has a non-constant expression in an
atomic specifier:

```c
_Atomic(int (*)[rand()]) p1;
```

What would such a declaration mean, if it were allowed?

It would be tempting to conclude that it is not allowed at file scope, since a
variably modified type is involved. Unfortunately, the standard doesn't actually
say so – or at least not yet. According to 6.7.6p3:

> Furthermore, any type derived by declarator type derivation from a variably
> modified type is itself variably modified.

But an atomic type specifier isn't described as involving declarator type
derivation. There is definitely a kind of type derivation involved, but possibly
of a new and different kind.

On the other hand, because of the unique dual nature of the syntax for
`_Atomic`, the preferred answer is probably that the previous declaration would
have the same meaning as this declaration:

```c
int (*_Atomic p2)[rand()];
```

If a qualifier other than `_Atomic` were used, the interpretation of the
declaration and the contained expression would be pretty clear from the
standard. But for `_Atomic`, the words of the standard seem to more or less
rewrite this declaration into the prior form, about which the standard has less
to say, by and large.

If it is true, as seems likely, that any atomic type specifier containing a
non-constant expression can be expressed equivalently using an atomic type
qualifier instead, then presumably the question of what to do when the
expression is syntactically a full expression is not all that interesting.

What remains interesting is how to express this intention normatively.

---

Comment from WG14 on 2018-10-18:

Oct 2017 meeting

### Committee Discussion

> The committee believes that there will be a review of the atomic specification
> in the next revision of the standard and that this issue will be examined in
> that context.

Apr 2018 meeting

### Committee Discussion

> The committee solicited a combined resolution for this issue with those raised
> in [DR 486](issue0486.md).

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that this proposed change and that from [CR 486](issue0486.md) be
> combined in a new paper to completely resolve this issue.
