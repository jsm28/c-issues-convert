## Issue 0208: Ambiguity in initialization

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 1999-09-06  
Reference document: [ISO/IEC WG14 N892](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n892.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_208.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_208.htm)

### Summary

When there is more than one initializer for the same object it is not clear
whether both initializers are actually evaluated. Wording changes are proposed
to clarify this.

### Details

Subclause 6.7.8 paragraph 19 reads:

> The initialization shall occur in initializer list order, each initializer
> provided for a particular subobject overriding any previously listed initializer
> for the same subobject; all subobjects that are not initialized explicitly shall
> be initialized implicitly the same as objects that have static storage duration.

Paragraph 23 reads:

> The order in which any side effects occur among the initialization list
> expressions is unspecified.

If the same object is initialized twice, as in:

> ```c
> int a [2] = { f (0), f (1), [0] = f (2) };
> ```

the term "overriding" could be taken to mean that the first initializer is
ignored completely, or it could be taken to mean that the expression is
evaluated and then discarded. The proposed wording change assumes the latter.

### Suggested Technical Corrigendum

Replace 6.7.8 paragraph 23 with:

> All the initialization list expressions are evaluated, even if the resulting
> value will be overridden, but the order in which any side effects occur is
> unspecified.

---

Comment from WG14 on 2000-11-02:

### Committee Response

The question asks about the expression

> ```c
> int a [2] = { f (0), f (1), [0] = f (2) };
> ```

and the meaning of the wording

> each initializer provided for a particular subobject overriding any previously
> listed initializer for the same subobject;

It was the intention of WG14 that the call `f(0)` might, but need not, be made
when `a` is initialized. If the call *is* made, the order in which `f(0)` and
`f(2)` occur is unspecified (as is the order in which `f(1)` occurs relative to
both of these). Whether or not the call is made, the result of `f(2)` is used to
initialize `a[0]`.

The wording of paragraph 23:

> The order in which any side effects occur among the initialization list
> expressions is unspecified.

should be taken to only apply to those side effects which actually occur.

### Technical Corrigendum

In 6.7.8 paragraph 19, attach a footnote to "the same subobject":

> \[\*] Any initializer for the subobject which is overridden and so not used to
> initialize that subobject might not be evaluated at all.
