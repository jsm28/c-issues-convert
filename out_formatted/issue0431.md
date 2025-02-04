## Issue 0431: `atomic_compare_exchange`: What does it mean to say two structs compare equal?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Douglas Walls  
Date: 2013-02-21  
Reference document: [N1675](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1675.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Cross-references: [0423](issue0423.md), [0474](issue0474.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

7.17.7.4 The atomic\_compare\_exchange generic functions  

7.17.7.4p2 Description  

Atomically, compares the value pointed to by **object** for equality with  
that in **expected**, and if true, replaces the value pointed to by **object**  
with **desired**, and if false, updates the value in expected with the  
value pointed to by **object**.  

When **object** is an atomic struct type and **expected** is the corresponding  
non-atomic struct type.  What does it mean to compare two struct types  
as equal?  

Where does the C standard define what it means for two objects of struct  
type to be equal?  

7.17.7.4 NOTE 1 gives an example using memcmp on how the test for  
equality might be defined.  But that is non-normative.  

But the padding bytes in a struct have unspecified values (6.2.6.1p6)  

7.24.4.1 The memcmp function, footnote 310 reminds us that the contents  
of padding in a struct is indeterminate.  

Even integers can have padding bits, whose values are unspecified (6.2.6.2p1)  

A similar issue probably occurs for Atomic union types.

### Suggested Technical Corrigendum

Either define equality of objects of struct type, add a restriction disallowing  
use of atomic structs as arguments for the atomic\_compare\_exchange generic
functions,  
or note that atomic\_compare\_exchange generic functions for objects of atomic  
struct type results in undefined behavior.

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* There is no sentiment to define equality for structs.
* 7.17.6 lists atomic types required to have the same size and alignment as the corresponding direct type. Other atomic types may have differing size and alignment as per 6.2.5p27.
* 6.5.2.3p5 states that any access to an atomic struct or union member is undefined behavior and as such so would atomic\_compare\_exchange since it requires access.

Oct 2013 meeting

### Committee Discussion

* There are several points that need addressing.
* The original intention of the atomics design was to allow `memcmp` and `memcpy` (with suitable synchronization) be a common implementation for all \_Atomic objects.
* This practice, however, would lead to undefined behavior for implementations that have padding bits for integer representations.
* For implementations that choose larger representations for some \_Atomic types, there would need to be at least one larger type specific implementation of `atomic_compare_exchange` compared to what might be possible to implement in common for all types. This seems to imply that an implementation must supply something akin to a type generic implementation of `atomic_compare_exchange`. Type generic macros as applied to \_Atomic is the subject of [DR423.](issue0423.md)
* A proposal to address these issues has been solicited.

Apr 2014 meeting

### Committee Discussion

* The proposed resolution from [N1803](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1803.htm) was withdrawn since there are implementations choosing to represent atomic non-lock-free types with extra state and hence a larger size.
* Structure compare will result in undefined behavior.
* A new paper to address this DR has been solicited

Oct 2014 meeting

### Committee Discussion

> As requested, the paper
> [N1864](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1864.htm) was written
> and provided. From our C\+\+ liaison, however, it was learned that corresponding
> behavior is well defined and is in use. Further investigation revealed that
> `atomic_compare_exchange` in C\+\+ is and has been explicitly defined to be that
> of bit comparison. C11 defines it as value comparison.
>
> It was noted that bit comparison for atomic bool would not give the expected
> answer if differing non-zero "true" values were compared. It was also noted that
> bit comparison exposes padding bits, whereas lock bits would be required to be
> discarded, leading to code that might work on one implementation of an
> architecture but fail on another.
>
> A new paper was solicited.

Apr 2015 meeting

### Committee Discussion

> The paper [N1906](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1906.htm)
> was provided and discussed and its Proposed Technical Corrigendum was adopted.
> This resolution clarifies that

### Proposed Committee Response

> `atomic_compare_exchange` is now aligned with C\+\+11 as operating on bit
> representations. Where these representations are unpadded integer or structure
> values, the operation is well defined. The type `bool` is padded in many
> implementations.

### Proposed Technical Corrigendum

In 7.17.7.4p2 replace

> Atomically, compares the value pointed to by **object** for equality with that
> in **expected**, and if true, replaces the value pointed to by **object** with
> **desired**, and if false, updates the value in **expected** with the value
> pointed to by **object**

with:

> Atomically, compares the contents of the memory pointed to by **object** for
> equality with that in **expected**, and if true, replaces the contents of the
> memory pointed to by **object** with **desired**, and if false, updates the
> value in **expected** with the value pointed to by **object**.
