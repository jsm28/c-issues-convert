## Issue 0164: Is there a constraint to prevent declarations involving types not defined by subclause 6.1.2.5?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_164.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_164.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 012: Bad declarations

The C Standard contains no constraint to prevent declarations involving types
not defined by subclause 6.1.2.5.

Subclause 6.5 states that:

A declaration shall declare at least a declarator, a tag, or the members of an
enumeration. There seems to be no constraint that a declarator generate a
well-formed type. Consider the following code:

```c
  {
         int a [][5];            /* Line A */
         int x, b [][5];         /* Line B */
         }
```

Neither `a` nor `b` has a well formed type. Does line A nevertheless *declare a
declarator,* or does it violate the quoted constraint? If it violates the
constraint, does line B?

Is it the intent of the C Standard that an ill-formed (but syntactically
correct) type generate a diagnostic? If so, then is there one, or does one need
to be added?

---

Comment from WG14 on 1997-09-23:

### Response

Line A declares a declarator. It violates the semantics described in subclause
6.5:

If an identifier for an object is declared with no linkage, the type for the
object shall be complete by the end of its declarator, ...

But no diagnostic is required.
