## Issue 0017.07: What is the scope and uniqueness of `size_t`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Cross-references: [0047](../c90/issue0047.md), [0050](../c90/issue0050.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citations are subclause 6.3.3.4

> The value of the result is implementation-defined, and its type (an unsigned
> integral type) is `size_t` defined in the `<stddef.h>` header.

and subclause 7.1.6

> The types are ...
>
> ```c
> size_t
> ```
>
> which is the unsigned integral type of the result of the `sizeof` operator; ...

These sections, both separately and together, define the relationship between
the result type of `sizeof` and the type `size_t` defined in `stddef.h`. The
result type of `sizeof` and the type `size_t` defined in `stddef.h` are an
unsigned integral type, and `size_t` defined in `<stddef.h>` is identical to the
result type of `sizeof`. To restate, in a conforming implementation, the result
type of `sizeof` will be the same as the type of `size_t` defined in
`<stddef.h>`.

Since these two types are the same, there need be no mechanism for a compiler to
discover the type of `size_t` defined in `<stddef.h>`. A compiler's private
knowledge of the result type of `sizeof` is as good as `stddef.h`'s private
knowledge of the type of `size_t`.

Note that the result of `sizeof` has the same type as not just any `size_t,` but
the `size_t` defined in `<stddef.h>`.
