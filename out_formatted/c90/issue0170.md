## Issue 0170: Are the description of operators and punctuators is confusing, and are the constraints contradictory?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_170.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_170.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 018: Operators and punctuators

The description of operators and punctuators is confusing, and the constraints
are contradictory.

Subclause 6.1.5 Constraints reads:

The operators `[ ]`, `( )`, and `? :` shall occur in pairs, possibly separated
by expressions. The operators `#` and `##` shall occur in macro-defining
preprocessing directives only.

Subclause 6.1.6 Constraints reads:

The punctuators `[ ]`, `( )`, and `{ }` shall occur (after translation phase 4\)
in pairs, possibly separated by expressions, declarations, or statements. The
punctuator `#` shall occur in preprocessing directives only.

Consider the code:

```c
#define STR(x)  #x
 STR ({)    /* Line A */
 STR (:)    /* Line B */
 STR ([)    /* Line C */
 STR (#)    /* Line D */
```

Line A appears to be strictly conforming, since the first sentence of the
constraint of subclause 6.1.6 does not apply during translation phase 4\. Line B
violates the constraint of subclause 6.1.5. The interpretation of line C depends
on whether the `[` is an operator or a punctuator!

Line D violates both constraints, but again which one depends on whether it is
an operator or a punctuator, something which is not made clear in the C
Standard.

Assuming that the intent was for line B to be strictly conforming, and that
*(after translation phase 4\)* was inadvertently omitted from subclause 6.1.5,
the first sentence of each of these Constraints is nugatory, as any program that
violates these constraints also violates a syntax rule elsewhere in clause 6\.
The remaining sentences would be better expressed as part of subclause 6.8. It
is also arguable that the concepts of operator and punctuator are better merged
at the syntactic level, and separated out only at the semantic level.

### Suggested Technical Corrigendum

Delete the Constraints of subclauses 6.1.5 and 6.1.6. Add the following
constraint to 6.8:

A `#` preprocessing token shall only occur within a replacement-list or when
permitted by the syntax rules of this subclause. A `##` preprocessing token
shall only occur within a replacement-list.

Add to the end of the Constraints of subclause 6.1, just before the full stop:

, and shall not be `#` or `##`

**Alternative Suggested Technical Corrigendum**

In subclause 6.1 syntax, delete both occurrences of *operator* and replace the
second occurrence of *punctuator* by *pp-punctuator.*

Delete subclauses 6.1.5 and 6.1.6, and replace them by the following:

**6.1.5 Punctuators**

**Syntax:**

```c
  pp-punctuator:
                 punctuator
                 pp-only-punctuator
         pp-only-punctuator: one of
                 # ## defined
         punctuator:
                 [ ] ( ) { } . -
                 ++ -- & * + - ~ ! sizeof
                 / %            =  = == != ^ | && ||
                 ? : , : ; ...
                 = *= /= %= += -=   =   = &= ^= |=
```

**Semantics:**

A punctuator is a symbol that has independent syntactic and semantic
significance. Depending on context, some punctuators may specify an operation to
be performed (an *evaluation*) that yields a value, or yields a designator, or
produces a side-effect, or a combination thereof; in that context, the
punctuator is known as an *operator.* An *operand* is an entity on which an
operator acts.

Add the following constraint to 6.8:

A `#` preprocessing token shall only occur within a replacement-list or when
permitted by the syntax rules of this subclause. A `##` preprocessing token
shall only occur within a replacement-list.

---

Comment from WG14 on 1997-09-23:

### Response

This is a work in progress item.

General feeling is that this should be cleaned up for C9X along the lines of
C\+\+ pp-punctuator grammar.

Suggested response is to add words to subclause 6.1.5 along the lines, *shall
occur in pairs within expressions...*
