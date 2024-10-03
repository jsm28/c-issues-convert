Scope and uniqueness of `size_t`

Subclause 6.3.3.4 on page 45, lines 1-2 says: “... and its type (...) is
`size_t` defined in the `<stddef.h>` header.” This line could be read as either
of the following:

1. “... and its type is `size_t` which happens to be defined in `stddef.h`.”
2. “... and its type is the `size_t` defined in `stddef.h`.”

(It was probably intended as a helpful piece of information only.) So what does
the compiler do?

In (1) the compiler has to define a `size_t` in some outer scope. This
definition does not make `size_t` visible, but gives a type to the return value
of `sizeof`. Now if the programmer defines a typedef making `size_t` synonymous
with `float` (say) then the compiler now has to use this new type. This
interpretation does not require the programmer to include `<stddef.h>` in order
to use `sizeof`.

In (2) the compiler picks up the type `size_t` from `<stddef.h>` (assuming that
the user included this header). Should the compiler give a diagnostic if this
header was not included and `sizeof` was used? A subsequent typedef for `size_t`
does not affect the type of the result of `sizeof`.

These problems do not arise with `int`, et al. because they are keywords. Thus
“`typedef float int`” would give a syntax error and need not be considered
semantically.

According to subclause 6.3.3.4, page 45, `sizeof` has type `size_t`. What
happens if the type of `size_t` does not match what the compiler thinks is the
type of `sizeof`?
