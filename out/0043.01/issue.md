Defining `NULL`

Subclause 7.1.6 defines `NULL` to be a macro “which expands to an
implementation-defined null pointer constant.” Subclause 6.2.2.3 defines a null
pointer constant to be “an integral constant expression with the value 0, or
such an expression cast to type `void *`.” The expression `4-4` is an integral
constant expression with the value 0\. Therefore, Standard C appears to permit

`#define NULL 4 - 4` as one of the ways `NULL` can be defined in the standard
headers. By allowing such a definition, Standard C forces programmers to
parenthesize `NULL` in several contexts if they wish to ensure portability. For
example, when `NULL` is cast to a pointer type, `NULL` must be parenthesized in
the cast expression.

At least one book about Standard C suggests defining `NULL` as

`#define NULL (void *) 0` That definition leads to a subtler version of the
problem described above. Consider the expression `NULL[p]`, where `p` is an
array of pointers. The expression expands to `(void *)0[p]` which is equivalent
to `(void *)(p[0])`. I doubt many users would expect such a result.

Have I correctly understood Standard C's requirements regarding `NULL`? If not,
what are those requirements?
