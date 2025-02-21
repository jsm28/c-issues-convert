## Issue 0043.01: Can `NULL` be defined as `4-4`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Robert Paul Corbett, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-004  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_043.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_043.html)

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

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 7.1.2, page 96 (before Forward references):***

Any definition of an object-like macro described in this clause shall expand to
code that is fully protected by parentheses where necessary, so that it groups
in an arbitrary expression as if it were a single identifier.
