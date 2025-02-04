## Issue 0334: Missing semantics of comparison macros

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred Tydeman (USA)  
Date: 2006-12-12  
Reference document: [ISO/IEC WG14 N1203](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1203.htm)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_334.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_334.htm)

### Summary

Section 7.12.14 Comparison macros (and subsections) are missing **Semantics**.
In particular, something along the lines of: "The usual arithmetic conversions
are performed on the operands." This matters if the two operands are of
different type, e.g., **isless(4.f/3.f,4.L/3.L)**.

In addition, we might need to add something alone the lines of: "The result of
the ... operator is ..." to each of the subsections. We should consider section
6.5.8 Relational operators when we process this defect.

We should review the **Constraints** of 6.5.\* and consider adding something
along the lines of: "Each of the operands shall have real floating-type." to
7.12.14 as a constraint. The example in 7.12.3.1 paragraph 4 which uses
**sizeof** will not work when **float** and **\_Decimal32** are the same size;
nor for **double** and **\_Decimal64** being the same size.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2008-04-16:

### Proposed Technical Corrigendum

### Committee Discussion (for history only)

#### Spring 2007

There seem to be consensus that the comparison functions are under-specified.

The Standard currently says:

> In the synopses in this subclause, real-floating indicates that the argument
> shall be an expression of real floating type.

This is well defined, see 6.2.5 para 10\. However, several in attendance believe
there should be explicit language explaining whether or not the two arguments to
a comparison macro must be the same real-floating type or allowed to be
different real-floating type.

#### Fall 2007

It as also asked for the following to be added to the committee discussion:

> IEEE-754 (and IEEE-754R) require that comparison operations work in all
> supported formats, even if the operands' format differ. C99\+TC1\+TC2, Annex
> F.3, printed page 445, first bullet says that the comparison macros (along with
> the relational and equality operators) are the IEC 60559 comparisons.

#### Spring 2008

This work could possibly fit into the *type generic/overloading* project that
needs to be completed for C1X.

### Committee Response

This issue will be addressed in a future revision of the C standard. See WG 14
document N**xxx**.
