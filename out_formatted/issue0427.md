## Issue 0427: Function Parameter and Return Value Assignments

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Shao Miller \<sha0.miller@gmail.com\>  
Date: 2013-01-24  
Reference document: [N1671](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1671.htm)  
Submitted against: C11 / C17  
Status: Closed  
Cross-references: [0423](issue0423.md), [0454](issue0454.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The wording for the the assignments of function arguments to function parameters
and for the assignment of a `return` statement's expression to the value of the
function call can potentially be confused.

6.5.2.2p2:

> If the expression that denotes the called function has a type that includes a
> prototype, the number of arguments shall agree with the number of parameters.
> Each argument shall have a type such that its value may be assigned to an object
> with the unqualified version of the type of its corresponding parameter.

The appearance of "may be assigned" can lead to the question (#1) of whether or
not the constraints and semantics under both 6.5.16 and 6.5.16.1 might apply.
The **Forward references** indicate 6.5.16.1, so this question might be
unwarranted.

The appearance of "unqualified version of the type of its corresponding
parameter" does not match 6.9.1p10, which doesn't use "unqualified" (see below).

6.5.16p2:

> An assignment operator shall have a modifiable lvalue as its left operand.

If 6.5.2.2p2's mention of "assigned" implies this constraint as a secondary
constraint, it is not clear which "modifiable lvalue" or even "lvalue" would
ever satisfy the constraint. The "modifiable lvalue" does not appear to be the
parameter, because:

* the mention of "unqualified version" suggests a theoretical object, while the parameter might be `const`-qualified, or
* the parameter might have an unqualified structure or union type having at least one `const`-qualified member (possibly via recursion)

6.7.3p4:

> The properties associated with qualified types are meaningful only for
> expressions that are lvalues.132)
>
> 132\) The implementation may place a const object that is not volatile in a
> read-only region of storage. Moreover, the implementation need not allocate
> storage for such an object if its address is never used.

This can suggest that 6.5.2.2p2's "an object with the unqualified version of the
type" implies an lvalue, but (question #2) is it a modifiable lvalue? Question
#3: If the type is a structure or union type with a `const`-qualified member
(possibly via recursion), are the members considered to be unqualified, too? If
so, this is an important difference from pointer types where the referenced type
(or its referenced type, recursively) would not be considered unqualified. Also
worth consideration would be an array object (which is not qualified) having
elements matching such a structure or union type (possibly via recursion).

The return type of a function might be `const`-qualified, or might be a
structure or union type having such a member (possibly via recursion). Question
#4: Should the return type of a function be adjusted to be an unqualified
version of the type? Such an adjustment might have implications for type
compatibility and composite type and might be better off left alone. (`const` is
being used for illustrative purposes, but all type qualifiers can equally be
considerations.)

6.8.6.4p3:

> If a return statement with an expression is executed, the value of the
> expression is returned to the caller as the value of the function call
> expression. If the expression has a type different from the return type of the
> function in which it appears, the value is converted as if by assignment to an
> object having the return type of the function.160)
>
> 160\) The return statement is not an assignment. The overlap restriction of
> subclause 6.5.16.1 does not apply to the case of function return. The
> representation of floating-point values may have wider range or precision than
> implied by the type; a cast may be used to remove this extra range and
> precision.

If the return type of a function is `const`-qualified, or is a structure or
union type having such a member (possibly via recursion), then "as if by
assignment" works for 6.5.16.1, but the constraint of 6.5.16p2 requires a
"modifiable lvalue".

The footnote reminds us that a `return` statement with an expression is not an
assignment, but it is not clear that only 6.5.16.1 applies for the "as if by
assignment" case.

6.9.1p10:

> On entry to the function, the size expressions of each variably modified
> parameter are evaluated and the value of each argument expression is converted
> to the type of the corresponding parameter as if by assignment. (Array
> expressions and function designators as arguments were converted to pointers
> before the call.)

6.9.1p11:

