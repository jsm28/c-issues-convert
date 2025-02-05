### Summary

The `aligned_alloc` function specifies the following constraints on its
arguments, `alignment` and `size`:

> The value of `alignment` shall be a valid alignment supported by the
> implementation and the value of `size` shall be an integral multiple of
> alignment.

Therefore, the behavior of the function is undefined when either constraint is
violated.

According to section 6.2.8, paragraph 1, the greatest alignment a conforming
implementation is required to support (known as *fundamental alignment*) is
`_Alignof(max_align_t)`. Furthermore, according to paragraph 2 of the same
section, whether alignments greater than the fundamental alignment (known as
*extended alignments*) are supported and in what contexts is
implementation-defined.

The standard specifies no mechanism by which programs could determine whether an
extended alignment is supported by an implementation, or whether the
`aligned_alloc` function is among the contexts where an extended alignment is
supported.

As a result, there is no way for strictly conforming programs to use the
`aligned_alloc` function with an `alignment` argument greater than the result of
`_Alignof(max_align_t)`. Since the `malloc` function returns objects that meet
the same alignment requirement, this restriction makes `aligned_alloc` useless
in portable programs.

This restriction is unnecessary since it's possible, and in fact nearly trivial
given access to the internal details of the memory allocator, to implement an
efficient `aligned_function` that fails when its arguments don't meet the
specified requirements.

As a data point, the POSIX Advanced Realtime function
[`posix_memalign`](http://pubs.opengroup.org/onlinepubs/9699919799/functions/posix_memalign.html),
as well as the historical BSD `memalign` function, are both required to return a
null pointer when either of their arguments don't meet the specified
requirements (in addition to setting `errno` to `EINVAL`.

### Suggested Technical Corrigendum

The proposed corrigendum below changes the standard to require `aligned_alloc`
to fail by returning a null pointer when either of its constraints is violated.

In section 7.22.3.1, modify paragraph 2 as indicated below:

> The `aligned_alloc` function allocates space for an object whose alignment is
> specified by `alignment`, whose size is specified by `size`, and whose value is
> indeterminate. <del>T</del><ins>If t</ins>he value of `alignment` <del>shall
> be</del> <ins>is not</ins> a valid alignment supported by the implementation
> <del>and</del><ins>or</ins> the value of `size` <del>shall be</del><ins>is
> not</ins> an integral multiple of `alignment` <ins>the function shall fail by
> returning a null pointer</ins>.

In addition, in section **J.2 Undefined behavior**, remove the following bullet:

> <del>— The alignment requested of the aligned\_alloc function is not valid or
> not supported by the implementation, or the size requested is not an integral
> multiple of the alignment (7.22.3.1).</del>

If the proposal above isn't acceptable, then an alternative solution to consider
that would allow `aligned_alloc` to be used even in strictly conforming programs
is to add a new function to determine whether a given alignment is supported by
an implementation. For example:

> ```c
> _Bool alignment_is_valid (size_t alignment);
> ```
>
> **Returns**
>
> The `alignment_is_valid` function returns non-zero if the value specified by
> `alignment` is a valid alignment argument to the `aligned_alloc` function, and
> zero otherwise.
