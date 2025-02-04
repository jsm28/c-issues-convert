## Issue 0044.01: What does it mean to say that the type of `offsetof` is `size_t`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Steve M. Hoxey, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-010  
Submitted against: C90  
Status: Closed  
Cross-references: [0072](issue0072.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_044.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_044.html)

Subclause 7.1.6, page 98, lines 24-30 describe the macro

```c
offsetof(type, member_designator)
```

“which expands to an integral constant expression that has type `size_t`, ...”

How is this statement to be interpreted? The expansion of the macro `offsetof`
is

a. an expression which can be evaluated during translation, the value of which
is in the range representable by a `size_t` type.

Or

b. an expression as (a) above, but further constrained to be an “integral
constant expression” as defined in subclause 6.4, page 55, lines 17-21.

---

Comment from WG14 on 1997-09-23:

### Response

Neither alternative (a) nor (b) in Question 1 fully captures the intent. What is
intended is exactly what is specified in the C Standard. A strictly conforming
program shall not produce output that varies depending upon details of
implementation of facilities defined by the standard headers. Hence, use of the
`offsetof` macro, in a context requiring an integer constant expression, per se
does not render a program not strictly conforming.

Further clarification provided by David Prosser:

Although the replacement for the `offsetof` macro must be an integral constant
expression, and must follow all the constraints appropriate to expressions, an
implementation is permitted to make use of its extensions to constant
expressions that behave like integral constant expressions. This is why the
sample replacement expressions for the `offsetof` macro in the Rationale are
valid candidates (for many implementations) but do not come under the strict
definition of integral constant expression that strictly conforming code must
follow. In particular, this is why the `offsetof` macro exists: there was
otherwise no portable means to compute such translation-time constants.
Therefore, of the two choices, (b) is the closest, but it is not the whole
story.
