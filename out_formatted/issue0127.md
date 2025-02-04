## Issue 0127: What is the composite type of an enumeration and an integer?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0013.03](issue0013.03.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_127.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_127.html)

ANSI/ISO C Defect Report #rfg34:

Subject: Composite type of an enumerated type and an integral type.

Given the declarations:

```c
enum E { red, green, blue } object;
 int object;
```

and given an implementation for which the type `int` is considered to be
compatible with the type `enum E`, what is the composite type of `object` at the
end of the translation unit which contains the above declarations?

Background:

Subclause 6.5.2.2 says:

> Each enumerated type shall be compatible with an integer type; the choice of
> type implementation-defined.

Subclause 6.1.2.6 says:

> A *composite type* can be constructed from two types that are compatible; ...
>
> For an identifier with external or internal linkage declared in the same scope
> as another declaration for that identifier, the type of the identifier becomes
> the composite type.

---

Comment from WG14 on 1997-09-23:

### Response

See [Defect Report #013, Question 3](issue0013.03.md). There is no requirement
that the composite type be unique, and either of the types could be chosen as
the composite type.
