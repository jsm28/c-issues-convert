This one is relevant only for hardware on which either null pointer or floating
point zero is *not* represented as all zero bits.

Consider this sentence in subclause 6.5.7 (starting on page 71, line 41):

> If an object that has static storage duration is not initialized explicitly, it
> is initialized implicitly as if every member that has arithmetic type were
> assigned 0 and every member that has pointer type were assigned a null pointer
> constant.

This implies that you cannot implicitly initialize a union object that could
contain overlapping members with different representations for zero/null
pointer. For example, given this translation unit:

```c
union { char *p; int i; } x;
```

If the null pointer is represented as, say, `0x80000000`, then there is no way
to implicitly initialize this object. Either the `p` member contains the null
pointer, or the `i` member contains 0, but not both. So the behavior of this
translation unit is undefined.

This is a bad state of affairs. I assume it was not the Committee's intention to
prohibit a large class of implicitly initialized unions; this would render a
great deal of existing code nonconforming.

The right thing \- although I can find no support for this idea in the draft \-
is to implicitly initialize only the first member of a union, by analogy with
explicit initialization. Here is a proposed new sentence; perhaps it can be
saved for the next time we make a C standard. (This sentence also tries to get
around the difficulty of the old “as if ... assigned” language in dealing with
`const` items; Dave Prosser tipped me off there.)

1. If an object that has static storage duration is not initialized explicitly, it is initialized implicitly according to these rules:
2. if it is a scalar with pointer type, it is initialized implicitly to a null pointer constant;
3. if it is a scalar with non-pointer type, it is initialized implicitly to zero;
4. if it is an aggregate, every member is initialized (recursively) according to these rules;
5. if it is a union, the first member is initialized (recursively) according to these rules.
