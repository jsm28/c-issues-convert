## Issue 0086: At object-like macros in system headers conforming?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_086.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_086.html)

Item 23 \- object-like macros in system headers

Consider an implementation where `<string.h>` defines the macro `strlen` thus:

```c
#define strlen  __internal_fast_strlen
```

and declares functions (defined elsewhere) called `__internal_fast_strlen` and
`strlen`, both with the functionality of `strlen` in subclause 7.11.6.3. Is such
an implementation conforming with respect to the rules of subclause 7.1.7?

Note that a strictly conforming application can detect this situation by
comparing the value of the expression `strlen` taken before and after a
`#undef`.

---

Comment from WG14 on 1997-09-23:

### Response

The question asks whether a system header can define the name of a library
function as an object-like macro, and cites subclause 7.1.7 as not using the
term “function-like.”

The Committee notes the absence of this term, but also notes that subclause
7.1.7 requires that the macro definition always be suppressed when not followed
by an open parenthesis. Therefore such macros must either be function-like, or
the implementation must cause them to act as function-like macros.
