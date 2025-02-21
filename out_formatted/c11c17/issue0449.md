## Issue 0449: What is the value of TSS\_DTOR\_ITERATIONS for implementations with no maximum?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Douglas Walls  
Date: 2013-08-24  
Reference document: [N1744](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1744.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

### Suggested Technical Corrigendum

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

### Committee Discussion

* The committee notes that existing practice in all cases has provided a small integer value for this definition.
* Allowing no restrictions is likely to break existing practice.

Apr 2014 meeting

### Committee Discussion

> The question posed should be answered.

### Proposed Committee Response

> The standard intentionally does not define a value of `TSS_DTOR_ITERATIONS` for
> implementations with no maximum.
>
> The `TSS_DTOR_ITERATIONS` macro is used to limit recursion at thread
> termination. The issue is that existing practice allows the creation of new
> `tss` bindings during the destructor call, and one destructor might reincarnate
> the original, thus forming an infinite recursive destructor loop. This loop may
> appear non-deterministically and is difficult to detect. The purpose of
> `TSS_DTOR_ITERATIONS` is as a bound to such recursion.
>
> It is possible monitor the recursion depth with careful defensive programming
> and in those cases the value of `TSS_DTOR_ITERATIONS` is useful as that bound.
