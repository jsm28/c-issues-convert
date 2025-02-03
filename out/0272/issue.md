### Problem

The concept of "type category" is defined but is never used in a useful way; it
is also used inconsistently. The term and its cognates appear in only six
places:

|  |  |
| --- | --- |
| 6.2.5#24: | defines the term; |
| 6.2.5#25: | qualified and unqualified versions of types belong to the same category; |
| 6.2.5#27: | example: `(float *)` has category "pointer"; |
| 6.2.5#28: | example: `(struct tag (*[5])(float))` has category "array"; |
| footnote 93: | "... removes any type qualifiers from the type category of the expression" |
| footnote 137: | "The intent is that the type category in a function definition cannot be inherited from a `typedef`." |

Note how the use in footnote 93 conflicts with that in #25, and that the use in
footnote 137 remains less than clear.

Having an unnecessary term defined leaves the reader confused to no benefit. The
term should be removed and the remaining wording changed.

Even if the other changes described here are foregone, footnote 93 is in error
and should be changed.

### Suggested Technical Corrigendum

Delete 6.2.5#24.

In 6.2.5#25, delete "belong to the same type category and".

In 6.2.5#27, change "Its type category is pointer" to "It is a pointer type".

In 6.2.5#28, change "Its type category is array" to "It is an array type".

In footnote 93 change "which removes any type qualifiers from the type category
of the expression" to "which removes any type qualifiers from the outermost
component of the type of the expression (for example, it removes `const` but not
`volatile` from the type `int volatile *const`)".

In footnote 137 change the first part to:

> The intent is that the fact that the identifier designates a function is shown
> explicitly and cannot be inherited from a `typedef`:

leaving the examples unchanged.
