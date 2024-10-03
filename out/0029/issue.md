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
