## Issue 0040.05: Can a conforming implementation accept `long long`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

In the constraint for subclause 6.5.2, page 59, lines 2-4: What does the C
Standard mean when it says “set?”

Does it mean that the construct:

```c
int int i;
```

violates a constraint?

It has been suggested that this wording was left vague to allow such constructs
as `long long` (which is supported by some compilers) to fall into the undefined
behavior category.

Would the Committee clarify the situation with regard to duplicate type
specifiers? Do such constructs result in a constraint error or undefined
behavior?

The related case `static static` is explicitly ruled out by the constraints in
the previous subclause.

Additionally, `volatile volatile` is ruled out by the constraint in subclause
6.5.3.

---

Comment from WG14 on 1997-09-23:

### Response

Example:

```c
int int i;
```

Must this be diagnosed?

Answer: Yes. It is allowed to rearrange the order of type specifiers within a
set, but not to duplicate them (cf. subclause 6.5.2). Thus `int int` is a
constraint violation.
