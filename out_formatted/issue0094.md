## Issue 0094: Is there an inconsistency between the constraints on passing values versus returning values?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_094.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_094.html)

ANSI/ISO C Defect report #rfg1:

There appears to be an inconsistency between the constraints on “passing” values
versus “returning” values. The constraints for function calls clearly indicate
that a diagnostic is required if any given actual argument is passed (to a
prototyped function) into a corresponding formal parameter whose type is not
assignment compatible with respect to the type of the passed value. In the case
of values returned by a return statement however, there seems to be no such
compatibility constraint imposed upon the expression given in the `return`
statement and the corresponding (declared) function return type.

A new constraint should be added to the C Standard like:

> If present, the expression given in a `return` statement shall have a type such
> that its value may be assigned to an object with the unqualified version of the
> return type of the containing function.

(This exactly mirrors the existing constraint on parameter matching imposed upon
calls to prototyped functions.)

---

Comment from WG14 on 1997-09-23:

### Response

The constraint in the description of the `return` statement is unneeded. Early
on, the Committee decided that if a behavior was described as being equivalent
to another construct, all of the constraints of that construct would apply. This
“chaining” process means that any violation of a constraint in any section
referred to explicitly or by the phrases “equivalent behavior” or “as if” will
generate a diagnostic.

The **Semantics** section of the `return` statement (subclause 6.6.6.4) states:
“If the expression has a type different from that of the function in which it
appears, it is converted as if it were assigned to an object of that type.” The
constraints in the section on simple assignment (subclause 6.3.16.1) are
sufficient to assure assignment compatibility of the two types.
