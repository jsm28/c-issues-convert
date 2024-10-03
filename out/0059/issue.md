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
