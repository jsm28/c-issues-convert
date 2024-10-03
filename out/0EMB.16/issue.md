Problem: The first sentence of 4.1.6.2.1 para 5 (' According to the rules above,
the result type of an arithmetic operation where (at least) one operand has a
fixed-point type is always a fixed- point type.') is wrong as it does not take
operands with floating-point type into account.

Solution: As it is the intention to only discuss integer types and fixed-point
types in this paragraph, change the sentence accordingly.

Change: Modify the first sentence of 4.1.6.2.1 para 5 to read: 'According to the
rules above, the result type of an arithmetic operation where one operand has a
fixed-point type and the other operand has an integer or a fixed-point type is
always a fixed-point type.'
