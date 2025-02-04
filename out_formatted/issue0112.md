## Issue 0112: A Null pointer constants and relational comparison question

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_112.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_112.html)

ANSI/ISO C Defect report #rfg19:

Subject: Null pointer constants and relational comparisons.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
void test (void *vp)
        {
 	(vp > (void*)0);	/* ? */
        }
```

Background:

Subclause 6.2.2.3:

> An integral constant expression with the value 0, or such an expression cast to
> type `void *`, is called a *null pointer constant.* If a null pointer constant
> is assigned to or compared for equality to a pointer, the constant is converted
> to a pointer of that type.

This last paragraph of subclause 6.2.2.3 seems to suggest that zero-valued
integral constant expressions which are cast to `void *` (and then called null
pointer constants) can *only* be used in assignments and/or equality
comparisons, but not in relational comparisons.

(It was probably the Committee's intent to permit such expression to be used in
all ways, and in all contexts where any other kind of `void *` non-lvalued
expressions can be used, but the current wording of subclause 6.2.2.3 does not
make that fact altogether apparent and unambiguous.)

---

Comment from WG14 on 1997-09-23:

### Response

The code does not require a diagnostic but has undefined behavior, so it renders
the translation unit not strictly conforming. Subclause 6.3.8 makes clear that
this behavior is undefined.
