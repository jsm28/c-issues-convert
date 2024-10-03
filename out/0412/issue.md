### Summary

It appears that `#elif` is not entirely equivalent to `#else`, `#if`, and
`#endif`.

Consider the code:

> ```c
> #if 1
> ...
> #else
> #if this is not a valid expression
> ...
> #endif
> #endif
> ```

This is well-defined. Since the controlling expression of the `#if` evaluates to
true, the `#else` group is skipped and thus the nested `#if` is only processed
through the directive name (6.10.1p6).

However, if this is recast using `#elif`:

> ```c
> #if 1
> ...
> #elif this is not a valid expression
> ...
> #endif
> ```

the `#elif` is not part of a group that is skipped and thus must be processed
completely, including evaluating the controlling condition (even though the
resulting value is of no interest).

I do not believe this was the committee's intent.

### Suggested Technical Corrigendum

In 6.10.1p6, change:

> Only the first group whose control condition evaluates to true (nonzero) is
> processed.

to:

> Only the first group whose control condition evaluates to true (nonzero) is
> processed; any following groups are skipped and their controlling directives are
> processed as if they were in a group that is skipped.
