### Summary

Section **7.17.1 Introduction** (to section **7.17 Atomics** `<stdatomic.h>`)
specifies that the `<stdatomic.h>` header define a number of macros having the
form `ATOMIC_XXX_LOCK_FREE` that indicate the lock-free property of the
corresponding atomic types. No further description of the macros is provided
here.

Section **7.17.5 Lock-free property**, then goes on to specify that the atomic
lock-free macros (presumably the same ones as those listed in 7.17.1) expand to
one of three values: 0, 1, or 2\.

Neither of the two sections above, nor any other in the standard, specifies
whether or not the macros are required to expand to constant expressions usable
in preprocessor `#if` directives. This is in contrast to some other standard
macros such as those defined in `<limits.h>` which are typically so specified
using language such as:

> The values given below shall be replaced by constant expressions suitable for
> use in `#if` preprocessing directives.

As discussed in the thread starting with SC22WG14.13216, the only purpose for
the existence of the `ATOMIC_XXX_LOCK_FREE` macros is to be able to write more
efficient code by relying on their use in preprocessor `#if` conditionals. Thus,
the absence of the requirement that they expand to constant expressions makes
the macros unsuitable for that purpose.

### Suggested Technical Corrigendum

In section 7.17.1, modify paragraph 3 as indicated below:

> ...which <u>expand to constant expressions suitable for use in `#if`
> preprocessing directives and which</u> indicate the lock-free property of the
> corresponding atomic types (both signed and unsigned); and
