## Issue 0084: When is an incomplete type in function declaration a parameter?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0104](../c90/issue0104.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_084.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_084.html)

Item 21 \- incomplete type in function declaration

Consider the following declarations:

```c
struct tag;
 extern void (*f) (struct tag);
```

At the point of the declaration of `f`, the type of the parameter is incomplete.
Now a parameter is an object (subclause 3.15) with no linkage (subclause
6.1.2.2), but it is unclear whether this is a declaration of the parameter. If
it is, then the declaration of `f` is forbidden by subclause 6.5. If it is not,
then the declaration is strictly conforming. Which is the case?

If the type `struct tag` is completed before a call to `f`, is the call strictly
conforming? Alternatively, since the declaration of `f` includes an incomplete
type, is it possible to make a call to it at all?

---

Comment from WG14 on 1997-09-23:

### Response

From subclause 6.5.2.3, the incomplete type specified by the tag may be used,
unless the size of the corresponding object is needed.

In responding to Defect Reports, the Committee has discussed at length when the
size of an object is actually required. The C Standard is inconclusive with
regard to whether or not the size of the structure is needed in the example
given, leaving the behavior undefined.

The Committee should revisit this issue during the revision of the C Standard.
