*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 026: Reservation of macro names

Is it permitted to `#undef` a reserved macro name? Consider the translation
unit:

```c
#include <errno.h>
 #undef EASTER
 #undef EDOM
 #undef __ERRNO_BASE
 int error (void) { return errno == ERANGE; }
```

Considering each of the three `#undef` directives independently, is each
directive permitted in a strictly conforming program? Is the translation unit
strictly conforming?

Subclause 7.1.3 describes various classes of reserved identifiers, and then
states:

> If the program declares or defines an identifier with the same name as an
> identifier reserved in that context (other than as allowed by 7.1.7), the
> behavior is undefined.

However, this does mention the use of `#undef`. Subclause 7.1.7 does so, for
certain identifiers, but in rather ambiguous words:

> The use of `#undef` to remove any macro definition will also ensure ...

It has been suggested that this wording merely describes a strictly conforming
coding technique, rather than establishing a special case (rather like the
wording about placing the name in parentheses does).

Therefore, can a strictly conforming program `#undef` a name which is reserved
for any use at that point?

There is a good reason to allow such an `#undef`. A program can make use of a
identifier which is convenient but would otherwise be reserved (for example, the
identifier `EASTER`). There is also a good reason to forbid it: the macro
`ERANGE` might actually be defined as (`__ERRNO_BASE + 42`). This leads to the
conclusion that it might be best to permit it for some names but not others.

A further example \[inserted at the request of BSI] is the translation unit:

```c
#include <stdlib.h>
 #undef __INCLUDED_STDLIB_H
 #include <stdlib.h>
```

### Suggested Technical Corrigendum:

Add to the end of subclause 7.1.3:

If the program removes (with `#undef`) the macro definition of an identifier in
the first group listed above, the behavior is undefined.
