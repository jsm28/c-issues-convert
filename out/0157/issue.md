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
