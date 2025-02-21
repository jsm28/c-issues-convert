## Issue 0165: Is the wording of subclause 6.5.2.3 concerning tags defective?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Cross-references: [0013.05](../c90/issue0013.05.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_165.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_165.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 013: Tags and incomplete types

The wording of subclause 6.5.2.3 concerning tags is defective in a number of
ways.

**Part 1**

The first paragraph states that:

If this declaration of the tag is visible, a subsequent declaration that uses
the tag and that omits the bracketed list specifies the declared structure,
union, or enumerated type.

This neither handles the case of a type name (for example, in the operand of the
`sizeof` operator), nor does it make it clear whether or not the rule applies
within the braces of the first declaration (the tag is in scope from the open
brace).

In other words, it fails to address either occurrence of `struct tag *` in the
following code:

```c
  {
         struct tag { int i [sizeof (struct tag *)]; };
         int j [sizeof (struct tag *)];
 /* ... */
        }
```

**Part 2**

The second paragraph does not adequately distinguish between type specifiers
which refer to an incomplete type and those which refer to a type in an outer
scope. For example, in the following code, it fails to indicate whether or not
all the uses of the tag refer to the same type:

```c
struct tag;
 struct tag *p;
         {
         struct tag *q;
         /* ... */
         }
        struct tag { int member; };
```

**Part 3**

The handling of enumerated types before their content is defined is also
unclear; this was covered to some extent in [DR013Q5](../c90/issue0013.05.md) and
subsequent discussion on the WG14 mailing list.

For example, what is the status of the following code:

```c
enum tag { e = sizeof (enum tag ******) };
```

or of:

```c
enum tag { e0, e1, e2, e3 };
         {
         enum tag2 { e4 = sizeof (enum tag); };
         enum tag  { e5 = sizeof (enum tag); };
        }
```

If an enumeration tag cannot be used before the end of the list defining its
contents, a diagnostic ought to be required.

**Part 4**

If the same tag is used in a type specifier with a contents list twice in the
same scope, it is unclear whether or not a diagnostic is required. It could be
argued that, since this is forbidden by the semantics in subclause 6.5.2.3, it
is not excluded from the second constraint of subclause 6.5, and so a diagnostic
is required by that constraint. However, this may be viewed as clutching at
straws. An explicit constraint should be added.

### Suggested Technical Corrigendum

Rather than making piecemeal changes to address each issue separately, the whole
subclause should be rewritten. Footnote numbers have been chosen to match the
present footnotes.

**Constraints**

A specific type shall have its content defined at most once.

A type specifier of the form

```c
          enum identifier
```

without an enumerator list shall only appear when the type it specifies is
complete.

**Semantics**

All declarations of structure, union, or enumerated types that have the same
scope and use the same tag declare the same type. The type is incomplete \[63\]
until the closing brace of the list defining the content, and complete
thereafter. \[Footnote 63: An incomplete type may only be used when the size of
an object of that type is not needed.\]

\[Append the present wording, or see Defect Report CA-2-09 \- submitted
independently \- for alternative wording.\]

Two declarations of structure, union, or enumerated types which are in different
scopes or use different tags declare distinct types. Each declaration of a
structure, union, or enumerated type which does not include a tag declares a
distinct type.

A type specifier of the form

```c
          struct-or-union identifier    { struct-declaration-list }
                                  opt or
            enum identifier    { enumerator-list }
                                 opt
```

declares a structure, union, or enumerated type. The list defines the *structure
content, union content,* or *enumeration content.* If an identifier is provided
\[64\], the type specifier also declares the identifier to be the tag of that
type. \[Footnote 64: If there is no identifier, the type can, within the
translation unit, only be referred to by the declaration of which it is a part.
Of course, when the declaration is of a typedef name, subsequent declarations
can make use of that typedef name to declare objects having the specified
structure, union, or enumerated type.\]

A declaration of the form

```c
          struct-or-union identifier ;
```

specifies a structure or union type and declares the identifier as the tag of
that type \[62\]. \[Footnote 62: A similar construction with `enum` does not
exist.\]

If a type specifier of the form

```c
          struct-or-union identifier
```

occurs other than as part of one of the above constructions, and no other
declaration of the identifier as a tag is visible, then it declares a structure
or union type which is incomplete at this point, and declares the identifier as
the tag of that type \[62\].

If a type specifier of the form

```c
          struct-or-union identifier
```

or

```c
          enum identifier
```

occurs other than as part of one of the above constructions, and a declaration
of the identifier as a tag is visible, then it specifies the same type as that
other declaration, and does not redeclare the tag.
