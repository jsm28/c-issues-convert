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
