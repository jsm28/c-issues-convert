Description: a couple of the statements concerning effective types in 6.5 of the
C Standard are not exactly correct in the presence of address-space qualifiers.
The easiest fix is probably to modify the concept of *effective type* in the C
Standard so as not to include an address-space qualifier. (The whole concept of
*effective type* is used only in 6.5 and in one footnote elsewhere in the C
Standard.)

Possible solution: add the following section to clause 5.3 of TR 18037:

> **Clause 6.5 \- Expressions**, replace the first two sentences of paragraph 6
> with: The *effective type* of an object for an access to its stored value is the
> declared type of the object, if any, without any address-space qualifier that
> the declared type may have.<sup>72\)</sup> If a value is stored into an object
> having no declared type through an lvalue having a type that is not a character
> type, then the type of the lvalue, without any address-space qualifier, becomes
> the effective type of the object for that access and for subsequent accesses
> that do not modify the stored value.

and remove the notion *additionally access-qualified version* from TR 18037
(first replacement paragraph of paragraph 26 of 6.2.5, replacement text for
paragraph 7 of 6.5).
