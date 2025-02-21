## Issue 0095: Are the initialization constraints clear?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_095.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_095.html)

ANSI/ISO C Defect report #rfg2:

There is an ambiguity with respect to the constraints which may (or may not)
apply to initializations.

Subclause 6.5.7 says:

> ... the same type constraints and conversions as for simple assignment apply,
> ...

Note however that this rule itself appears within a **Semantics** section, thus
leading some implementors to feel that no diagnostics are required in cases
where an attempt is made to provide an initializer for a given scalar and where
the type of the initializer is *not* assignment compatible with the type of the
scalar object being initialized. This ambiguity should be removed by adding an
explicit constraint to the section covering initializations, such as:

> Each scalar initializer expression given in an initializer shall have a type
> such that its value may be assigned to an object with the unqualified version of
> the corresponding scalar object to be initialized by the given scalar
> initializer expression.

(This roughly mirrors the existing constraint on parameter matching imposed upon
calls to prototyped functions.)

---

Comment from WG14 on 1997-09-23:

### Response

An explicit constraint is not required in the initializer section. Early on, the
Committee decided that if a behavior was described as being equivalent to
another construct, all of the constraints of that construct would apply. This
“chaining” process means that any violation of a constraint in any section
referred to explicitly or by the phrases “equivalent behavior” or “as if” will
generate a diagnostic.

The constraints in the section on simple assignment (subclause 6.3.16.1) are
sufficient to assure type compatibility of the object and the initializer.
