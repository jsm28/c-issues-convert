C11, section 6.8.5 paragraph 6 reads:

> An iteration statement whose controlling expression is not a constant
> expression,156) that performs no input/output operations, does not access
> volatile objects, and performs no synchronization or atomic operations in its
> body, controlling expression, or (in the case of a for statement) its
> expression-3, may be assumed by the implementation to terminate.157)

Question: to what does the *that* refers back to: to the *controlling
expression* or to the *constant expression*?
