ANSI/ISO C Defect Report #rfg31:

Subject: Casts to “a void type” versus casts to “the `void` type.”

Must a conforming implementation issue a diagnostic for the following code?

```c
void example ()
        {
 	(const volatile void) 0;	/* diagnostic required? */
        }
```

Background:

Subclause 6.3.4 (**Constraints**):

> Unless the type name specifies void type, the type name shall specify qualified
> or unqualified scalar type and the operand shall have scalar type.

Note that this constraint is *not* specific about whether a qualified void type
is permitted in a cast or not; i.e. it should say either “a void type” or else
say “the `void` type.”

A quick check of several existing implementations seems to indicate that a
majority of implementors have assumed that any void type (however qualified) is
acceptable in a cast. Therefore it would seem prudent for the Committee to
clarify the above quoted rule by changing “void type” to “a `void` type.”
