## Issue 0017.17: How do you initialize the first member of a union if it has no name?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0017.26](../c90/issue0017.26.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Initialization of unions with unnamed members

Subclause 6.5.7 on page 71, line 39 says: “All unnamed structure or union
members are ignored ...” On page 72, lines 22-23, it says: “... for the first
member of the union.” Subclause 6.5.2.1, page 60, line 40 and Footnote 60 say
that a field with no declarator is a member.

```c
union {
        int  :3;
        float f;} u = {3.4};
```

Should page 72 be changed to refer to the first named member or is the
initialization of a union whose first member is unnamed illegal?

It has been suggested that the situation described above is implicitly
undefined.

I think that it is a straightforward ambiguity that needs resolution one way or
the other.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.7, page 71, line 39, change:***

All unnamed structure or union members are ignored during initialization.

***to:***

Except where explicitly stated otherwise, for the purposes of this subclause
unnamed members of objects of structure and union type do not participate in
initialization. Unnamed members of structure objects have indeterminate value
even after initialization. A union object containing only unnamed members has
indeterminate value even after initialization.

***In subclause 6.5.7, page 72, line 11, change:***

The initial value of the object is that of the expression.

***to:***

The initial value of the object, including unnamed members, is that of the
expression.
