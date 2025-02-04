## Issue 0339: Variably modified compound literals

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Joseph Myers \<joseph@codesourcery.com\>, Joseph Myers (UK)  
Date: 2007-03-24  
Reference document: [ISO/IEC WG14 N1120](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1220.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Cross-references: [0328](issue0328.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_339.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_339.htm)

### Summary

Consider the code:

```c
    extern int a;
    void *p = &(int (*)[a]){ 0 };
```

Does such a variably modified compound literal at file scope violate any
constraint? 6.7.5.2#2 says:

> \[#2] Only an ordinary identifier (as defined in 6.2.3) with both block scope or
> function prototype scope and no linkage shall have a variably modified type. If
> an identifier is declared to be an object with static storage duration, it shall
> not have a variable length array type.

However, this only seems to constrain declarations of identifiers, not any other
expression with variably modified type (such as a compound literal, inside or
outside a function). If however the above code is valid, when is `a` evaluated
for the purposes of the requirement in 6.7.5.2#5 that "each time it is evaluated
it shall have a value greater than zero"? Must `a` have positive value
throughout execution of the program, or is it only the initial value of `a`
which must be positive? (I think the initializer **is** a constant expression,
being the address of an object of static storage duration.)

The variably modified compound literal is an object, and I think it should be
treated like other objects outside functions and required not to have variably
modified type (even if inside sizeof, just like the initializers of compound
literals outside functions must be constant even if inside `sizeof`).

### Suggested Technical Corrigendum

6.5.2.5 paragraph 3, after "shall consist of constant expressions" add "and the
type name shall not specify a variably modified type".

---

Comment from WG14 on 2008-07-21:

### Committee Discussion

Paragraph in question (paragraph 3 of 6.5.2.5) has been changed by [DR
328](issue0328.md).

The suggested Technical Corrigendum looks appropriate, however, it could be
redundant.

### Committee Response

This defect report is answered by [DR 328](issue0328.md).

Constraints and Semantics are the same as 6.7.8 Initialization
