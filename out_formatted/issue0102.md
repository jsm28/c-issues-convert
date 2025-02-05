## Issue 0102: Does a constraint violation win over undefined behavior?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0017.03](issue0017.03.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_102.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_102.html)

ANSI/ISO C Defect report #rfg9:

Subclause 6.5 **Constraints** says:

If an identifier has no linkage, there shall be no more than one declaration of
the identifier (in a declarator or type specifier) with the same scope and in
the same name space, except for tags as specified in 6.5.2.3.

Subclause 6.5.2.3, **Semantics** section says:

Subsequent declarations \[of a tag\] in the same scope shall omit the bracketed
list.

Given that one of the above two rules appears in a **Constraints** section,
while the other appears in a **Semantics** section, it is ambiguous whether or
not diagnostics are strictly required in the following cases (in which more than
one defining declaration of each tag appears within a single scope):

```c
void example ()
        {
        struct S { int member; };
 	struct S { int member; };  /* diagnostic required? */

        union U { int member; };
 	union U { int member; };   /* diagnostic required? */

        enum E { member };
 	enum E { member };         /* diagnostic required? */
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

A diagnostic is required for the `struct`, `union`, and `enum` redeclarations
indicated in the question. Subclause 6.5 indicates that there must be a
diagnostic “except for tags as specified in 6.5.2.3.” In subclause 6.5.2.3, the
specified exception is for subsequent declarations that omit the bracketed list.

See also the response to [Defect Report #017, Question 3](issue0017.03.md).
