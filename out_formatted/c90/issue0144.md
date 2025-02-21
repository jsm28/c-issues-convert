## Issue 0144: Can the white space preceeding the initial `#` of a preprocessing directive be derived from macro expansion?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_144.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_144.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 028: Preprocessing of preprocessing directives

Can the white space preceding the initial `#` of a preprocessing directive be
derived from macro expansion? Consider the following code extract:

```c
#define EMPTY
 # EMPTY include <file.h>  /* Line A */
 EMPTY # include <file.h>  /* Line B */
```

Line A is clearly forbidden by subclause 6.8:

> The preprocessing tokens within a preprocessing directive are not subject to
> macro expansion unless otherwise stated.

However, this text does not appear to forbid line B. Nor does subclause 6.8.3.4:

> The resulting completely macro-replaced preprocessing token sequence is not
> processed as a preprocessing directive even if it resembles one. If that
> subclause applies only to the expansion of `EMPTY`, it is not relevant. If it
> applies to both the expansion and the following preprocessing token sequence,
> then no subsequent preprocessing directive could ever be processed.

Is line B strictly conforming, or does it violate a constraint (and if so,
which), or does it cause undefined behavior?

### Suggested Technical Corrigendum:

In subclause 6.8 Description, change:

> A preprocessing directive consists of a sequence of preprocessing tokens that
> begins with a \# preprocessing token that is either ...

to:

> A preprocessing directive consists of a sequence of preprocessing tokens that
> begins with a \# preprocessing token that (at the start of translation phase 4,
> before any preprocessing takes place) is either ...

---

Comment from WG14 on 1997-09-23:

### Suggested Future Change

The current C Standard has correct meaning, but the wording could be clearer. We
suggest the following change for the revised C Standard:

> A preprocessing directive consists of a directive consists of a sequence of
> preprocessing tokens that begins with a `#` preprocessing token that (at the
> start of translation phase 4\) is either ...
