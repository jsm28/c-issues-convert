### Summary

The handling of imaginary types in the Standard is somewhat inconsistent. For
example, they are not mentioned at all in 6.2.5 (other than a footnote), but are
treated as first-class types in 6.7.2. Annex G makes certain assumptions about
such types but these assumptions are not supported by the Standard.

### Details

There are two reasonable approaches that could be followed. The first is to
remove all mention of imaginary types from the main text of the Standard and put
them all in Annex G. The second is to make the basic properties of imaginary
types part of the main language (while still making them optional), leaving
Annex G to handle the details of ISO 60559 imaginary types.

After some thought, the author of this DR feels that imaginary types are
experimental enough that the first approach is better and has worded the
Suggested Technical Corrigendum on that basis.

The keyword `_Imaginary` is mentioned in 6.4.1, 6.7.2, and 7.3.1. These
references \- and any related text \- are all to be removed and replacement
wording added to Annex G.

A new subclause G.4.4 is added. This specifies the practical implications of
giving imaginary types the same representation and alignment as real floating
types.

### Suggested Technical Corrigendum

Delete "\_Imaginary" from the list of keywords in 6.4.1. If this is felt to be
too radical, instead add the following text to paragraph 2:

> The keyword `_Imaginary` is not used in the C language, but is reserved for
> specifying imaginary types such as described in Annex G.

Delete "`_Imaginary`" from 6.7.2p1 and the three imaginary cases from 6.7.2p2.

Change 6.7.2p3 to read:

> The type specifier `_Complex` shall not be used if the implementation does not
> provide complex types.

Delete 7.3.1p3.

Delete "`imaginary`" from 7.3.1p5.

Replace 7.3.1p4 with:

> The macro `I` expands to `_Complex_I`.

Add a new paragraph before G.2p1:

> There is a new keyword `_Imaginary` used to specify imaginary types. It is used
> as a type-specifier within declaration-specifiers in the same way as `_Complex`
> is (thus "`_Imaginary float`" is a valid type name).

Add a new subclause G.4.4

> **G.4.4 Interchangeable values**
>
> Though imaginary types are not compatible with the corresponding real type,
> values of one may be used where the other is expected in the following cases. In
> each case the value is converted to the value of the other type that has the
> same representation (that is, by multiplying by the imaginary unit when
> converting to an imaginary type, and by dividing by the imaginary unit when
> converting to a real type).
>
> * one type is the type of the parameter, and the other type the type of the argument, when a function is called without a prototype in scope; \[\*\]
> * one type is the type of an argument corresponding to a trailing ellipsis in a function call and the other is specified as the type argument of an invocation of the `va_arg` macro;
> * one type is the type of an argument to a function such as `fprintf` or the type pointed to by an argument to a function such as `fscanf`, and the other is the type implied by the corresponding conversion specifier.
>
> \[\*\] If a prototype is in scope, conversion is as if by assignment and the
> value will be converted to zero.

Replace G.6p1 with:

> The macros
>
> > ```c
> > imaginary
> > ```
>
> and
>
> > ```c
> > _Imaginary_I
> > ```
>
> are defined, respectively, as `_Imaginary` and a constant expression of type
> `const float _Imaginary` with the value of the imaginary unit. The macro `I` is
> defined to be `_Imaginary_I` (not `_Complex_I` as stated in 7.3).
> Notwithstanding the provisions of 7.1.3, a program may undefine and then perhaps
> redefine the macro imaginary.

**Afternote**  
If WG14 wishes to take the alternative approach of moving `_Imaginary` types
more firmly into the body of the Standard, then the following areas would be
affected.

* Do not make any of the above changes.
* Add text to 4p6 explaining that imaginary types are never required.
* Merge the text from G.2 into 6.2.5.
* Merge the existing text from G.4 into 6.3.1.
* Make the cases described in the new G.4.4 above further cases of the relevant subclauses (6.5.2.2, 7.15.1.1, 7.19.6.1, 7.19.6.2, 7.24.2.1, and 7.24.2.2).
* Move G.5.1p1 and G.5.2p1 into 6.5.5 and 6.5.6.
* Delete G.6p1.
