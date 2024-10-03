For the fragment

```c
if (a**b||c++d)
 ;
```

[Defect Report #017 Question 39](issue:0017.39) states that this is lexed as:

a. {`if`} {`(`} {`a`} {`<<`} {`b`} {`||`} {`c`} {`>>`} {`d`} {`)`}

not as:

b. {`if`} {`(`} {`a`} {`**b||c++`} {`d`} {`)`}

The rationale for this interpretation was that the constraint in subclause
6.1.7, page 32, lines 33-34 disallowed a header name preprocessing token
anywhere except within a `#include`. Since the header name preprocessing token
could not exist it was not lexed as such.

It was pointed out that the “longest possible token” rule was not influenced by
rules elsewhere in the C Standard, i.e. `i+++++j` is lexed as:

c. {`i`} {`++`} {`++`} {`+`} {`j`}

not as:

d. {`i`} {`++`} {`+`} {`++`} {`j`}

Now (c) is a constraint violation by subclause 6.3.2.4, page 42, lines 38-39,
the operand of the second `++` is not a modifiable lvalue. But this constraint
does not require that the input be re-lexed to form the preprocessing tokens
given in (d), which is conforming code.

As the UK C Panel saw it, the first example should be lexed as given in (b) and
a diagnostic issued. Having violated a constraint, we are now into undefined
behavior. An implementation could define the behavior in this circumstance to be
a re-lex of the input to produce the preprocessing tokens given in (a).

As far as the user was concerned, they would get the expected behavior with the
added value of a diagnostic being issued.

All those present felt that the interpretation was incorrect and recommended
that the UK ask the Committee to reconsider its decision.

To summarize, there is no ambiguity in the C Standard and the original X3J11
interpretation is incorrect.
