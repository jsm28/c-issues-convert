## Issue 0093: Can a conforming freestanding implementation reserve identifiers?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_093.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_093.html)

Item 30 \- reservation of identifiers

Can a conforming freestanding implementation reserve identifiers? Subclause
5.1.2.1 states that only one identifier (the equivalent of `main`) is reserved
in a freestanding implementation. Subclause 7.1.3 states that certain
identifiers are reserved, even when the corresponding headers are not included.
This is a direct contradiction.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee observes that conforming freestanding implementations tend to vary
widely in the library facilities provided, and that the simple binary choice
implied by the above text is really a continuum. It also notes that it is
difficult to provide a C implementation with no reserved names (not even those
beginning with two underscores). It is therefore felt to be unreasonable to
restrict the names available to implementors of freestanding implementations
compared with hosted implementations.

The Committee notes that certain freestanding programs (such as UNIX kernels)
have tended to use names such as `exit`, but agrees that existing practice
dictates that the authors of such programs must already be prepared to change
such names when using certain compilers.

### Correction

***In subclause 5.1.2.1, page 6, delete:***

There are otherwise no reserved external identifiers.
