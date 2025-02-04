## Issue 0502: Flexible array member in an anonymous struct

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Martin Sebor  
Date: 2016-09-18  
Reference document: [N2080](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2080.htm)  
Submitted against: C11 / C17  
Status: Closed  
Cross-references: [0499](issue0499.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

**EXAMPLE 3** in paragraph 26 of **§6.7.2.1 Structure and union specifiers**
shows a valid definition of a struct containing both an anonymous struct and a
flexible array member:

> –26–   EXAMPLE 3   Because members of anonymous structures and unions are
> considered to be members of the containing structure or union, `struct s` in the
> following example has more than one named member and thus the use of a flexible
> array member is valid.
>
> ```c
>     struct s {
>         struct { int i; };
>         int a[];
>     };
> ```

Now consider the following ever so slightly modified but seemingly equivalent
version of the same example. Is it also valid?

```c
    struct s {
        int i;
        struct { int a[]; };
    };
```

Paragraph 13 of the section referenced above specifies that:

> An unnamed member whose type specifier is a structure specifier with no tag is
> called an anonymous structure; \[...]. The members of an anonymous structure or
> union are considered to be members of the containing structure or union. This
> applies recursively if the containing structure or union is also anonymous.

Subsequently, paragraph 18 of the same section defines a *flexible array member*
as follows:

> As a special case, the last element of a structure with more than one named
> member may have an incomplete array type; this is called a *flexible array
> member*.

A possible interpretation of these two paragraphs applied to the modified
example above is that, since the flexible array member `a` is considered to be a
member of `struct s` that has a preceding data member and no members following
the anonymous struct, the example is valid.

However, another possible interpretation (offered in reflector message
[SC22WG14.14299](https://www.open-std.org/jtc1/sc22/wg14/14299 "flexible array
member in an anonymous struct")) is that:

> *...the layout \[of a struct containing an anonymous struct] is exactly as if
> the contained anonymous structure or union had a name (so it acts like a
> structure is declared as such even if contained in a union, or like a union if
> declared as such even if contained in a structure), with all the usual
> constraints applying to the contained structure or union, and the only
> difference being a shorthand notation for naming members of the contained
> structure or union.*

According to this interpretation, the defintion in the example is not valid.
This interpretation appears to be reflected in the behavior of a number of
tested implementations: they all diagnose it, indicating that a flexible array
may not be the sole member of a struct.

We believe both of these interpretations are reasonable and the standard,
therefore, to be ambiguous on this point. In addition, despite support for the
latter interpretation in existing practice, we don't know of any technical
reason to disallow flexible arrays as sole members in anonymous structs.

It is worth noting that the lack of clarity in this area has also given rise to
DR [499](issue0499.md).

As a separate issue, the definition of a flexible array member cited above
refers to such a member as an *element* of a structure. This is unusual (and
raises a question about the meaning of the word in this context) because the
term element is otherwise reserved to refer to elements of an array or to
enumerators, but not to members of structures. If the text doesn't intend to
differentiate flexible array members from other members beyond the explicitly
spelled out constraints it should make use of the word member consistently and
avoid using the term *element*.

### Suggested Technical Corrigendum

The standard needs to be clarified to avoid the ambiguity discussed above.

We suggest that the standard be made clear that defining a flexible array as the
sole member of an anonymous struct is permitted as long as the flexible array is
not the sole member of the enclosing object.

Since we believe the standard can already be interpreted as proposed, we suggest
to add a new paragraph to the end of **§6.7.2.1 Structure and union specifiers**
with the following text.

> –27–   EXAMPLE 4   Similarly to example 3, since the flexible array member `a`
> defined in the anonymous struct is considered a member of the enclosing `struct
> t` that declares a preceding named member and no subsequent members, the use of
> the flexible array member is valid:
>
> ```c
>     struct t {
>         int i;
>         struct { int a[]; };
>     };
> ```

In addition, we suggest that the word *element* in the definition of the term
*flexible array member* be replaced with the word *member* (or, alternatively,
that the meaning of the term element in this context be defined and clearly
distinguished from other uses of the term in the text such as those referring to
elements of arrays).

To that end, we propose to modify **§6.7.2.1 Structure and union specifiers**,
paragraph 18, as indicated below:

> –18–   As a special case, the last <u>member</u> ~~element~~ of a structure with
> more than one named member may have an incomplete array type; this is called a
> *flexible array member*. …

---

Comment from WG14 on 2018-04-26:

Oct 2016 meeting

### Committee Discussion

> The committee agrees that defining a flexible array as the sole member of an
> anonymous struct is permitted as long as the flexible array is not the sole
> member of the enclosing object.
>
> This issue might also be resolved via [DR 499](issue0499.md)

Apr 2017 meeting

### Committee Discussion

> After further discussion and review, the committee does not support the
> interpretation that §6.7.2.1 paragraph 13 overrides the paragraph 18\.

### Proposed Committee Response

> The committee does not support the interpretation that §6.7.2.1 paragraph 13
> overrides the paragraph 18\. No struct or union, even anonymous, should have a
> size of zero, and since the effect desired is easily achieved, there is no
> motivation for creating a second mechanism to achieve that purpose.
