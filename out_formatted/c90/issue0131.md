## Issue 0131: What is the meaning of *const-qualification*?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Douglas Gwyn, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_131.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_131.html)

I've discovered an apparent bug in the C Standard. The code snippet:

```c
struct {const int a[5]; } s1, s2;
 void f(void) {s1 = s2; }
```

can be contained in a strictly conforming program, which runs counter to my
understanding of the meaning of “const-qualification.” That occurs because,
according to subclause 6.5.3, the member `s1.a` is *not* const-qualified and
thus slips past the modifiable-lvalue definition in subclause 6.2.2.1. Subclause
6.5.3 says that the *elements* of the array `s1.a` are const-qualified, not the
array itself, and I can find no reasonable way to construe `s1.a[3]`, for
example, as a “member” of `s1`; its only member is `s1.a`, as I see it.
Apparently, the C Standard does not define the term “member,” except implicitly
through its use in subclause 6.3.2.3 **Semantics**, which says that `s1.a` is
the member (on which the subscripting operator can operate to extract an
element, but the element is not a member of the structure.)

What I think is desirable would be a required diagnostic for this example, as it
*should* be considered to violate the constraint in subclause 6.3.16 that
requires the left operand of an assignment operator to be a modifiable lvalue.

Relevant citations:

Subclause 6.2.2.1 **Lvalues and function designators**:

> A *modifiable lvalue* is an lvalue that does not have array type, does not have
> an incomplete type, does not have a const-qualified type, and if it is a
> structure or union, does not have any member (including, recursively, any member
> of all contained structures or unions) with a const-qualified type.

Subclause 6.3.16 **Assignment operators**:

> **Constraints**:
>
> An assignment operator shall have a modifiable lvalue as its left operand.

Subclause 6.5.3 **Type qualifiers**:

> If the specification of an array type includes any type qualifiers, the element
> type is so-qualified, not the array type. If the specification of a function
> type includes any type qualifiers, the behavior is undefined.

---

Comment from WG14 on 1997-09-23:

### Response

The example code is *not* strictly conforming, because some objects (the
elements of the array `s1.a`) are being modified through use of an lvalue (`s1`)
with non-const-qualified type, which according to subclause 6.5.3 results in
undefined behavior.

However, a diagnostic is indeed desired here.

### Correction

***In subclause 6.2.2.1, page 36, change the parenthetic remark in the final
sentence of the first paragraph:***

(including, recursively, any member of all contained structures or unions)

***to:***

(including, recursively, any member or element of all contained aggregates or
unions)
