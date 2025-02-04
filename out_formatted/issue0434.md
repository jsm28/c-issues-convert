## Issue 0434: Missing constraint w.r.t. Atomic

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred J. Tydeman (USA)  
Date: 2012-10-26  
Reference document: N1660 [N1660](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1660.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

6.7.2.4 Atomic type specifiers, has in paragraph 2:

> Atomic type specifiers shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).

But, 6.7.3 Type qualifiers, has no similar constraint with respect to \_Atomic.

Also, 7.17.6 Atomic integer types, has no similar constraint. Aside: The only
constraints I see in the library are in \<float.h\> and \<limits.h\>, so it is
not clear if this case should be a constraint.

### Suggested Technical Corrigendum

Add to 6.7.3 Type qualifiers, a new paragraph after paragraph 3,

> Atomic type qualifiers shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).

Add to 7.16.6 Atomic integer types, a new paragraph before paragraph 1:

> Constraints
>
> Atomic type names shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

* The committee agrees to the first additional constraint.
* The second constraint is not required due to 7.17 paragraph 2\.

### Proposed Technical Corrigendum

Add to 6.7.3 Type qualifiers, a new paragraph after paragraph 3,

> Atomic type qualifiers shall not be used if the implementation does not support
> atomic types (see 6.10.8.3).
