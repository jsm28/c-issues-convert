## Issue 0119: Is a diagnostic required on an example of an initialization of multi-dimensional array objects

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_119.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_119.html)

ANSI/ISO C Defect Report #rfg26:

Subject: Initialization of multi-dimensional array objects.

a) Is a diagnostic required for the following declaration?

b) Is the following declaration strictly conforming or not?

```c
static int array[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9  } };
```

Background:

Subclause 6.5.7 (**Semantics**):

> If an array of unknown size is initialized, its size is determined by the number
> of initializers provided for its elements.

Subclause 6.5.7 (**Semantics**):

> If the aggregate contains members that are aggregates or unions, or if the first
> member of a union is an aggregate or union, the rules apply recursively to the
> subaggregates or contained unions.

On the basis of the above quoted rules, one might conclude that the code example
given above is strictly conforming. (Many existing implementations seem to
disagree, however.)

---

Comment from WG14 on 1997-09-23:

### Response

a) No, a diagnostic is not required. It is a semantic requirement that array
elements must be objects, not a constraint.

b) No, this is undefined behavior. Note that `array` does not have an array type
because its element type is not an object type; hence subclause 6.5.7 does not
apply. See subclause 6.1.2.5.