> After all parameters have been assigned, the compound statement that constitutes
> the body of the function definition is executed.

A `const`-qualified lvalue cannot normally be assigned-to. An lvalue for an
object having a structure or union type containing a `const`-qualified member
(possible via recursion) cannot normally be assigned-to.

6.9.1p10 doesn't match the use of "unqualified" in 6.5.2.2p2 (see above).

### Suggested Technical Corrigendum

**Sun c99** and **GCC** disagree on the `return` statement's semantics.

Change 6.5.2.2p2 to:

> If the expression that denotes the called function has a type that includes a
> prototype, the number of arguments shall agree with the number of parameters.
> Each argument shall be such that it satifies the constraints of simple
> assignment when considering the argument to be the right operand and considering
> the left operand to have the unqualified version of the type of the
> corresponding parameter.

(Loosely establishes an example for "as if by simple assignment".)

Change 6.8.6.4p3 to:

> If a return statement with an expression is executed, the value of the
> expression is returned to the caller as the value of the function call
> expression. If the expression has a type different from the return type of the
> function in which it appears, the value is converted as if by simple assignment
> to an object having the unqualified version of the return type of the
> function.160)

Change 6.9.1p10 to:

> On entry to the function, the size expressions of each variably modified
> parameter are evaluated in an unspecified order, the value of each argument
> expression is converted to the unqualified version of the type of the
> corresponding parameter as if by simple assignment, then each converted value
> becomes the initial value for the corresponding parameter. (Array expressions
> and function designators as arguments were converted to pointers before the
> call.)

Change 6.9.1p11 to:

> After all parameters have initial values, the compound statement that
> constitutes the body of the function definition is executed.

Add bullet to J.1

> \- The order in which the size expressions of variably modified parameters are
> evaluated upon function entry (6.9.1).

---

Comment from WG14 on 2016-10-21:

Apr 2013 meeting

### Committee Discussion

* No one on the committee understood the problem that this paper was trying to discuss.
* In particular, the actual difference in behavior referenced between Sun c99 and GCC is not elaborated upon.
* The committee will solicit further input from the author.

Oct 2013 meeting

* As a result of further correspondence with the author, a proposed resolution was made on the WG14 reflector in message 13024 and refined in 13035\.
* The defect is that the initial values of parameters to function calls are specified in the standard in terms of assignment instead of initialization, such that `const` and aggregates containing `const` would be excluded since they cannot be the subject of assignments!
* A Suggested Technical Corrigendum was composed, and follows. It is not yet a Proposed Technical Corrigendum due to the following unresolved discussion points.
* In 6.5.2.2p2 change:

  If the expression that denotes the called function has a type that includes a
  prototype, the number of arguments shall agree with the number of parameters.
  Each argument shall have a type such that its value may be assigned to an object
  with the unqualified version of the type of its corresponding parameter.

  to

  If the expression that denotes the called function has a type that includes a
  prototype, the number of arguments shall agree with the number of parameters.
  Each argument shall have a type such that its value may be used to initialize an
  object having the type of its corresponding parameter.

  In 6.5.2.2p4 change

  An argument may be an expression of any complete object type. In preparing for
  the call to a function, the arguments are evaluated, and each parameter is
  assigned to the value of the corresponding argument.

  to

  An argument may be an expression of any complete object type. In preparing for
  the call to a function, the arguments are evaluated, and each parameter is
  initialized to the value of the corresponding argument.
* It is not clear yet whether there are issues around conversions with respect to this change since this is actual practice that we are intending to simply reflect and to not introduce new constraints.
* This change might be augmented by a new example along the lines of, say, 6.5.16.1 example 3\.

Apr 2014 meeting

### Committee Discussion

> The issue of conversion has to do with whether there are differing promotions
> and type conversions that would apply when constructing an argument list that
> would not occur if these expressions were used as initializers in a declaration.

Oct 2014 meeting

### Committee Discussion

