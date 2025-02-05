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
