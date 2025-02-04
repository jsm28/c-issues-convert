## Issue 0206: Default argument conversion of `float _Complex`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 1999-09-13  
Reference document: [ISO/IEC WG14 N892](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n892.htm)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_206.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_206.htm)

### Summary

For consistency with real floating types, the type `float _Complex` should be
promoted by the default argument promotions to `double _Complex`.

### Suggested Technical Corrigendum

Change 6.5.2.2p6 in part, from:

> and arguments that have type `float` are promoted to `double`.

to:

> and arguments that have a corresponding real type of `float` are promoted,
> without change of type domain, to a type whose corresponding real type is
> `double`.

---

Comment from WG14 on 2001-09-18:

### Committee Response

This was intentional because real float promotion to double is in Standard C
purely for compatibility with K\&R. Since complex is new, that compatibility is
not an issue, and having it behave like real float would introduce undesired
overhead (and be less like Fortran).

The following words were added the Rationale.

> `float _Complex` is a new type with C99. It has no need to preserve promotions
> needed by pre-ANSI-C. It does not break existing code.
