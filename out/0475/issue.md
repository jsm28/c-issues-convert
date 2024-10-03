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
