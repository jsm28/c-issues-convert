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
