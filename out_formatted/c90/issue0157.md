## Issue 0157: Is it clearly indicated when the spelling of a type name is or is not significant?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_157.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_157.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 005: Legitimacy of type synonyms

The C Standard does not clearly indicate when the spelling of a type name is or
is not significant; in other words, when a type name may be replaced by another
type name representing the same type.

**Part 1**

Subclause 6.5.4.3 reads in part:

The special case of `void` as the only item in the list specifies that the
function has no parameters.

Subclause 6.7.1 reads in part:

(except in the special case of a parameter list consisting of a single parameter
of type `void`, in which there shall not be an identifier).

In both cases, the word `void` is set in the typeface used to indicate C code.

In the code:

```c
typedef void Void;
 extern int f (Void);
 int f (Void) { return 0; }
```

is the declaration on line 2 strictly conforming, and is the external definition
on line 3 strictly conforming?

**Part 2**

Subclause 5.1.2.2.1 reads in part: It can be defined with no parameters:

```c
                int main (void) { /* ... */ }
```

Is the following definition of `main` strictly conforming?

```c
typedef int word;
 word main (void) { /* ... */ }
```

**Part 3**

Are there any circumstances in which a typedef name is not permitted instead of
the type it is a synonym for? If so, what are they?

---

Comment from WG14 on 1997-09-23:

Proposed Response

A synonym is always acceptable, except that a function definition may not use a
typedef for the function type.

### Response

**Part 1**

Both function declarations are strictly conforming.

Subclause 6.7.1 makes clear that it is a single parameter having the type `void`
(as opposed to use of the `void` keyword) that indicates that a function takes
no parameters.

For clarity, Subclause 6.5.4.3 should be rephrased to emphasize that it is the
type `void`, not the keyword `void`that matters.

### Future Change

In Subclause 6.5.4.3,

Change

> "The special case of `void` as the only item in the list specifies that the
> function has no parameters."

To

> "The special case of an unnamed parameter of type `void` as the only item in the
> list specifies that the function has no parameters."

**Part 2**

Yes, the definition of `main` is strictly conforming.

**Part 3**

A synonym is not acceptable in these cases:

1. A function definition may not use a typedef for the function type:
   > ```c
   > typedef void F(void);
   > extern F g { } /* Invalid */
   > ```
2. A typedef may not be combined with another type specifier:
   > ```c
   > typedef int I;
   >  short I x;     /* Invalid */
   > ```
