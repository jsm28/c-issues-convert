## Issue 0108: Is it conforming to allow macros to make keywords?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_108.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_108.html)

ANSI/ISO C Defect Report #rfg15:

Subclause 7.1.3 lists the set of reserved identifiers, but this list does not
include keywords (subclause 6.1.1).

Subclause 6.1.1 says (in a **Semantics** section):

> The above tokens (entirely in lower-case) are reserved (in translation phases 7
> and 8\) for use as keywords, and shall not be used otherwise.

Based upon the above named sections of the C Standard, I am forced to conclude
that the following code is strictly conforming. Is this a correct conclusion?

```c
#define double void
 #include <math.h>
 #undef double

 void example (double d1, double d2)
        {
        d1 = acos (d2);
        }
```

My impression is that few (if any) existing implementations now accept such
code. I am therefore inclined to believe that the Committee's true intentions
were that *all* keywords (as listed in subclause 6.1.1) should be considered to
be reserved identifiers, at least during translation phase 4, and at least while
processing `#include` directives which name standard include files provided by
the implementation (as listed in subclause 7.1.2).

I believe that the proper way to address this problem would be to add another
stipulation (regarding reserved identifiers) to subclause 7.1.2.1. This
additional stipulation might read as follows:

> If, during inclusion of any one of the standard headers listed in the preceding
> section (during translation phase 4\) any one of the keywords listed in
> subclause 6.1.1 is defined as a preprocessor macro, the behavior is undefined.

---

Comment from WG14 on 1997-09-23:

### Response

This program's behavior is undefined because of the restriction on inclusion of
standard headers in subclause 7.1.2:

The program shall not have any macros with names lexically identical to keywords
currently defined prior to the inclusion.

The Committee's intention was indeed to otherwise allow macros to mask keywords.
