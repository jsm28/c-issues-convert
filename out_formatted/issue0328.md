## Issue 0328: String literals in compound literal initialization

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: \<whyglinux@gmail.com\>, Project Editor (Larry Jones)  
Date: 2006-06-03  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Cross-references: [0339](issue0339.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_328.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_328.htm)

### Summary

6.5.2.5 Compound literals, paragraph 3 in ISO/IEC 9899:1999 C Standard says:

> If the compound literal occurs outside the body of a function, the initializer
> list shall consist of constant expressions.

This is to say a string literal, which is neither a constant nor a constant
expression, can not be taken to initialize a compound literal with static
storage duration. However, this is not the fact.

String literals can not be constants because they are not among constants
(defined in Section 6.4.4). When a string literal is used to initialize a
compound literal (in the case an array type), the array-to-pointer conversion
does not occur (6.3.2.1 Lvalues, arrays, and function designators, paragraph 3),
and hence the string literal can not be an address constant, which is the only
chance to become a constant expression.

Obviously string literals should be mentioned together with constant
expressions. It should be:

> If the compound literal occurs outside the body of a function, the initializer
> list shall consist of constant expressions or string literals.

The following paragraph excerpted from Page 125, 6.7.8-4 seems to support the
above correction:

> All the expressions in an initializer for an object that has static storage
> duration shall be constant expressions or string literals.

### Suggested Technical Corrigendum

Change 6.5.2.5, paragraph 3, to:

> If the compound literal occurs outside the body of a function, the initializer
> list shall consist of constant expressions or string literals.

---

Comment from WG14 on 2007-10-10:

### Proposed Technical Corrigendum

Replace 6.5.2.5 paragraph 2 and 3 to:

> All the constraints for initializer lists in 6.7.8 are applicable to compound
> literals.

Change 6.5.2.5 paragraph 7 to:

> All the semantic rules for initializers lists in 6.7.8 are applicable to
> compound literals.<sup>82\)</sup>
