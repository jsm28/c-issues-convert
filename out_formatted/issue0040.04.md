## Issue 0040.04: Should the response to [Defect Report #017, Q39](issue0017.39.md) be reconsidered?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Submitted against: C90  
Status: Closed  
Cross-references: [0017.39](issue0017.39.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

For the fragment

```c
if (a**b||c++d)
 ;
```

[Defect Report #017 Question 39](issue0017.39.md) states that this is lexed as:

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

---

Comment from WG14 on 1997-09-23:

### Response

Is a diagnostic required for an input such as

```c
if (a**b||c++d)
```

because of a violation of the constraint specified in subclause 6.1.7, page 32,
lines 33-34?

Answer: No. Our response to [Defect Report #017 Question 39](issue0017.39.md)
addresses this issue.
