## Issue 0160: It is unclear what applications can and cannot do with identifiers that are reserved?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_160.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_160.html)

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

---

Comment from WG14 on 1997-09-23:

### Suggested Future Change

In subclause 7.1.3, Reserved Identifiers, change bullet 2 to:

> All identifiers that begin with an underscore are always reserved for use as
> macros and as identifiers with file scope in both the ordinary and tag name
> spaces.

Change bullet 5 to:

> Each identifier with file scope listed in any of the following subclauses
> (including the Future library directions) is reserved for use as a macro and as
> an identifier with file scope in the same name space if any of its associated
> headers is included.
