## Issue 0099: What does the term *assignment operator* mean?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_099.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_099.html)

ANSI/ISO C Defect report #rfg6:

Subclause 6.2.1.5 explicitly allows an implementation to evaluate a
floating-point expression using some type which has *more* precision than the
apparent type of the expression itself:

> The values of floating operands and the results of floating expressions may be
> represented in greater precision and range than that required by the type, ...

A footnote on this rule also says explicitly that:

> The cast and assignment operators still must perform their specified
> conversions, as described in 6.2.1.3 and 6.2.1.4.

As noted in the first of these two quotes (above) some compilers (most notably
for x86 and mc680x0 target systems) may perform floating-point expression
evaluation using a type which has more precision and/or range than that of the
“apparent type” of the expression being evaluated.

The clear implication of the above rules is that compilers must sometimes
generate code to implement narrowing of floating-point expression results, when
(a) those results were generated using a format with more precision and/or range
than the “apparent type” of the expression would seem to call for, and where (b)
the expression result is the operand of a cast or is used as an operand of an
“assignment operator.”

My question is simply this: For the purposes of the above rules, does the term
“assignment operator” mean exactly (and only) those operators listed in
subclause 6.3.3.16, or should implementors and users expect that other
operations described within the C Standard as being similar to “assignment” will
also produce floating-point narrowing effects (under the right conditions)?

Specifically, may (or must) implicit floating-point narrowing occur as a result
of parameter passing if the actual argument expression is evaluated in a format
which is wider than its “apparent type?” May (or must) implicit floating-point
narrowing occur as a result of a `return` statement if the `return` statement
contains a floating-point expression which is evaluated in some format which is
wider than its “apparent type?”

Here are two examples illustrating these two questions. Imagine that these
examples will be compiled for a type of target system which is capable of
performing floating-point addition *only* on floating-point operands which are
represented in the same floating-point format normally used to hold type `long
double` operands in C:

Example 1:

```c
extern void callee ();  /* non-prototyped */
 double a, b;

 void caller ()
        {
        callee(a+b);  /* evaluated in long double then narrowed? */
        }
```

Example 2:

```c
double a, b;

 double returner ()
        {
        return a+b;  /* evaluated in long double then narrowed? */
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

A careful reading of the C Standard indicates that everything that is done “as
if by assignment” must pass through a knot-hole (be narrowed). See the following
references: subclause 6.3.16 for assignment, 6.3.2.2 for parameters, and 6.6.6.4
for return types.
