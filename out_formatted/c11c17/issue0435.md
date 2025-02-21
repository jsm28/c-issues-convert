## Issue 0435: Missing constraint w.r.t. Imaginary

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred J. Tydeman (USA)  
Date: 2012-10-26  
Reference document: [N1661](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1661.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

> The type specifier \_Complex shall not be used if the implementation does not
> support complex types (see 6.10.8.3).

But, G.2 Types, has no similar constraint with respect to \_Imaginary.

### Suggested Technical Corrigendum

Add to G.2 Types, a new sentence in paragraph 1:

> The \_Imaginary type specifier shall not be used if the implementation does not
> support imaginary types (see 6.10.8.3).

---

Comment from WG14 on 2014-10-31:

Oct 2013 meeting

### Committee Discussion

> This is not actually a defect.

### Proposed Committee Response

> Annex G requires `_Imaginary` be supported, so there is no need to cite a
> requirement for when it is not supported.
