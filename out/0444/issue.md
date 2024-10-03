### Summary

There are various deficiencies in the C11 text about alignment requirements.

Issue 1: Existence of over-aligned types

6.2.8#3 defines the concept of an over-aligned type, with a footnote saying
"Every over-aligned type is, or contains, a structure or union type with a
member to which an extended alignment has been applied.". But there is no way in
the syntax to apply such an alignment to a member. \_Alignas appears in the
syntax for alignment-specifier, which in turn appears in that for
declaration-specifiers (6.7#1). But structure and union members instead use
struct-declaration which uses specifier-qualifier-list which doesn't include a
case for alignment-specifier at all. So for the reference to over-aligned types,
and the reference in 6.7.5#6 to the "declared object or member", to be
meaningful, something needs adding to the syntax for struct-declaration. (Note
that specifier-qualifier-list is also used in the syntax for type-name, and it
seems less likely that a type-name was intended to be able to include
alignment-specifiers.)
