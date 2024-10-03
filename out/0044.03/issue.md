Assuming (b) is the correct interpretation of Question 1, if a particular
implementation expands `offsetof` into an expression which contains operands
and/or operators which result in a violation of the definition of “integral
constant expression” from subclause 6.4, page 55, lines 17-21, does this
situation constitute:

a. a constraint violation since the expansion presented for further translation
is not an “integer constant expression?”

or

b. undefined behavior since the definition of “integral constant expression”
appears in a “shall” requirement in the semantic description of subclause 6.4
**Constant expressions**?
