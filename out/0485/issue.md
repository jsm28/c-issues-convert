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
