## Issue 0444: Issues with alignment in C11, part 1

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Joseph Myers  
Date: 2013-07-23  
Reference document: [N1731](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1731.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

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

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

> * The desired and intended syntax is indeed missing.
> * Whereas one could achieve the desired effect by placing the directive on the aggregate itself and controlling it by the maximum alignment of each of its members, this is far from the intended goal, and we do consider this a defect.
> * We solicit a suggested technical corrigendum from the author.
> * Modifying the definition of type name will require considerable thought.
> * Applying the directive beyond aggregate members, such as a simple scalar declaration, is not well defined, and brings in the various storage durations and how or whether all or any are supported.

Apr 2014 meeting

### Committee Discussion

* The author provided the following technical corrigendum as input to [N1804](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1804.htm):   
   6.7.2.1#1: Move the definition of specifier-qualifier-list to 6.7.7#1. Insert a new definition in 6.7.2.1#1:
  > specifier-qualifier-alignment-list:
  >
  > type-specifier specifier-qualifier-alignment-list\_opt  
  > type-qualifier specifier-qualifier-alignment-list\_opt  
  > alignment-specifier specifier-qualifier-alignment-list\_opt

  Change the use of specifier-qualifier-list in the syntax for struct-declaration
  to specifier-qualifier-alignment-list.

  6.7.2#2:

  > Change "and in the specifier-qualifier list in each struct declaration and type
  > name" to ", in the specifier-qualifier-alignment list in each struct declaration
  > and in the specifier-qualifier list in each type name".

  6.7.3#5:

  > Change "specifier-qualifier-list" to "specifier-qualifier-list,
  > specifier-qualifier-alignment-list or declaration-specifiers" (twice).

  (That the wording about duplicate qualifiers and qualifiers used with \_Atomic doesn't deal with declaration-specifiers, the syntax production relevant to normal declarations, is a pre-existing problem noticed in the course of preparing this wording.)

  (I believe all the semantics and constraints required for alignment specifiers
  on members are in place, including 6.2.7#1 dealing with cross-translation-unit
  type compatibility and references to bit-fields and members in 6.7.5.)
* The committee agrees with this as the proper direction and will solicit further review from implementors.

Oct 2014 meeting

### Committee Discussion

> There still has not been adequate review of these changes. The Project Editor
> and others have been asked to examine these changes closely prior to our next
> meeting.

Apr 2015 meeting

### Committee Discussion

> The suggested syntax provided by the author has been adopted on a trial basis in
> at least one implementation. It does not, however, provide for compound
> literals.
>
> A simpler syntax change was discussed, to wit
>
> > *specifier-qualifier-list*:
> >
> > > *type-specifier specifier-qualifier-list<sub>opt</sub>*
> > >
> > > *type-qualifier specifier-qualifier-list<sub>opt</sub>*
> > >
> > > <ins>*alignment-specifier specifier-qualifier-list<sub>opt</sub>*</ins>
>
> where *specifier-qualifier-list* is used in the grammar in only two productions:
> *struct-declaration* (which relates to the primary purpose of this DR), and
> *type-name*, which is used only in the definitions of these constructs:
>
> * generic association (generic selection)
> * compound literal
> * `sizeof` expression
> * `_Alignof` expression
> * cast expression
> * atomic type specifier
> * alignment specifier
>
> A constraint could be added to 6.7.7 *type-name* after paragraph 1 disallowing
> the use of *alignment-specifier* in a *type-name* except in the case of
> *compound literal* which was deemed useful by the committee. The following
> principles were elucidated:
>
> * `_Alignas` needs to be applied wherever objects are laid out in memory. On modern architectures page and cache line alignment of data structures is increasingly critical for performance.
> * Alignment is incorporated into the type system for structure (and union) members, but otherwise is not considered part of the type.
>
> In 6.7.3p5, there are two references to *specifier-qualifier-list*, which should
> also reference declaration specifiers.
>
> In 6.7.5 paragraphs 2 and 4, there are occurrences of the phrase “alignment
> attribute” which should instead read “alignment specifier”

Oct 2015 meeting

### Committee Discussion

> The committee did not discuss the direction from the last meeting in any
> substantial manner. It has solicited a paper from the author of the direction
> expressing these ideas as a Suggested Technical Corrigendum.

Apr 2016 meeting

### Committee Discussion

> A new paper [N2028](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2028.htm)
> was submitted that embodied the direction above and the committee accepted it.

Oct 2016 meeting

### Committee Discussion

> It was noted that C\+\+ allows one additional production for
> *alignment-specifier* between `struct` and *tag*.
>
> The paper [N2028](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2028.htm)
> was presented which had an alternate suggestion for a resolution, but the
> committee preferred the following.

**Proposed Technical Correigendum**

Change 6.7.2.1p1 from

> *specifier-qualifier-list*:
>
> > *type-specifier specifier-qualifier-list<sub>opt</sub>*
> >
> > *type-qualifier specifier-qualifier-list<sub>opt</sub>*

to

> *specifier-qualifier-list*:
>
> > *type-specifier specifier-qualifier-list<sub>opt</sub>*
> >
> > *type-qualifier specifier-qualifier-list<sub>opt</sub>*
> >
> > *alignment-specifier specifier-qualifier-list<sub>opt</sub>*

Change 6.7.5p2 from

> An alignment attribute shall not be specified in a declaration of a typedef, or
> a bit-field, or a function, or a parameter, or an object declared with the
> `register` storage-class specifier.

to

> An alignment specifier shall appear only in the declaration specifiers of a
> declaration, or in the specifier-qualifier list of a member declaration, or in
> the type name of a compound literal. An alignment specifier shall not be used in
> conjunction with either of the storage-class specifiers `typedef` or `register`,
> nor in a declaration of a function or bit-field.

Change 6.7.3p5 from

> If the same qualifier appears more than once in the same
> *specifier-qualifier-list*, either directly or via one or more `typedef`s, the
> behavior is the same as if it appeared only once. If other qualifiers appear
> along with the `_Atomic` qualifier in a *specifier-qualifier-list*, the
> resulting type is the so-qualified atomic type.

to

> If the same qualifier appears more than once in the same
> *specifier-qualifier-list* or as *declaration-specifiers*, either directly or
> via one or more `typedef`s, the behavior is the same as if it appeared only
> once. If other qualifiers appear along with the `_Atomic` qualifier the
> resulting type is the so-qualified atomic type.

Change 6.7.5p4 from

> The combined effect of all alignment attributes in a declaration shall not...

to

> The combined effect of all alignment specifiers in a declaration shall not...
