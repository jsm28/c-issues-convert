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
