## Issue 0059: Must an incomplete type be completed by the end of a translation unit?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Martin Ruckert, Project Editor (P.J. Plauger)  
Date: 1993-06-15  
Submitted against: C90  
Status: Closed  
Cross-references: [0139](../c90/issue0139.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_059.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_059.html)

The ISO Standard for the programming language C explains the notion of
*incomplete type* in subclause 6.1.2.5 and subclause 6.5.2.3 (for structures).
Both sections do not explicitly require that an incomplete type eventually must
be completed, nor do they explicitly allow incomplete types to remain incomplete
for the whole compilation unit.

Since this feature is of importance for the declaration of true opaque data
types, it deserves clarification. I propose to add to the fourth paragraph on
page 24 (subclause 6.1.2.5) the sentence: “It is admissable that an incomplete
type remain incomplete in the whole compilation unit.”

The type `void` is already an incomplete type which is never completed.

The examples given in the standard document explain that incomplete types are
exclusively needed to define mutual referential structures. Opaque data types,
however, constitute a second use for this feature. Considering mutual
referential structures defined and implemented in different compilation units
makes the idea of an opaque data type a natural extension of an incomplete data
type.

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard intentionally contains no prohibition against leaving a type
incomplete. (As you so aptly observe, `void` is an incomplete type that is never
completed.) There is no need to make a positive statement about the absence of a
prohibition.

Moreover, the examples were not intended to represent that mutual referencing
was the only reason for permitting incomplete structure types. Opaque data types
were considered, and endorsed, by the Committee when drafting the C Standard.
