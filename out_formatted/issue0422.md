## Issue 0422: initialization of atomic types

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jens Gustedt  
Date: 2012-10-08  
Reference document: [N1649](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1649.htm)  
Submitted against: C11 / C17  
Status: Closed  
Cross-references: [0454](issue0454.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The current version of the standard doesn't specify to which value an atomic
object should be initialized if it is initialized by default.

> An atomic object with automatic storage duration that is not explicitly
> initialized using `ATOMIC_VAR_INIT` is initially in an indeterminate state;
> however, the default (zero) initialization for objects with static or
> thread-local storage duration is guaranteed to produce a valid state.

The mentioned valid state (in contrast to the indeterminate state mentioned
before) is thus a determinate state, but the value that is stored is not
mentioned explicitly. In the introduced language of the standard it is no
definition of a "determinate state". It could be an "implementation-defined
value", just an "unspecified value" or a default (zero) initialization.
Everything suggests the later, that this would be the same value as for
initializing a variable of the underlying base type by `{ 0 }`. But I think it
would have helped to make that explicit.

### Suggested Technical Corrigendum

Proposed change for the initialization of atomic objects, 7.17.2.1p2:

<ins>An atomic object with automatic storage duration that is not explicitly
initialized using `ATOMIC_VAR_INIT` is initially in an indeterminate state;
however, the default (zero) initialization for objects with static or
thread-local storage duration is guaranteed to produce a valid state that
corresponds to the value of a zero initialized object of the unqualified base
type.   
EXAMPLE All three of the following objects initially have an observable value of
`0`.</ins>

<ins>`_Atomic(unsigned) A = { 0 };`  
`_Atomic(unsigned) B = ATOMIC_VAR_INIT(0u);`  
`static _Atomic(unsigned) C;`</ins>

---

Comment from WG14 on 2014-04-11:

Oct 2012 meeting

### Committee Discussion

> * `ATOMIC_VAR_INIT` is required to initialize an atomic object to a known value.
> * The default value for an atomic object is defined to be valid but is unspecified.
> * The committee does not see this as a defect.
> * N1649 proposes that the default value be specified to be the same as the non-atomic type’s default value.
> * Such a proposal should be submitted as such and may also need to be submitted to and addressed by WG21 (C\+\+) as well.

Apr 2013 meeting

### Proposed Committee Response

`ATOMIC_VAR_INIT` is required to initialize an atomic object to a known value.
This value is defined to be valid but is unspecified in order to support the
widest possible set of architectures. This is not a defect.
