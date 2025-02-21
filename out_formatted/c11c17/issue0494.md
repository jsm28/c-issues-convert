## Issue 0494: Part 1: Alignment specifier expression evaluation

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Clark Nelson  
Date: 2016-03-17  
Reference document: [N2027](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2025.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C23  
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

### The alignment specifier case

The interesting thing about `_Alignas` is that the “answer” is just a number;
all other details of the type named are irrelevant. Since the alignment of an
array type must be the same as that of its element type, the value of the array
size is irrelevant, so strictly speaking it need not be evaluated.

This is similar to `sizeof`; according to 6.7.6.2p5:

> Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.

For an alignment specifier, I would prefer that the behavior not depend on the
scope in which it appears. It would also be simpler to require that a
non-constant size expression **not** be evaluated than to permit implementation
latitude. That would be consistent with the parameter declaration case, and I
doubt that any real-world code would change behavior as a result.

As an aside, here is an interesting related example:

```c
size_t s = sizeof(int [rand()]);
```

According to 6.5.3.4p2:

> If the type of the operand is a variable length array type, the operand is
> evaluated; otherwise, the operand is not evaluated and the result is an integer
> constant.

If the declaration of `s` appeared at file scope, the fact that the result of
`sizeof` is not an integer constant would run afoul of the constraints on
initialization, so a diagnostic would be required. That might be considered
enough to override the requirement that “the operand is evaluated” in an
initializer at file scope – but the phrasing would seem to be suboptimal.

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

> From [(SC22WG14.14483) Suggested TC for DR
> 494](https://www.open-std.org/jtc1/sc22/wg14/14483) the following suggestion was
> made:

In 6.7.6.2 paragraph 5, change:

> ... Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.

to:

> ... Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.
> Where a size expression is part of the operand of an `_Alignof` operator, that
> expression is not evaluated.

Apr 2017 meeting

### Committee Discussion

The words discussed and reported in the last meeting were adopted.

### Proposed Change

In 6.7.6.2 paragraph 5, change:

> ... Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.

to:

> ... Where a size expression is part of the operand of a `sizeof` operator and
> changing the value of the size expression would not affect the result of the
> operator, it is unspecified whether or not the size expression is evaluated.
> Where a size expression is part of the operand of an `_Alignof` operator, that
> expression is not evaluated.
