## Issue 0485: Problem with the specification of `ATOMIC_VAR_INIT`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jens Gustedt  
Date: 2015-08-07  
Reference document: [N1951](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1951.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The current version of the standard states that the argument to this macro
should be a value of the corresponding base type of the atomic object that is to
be initialized.

> The `ATOMIC_VAR_INIT` macro expands to a token sequence suitable for
> initializing an atomic object of a type that is initialization-compatible with
> value.

This is problematic, because it excludes the primary form of initializers, the
`{ }` form, from the possible uses, that would be necessary to initialize
`struct` or `union` types properly.

**Problem discussion**

As a consequence, there is a problem for atomic objects that combine the two
properties:

1. The base type is a `struct` or `union` type.
2. The object has static or thread-local storage duration.

The problem is, that for such types there are no compile time constants that
could be used as *value*, here. As a consequence the standard *doesn't allow
explicit initialization* for these objects.

1. Atomic objects of `struct` or `union` type and static or thread-local storage duration can only be default initialized.
2. At program and thread startup, respectively, atomic objects of `struct` or `union` type and static or thread-local storage duration are in an indeterminate state.

This is an important drawback that doesn't seem to be intentional:

* The `ATOMIC_VAR_INIT` had exactly been introduce for the purpose of initializing objects of static storage to a valid state with known value.
* `struct` atomics play an important role for lock-free data structures to avoid the ABA problem.

**Current practice**

Both compilers that I have my hands on (gcc 4.9 and clang 3.6) that implement
`<stdatomic.h>` have something equivalent to

```c
#define ATOMIC_VAR_INIT(VALUE)  (VALUE)
```

This is of course conforming to the standard text as it is now, but exhibit the
exact problem. They don't allow for a compile time initializer since the `()`
around `VALUE` result in invalid syntax if `VALUE` is a `{ }` initializer.

Clang has an implementation specific way out of this: they allow compound
literals with constant initializers in that context. Gcc provides no such
solution.

For both compilers, it is easily possible to overwrite the macro definition into
one that omits the parenthesis and all works fine.

### Suggested Technical Corrigendum

Change the beginning of the corresponding section, 7.17.2.1p2, to:

<ins>7.17.2.1 The `ATOMIC_VAR_INIT` macro  
**Synopsis**</ins>

<ins>`#include <stdatomic.h>`  
`#define ATOMIC_VAR_INIT(initializer)`</ins>

<ins>**Description**  
The `ATOMIC_VAR_INIT` macro expands to a token sequence suitable for
initializing an atomic object `X`. For any invocation of this macro, the
*initializer* argument shall expand to a token sequence that would be suitable
to initialize `X` if the atomic qualification would be dropped.**footnote**That
is, it could be used to initialize an object `Y` of the same base type, storage
duration and place of declaration as `X`, but without atomic qualification.**end
footnote**  
An atomic object with automatic storage duration ...</ins>

Then append a new note after the actual para 4:

<ins>*Note:* Since *initializer* may be a token sequence that contains commas
which are not protected by `()` it may constitute a variable number of arguments
for the macro evaluation. Implementations should be able to deal with such
situations by defining `ATOMIC_VAR_INIT` as accepting a variable argument
list.</ins>

---

Comment from WG14 on 2017-11-03:

Oct 2015 meeting

### Committee Discussion

* The fundamental issue is the apparent inability to initialize atomic structures or unions due to the definition of the `ATOMIC_VAR_INIT` macro as taking a single argument. Some implementations have already taken the liberty of treating the macro as variadic for purposes of atomic structure initialization and moreover to also implicitly provide surrounding `{` and `}` that form the syntax for a structure initializer or compound literal as appropriate to the implementation.
* The committee agrees with the sentiment expressed in the suggested NOTE although the wording was not discussed.
* The suggested changes to 7.17.2.1 were not acceptable to the committee, however, and may not be needed at all since, in particular the declared type `C` is already the non-atomic version of the atomic type `A` of the variable being initialized. Use of the term “base type” is undefined in C for example.
* The committee requests that the author take this input under advisement in a new solicited paper that would, in effect, make explicit the extended practice.

Apr 2016 meeting

### Committee Discussion

> A short paper was provided with a Suggested Technical Corrigendum and, although
> close, more work was solicited from the authors. The direction discussed by the
> committee was given that in the section `C` is defined to be the non-atomic
> equivalent of type `A`,
>
> * new wording must be provided to say it takes an initializer for an object of type `C`, and the macro expands to an object of type `A`, and that
> * the macro can be defined as in the Suggested Technical Corrigendum:
>
>   ```c
>       #define ATOMIC_VAR_INIT(...)
>   ```

Oct 2016 meeting

### Committee Discussion

> The definition of `ATOMIC_VAR_INIT` as a macro is problematic. Several
> implementations use locks introduced by compiler magic for larger structures and
> the macro cannot provide for the proper initialization of a lock that is not
> visible. For these and other implementations, `ATOMIC_VAR_INIT` should be fully
> implemented as compiler magic.
>
> Since removing the definition of the macro is outside the scope of a DR, this
> issue may only be addressable in a future revision of the standard.

Apr 2017 meeting

### Committee Discussion

> Although discussed at the last meeting, the point that there are no known
> implementations using *embedded* locks was not accurately reflected in the prior
> discussion. Atomic structures may still differ in size due to potentially
> increased alignment requirements. It was further noted that some implementations
> use "compiler magic" at initialization time.
>
> Since the macro definition is neither necessary nor sufficient for structures,
> the email [(SC22WG14.14645) DR 485 wording for TC
> 2017](https://www.open-std.org/jtc1/sc22/wg14/14645) containing two suggested
> technical corrigenda was discussed at some length. Neither change, however, is
> appropriate as a technical corrigendum, and as such this issue cannot be
> addressed using the Defect Report process.

### Proposed Committee Response

> The `ATOMIC_VAR_INIT` macro was added to the standard without wide
> implementation experience with the intent being to allow implementations to use
> embedded locks in atomic types. It was not, however, well formulated to
> accommodate the extension of atomics to structures since it would, perhaps,
> require variadic arguments. No known implementations use embedded locks,
> however, and as such there is no technical requirement for the use of the
> `ATOMIC_VAR_INIT` macro.
>
> Correcting this is beyond the scope of the Defect Report process.
>
> There was consensus in the committee to deprecate this macro in the next
> revision of the standard. The following words, drawn from [(SC22WG14.14645) DR
> 485 wording for TC 2017](https://www.open-std.org/jtc1/sc22/wg14/14645), are the
> proposed direction:
>
> In §7.17.2.1 replace paragraph 2 with:
>
> > An atomic object with automatic storage duration that is not explicitly
> > initialized is initially in an indeterminate state.
