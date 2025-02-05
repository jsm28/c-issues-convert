## Issue 0486: Inconsistent specification for arithmetic on atomic objects

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jens Gustedt  
Date: 2015-08-07  
Reference document: [N1955](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1955.htm)  
Submitted against: C11 / C17  
Status: Closed  
Cross-references: [0495](issue0495.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Whereas its intent is clear, the text in the C standard that concerns atomics
has several consistency problems. There are contradictions and the standard
vocabulary is not always applied correctly.

**Problem discussion**

*— Memory order of operators —*

The following sections on arithmetic operators, all specify that if they are
applied to an atomic object as an operand of **any** arithmetic base type, the
memory order sematic is `memory_order_seq_cst`:

* 6.2.6.1 Loads and stores of objects with atomic types are done with `memory_order_seq_cst` semantics.
* 6.5.2.4 (postfix `++` and `--`)
* 6.5.16.2 Compound assignment. No constraints formulated concerning traps for integer types. In contrast to that, no floating exceptions for floating types are allowed. Also, this defines atomic operations for **all** arithmetic operands, including some that don't have library calls (`*=`, `/=`, `%=`, `<<=`, `>>=`)

No such mention is made for

* 6.5.3.1 (prefix `++` and `--`), although it explicitly states that these operators are defined to be equivalent to `+= 1` and `-= 1`, respectively.
* 6.5.16.1 Simple assignment, although the paragraph about store says that such a store should be `memory_order_seq_cst`.

*— Integer representations and erroneous operations —*

Concerning the generic library calls, they state in 7.17.7.5

> For signed integer types, arithmetic is defined to use two’s complement
> representation with silent wrap-around on overflow; there are no undefined
> results.

and

> For address types, the result may be an undefined address, but the operations
> otherwise have no undefined behavior.

Can the sign representation depend on the operation that we apply to an object?  
Are these operations supposed to be consistent between operator and function
notation?  
What is an *address type*?  
What is "*no undefined behavior*"? How is the behavior then defined, when we are
not told about it?

*— Operators versus generic functions —*

Then a **Note** (7.17.7.5 p 5\) states

> The operation of the atomic\_fetch and modify generic functions are nearly
> equivalent to the operation of the corresponding `op=` compound assignment
> operators. The only differences are that the **compound assignment operators are
> not guaranteed to operate atomically**, ...

Although there are obviously also operators that act on atomic objects, 5.1.2.4
p 4 gives the completely false impression that atomic operations would only be a
matter of the C library:

> The library defines a number of atomic operations (7.17) ...

*— Pointer types are missing for `atomic_fetch_OP` —*

In the general introduction (7.17.1 p4) there is explicitly an extension of the
notations to atomic pointer types:

> For atomic pointer types, `M` is `ptrdiff_t`.

Whereas the only section where this notation is relevant (7.17.7.5
`atomic_fetch_OP`) is restricted to *atomic integer types*, but then later talks
about the result of such operations on *address types*.

*— Vocabulary —*

For the vocabulary, there is a mixture of the use of the verb combinations
between *load/store*, *read/write* and *fetch/assign*. What is the difference?
Is there any?

*— Over all —*

This is

* contradictory (the Note is not normative, but still wrong),
* confusing (`=` is handled different from `op=`, operators are not mentioned where they should),
* weird (the sign representation is described as the result of an operation, not as the value representation of a data type; what is "no undefined behavior" of a address operation?)
* inconsistent (operators may result in any sign representation ?, and can trap, generic functions are safe)
* incomplete (the set of operators and generic functions are distinct)

**Conclusion**

Combining all these texts, a number of constraints emerge for arithmetic types
on platforms that support the atomics extension. They would better be stated as
such.

1. Since sign representation is a property of a type and not an operation. To comply to the atomics extension all signed integer types must have two's representation for negative values.
2. Pointer arithmetic must have a variant that always has defined behavior, only that the stored address may be invalid, if the addition or subtraction passed beyond the boundaries of the object. But that behavior is **not** defined by the standard, the negation of undefined doesn't give a definition.
3. Binary integer operations `+`, `-`, `&`, `|` and `^` must have versions that do not trap.
4. All floating point operations must have versions that don't raise signals.

The distinction in operations on atomics that are realized by operators (all
arithmetic) and only by generic functions is arbitrary. As soon as a type has a
lock-free `atomic_compare_exchange` operation, all `fetch_op` or `op_fetch`
generic functions can be synthesized almost trivially.

* Why are atomic operations on pointer types and floating point types restricted to applying the operator, and don't allow for the generic function?

**Current practice**

Both gcc and clang permit `atomic_fetch_add` and `atomic_fetch_sub` on atomic
pointer types.

Both disallow floating point types for the functions but allow them for the
operators.

Gcc extends the infrastructure that it provides of atomics to `op_fetch` generic
fuctions and adds a new operator `nand`.

**Suggested strategy for improvement**

I suggest to first do some minimal changes to the text with a TC to avoid its
contradictions and to centralize its requirements. Then, in a feature request
for a new version of the standard we could discuss to add some more features
that would make the approach internally consistent.

### Suggested Technical Corrigendum

Change the beginning of 5.1.2.4 p5:

<del>The library defines a number of atomic operations (7.17) and operations on
mutexes (7.26.4) that are specially identified as synchronization
operations.</del>

to

<ins>There are a number of operations that are specially identified as
synchronization operations: if the implementation supports the atomics extension
these are operators and generic functions that act on atomic objects (6.5 and
7.17); if the implementation supports the thread extension these are operations
on mutexes (7.26.4).</ins>

Replace paragraph 6.2.6.1 p9

<del>Loads and stores of objects with atomic types are done with
memory\_order\_seq\_cst semantics.</del>

by the following

<ins>All operations that act on atomic objects that do not specify otherwise
have `memory_order_seq_cst` memory consistency. If the operation with identical
values on the unqualified type is erroneous it results in an unspecific object
representation, that may or may not be an invalid value for the type, such as an
invalid address or a floating point NaN. Thereby no such operation may by itself
raise a signal, a trap, a floating point exception or result otherwise in an
interruption of the control flow.FOOTNOTE</ins>

<ins>FOOTNOTE Whether or not an atomic operation may be interrupted by a signal
depends on the lock-free property of the underlying type.</ins>

Insert a new paragraph after 6.2.6.2 p2

<ins>Implementations that support the atomics extension, represent all signed
integers with two's complement such that the object representation with sign bit
1 and all value bits zero is a normal value.</ins>

Insert a new paragraph after 6.5 p3

<ins>An operation on an lvalue with an atomic type, that consists of the
evaluation of the object, an optional arithmetic operation and a side effect for
updating the stored value forms a single read-modify-write operation.</ins>

Remove the following phrase in 6.5.2.4 p2:

<del>Postfix `++` on an object with atomic type is a read-modify-write operation
with memory\_order\_seq\_cst memory order semantics.</del>

Remove the following phrase in 6.5.16.2 p3:

<del>If **E1** has an atomic type, compound assignment is a read-modify-write
operation with memory\_order\_seq\_cst memory order semantic</del>

Replace 7.17.7 p1

<del>There are only a few kinds of operations on atomic types, though there are
many instances of those kinds. This subclause specifies each general kind.</del>

by

<ins>In addition to the operations on atomic objects that are described by
operators, there are a few kinds of operations that are specified as generic
functions. This subclause specifies each generic function. After evaluation of
its arguments, each of these generic functions forms a single read, write or
read-modify-write operation with same general properties as described in 6.2.6.1
p9.</ins>

Assuming that the intent of 7.17.7.5 has been to allow operations on atomic
pointer types, in p1, change:

<del>... to an object of any atomic integer type. None of these operations is
applicable to `atomic_bool`</del>

to

<ins>... to an object of any atomic integer or pointer type, as long as the
unqualified type is valid as left operand of the corresponding operator
`op=`.FOOTNOTE  

FOOTNOTE: Thus these operations are not permitted for pointers to atomic
`_Bool`, and only "add" and "sub" variants are permitted for atomic pointer
types.</ins>

Since this topic is then covered already by a more general section, remove this
sentence from p3:

<del>For address types, the result may be an undefined address, but the
operations otherwise have no undefined behavior.</del>

In 7.17.7.5 p 5 replace:

<del>... the compound assignment operators are not guaranteed to operate
atomically, and ...</del>

by

<ins>... the `order` parameter may make the memory consistency less strict than
`memory_order_seq_cst`, and that ...</ins>

**Future Directions**

An editorial revision of the C standard should clarify the vocabulary for the
use of the terms *load*, *store*, *read*, *write*, *modify*, *fetch* and
*assign*.

A feature revision of the standard should:

* Add generic interfaces for all arithmetic operations. That is, it should add function-like interfaces for the missing operators `*=`, `/=`, `%=`, `<<=`, `>>=`
* Add atomic pointer types (if not by the TC above) and atomic floating point types to the permitted types of the function-like arithmetic operations, such that they are uniformly defined for all types where the corresponding operator applies.
* Add generic interfaces `atomic_OP_fetch` for all `atomic_fetch_OP`.
* Reduce 7.17.6 "Atomic integer types" to just a definition of `typedef` as indicated in the table.

---

Comment from WG14 on 2018-10-18:

Oct 2015 meeting

### Committee Discussion

* The committee agrees that there are small inconsistencies remaining in the standard but that they are largely editorial in nature, and yet of potentially of such a sweeping scope that is difficult to assess as a defect. In particular, the various uses of *load/store*, *read/write*, and *fetch/assign* should be clarified and made consistent where possible. It may be advantageous to use ISO standardized vocabulary for this and perhaps other new terms introduced in C11.
* Additional related issues were raised in [(SC22WG14.13844) atomic\_fetch and modify generic functions](https://www.open-std.org/jtc1/sc22/wg14/13844).
* The committee does not feel that this DR is “actionable” and should, in this form, result in a Proposed Committee Response. The author is encouraged to extract and provide in a new paper a simpler list of inconsistencies that can be addressed in a DR. The author is also solicited to address the broader issues as a proposal in a new paper for consideration in a new revision of the standard.

Oct 2015 meeting

### Committee Discussion

The proposed changes to §6.2.6.1 paragraph 9 are superfluous and unnecessary.

The other changes require a comprehensive review of the standard and as such
will be addressed in a future revision of the standard.

Apr 2018 meeting

### Committee Discussion

> The committee solicited the author for a combined resolution for this issue with
> that raised in [DR 495](issue0495.md).

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that this proposed change and that from [CR 495](issue0495.md) be
> combined in a new paper to completely resolve this issue.
