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
