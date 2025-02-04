## Issue 0465: Fixing an inconsistency in `atomic_is_lock_free`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, David Keaton (suggested by Hans Boehm)  
Date: 2014-07-14  
Reference document: [N1847](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1847.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The C committee intended to adopt the same model for atomics as C\+\+ to ensure
compatibility. Somewhere along the way, there was an error in synchronizing with
the C\+\+ atomic model. This could have serious consequences for code that needs
to share atomic objects between modules written in C and modules written in
C\+\+ (for example, in the case of libraries written in one language being used
by a program written in the other).

The C\+\+ standard states the following in 29.4p2.

> The function `atomic_is_lock_free` (29.6) indicates whether the object is
> lock-free. *In any given program execution, the result of the lock-free query
> shall be consistent for all pointers of the same type.*

However, the C standard states the following in 7.17.5.1p3.

> The `atomic_is_lock_free` generic function returns nonzero (true) if and only if
> the object's operations are lock-free. *The result of a lock-free query on one
> object cannot be inferred from the result of a lock-free query on another
> object.*

The primary issue is compatibility. Secondarily, if the lock-free property for a
given pointer type can change after an algorithm starts, then
`atomic_is_lock_free` cannot be used to select an algorithm in advance if the
algorithm will allocate new atomic objects. The C\+\+ model is therefore more
useful.

The error in synchronizing with C\+\+ should be fixed by correcting the behavior
of `atomic_is_lock_free` to be the same in C as in C\+\+.

### Suggested Technical Corrigendum

Replace the following sentence from 7.17.5.1p3

> The result of a lock-free query on one object cannot be inferred from the result
> of a lock-free query on another object.

with the following.

> In any given program execution, the result of the lock-free query shall be
> consistent for all pointers of the same type.

---

Comment from WG14 on 2017-11-03:

Oct 2014 meeting

### Committee Discussion

> The Suggested Technical Corrigendum needed revision, and new words were crafted
> and adopted. One consequence from this change that a NULL pointer is now a valid
> argument.

Apr 2015 meeting

### Committee Discussion

> No revisions were deemed necessary. Value 1 remains in 7.17.5p1 for
> implementations where only the runtime can determine if an operation on a
> particular type is lock-free due to architectural differences.

Oct 2015 meeting

### Committee Discussion

> As solicited, a new paper
> [N1976](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1976.htm) was
> presented and discussed to clarify that null pointers to atomic types are
> allowed and thus can be used at compile time. After discussion, the Proposed
> Technical Corrigendum was modified to incorporate this point as a non-normative
> explanatory footnote.

### Proposed Technical Corrigendum

Change 7.17.5.1 paragraph 2 from:

> The `atomic_is_lock_free` generic function indicates whether or not the object
> pointed to by `obj` is lock-free.

to:

> The `atomic_is_lock_free` generic function indicates whether or not atomic
> operations on objects of the type pointed to by `obj` are lock-free.

Change 7.17.5.1 paragraph 3 from:

> The `atomic_is_lock_free` generic function returns nonzero (true) if and only if
> the object's operations are lock-free. The result of a lock-free query on one
> object cannot be inferred from the result of a lock-free query on another
> object.

to:

> The `atomic_is_lock_free` generic function returns nonzero (true) if and only if
> atomic operations on objects of the type pointed to by the argument are
> lock-free. In any given program execution, the result of the lock-free query
> shall be consistent for all pointers of the same type.<sup>new</sup>

<sup>new)</sup>`obj` may be a null pointer.
