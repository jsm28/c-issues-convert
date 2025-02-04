## Issue 0124: What is the difference between casts to *a void type* versus casts to the `void` type?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_124.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_124.html)

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

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.3.4, page 45, change the paragraph under Constraints:***

Unless the type name specifies void type, the type name shall specify qualified
or unqualified scalar type and the operand shall have scalar type.

***to:***

Unless the type name specifies a void type, the type name shall specify
qualified or unqualified scalar type and the operand shall have scalar type.
