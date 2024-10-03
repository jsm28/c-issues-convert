### Summary

What the heck is a "generic function", and what are the sections of the standard
covering how a user (or implementor) can write a stardard conforming program
defining a "type generic function"?

I was trying to reconcile the rules in 7.1.4 Use of library functions allowing
an implementation to define a function as a macro, and the user suppressing the
macro by enclosing the name of the function in parentheses. But, I don't see how
to make a function declaration, where a parameter can be any atomic type.

I've convinced myself, generic functions will take compiler magic. There is no
way to declare them using C standard conforming code. Just like the type generic
macros of \<tgmath.h\> in C99.

Somehow I missed this. I remember all the discussion of adding atomic operation
to operators like \+\= but somehow I missed the fact we were again adding in
function specifications that cannot be implemented using standard C. I thought
we were adding type generic macros. Sigh ...

I've been told that the discussion included talk about a proposal to recast them
as generic macros, but that never happened so we ended up with generic functions
through the back door without much explication.

### Suggested Technical Corrigendum

Redefine the atomic type generic functions as type generic macros. Define the
underlying functions to which the type generic macros expand.
