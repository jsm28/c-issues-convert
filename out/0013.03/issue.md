Composite type of `enum` vs. integer not defined

There is one case where two types are compatible, but their composite type is
not defined. To fix this problem, in subclause 6.1.2.6 insert after page 25,
line 17:

> \- If one type is an enumeration and the other is an integer type, the composite
> type is the enumeration.

There may be other cases where “compatible” is not defined. I made a cursory
search and did not find any.
