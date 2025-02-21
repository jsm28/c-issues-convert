## Issue 0101: Are mismatched qualifiers allowed?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_101.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_101.html)

ANSI/ISO C Defect report #rfg8:

Subclause 6.3.2.2 **Function calls** says:

If the expression that denotes the called function has a type that includes a
prototype, the arguments are implicitly converted, as if by assignment, to the
types of the corresponding parameters.

The problem with this statement is the phrase “as if by assignment.” The above
rule fails to yield an unambiguous meaning in cases where an assignment of the
actual to the formal would be prohibited by other rules of the language, as in:

```c
void callee (const int formal);
 int actual;
 void caller () { callee(actual); }
```

(Here, the name of the formal parameter `formal` may be initialized but not
assigned to, because it is a non-modifiable lvalue.)

A similar problem exists within subclause 6.6.6.4 **The `return` statement**. It
says:

If the expression has a type different from that of the function in which it
appears, it is converted as if it were assigned to an object of that type.

This statement leaves the validity of the following code open to question:

```c
 const int returner () { return 99; }
```

Last but not least, subclause 6.5.7 **Initialization** says:

The initializer for a scalar shall be a single expression, optionally enclosed
in braces. The initial value of the object is that of the expression; the same
type constraints and conversions as for simple assignment apply, ...

This statement leaves the validity of the following code open to question:

```c
const int i = 99;
```

(Note that *assignment* to the data object `i` is not normally permitted, as its
name does not represent a modifiable lvalue.)

---

Comment from WG14 on 1997-09-23:

### Response

There are three questions about mismatched type qualifiers in places where
conversions “as if by assignment” takes place. Two of these are in
initialization and in function returns. A careful reading of the C Standard
shows that mismatched qualifiers are allowed in these two cases; see subclauses
6.5.7 and 6.5.3 **Semantics**.

The other issue deals with a qualifier mismatch between arguments and the
parameters of a called function. The C Standard should be modified to clarify
that such a mismatch is allowed.

### Correction

***In subclause 6.3.2.2, page 41, second paragraph, change:***

If the expression that denotes the called function has a type that includes a
prototype, the arguments are implicitly converted, as if by assignment, to the
types of the corresponding parameters.

***to:***

If the expression that denotes the called function has a type that includes a
prototype, the arguments are implicitly converted, as if by assignment, to the
types of the corresponding parameters, taking the type of each parameter to be
the unqualified version of its declared type.
