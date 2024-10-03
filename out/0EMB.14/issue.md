Problem: The new text for 6.5.8 (relational operators) and 6.5.9 (equality
operators) add as a constraint: 'If the two operands are pointers into different
address spaces, the address spaces must overlap.'. Such a constraint is missing
for 6.5.6 (additive operators), where it is relevant for pointer subtraction.

Solution: Add the requested constraint.

Change: Add the following constraint to 6.5.6 : 'For subtraction, if the two
operands are pointers into different address spaces, the address spaces must
overlap.'
