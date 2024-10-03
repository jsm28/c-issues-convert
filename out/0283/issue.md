*\[This report isolates one of the points from [DR257](issue:0257).]*

### Problem

In the paragraph corresponding to 6.5.2.3#5, C89 contained this sentence:

> With one exception, if a member of a union object is accessed after a value has
> been stored in a different member of the object, the behavior is
> implementation-defined.

Associated with that sentence was this footnote:

> The "byte orders" for scalar types are invisible to isolated programs that do
> not indulge in type punning (for example, by assigning to one member of a union
> and inspecting the storage by accessing another member that is an appropriately
> sixed array of character type), but must be accounted for when conforming to
> externally imposed storage layouts.

The only corresponding verbiage in C99 is 6.2.6.1#7:

> When a value is stored in a member of an object of union type, the bytes of the
> object representation that do not correspond to that member but do correspond to
> other members take unspecified values, but the value of the union object shall
> not thereby become a trap representation.

It is not perfectly clear that the C99 words have the same implications as the
C89 words.

### Suggested Technical Corrigendum

*\[Essentially verbatim from [DR257](issue:0257)]*

Attach a new footnote 78a to the words "named member" in 6.5.2.3#3:

> 78a If the member used to access the contents of a union object is not the same
> as the member last used to store a value in the object, the appropriate part of
> the object representation of the value is reinterpreted as an object
> representation in the new type as described in 6.2.6 (a process sometimes called
> "type punning"). This might be a trap representation.
