ANSI/ISO C Defect Report #rfg30:

Subject: “Type categories” and qualified types.

a) Is the following code strictly conforming?

b) Must a conforming implementation correctly translate the following code?

```c
enum E1 { enumerator1 = (const int) 9 };        /* ? */
 enum E2 { enumerator2 = (volatile int) 9 };    /* ? */
```

Background:

Subclause 6.5.2.2 (**Constraints**):

> The expression that defines the value of an enumeration constant shall be an
> integral constant expression that has a value representable as an `int`.

Subclause 6.4 (**Semantics**):

> Cast operators in an integral constant expression shall only convert arithmetic
> types to integral types, ...

Subclause 6.1.2.5:

> The type `char`, the signed and unsigned integer types, and the enumerated types
> are collectively called *integral types.*

Subclause 6.1.2.5:

> Any type so far mentioned mentioned is an unqualified type. Each *unqualified
> type* has three corresponding *qualified versions* of its type: ... The
> qualified or unqualified versions of a type are distinct types that belong to
> the same type category ...

The problem is with the term “type category.” I have been unable to find any
actual definition of this term in the C Standard. My assumption is that
*integral types* constitute one such “type category,” but it would be nice to
have the Committee's assurances about this. More specifically, I think that it
would be advisable to add a statement somewhat like the following one just after
the first paragraph in subclause 6.1.2.5:

> In addition to the partitioning of types into *object types, function types,*
> and *incomplete types,* each type is also said to belong to some *type
> category.* The *type categories* are *integral types, floating types, pointer
> types, structure types, union types, array types, void types,* and *function
> types.*
