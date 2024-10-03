Subclause 6.8.3: Empty arguments to function-like macros I would like to make a
request for clarification and a request for a stronger statement of
standardization. Given

```c
#define macro( xx ) xx
         macro()
```

is this a constraint violation of subclause 6.8.3 **Constraints** paragraph 4:

> The number of arguments in an invocation of a function-like macro shall agree
> with the number of parameters in the macro definition, ...

or is this an undefined, implementation-dependent program \- subclause 6.8.3,
**Semantics** paragraph 5:

> If (before argument substitution) any argument consists of no preprocessing
> tokens, the behavior is undefined.

In connection with the above I would request that the Committee make a much
stronger statement as to whether empty arguments are to be treated as valid
arguments or are to be treated as errors. They can have their uses, but if that
is recognized then it should be standardized; if not, it should not be allowed.
