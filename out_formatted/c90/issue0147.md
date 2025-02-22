## Issue 0147: Is there a requirement for a sequence point to occur within a library function?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_147.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_147.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 031: Sequence points in library functions

There is no requirement for a sequence point to occur within a library function,
since it might not be written in C. Consider the following code:

```c
#include <string.h>
 char s[10];
 /* ... */
 (strcpy)(s, "Testing") [0] = 'X';
```

Any function written in C must have a sequence point after the last full
expression evaluated (which will be the returned value if there is one), so if
`strcpy` were a C function, the assigning of `'T'` to `s[0]` would be completed
before the call returned.

However, since library functions might not be written in C, they might not have
such a sequence point. If not, then the above statement is in breach of the
requirements of the second paragraph of subclause 6.3.

### Suggested Technical Corrigendum:

Add to the end of subclause 7.1.7:

There is a sequence point immediately before a library function returns.

Add to the end of annex C:

Immediately before a library function returns (7.1.7).

Add a reference to 7.1.7 in the **Forward References** of 5.1.2.3, and in the
relevant **Index** entry.

---

Comment from WG14 on 1997-09-23:

### Response

We agree that the current wording does not make this clear. The next revision of
the C Standard will clarify that every function return is a sequence point. The
suggested changes will be used.
