### Summary

C11 expresses the intention to have `atomic_flag` as a primitive that should
allow to emulate all other atomic types and operations, *7.17.8 p3* in a note
says:

> The remaining types can be emulated with `atomic_flag`, though with less than
> ideal properties.

With the current semantic for the initialization of `atomic_flag` this goal
cannot be achieved.

### Details

This is a very good concept as far as I can see, but I have one problem to
achieve this, initialization. The phrasing for atomic types in general and for
`atomic_flag` are different. For `atomic_flag` we have:

> An atomic\_flag that is not explicitly initialized with `ATOMIC_FLAG_INIT` is
> initially in an indeterminate state.

The problem is how to emulate an atomic type with `atomic_flag` during
initialization. Say we emulate with something like

```c
struct atomic_int_struct {
  atomic_flag cat;
  int val;
};
```

Then the `ATOMIC_VAR_INIT` macro could simply look like:

```c
#define ATOMIC_VAR_INIT(V) { .cat = ATOMIC_FLAG_INIT, .val = (V), }
```

But if I’d have a variable of `atomic_int_struct` with static storage duration

```c
struct atomic_int_struct v;
```

is supposed to do the right thing, namely to guarantee that `v` has a valid
state at startup, so it should contain a `0` for `.val`, and `.cat` must be in a
determinate state. Since all atomic operations should work without problems on
`v`, the state of `.cat` can’t be anything else than “clear”.

Now looking into the possible implementations of `atomic_flag` in assembler I
didn’t yet meet a processor where the “clear” state would not be naturally
represented by an all `0` value. So I guess in any reasonable implementation we
would just have

```c
#define ATOMIC_FLAG_INIT { 0 }
```

(or some equivalent formulation.)

If this is so, why `ATOMIC_FLAG_INIT` at all? Why not phrasing the same as for
the other atomic types

### Suggested Technical Corrigendum

Eliminate the mention of `ATOMIC_FLAG_INIT` in 7.17.1p3, B.16 and the index.

Proposed change for the initialization of `atomic_flag`, 7.17.8p4:

<u>The default initializer `{ 0 }` may be used to initialize an `atomic_flag` to
the clear state. An `atomic_flag` object with automatic storage duration that is
not explicitly initialized using `{ 0 }` is initially in an indeterminate state;
*however, the default (zero) initialization for objects with static or
thread-local storage duration initializes an `atomic_flag` to the clear state.*   
EXAMPLE</u>

```c
atomic_flag guard = { 0 };
```

If the committee would want to keep the macro `ATOMIC_FLAG_INIT` arround, a
partial alternative to the above text would be to modify the text in 7.17.1

```c
ATOMIC_FLAG_INIT
```

<u>which expands to a default initializer (`{ 0 }` or equivalent) for an object
of type `atomic_flag`.</u>
