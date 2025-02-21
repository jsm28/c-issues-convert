## Issue 0109: Does the C Standard draw any significant distinction between *undefined values* and *undefined behavior*?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_109.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_109.html)

\[Question was revised in Jun 94.\]

ANSI/ISO C Defect Report #rfg16:

Does the C Standard draw any significant distinction between “undefined values”
and “undefined behavior?” (It appears that it does, but if it does, that fact is
not always apparent.)

Just to give two examples which, it would appear, involve the generation (in a
running program) of undefined values (as opposed to totally undefined behavior
at either compile-time or link-time or run-time) I provide the following two
citations.

Subclause 6.3.8 **Relational operators**:

> If the objects pointed to are not members of the same aggregate or union object,
> the *result* is undefined,...

(Emphasis added.)

Subclause 7.5.2.1 **The `acos` function**:

> A domain error occurs for arguments not in the range \[-1,\+1\].

The issue of “undefined values” versus “undefined behavior” has great
significance and importance to people doing compiler testing. It is generally
accepted that the C Standard's use of the term “undefined behavior” is meant to
imply that absolutely *anything* can happen at any time, e.g. at compile-time,
at link-time, or at run-time. Thus, people testing compilers must either totally
avoid writing test cases which involve any kind of “undefined behavior” or else
they must treat any such test cases which they *do* write as strictly “quality
of implementation” tests which may validly cause errors at compile-time, at
link-time, or at run-time.

If however the C Standard recognizes the separate existence of “undefined
values” (whose mere creation *does not* involve wholly “undefined behavior”)
then a person doing compiler testing could write a test case such as the
following, and he/she could also expect (or possibly demand) that a conforming
implementation should, at the very least, compile this code (and possibly also
allow it to execute) without “failure.”

```c
 int array1[5];
 int array2[5];
 int *p1 = &array1[0];
 int *p2 = &array2[0];

 int foo()
        {
        int i;
        i = (p1 > p2);  /* Must this be "successfully translated"? */
        1/0;             /* Must this be "successfully translated"? */
        return 0;
        }
```

So the bottom line question is this: Must the above code be “successfully
translated” (whatever that means)? (See the footnote attached to subclause
5.1.1.3.)

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard uses the term “indeterminately valued” not “undefined value.” Use
of an indeterminate valued object results in undefined behavior.

The footnote to subclause 5.1.1.3 points out that an implementation is free to
produce any number of diagnostics as long as a valid program is still correctly
translated.

If an expression whose evaluation would result in undefined behavior appears in
a context where a constant expression is required, the containing program is not
strictly conforming. Furthermore, if *every* possible execution of a given
program would result in undefined behavior, the given program is not strictly
conforming.

A conforming implementation must not fail to translate a strictly conforming
program simply because *some* possible execution of that program would result in
undefined behavior. Because `foo` might never be called, the example given must
be successfully translated by a conforming implementation.
