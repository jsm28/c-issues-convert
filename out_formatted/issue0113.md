## Issue 0113: Return expressions in functions declared to return qualified `void` questions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_113.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_113.html)

ANSI/ISO C Defect report #rfg20:

Subject: Return expressions in functions declared to return qualified `void`.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
volatile void func0 (volatile void *vvp)
        {
        return *vvp;    /* ? */
        }

 const void func1 (const void *cvp)
        {
        return *cvp;    /* ? */
        }
```

Background:

Subclause 6.6.6.4 (**Constraints**):

> A `return` statement with an expression shall not appear in a function whose
> return type is `void`.

Note that this constraint doesn't say anything about functions declared to
return some qualified version of the `void` type.

I believe that it was probably the Committee's true intent to require a
diagnostic for any attempt to specify an expression in a return statement within
any function declared to return *any* qualified or unqualified version of the
`void` type (and indeed, many existing implementations do already issue
diagnostics for usage such as that shown in the example above). Thus, it would
seem appropriate for the Committee to amend the above quoted constraint (from
subclause 6.6.6.4) to read:

> A `return` statement with an expression shall not appear in a function whose
> return type is a void type.

---

Comment from WG14 on 1997-09-23:

### Response

a) Yes, a diagnostic is required.

b) Yes, this renders the program not strictly conforming code.

A qualified `void` function return type is disallowed by the constraints of
subclause 6.7.1:

> The return type from a function shall be `void` or an object type other than
> array.

The constraint does not say “a void type” and thus `void` must not be qualified
when used as a function return type. Since a qualified `void` return type is
already invalid, there is no need for the additional constraint on the `return`
statement (subclause 6.6.6.4).