> The committee concluded after a discussion that there were no promotion or type
> conversion issues raised by the proposed wording above, and that the following
> should be adopted as a Proposed Technical Corrigendum.

### Proposed Technical Corrigendum (superceded)

In 6.5.2.2p2 change:

> If the expression that denotes the called function has a type that includes a
> prototype, the number of arguments shall agree with the number of parameters.
> Each argument shall have a type such that its value may be assigned to an object
> with the unqualified version of the type of its corresponding parameter.

to

> If the expression that denotes the called function has a type that includes a
> prototype, the number of arguments shall agree with the number of parameters.
> Each argument shall have a type such that its value may be used to initialize an
> object having the type of its corresponding parameter.

In 6.5.2.2p4 change

> An argument may be an expression of any complete object type. In preparing for
> the call to a function, the arguments are evaluated, and each parameter is
> assigned the value of the corresponding argument.

to

> An argument may be an expression of any complete object type. In preparing for
> the call to a function, the arguments are evaluated, and each parameter is
> initialized to the value of the corresponding argument.

Apr 2015 meeting

### Committee Discussion

> The goal of preserving conversions as if by assignment is fulfilled by the
> definition of initialization found in **6.7.9 Initialization** paragraph 11\.
> Another instance of assignment that should be changed was found in **6.9.1
> Function Definitions** paragraph 11\.
>
> It was noted that implicit conversion is described only in terms of assignment
> (6.5.16.1). There was broad agreement that committee members and implementors
> are unconfused by the intent of the standard here despite the inconsistencies.
> It was also noted that initialization is distinct from assignment and, in the
> case of non-lock free atomic implications, this requires operational differences
> and as such that it is worth further consideration. As such, the following
> should be regarded as a possible direction.
>
> In 6.5.2.2p2 change:
>
> > If the expression that denotes the called function has a type that includes a
> > prototype, the number of arguments shall agree with the number of parameters.
> > Each argument shall have a type such that its value may be assigned to an object
> > with the unqualified version of the type of its corresponding parameter.
>
> to
>
> > If the expression that denotes the called function has a type that includes a
> > prototype, the number of arguments shall agree with the number of parameters.
> > Each argument shall have a type such that its value may be used to initialize an
> > object having the type of its corresponding parameter.
>
> In 6.5.2.2p4 change
>
> > An argument may be an expression of any complete object type. In preparing for
> > the call to a function, the arguments are evaluated, and each parameter is
> > assigned the value of the corresponding argument.
>
> to
>
> > An argument may be an expression of any complete object type. In preparing for
> > the call to a function, the arguments are evaluated, and each parameter is
> > initialized to the value of the corresponding argument.
>
> In 6.9.1 paragraph 11 change:
>
> > After all parameters have been assigned,
>
> to
>
> > After all parameters have been initialized,

Oct 2015 meeting

### Committee Discussion

* The committee no longer believes that any of the issues raised in this report warrant changes to the standard.
* The difference in behavior on return value semantics cited in gcc has been resolved by a bug fix to gcc
* Qualifiers on the return type of a function are superfluous since by resolution to [DR 423](issue0423.md) the committee affirms that qualifiers are dropped as part of the evaluation of expressions including function calls.
* The committee does agree that the use of “assignment” to describe the initialization of function parameters can be misleading, but that in fact there is not an implementation that has ever been misled. Careful reading of the Standard notes that initialization is described fundamentally “as if by assignment”, and that it would take a comprehensive review and edit of the Standard to possibly achieve a more consistent treatment of the topics. There is a danger of circularity that must be avoided as well.

### Proposed Committee Response

> The committee believes that the primary issue of return value semantics was a
> consequence of a mistake in the implementation of `gcc` which has been
> rectified, and that further the treatment of qualifiers has been clarified in
> the Proposed Technical Corrigendum of [DR 423](issue0423.md). The treatment of
> initialization in the Standard is clear enough that no errors have been observed
> in implementations, and as such further clarification is unwarranted at this
> time.
