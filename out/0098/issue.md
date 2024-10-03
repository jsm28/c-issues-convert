ANSI/ISO C Defect report #rfg5:

Subclause 6.3.3.4 provides the following constraint:

> The `sizeof` operator shall not be applied to an expression that has function
> type or an incomplete type...

The logical implication of this constraint is that neither function types nor
incomplete types have “sizes” per se, at least not as far as the C Standard is
concerned.

I have noted however that neither subclause 6.3.2.4 **Postfix increment and
decrement operators** nor subclause 6.3.3.1 **Prefix increment and decrement
operators** contain any constraints which would prohibit the incrementing or
decrementing of pointers to function types or pointers to incomplete types.

I believe that this logical inconsistency needs to be addressed (and rectified)
in the C Standard. It seems that the most appropriate way to do this is to add
the following additional constraint to subclause 6.3.2.4:

> The operand of the postfix increment or decrement operator shall not have a type
> which is a pointer to incomplete type or a pointer to function type.

Likewise, the following new constraint should be added to subclause 6.3.3.1:

> The operand of the prefix increment or decrement operator shall not have a type
> which is a pointer to incomplete type or a pointer to function type.
