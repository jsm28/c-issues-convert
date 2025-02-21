## Issue 0029: Must compatible structs/unions have the same tag in different translation units?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-016  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_029.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_029.html)

Subclause 6.1.2.6 says:

> ... two structure, union, or enumeration types declared in separate translation
> units are compatible if they have the same number of members, the same member
> names, and compatible member types; for two structures, the members shall be in
> the same order; for two structures or unions, the bit-fields shall have the same
> widths; for two enumerations, the members shall have the same values.

I have one question and one clarification, both about compatibility between two
`struct`/`union`/`enum` types declared in separate translation units.

(1) Was it the Committee's intent that the two types must have the same tag (or
both lack tags) to be compatible? As the standard is written, the following is
legal:

```c
One Translation Unit:
 struct foo { int i; } x;
 Another Translation Unit:
 extern struct bar { int i; } x;
```

Recommendation: This seems like an accidental omission. To be compatible, the
two types should have the same tag, or both lack tags. I would guess that such
was the Committee's intent.

(2) Clarification: The phrase “two structure, union, or enumeration types”
should be written “two structure types, two union types, or two enumeration
types.” The current standard, interpreted literally, allows a structure and a
union with identical member lists to be compatible, even though this is clearly
not the intent of the Committee.

```c
One Translation Unit:
 union foo { int i; } x;
 union bar { int i, j; } y;
 Another Translation Unit:
 extern struct foo { int i; } x;
 extern struct bar { int i, j; } y;
```

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.1.2.6 says (by omission) that tags do not have to be the same for
structure, union, or enumeration types to be compatible in separate translation
units. Tags are used in succeeding declarations to ensure that they are of the
same type. They are not used for type compatibility.

Does “two structure, union, and enumeration types” mean “two structure types,
two union types, or two enumeration types?”

Answer: Yes.
