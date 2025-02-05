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

```c
_Atomic(unsigned) A = { 0 };
_Atomic(unsigned) B = ATOMIC_VAR_INIT(0u);
static _Atomic(unsigned) C;
```
