## Issue 0163: Is it clear whether the use of an undeclared identifier as a primary expression requires a diagnostic message to be issued?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_163.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_163.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 011: Undeclared identifiers

The C Standard is not clear on whether the use of an undeclared identifier as a
primary expression requires a diagnostic message.

Subclause 6.3.1 states that:

An identifier is a primary expression, provided it has been declared as
designating an object (in which case it is an lvalue) or a function (in which
case it is a function designator).

It has been suggested that if no declaration of some identifier is visible in
the current scope when that identifier appears in an expression, the identifier
is not a primary expression, and therefore the syntax of subclause 6.3.1 is
violated (in other words, there is no valid parse for the expression). This
would thus require a diagnostic for an undeclared identifier.

Is this interpretation correct? If yes, then it needs to be made clear that this
does not prevent a previously undeclared function from being called by a
strictly conforming program (see 6.3.2.2).

If not, does an undeclared identifier require a diagnostic, and if so, why? If
not, is this a deliberate policy, or is it a defect that needs correction?

---

Comment from WG14 on 1997-09-23:

### Response

Identifiers that designate objects must be declared and be visible before they
can be primary expressions (subclause 6.1.2.1, *An identifier is visible (i.e.,
can be used) ...*). A reasonable person could interpret that if no declaration
of some identifier is visible, the identifier cannot be a primary expression.
This affects undeclared identifiers that are intended to be used as implicitly
declared functions. The Committee's intent is that the C Standard be read in the
following order:

1\. **6.3.1 Primary expressions**

**Syntax**

```c
          primary-expression:
                         identifier
```

2\. **6.3.2.2 Function calls**

**Semantics**

If the expression that precedes the parenthesized argument list in a function
call consists solely of an identifier, and if no declaration is visible for this
identifier, the identifier is implicitly declared exactly as if, in the
innermost block containing the function call, the declaration

```c
extern int identifier();
```

appeared.

3\. 6.3.1 **Primary expressions**

**Semantics**

An identifier is a primary expression, provided it has been declared as
designating ... a function (...).

However, a reasonable person may not interpret the current wording as having
that meaning (i.e., it might not be read in that order). This needs to be
clarified in the next revision of the C Standard.

### Response

Identifiers must be declared and visible before they can be primary expressions
(Subclause 6.1.2.1, "An identifier is visible (i.e., can be used) ..."). If no
declaration of some identifier is visible, the identifier cannot be a primary
expression, and a diagnostic is required for a violation of the syntax rule.

Note that a declaration of an identifier might be visible due to the identifier
being implicitly declared (Subclause 6.3.2.2). This should be clarified in the
Standard.

### Future Change

In Subclause 6.3.1, first paragraph in "Semantics"

Change

> "An identifier is a primary expression, provided is has been declared as
> designating an object (in which case it is an lvalue) or a function (in which
> case it is a function designator)."

To

> "An identifier is a primary expression, provided is has been declared as
> designating an object (in which case it is an lvalue) or implicitly**\*** or
> explicitly declared as designating a function (in which case it is a function
> designator)."
>
> The **\*** above references the new footnote:

"See 6.3.2.2."
