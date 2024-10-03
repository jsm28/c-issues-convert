*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 008: Reservation of identifiers

The C Standard is unclear in its description of what applications can and cannot
do with identifiers that are reserved to the implementation for certain uses.

Subclause 7.1.3 reads in part:

Each identifier with file scope listed in any of the following subclauses
(including the future library directions) is reserved for use as an identifier
with file scope in the same name space if any of its associated headers is
included.

Does this include reservation as macros? In particular, is the following code:

```c
#include  <stddef.h>
 #define size_t 42
```

strictly conforming, or could it cause a redefinition of the macro `size_t`?
Similarly, can another macro legitimately defined by `stddef.h` (such as
`offsetof`) include `size_t` in its replacement list, so that:

```c
#include  <stddef.h>
 #undef size_t
 #define size_t 42
  /* ... */
 offsetof (struct_type, field)
```

fails to expand correctly? It is not clear how the wording of Footnote 91
applies, and this is in any case not part of the C Standard (except in Australia
:-).
