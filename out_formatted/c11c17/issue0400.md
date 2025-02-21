## Issue 0400: `realloc` with size zero problems

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Austin Group, Nick Stoughton (US)  
Date: 2011-10-24  
Reference document: [N1559](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1559.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

There are at least three existing `realloc` behaviors when `NULL` is returned;
the differences only occur for a size of 0 (for non-zero size, all three
implementations set `errno` to `ENOMEM` when returning `NULL`, even though that
is not required by C99).

> **AIX**
>
> > `realloc(NULL,0)` always returns NULL, errno is EINVAL  
> > `realloc(ptr,0)` always returns NULL, ptr freed, errno is EINVAL
>
> **BSD**
>
> > `realloc(NULL,0)` only gives NULL on alloc failure, errno is ENOMEM  
> > `realloc(ptr,0)` only gives NULL on alloc failure, ptr unchanged, errno is
> > ENOMEM
>
> **glibc**
>
> > `realloc(NULL,0)` only gives NULL on alloc failure, errno is ENOMEM  
> > `realloc(ptr,0)` always returns NULL, ptr freed, errno unchanged

The Austin Group raised this matter with WG14 during earlier meetings (most
notably during the London 2011 meeting). The direction from WG14 has led to The
Austin Group aligning the POSIX text more closely to that in C99 and C1x as a
part of TC1.

The behavior now required in POSIX is that implemented by **BSD** above.
However, C99 has a loophole in implementation-defined behavior that still
appears to permit AIX and glibc behaviors. The C1x draft carries the same
wording loophole, so the planned course of action is to raise a defect against
C1x once it completes standardization, where the outcome of that defect will
either be that C1x tightens the wording to eliminate the loophole or relaxes the
wording to align with existing practice. Therefore, the behavior of errno in
Issue 8 should be deferred until after any C1x defect has been resolved.

> If the size of the space requested is zero, the behavior is
> implementation-defined: either a null pointer is returned, or the behavior is as
> if the size were some nonzero value, except that the returned pointer shall not
> be used to access an object.

An implementation should not be allowed to define the behavior of returning a
null pointer as a successful reallocation; if a null pointer is returned, then
the orignal pointer has not been freed.

### Suggested Change

At 7.22.3, para 1, change:

> If the size of the space requested is zero, the behavior is
> implementation-defined: either a null pointer is returned, or the behavior is as
> if the size were some nonzero value, except that the returned pointer shall not
> be used to access an object.

to

> If the size of the space requested is zero, the behavior is
> implementation-defined: either a null pointer is returned <ins>and errno set to
> indicate the error</ins>, or the behavior is as if the size were some nonzero
> value, except that the returned pointer shall not be used to access an object.

Add a footnote to this sentence stating:

> <ins>**Note** Memory allocated by these functions should be freed via a call to
> `free`, and not by means of a `realoc(p, 0)`.</ins>

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee Discussion

> * It was pointed out that the AIX behavior was not correct according to Rajan, in fact the behavior is that `errno` is not set.
> * This change came out of a defect report on C99

Feb 2012 meeting

### Committee Discussion

> * The current C Rationale needs to be edited.

### Proposed Technical Corrigendum

> In subsection 7.22.3 paragraph 1, change
>
> > If the size of the space requested is zero, the behavior is
> > implementation-defined: either a null pointer is returned, ...
>
> to
>
> > If the size of the space requested is zero, the behavior is
> > implementation-defined: either a null pointer is returned to indicate an error,
> > ...
>
> In subsection 7.22.3.5 (The `realloc` function), change the final sentence of
> paragraph 3 from
>
> > If memory for the new object cannot be allocated, the old object is not
> > deallocated and its value is unchanged.
>
> to
>
> > If `size` is non-zero and memory for the new object is not allocated, the old
> > object is not deallocated. If `size` is zero and memory for the new object is
> > not allocated, it is implementation-defined whether the old object is
> > deallocated. If the old object is not deallocated, its value shall be unchanged.
>
> In subsection 7.22.3.5 (The `realloc` function), change paragraph 4 from
>
> > The `realloc` function returns a pointer to the new object (which may have the
> > same value as a pointer to the old object), or a null pointer if the new object
> > could not be allocated.
>
> to
>
> > The `realloc` function returns a pointer to the new object (which may have the
> > same value as a pointer to the old object), or a null pointer if the new object
> > has not been allocated.
>
> Add to subsection 7.31.12 a new paragraph (paragraph 2):
>
> > Invoking `realloc` with a size argument equal to zero is an obsolescent feature.
