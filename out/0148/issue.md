*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 032: Defining library functions

Subclause 7.1.7 is unclear about when it is permitted to declare a library
function. Consider the following translation unit:

```c
#include <math.h>
 double (sin)(double);
```

Subclause 7.1.7 states in part:

Any function declared in a header may be additionally implemented as a macro
defined in the header, so a library function should not be declared explicitly
if its header is included.

Since the wording uses the term "should", this does not appear to actually be a
requirement on programs, and the code appears to be strictly conforming; in
other words, the C Standard here simply uses overly restrictive wording while
trying to assist readers, and does not actually forbid the above code.

Is this interpretation correct?

Note that code such as the above is useful if the `#include` is conditionally
compiled or is within a header not under the control of the code's author.

### Suggested Technical Corrigendum:

If the intent was to forbid such a declaration, then change the quoted text to:

A library function shall not be declared explicitly if its header is included.

If the intent was to allow the macros described in subclause 7.1.7 to be
object-like macros (though other wording in 7.1.7 appears to forbid this), then
change the quoted text to:

A library function must not be declared explicitly if its header is included,
unless any macro definition of the name has been removed with `#undef`.

If the intent was to allow the example declaration, then change the quoted text
to:

Any function declared in a header may be additionally implemented as a macro
defined in the header, so one of the techniques below should be used to ensure
that any explicit declaration of a library function is not affected by any such
macro.
