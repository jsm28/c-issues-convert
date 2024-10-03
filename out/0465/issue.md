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
