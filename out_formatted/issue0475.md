## Issue 0475: Misleading Atomic library references to atomic types

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Blaine Garst  
Date: 2015-04-15  
Reference document: [N1927](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1927.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The 7.17 atomic library section of the standard and the syntax for atomic types
arose from different authors. The library section was adopted first and then
amended when the syntax proposal was approved during the development of the C11
Standard. The syntax is constructive and applies, with a few exceptions, to all
types, including floats and bitfields.

There are a few unfortunate phrasings remaining in the **7.17 Atomics
\<stdatomic.h\>** section, however, that have caused a small degree of confusion
and are worth fixing.

### Suggested Technical Corrigendum

In **7.17.1 Introduction** p3 Replace

> and several atomic analogs of integer types.

with

> and atomic types declared with the \_Atomic or \_Atomic() construct.

In **7.17.1 Introduction** p5 Replace

> \- An A refers to one of the atomic types.

with

> \- An A refers to an atomic type.

In **7.17.6 Atomic Integer Types** paragraph 2 replace

> The semantics of the operations on these types are defined in 7.17.7

with

> The semantics of the operations on atomic types are defined in 7.17.7

---

Comment from WG14 on 2017-11-03:

Apr 2015 meeting

### Committee Discussion

> The first suggested change is incorrect since it is deliberately speaking of the
> types declared in `<std atomic.h>`.
>
> After discussion, the direction is
>
> In **7.17.1 Introduction** p5 replace
>
> > \- An A refers to one of the atomic types.
>
> with
>
> > \- An A refers to an atomic type.
>
> Delete 7.17.6 paragraph 2\.

Oct 2015 meeting

### Committee Discussion

> The committee accepts the proposed direction as the Proposed Technical
> Corrigendum.

### Proposed Technical Corrigendum

In 7.17.1p5 replace

> \- An A refers to one of the atomic types.

with

> \- An A refers to an atomic type.

Delete 7.17.6 paragraph 2\.
