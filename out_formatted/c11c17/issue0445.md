## Issue 0445: Issues with alignment in C11, part 2

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Joseph Myers  
Date: 2013-07-23  
Reference document: [N1731](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1731.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

There are various deficiencies in the C11 text about alignment requirements.

Issue 2: Contexts in which alignments are supported

6.2.8#2 defines "fundamental alignment": "A fundamental alignment is represented
by an alignment less than or equal to the greatest alignment supported by the
implementation in all contexts, which is equal to \_Alignof (max\_align\_t)."

6.2.8#3 defines "extended alignment": "An extended alignment is represented by
an alignment greater than \_Alignof (max\_align\_t). It is
implementation-defined whether any extended alignments are supported and the
contexts in which they are supported. A type having an extended alignment
requirement is an over-aligned type."

6.2.8#4 defines "valid alignment", saying "Alignments are represented as values
of the type size\_t. Valid alignments include only those values returned by an
\_Alignof expression for fundamental types, plus an additional
implementation-defined set of values, which may be empty. Every valid alignment
value shall be a nonnegative integral power of two.".

max\_align\_t is specified in 7.19#2 as "an object type whose alignment is as
great as is supported by the implementation in all contexts".

The memory management functions in 7.22.3 are defined to return a pointer
"suitably aligned so that it may be assigned to a pointer to any type of object
with a fundamental alignment requirement and then used to access such an object
or an array of such objects in the space allocated". In the case of
aligned\_alloc, there may be a stricter requirement given by the alignment
passed to the function, but the alignment passed to the function can't result in
memory any less-aligned than a fundamental alignment requirement. The alignment
requirement still applies even if the size is too small for any object requiring
the given alignment (see the response to C90 DR#075).

There are various problems with the above:

* The term "fundamental type" is not defined in C11.
* There is also no definition of what a "context" is in which an alignment might or might not be supported. In common implementation practice, separate contexts might be by the storage duration of the object (static, thread, automatic, allocated, with the last referring to the alignments guaranteed by calloc, malloc and realloc).
* A "valid alignment" may not be a "fundamental alignment". Thus, whatever interpretation is adopted for "fundamental type", nothing in the standard requires the alignment of a "fundamental type" to be a "fundamental alignment". For example, say "long double" is a "fundamental type"; it would seem nonsensical if declaring "long double" objects (in any context) failed to work, but nothing seems to require malloc to return objects sufficiently aligned for long double.
* Given these gaps in the definition, nothing in the normative text appears to imply footnote 57 "Every over-aligned type is, or contains, a structure or union type with a member to which an extended alignment has been applied.", although no doubt it reflects the intent.
* If "fundamental type" is interpreted to mean "basic type", that is not sufficient to resolve these lacunae. For example, if

  ```c
  struct s { long double ld; }
  ```

  has an alignment requirement bigger than long double, it should still be
  possible to allocate memory for it with malloc, and the same applies to any
  typedef from a standard header that might also have a bigger alignment
  requirement than any basic type.

The following principles seem natural for any fix for this issue:

* C99 referred to "any type of object" in the alignment requirements for calloc, malloc and realloc. As a matter of compatibility, this means that any type that could be constructed within C99 (including one using types from standard headers) should have an alignment required by C11 to be supported in all contexts, and the same applies to types from C extensions originally specified as extensions to C99. Most of the following principles follow to a greater or lesser extent from this compatibility principle.
* All basic types have alignments supported in all contexts.
* All enumerated types have alignments supported in all contexts.
* All pointer types have alignments supported in all contexts (even if the type pointed to does not).
* All types from standard headers specified as complete object types in the definitions of those headers have alignments supported in all contexts. (This includes both types specified as typedefs and types specified as structs or unions with a given tag.)
* If a type has an alignment supported in all contexts, so do arrays of that type, qualified versions of that type, and atomic versions of that type.
* If all the members of a structure or union have types with alignments supported in all contexts, and none of them use an \_Alignas specifier specifying an alignment bigger than supported in all contexts, then that structure or union has an alignment supported in all contexts.
* Where C extensions such as TS 18661-2 and 18661-3 are proposed that define new types, or existing such extensions such as TR 18037 are revised and updated for C11, care should be taken that the new types are covered under the above, whether through being basic types or through being defined in standard headers. (If SIMD vector types, as mentioned at [http://www.open-std.org/pipermail/cplex/2013-June/000010.html](https://www.open-std.org/pipermail/cplex/2013-June/000010.html), were to end up in any such extension, it would probably be appropriate to define them in a way that does \*not\* require calloc, malloc and realloc to return memory suitably aligned for them; such types often require alignments bigger than needed for any other type, so imposing such requirements on memory allocation functions would result in undue inefficiency.)

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

* It is indeed the case that 6.2.8p3 "fundamental type" is not defined. The intention is that it be "basic type", such that "fundamental alignment" is well defined, and yet this is not the case, and "fundamental alignment" also needs a definition. It is likely that the definition of fundamental type can be made editorially, but that when and where fundamental alignment is required is substantive.
* It is also the case that 6.2.8p3 "contexts" is not defined. It is intended to mean the full set of storage durations. Perhaps we should say "storage duration contexts".
* It is also the case that "valid alignment" may not be a "fundamental alignment".
* It was the case in C99 that `malloc` was required to return memory appropriate for "any type", and this should not be lost in the new wording regarding types that are not over-aligned. All other C99 behaviors must also be preserved as he describes as guidance.
* All types declared without the \_Alignas directive are intended to have fundamental alignment, which must be tied somehow to basic type. A consequence is that the only manner in which one can produce an over-aligned type is through \_Alignas. `malloc` has been defined in terms of fundamental alignment, yet we do not anywhere strongly state that, say, `int` has such fundamental alignment.
* These are several interwoven definitions and missing definitions that need a comprehensive review for adequate correction. We solicit the author for a suggested technical corrigendum. A copy of the audio discussion can be provided.

Apr 2014 meeting

### Committee Discussion

* The author provided input to [N1804](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1804.htm) as a proposed technical corrigendum:
* Change 6.2.8#2 to:
  > A fundamental alignment is a valid alignment less than or equal to `_Alignof
  > (max_align_t)`. Fundamental alignments shall be supported by the implementation
  > for objects of all storage durations. The alignment requirements of the
  > following types shall be fundamental alignments:
  >
  > + all atomic, qualified or unqualified basic types;
  > + all atomic, qualified or unqualified enumerated types;
  > + all atomic, qualified or unqualified pointer types;
  > + all array types whose element type has a fundamental alignment requirement;
  > + all types specified in clause 7 as complete object types;
  > + all structure or union types all of whose elements have types with fundamental alignment requirements and none of whose elements have an alignment specifier specifying an alignment that is not a fundamental alignment.

  In 6.2.8#3, change "the contexts in" to "the storage durations of objects for
  which".

  In 6.2.8#4, change "those values returned by an \_Alignof expression for
  fundamental types" to "fundamental alignments".

  (Note that the above admits the possibility that e.g. 1 and 4 are fundamental
  alignments, but 2 isn't, in which case it can't be an extended alignment either.
  If we want to ensure that 2 isn't a valid alignment at all in that case, rather
  than possibly having valid alignments that are neither fundamental nor extended,
  also change "additional implementation-defined set of values" to "additional
  implementation-defined set of extended alignments" in 6.2.8#4.) In 6.7.5#3,
  change "in the context in which it appears" to "for an object of the storage
  duration, if any, being declared". Add a new constraint at the end of 6.7.5#3:
  "An object shall not be declared with an over-aligned type with an extended
  alignment requirement not supported by the implementation for an object of that
  storage duration.".

  (This deals with the point that if an over-aligned struct is defined, then
  objects with that type may be supported with some storage durations but not
  others, so it is the declaration of an object with that type that can violate a
  constraint rather than the declaration of the struct.)

  In 7.19#2, change "whose alignment is as great as is supported by the
  implementation in all contexts" to "whose alignment is the greatest fundamental
  alignment".

  (I'm trying to avoid an undesirable implication that if an alignment of e.g. 1MB
  is supported in all contexts \- and it's quite plausible that an implementation
  can support more or less arbitrary alignments \- then max\_align\_t must have
  such an alignment and so such an alignment must count as fundamental and so
  malloc must return memory suitable aligned for it.)
* This is a difficult area and further study is required.

Oct 2014 meeting

### Committee Discussion

> The proposed changes have raised no concerns and so the committee has agreed to
> use them as the following Proposed Technical Corrigendum.

### Proposed Technical Corrigendum

Change 6.2.8#2 to:

> A fundamental alignment is a valid alignment less than or equal to `_Alignof
> (max_align_t)`. Fundamental alignments shall be supported by the implementation
> for objects of all storage durations. The alignment requirements of the
> following types shall be fundamental alignments:
>
> * all atomic, qualified or unqualified basic types;
> * all atomic, qualified or unqualified enumerated types;
> * all atomic, qualified or unqualified pointer types;
> * all array types whose element type has a fundamental alignment requirement;
> * all types specified in clause 7 as complete object types;
> * all structure or union types all of whose elements have types with fundamental alignment requirements and none of whose elements have an alignment specifier specifying an alignment that is not a fundamental alignment.

In 6.2.8#3, change

> "the contexts in"

to

> "the storage durations of objects for which".

In 6.2.8#4, change

> "those values returned by an \_Alignof expression for fundamental types"

to

> "fundamental alignments".

In 6.7.5#3, change

> "in the context in which it appears"

to

> "for an object of the storage duration, if any, being declared".

Add a new constraint at the end of 6.7.5#3:

> "An object shall not be declared with an over-aligned type with an extended
> alignment requirement not supported by the implementation for an object of that
> storage duration.".

In 7.19#2, change

> "whose alignment is as great as is supported by the implementation in all
> contexts"

to

> "whose alignment is the greatest fundamental alignment".
