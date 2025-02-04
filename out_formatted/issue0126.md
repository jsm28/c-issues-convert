## Issue 0126: What does *synonym* mean with respect to typedef names?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_126.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_126.html)

ANSI/ISO C Defect Report #rfg33:

Subject: What does “synonym” mean with respect to typedef names?

Given the declarations:

```c
typedef int *IP;
 const IP object;
```

what is the type of `object`?

Background:

Subclause 6.5.6 says:

> A `typedef` declaration does not introduce a new type, only a synonym for the
> type so specified.

At least one person has wondered aloud about the true meaning of this rule.

Note that if the name `IP` in the above example is expanded as if it were a mere
macro, then the type of `object` would be `(const int *)`. But essentially all
existing implementations act as if there were some sort of magical parsing
precedence (or extra parenthesization) which causes the `IP` (when used in the
second line of the example above) to be treated as a single type, to which the
`const` qualifier is applied (after the fact) thus resulting in `object` having
type `(int * const)` rather than `(const int *)`.

While this treatment is well known to experienced implementors and users, it
appears that the C Standard doesn't really explain it very well (or very
precisely). I consider this to be a defect in the C Standard, worthy of the
Committee's attention.

---

Comment from WG14 on 1997-09-23:

### Response

A `typedef` introduces a name for a type. This is not a macro, and the type must
indeed be “magically parenthesized.” In

```c
 typedef int *ip;
 ip x;
 const ip y;
```

the type of `x` is *pointer to* `int`, and the type of `y` is `const` *pointer
to* `int`. This is exactly analogous to the fact that

```c
 ip x1, x2;
```

declares both `x1` and `x2` as having the type *pointer to* `int`, and is not to
be read as

```c
 int *x1, x2;
```
