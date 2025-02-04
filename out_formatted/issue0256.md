## Issue 0256: multiple inclusion of headers

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_256.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_256.htm)

### Problem

Consider the code:

```c
   #include <stdio.h>     // Line 1
    #undef FOPEN_MAX       // Line 2, permitted by 7.1.3#3    #include <stdio.h>     // Line 3    #ifdef FOPEN_MAX       // Line 4
```

7.1.2 says:

> \[#4] Standard headers may be included in any order; each may be included more
> than once in a given scope, with no effect different from being included only
> once, except that the effect of including `<assert.h>` depends on the definition
> of `NDEBUG` (see 7.2).

Does "with no effect different" mean:

1. the includes on lines 1 and 3 have the same effect, so at line 4 the macro `FOPEN_MAX` is defined;
2. the include on line 3 has no effect, so that at line 4 the macro `FOPEN_MAX` is undefined;
3. something else ?

Most current implementations wrap the contents of headers with an "idempotent
guard", such as:

```c
   #ifndef _STDIO_H_INCLUDED_
    #define _STDIO_H_INCLUDED_
    // Real contents go here   #endif
```

This will provide behaviour (2), which I would suggest is the most desirable.

Furthermore, the concept of scope doesn't apply here, both because includes
happen during preprocessing and because there is a requirement in the same
paragraph that:

> If used, a header shall be included outside of any external declaration or
> definition,

If the wording is being altered, this would be a good opportunity to fix this as
well.

### Suggested Technical Corrigendum

Change the first sentence of 7.1.2#4 to:

> \[#4] Standard headers may be included in any order; each may be included any
> number of times in a preprocessing translation unit. The second and subsequent
> occurrences of a given header shall be ignored, except in the case of
> `<assert.h>` (where the behaviour is defined in subclause 7.2).

---

Comment from WG14 on 2002-03-06:

### Committee Response

The Committee believe that both answer 1 and 2 are allowed, and does not see a
compelling reason to change this.
