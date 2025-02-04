## Issue 0033: Must a conforming implementation diagnose *shall* violations outside **Constraints**?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Mike Vermeulen, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-037  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_033.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_033.html)

Is a conforming implementation required to diagnose all violations of “shall”
and “shall not” statements in the standard, even if those statements occur
outside of a section labeled **Constraints**?

An example that illustrates this question is:

```c
struct s { char field:1; };
```

This fragment violates a statement in subclause 6.5.2.1 on page 60, line 30: “A
bit-field shall have a type that is a qualified or unqualified version of one of
`int`, `unsigned int`, or `signed int`.” Must a conforming implementation issue
a diagnostic for this violation of “shall?”

Following are two different ways in which the C Standard has been interpreted.
These interpretations came up during discussions over NIST conformance tests for
an ANSI-C FIPS. I would like to ask the Committee for an interpretation of this
issue, perhaps based on one or both of the interpretations given.

**Suggested Interpretation #1**:

Clause 3 **Definitions and conventions** states in the very beginning: “In this
International Standard, ‘shall' is to be interpreted as a requirement on an
implementation or on a program; conversely, ‘shall not' is to be interpreted as
a prohibition.”

Therefore *every* “shall” is viewed as testable. The question is what happens if
a “shall” is violated.

Subclause 5.1.1.3 **Diagnostics** provides the answer: “A conforming
implementation shall produce at least one diagnostic message (identified in an
implementation-defined manner) for every translation unit that contains a
violation of *any syntax rule* or *constraint.* Diagnostic messages *need not
be* produced in other circumstances.” (emphasis added)

Therefore every violation of a “shall” should be treated as a failure to meet
the requirements of the C Standard (first definition). Any violation of syntax
rules, semantic rules, or sections labeled as **Constraints** should therefore
generate a diagnostic.

According to this interpretation, a diagnostic should be produced for the
example given above.

**Suggested Interpretation #2**:

Subclause 5.1.1.3 states that diagnostics must be produced “for every
translation unit that contains a violation of any syntax rule or constraint.
Diagnostic messages need not be produced in other circumstances.”

*Syntax rules* are those items listed in the **Syntax** sections of the
standard. *Constraints* are those items listed in the **Constraints** sections
of the standard.

The C Standard specifies in clause 3, page 3, lines 12-13 that when the words
“shall” or “shall not” appearing outside of a constraint are violated, the
behavior is undefined.

For undefined behavior, the C Standard specifies in clause 3, page 3, lines 6-7
that the standard “imposes no requirements.” Thus a conformance suite should not
test for the words “shall” or “shall not” outside of a **Constraints** section,
since the standard imposes no requirements.

According to this interpretation, the C Standard imposes no requirements on a
conforming implementation for the program fragment above. A conforming
implementation could choose to accept this program (see also Footnote 6 to
subclause 5.1.1.3 on page 6), it could issue a diagnostic, or have any other
behavior.

---

Comment from WG14 on 1997-09-23:

### Response

Concerning a violation of subclause 6.5.2.1, **Semantics**, page 60, line 30: No
diagnostic is required; this is undefined behavior. It is not a violation of a
constraint or syntax.

Concerning a violation of clause 3, page 2, lines 2-3, No diagnostic is
required.

Suggested Interpretation #2 is the correct one.

Conformance to FIPS is beyond the scope of WG14. We can't comment on this.
