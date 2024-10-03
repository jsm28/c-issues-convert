Reference: subclause 7.5.1 **Treatment of error conditions**, page 111, lines
14-17:

> For all functions, a *domain error* occurs if an input argument is outside the
> domain over which the mathematical function is defined. ... an implementation
> may define additional domain errors, provided that such errors are consistent
> with the mathematical definition of the function.

If `sin(DBL_MAX)` results in `errno` being set to `EDOM`, is this a violation of
the standard? If yes, what should be the result of this call?
