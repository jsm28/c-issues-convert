## Issue 0050: Does a proper definition of `wchar_t` need to be in scope to write a wide-character literal?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: C. Breeus, Project Editor (P.J. Plauger)  
Date: 1993-02-24  
Submitted against: C90  
Status: Closed  
Cross-references: [0017.07](../c90/issue0017.07.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_050.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_050.html)

Subclause 6.1.3.4 says that the type of a wide character constant is `wchar_t`,
and subclause 6.1.4 says the type of a wide character string is array of
`wchar_t`.

Subclause 7.1.6 says the typedef name `wchar_t` must be defined in `<stddef.h>`.

Question: When a compiler sees a literal of the form `L'...'` or `L"..."` must
it not check that

1. The name `wchar_t` is visible at that place.
2. The name is a typedef name. It could be redefined in an inner scope.
3. It is a typedef for an integral type. Again, it could be redefined.

And then, take that integral type as the meaning of `wchar_t`. I suppose it
cannot just hope for the best and take a type that makes it feel good.

---

Comment from WG14 on 1997-09-23:

### Response

A similar issue was explained in response to [Defect Report #017
Question](../c90/issue0017.07.md) 7, regarding `size_t`. The relevant citation here is
from subclause 6.1.3.4, page 29, lines 36-37:

> A wide character constant has type `wchar_t`, an integral type defined in the
> `<stddef.h>` header.

The intent of this sentence is to note that a wide character constant has an
integral type. That integral type is the same integral type used to define
`wchar_t` in the header `<stddef.h>`. The sentence imposes no requirement that
this particular definition of `wchar_t` be in scope wherever you write a wide
character constant. It certainly does not suggest that the translator should
honor any other definition of `wchar_t` that may be in scope, as the type for a
wide character constant.

Rather, the sentence suggests that the translator knows what integral type to
assign to a wide character constant. The implementation further knows to define
`wchar_t` within the header `<stddef.h>` as having that same integral type.
Thus, the program has a way of obtaining a name for this type, if it chooses \-
by including the header `<stddef.h>`. But it need not invoke that mechanism just
to assist the translator.

It is an unfortunate, but widespread, practice within the C Standard to use
abbreviated language for describing some types. Thus, subclause 6.1.4, page 31,
lines 5-6 say:

> for wide string literals, the array elements have type `wchar_t`, ...

instead of the more long winded (but clearer):

> for wide string literals, the array elements have the same type used to define
> `wchar_t` in the header `<stddef.h>`, ...

We feel the usage is sufficiently uniform that the meaning intended by the
Committee is sufficiently clear, even as we acknowledge that the words can be
(and have been) misread.

So to put the matter crassly, the translator *does* “just hope for the best and
take a type that makes it feel good,” as you conjectured.
