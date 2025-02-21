## Issue 0436: Request for interpretation of C11 6.8.5#6

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Willem Wakker (NL)  
Date: 2013-05-08  
Reference document: [N1713](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1713.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

C11, section 6.8.5 paragraph 6 reads:

> An iteration statement whose controlling expression is not a constant
> expression,156) that performs no input/output operations, does not access
> volatile objects, and performs no synchronization or atomic operations in its
> body, controlling expression, or (in the case of a for statement) its
> expression-3, may be assumed by the implementation to terminate.157)

Question: to what does the *that* refers back to: to the *controlling
expression* or to the *constant expression*?

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

> This is indeed an ambiguity, and after considering various proposals, the
> following was approved.

Apr 2014 meeting

### Committee Discussion

> The committee noted a typo in the Suggested Technical Corrigendum where "its
> expression \*157" was intended to be "its expression-3 \*157", and so has been
> corrected below.

### Proposed Technical Corrigendum

Replace 6.8.5 paragraph 6 with:

> An iteration statement may be assumed by the implementation to terminate if its
> controlling expression is not a constant expression \*156), and none of the
> following operations are performed in its body, controlling expression or (in
> the case of a for statement) its expression-3 \*157):
>
> * input/output operations
> * accessing a volatile object
> * synchronization or atomic operations.
