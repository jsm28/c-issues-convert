### Summary

6.7.2.4 Atomic type specifiers, has in paragraph 2:

> Atomic type specifiers shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).

But, 6.7.3 Type qualifiers, has no similar constraint with respect to \_Atomic.

Also, 7.17.6 Atomic integer types, has no similar constraint. Aside: The only
constraints I see in the library are in \<float.h\> and \<limits.h\>, so it is
not clear if this case should be a constraint.

### Suggested Technical Corrigendum

Add to 6.7.3 Type qualifiers, a new paragraph after paragraph 3,

> Atomic type qualifiers shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).

Add to 7.16.6 Atomic integer types, a new paragraph before paragraph 1:

> Constraints
> 
> Atomic type names shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).
