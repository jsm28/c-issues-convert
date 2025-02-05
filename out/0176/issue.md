*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 024: Diagnostics for `#error`

The rules concerning whether `#error` generates a diagnostic are contradictory.

Subclause 5.1.1.3 reads:

> A conforming implementation shall produce at least one diagnostic message
> (identified in an implementation-defined manner) for every translation unit that
> contains a violation of any syntax rule or constraint. Diagnostic messages need
> not be produced in other circumstances.

Subclause 6.8.5 reads:

> **Semantics**
>
> A preprocessing directive of the form
>
> ```c
>           # error pp-tokens    new-line                   opt
> ```

causes the implementation to produce a diagnostic message that includes the
specified sequence of preprocessing tokens.

Since this is not in a Constraints section, these two statements directly
contradict one another. Furthermore, the second statement can be read as
applying to a `#error` directive that is excluded by a false `#if` condition.

### Suggested Technical Corrigendum

In subclause 6.8.5, replace the entire subclause with:

**Constraints**

A `#error` preprocessing directive shall not occur in a translation unit. Any
diagnostic message generated because of the violation of this constraint
\[Footnote: The intent of this subclause is that `#error` indicates that
translation should fail. As stated in subclause 5.1.1.3, a translation unit
excludes lines within the *false* side of `#if` ... `#else` ... `#endif`
groups.\] shall include the sequence of preprocessing tokens in the directive.
