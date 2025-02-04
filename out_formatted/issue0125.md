## Issue 0125: When are declarations useing `extern` *(qualified)* `void` not conforming?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0012](issue0012.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_125.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_125.html)

ANSI/ISO C Defect Report #rfg32:

Subject: Using things declared as “`extern` (qualified) `void`.”

May a conforming implementation fail to correctly translate a translation unit
containing the following declarations?

```c
extern const void etext;
 const void *vp = &etext;
```

Background:

[Defect Report #012](issue0012.md) discusses at length the issue of applying unary
`&` to an expression whose type is some void type. The conclusion of that
discussion seem to be that although unary `&` *may not* be applied to an
expression having *the* `void` type (because such expressions are not lvalues)
it *is* permissible to apply unary `&` to an expression whose type is some
qualified version of `void`. The text of the interpretation for [Defect Report
#012](issue0012.md) even goes so far as to actively recommend the practice of
declaring things to be `extern` and to have some qualified void type (so that
the address may then be taken).

The question raised herein is a different one. Tom Pennello has pointed out the
following rule from the second **Semantics** paragraph of subclause 6.7:

> If an identifier declared with external linkage is used in an expression (other
> than as part of the operand of a `sizeof` operator), somewhere in the entire
> program there shall be exactly one external definition for the identifier; ...

Thus, as Tom has noted, applying unary `&` to an entity declared to be both
`extern` and of some qualified void type is a “use” of that entity which would
necessarily force you to supply a definition of that entity, somewhere in the
program. But as Tom has further noted, there is simply no way to accomplish that
(in a strictly conforming program) because of the following rule (given in
subclause 6.5):

> All declarations ... that refer to the same object or function shall specify
> compatible types.

Thus, if you either define or fail to define `etext`, it would appear that the
behavior is undefined. Is this a correct interpretation?

(Footnote: It would appear that a strictly conforming program may contain a mere
declaration of an `extern` entity whose type is any qualified or unqualified
void type, but that any use of such an entity within an expression, other than
within a `sizeof` expression, renders the program not strictly conforming.)

---

Comment from WG14 on 1997-09-23:

### Response

Applying `&` to an identifier of type `const void` has undefined behavior. Thus
an implementation can define any semantics it wishes. A strictly conforming
program cannot contain such a construct.
