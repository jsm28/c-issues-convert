## Issue 0076: A set of pointers to the end of arrays questions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0012](issue0012.md), [0166](issue0166.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_076.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_076.html)

Item 13 \- pointers to the end of arrays

Consider the following code extracts:

```c
int a [10];
        int *p;
        /* ... */
        p = &a[10];
```

and

```c
int *n = NULL;
        int *p
        /* ... */
        p = &*n;
```

In the first extract, is the assignment strictly conforming (with `p` being set
to the expression `a + 10`), or is the constraint in subclause 6.3.3.2 violated
because `a[10]` is not an object? Note that this expression is often seen in the
idiom:

> ```c
> for (p = &a[0]; p &lt; &a[10]; p++)
>                 /* ... */
> ```

In the second extract, is the assignment strictly conforming (with `p` being set
to a null pointer), or is the constraint in subclause 6.3.3.2 violated because
`*n` is not an object?

If only one assignment is strictly conforming, what distinguishes the two cases?
If either assignment is strictly conforming, what distinguishes it from the
situation described in the following extract from the response to [Defect Report
#012](issue0012.md)?

> Given the following declaration:
>
> ```c
> void *p;
> ```
>
> the expression `&*p` is invalid. This is because `*p` is of type `void` and so
> is not an lvalue, as discussed in the quote from subclause 6.2.2.1 above.
> Therefore, as discussed in the quote from subclause 6.3.3.2 above, the operand
> of the `&` operator in the expression `&*p` is invalid because it is neither a
> function designator nor an lvalue.
>
> This is a constraint violation and the translator must issue a diagnostic
> message.

---

Comment from WG14 on 1997-09-23:

### Response

This issue remains open. The C Standard as currently worded has the following
consequences:

1\) Subclause 6.3.3.2 requires the operand of `&` to be an lvalue designating an
object; `a[10]` is not an object.

2\) Subclause 6.3.3.2 requires the operand of `&` to be an lvalue; `NULL` is not
an lvalue.

Since the use of either construct prevents a program from being strictly
conforming, the remaining portion of the question is not applicable.

However, the Committee is not entirely comfortable with these restrictions and
may decide to relax them in resolving this issue.
