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
