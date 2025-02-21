## Issue 0345: Where does parameter scope start?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Rob Arthan \<UK\>, Derek Jones (UK)  
Date: 2007-04-23  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_345.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_345.htm)

### Summary

1\)

The wording in 6.2.1p7:

> Any other identifier \[except a struct/union tag or an enumeration constant\]
> has scope that begins just after the completion of its declarator.

permits the use of `q` in the following declaration of the parameter `r`.

> ```c
> void f(
>      long double q,
>      char (**r)[10 * sizeof q])
> { }
> ```

However, consider 6.9.1p9 (which was not in C90):

> Each parameter has automatic storage duration. Its identifier is an lvalue,
> which is in effect declared at the head of the compound statement that
> constitutes the function body ...

This does not appear to permit the use of `q` in the declaration of the
parameter `r`.

Does `q` have two points of declaration (one at the end of its declarator and
one at the head of the compound statement)?

2\)

Consider the situation when a function has a parameter with the same name as the
function, as in the following example:

> ```c
> #include>stdio.h<
> void f(
>      long double f,
> /* #1 */
>      char (**a)[10 * sizeof f])
> {
> /* #2 */
>          printf("%d\n", (int) sizeof **a);
> /* #3 */
> }
> int main(void)
> {
>          f(0, 0);
>          return 0;
> }
> /* #4 */
> ```

6.2.1p4 says:

> ... If an identifier designates two different entities in the same name space,
> the scopes might overlap. If so, the scope of one entity (the inner scope) will
> be a strict subset of the scope of the other entity (the outer scope). Within
> the inner scope, the identifier designates the entity declared in the inner
> scope ...

The scope of the function `f` starts at #2 and continues to the end of the file
(#4). The scope of the parameter `f` starts at #1 and continues to the end of
the definition of the function `f` (#3). Neither of these scopes is a strict
subset of the other.

### Suggested Technical Corrigendum

1\)

None proposed.

2\)

One solution is to fix up the scope overlap wording in 6.2.1p4 and acknowledge
that the function `f` in the above example is not callable (although currently
callable by some compilers that have been tried).

The second sentence from 6.2.1p4 could be amended to read:

> ... scopes might overlap. If so, the scope of one entity (the inner scope) will
> end strictly before the scope of the other entity (the outer scope). Within the
> inner scope, ...

So the example would be conformant and would print out 10 times the size of a
`long double`.

---

Comment from WG14 on 2008-09-12:

### Committee Discussion

#### Spring 2007

There was no consensus for question 2\.

For question 1: The Committee believes that 6.9.1 paragraph 9 is a comment on
the storage duration and does not override the lexical scope described in 6.2.1
paragraph 7\.

#### Fall 2007

General consensus is that the wording in the Standard is basically not correct
and needs to be reworked.

Also see comments in WG14 e-mail *SC22WG14.11380*

#### Spring 2008

#### Question 1

C\+\+ 3.3.2p2 has three sentences (words irrelevant to C are deleted):

1. The potential scope of a function parameter name or of a function-local predefined variable in a function definition begins at its point of declaration.
2. The potential scope of a parameter or of a function-local predefined variable ends at the end of the outermost block of the function definition.
3. A parameter name shall not be redeclared in the outermost block of the function definition.

For sentence 1, 6.2.1p7 already says:

> Any other identifier has scope that begins just after the completion of its
> declarator.

For sentence 2, 6.2.1p4 already says:

> If the declarator or type specifier that declares the identifier appears inside
> a block or within the list of parameter declarations in a function definition,
> the identifier has *block scope*, which terminates at the end of the associated
> block.

For sentence 3, 6.7p3 already says:

> If an identifier has no linkage, there shall be no more than one declaration of
> the identifier (in a declarator or type specifier) with the same scope and in
> the same name space, except for tags as specified in 6.7.2.3.

And 6.2.1p6 says:

> Two identifiers have the *same scope* if and only if their scopes terminate at
> the same point.

So what the C\+\+ standard says, and what the C standard needs to say, about the
scope of a parameter name is already covered in the C standard, outside of
6.9.1p9. Therefore, I suggest modifying 6.9.1p9 as indicated:

> Each parameter has automatic storage duration. Its identifier is an lvalue<del>,
> which is in effect declared at the head of the compound statement that
> constitutes the function body (and therefore cannot be redeclared in the
> function body except in an enclosed block)</del>. The layout of the storage for
> parameters is unspecified.

Additionally, if desired, add a footnote at the point of the deletion:

> <ins>A parameter identifier cannot be redeclared in the function body except in
> an enclosed block.</ins>

#### Question 2

The words "a strict subset" are technically incorrect, but nothing really
depends on them. Fixing them can be treated as an editorial matter.

One possibility would be simply to qualify that statement with "generally" or
"usually". The submitter's suggested technical corrigendum would also be
technically correct. In 6.2.1p4:

> ... If an identifier designates two different entities in the same name space,
> the scopes might overlap. If so, the scope of one entity (the *inner scope*)
> will <del>be a strict subset of</del> <ins>end strictly before</ins> the scope
> of the other entity (the *outer scope*). Within the inner scope, the identifier
> designates the entity declared in the inner scope; the entity declared in the
> outer scope is *hidden* (and not visible) within the inner scope.

**Change for C1X**

Change 6.9.1 paragraph 9 to:

> Each parameter has automatic storage duration. Its identifier is an
> lvalue,<sup>\*</sup> the layout of the storage for parameters is unspecified.
>
> <sup>\*</sup>A parameter identifier cannot be redeclared in the function body
> except in an enclosed block.

Change 6.2.1 paragraph 4 to:

> ... If an identifier designates two different entities in the same name space,
> the scopes might overlap. If so, the scope of one entity (the *inner scope*)
> will end strictly before the scope of the other entity (the *outer scope*).
> Within the inner scope, the identifier designates the entity declared in the
> inner scope; the entity declared in the outer scope is *hidden* (and not
> visible) within the inner scope.
