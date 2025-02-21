## Issue 0013.03: What is the composite type of an enumeration and an integer?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Submitted against: C90  
Status: Closed  
Cross-references: [0127](../c90/issue0127.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

Composite type of `enum` vs. integer not defined

There is one case where two types are compatible, but their composite type is
not defined. To fix this problem, in subclause 6.1.2.6 insert after page 25,
line 17:

> \- If one type is an enumeration and the other is an integer type, the composite
> type is the enumeration.

There may be other cases where “compatible” is not defined. I made a cursory
search and did not find any.

---

Comment from WG14 on 1997-09-23:

### Response

The issue is that in

```c
enum {r,w,b} x;
```

and

```c
some-int-type x;
```

where `some-int-type` happens to be the type that by subclause 6.5.2.2, page 61,
line 40 is compatible with the type of the `enum`, what is the resultant
composite type?

Subclause 6.1.2.6 on page 25, lines 11-12 says “*a* type that ... satisfies the
following conditions” (added emphasis on “*a*”). The composite type of two
compatible types is not necessarily unique. In this case both the `enum` type
and the `some-int-type` satisfy the definition of “composite” type. This refutes
the claim that the “composite type is not defined;” the point is that the
standard does not guarantee a *unique* composite type.

As an example, in the following declarations:

```c
enum {r, w, b} x;
 some_int_type x;
```

provided the enumeration type is compatible with the type of `some_int_typ e`,
it is unspecified whether the composite type of `x` is the enumeration type or
`some_int_type`.
