## Issue 0016.02: Can you implicitly initialize a union when null pointers have nonzero bit patterns?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-052  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_016.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_016.html)

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

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.7, page 71, line 41 through page 72, line 2, change:***

If an object that has static storage duration is not initialized explicitly, it
is initialized implicitly as if every member that has arithmetic type were
assigned 0 and every member that has pointer type were assigned a null pointer
constant.

***to:***

1. If an object that has static storage duration is not initialized explicitly, then:
2. if it has pointer type, it is initialized to a null pointer;
3. if it has arithmetic type, it is initialized to zero;
4. if it is an aggregate, every member is initialized (recursively) according to these rules;
5. if it is a union, the first named member is initialized (recursively) according to these rules.
