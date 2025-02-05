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
