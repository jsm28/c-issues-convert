## Issue 0420: syntax error in specification of for-statement

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jens Gustedt  
Date: 2012-10-08  
Reference document: [N1647](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1647.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The standard lists two different forms for the `for`-statement in 6.8.5p1:

```c
for ( expression[opt] ; expression[opt] ; expression[opt] ) statement
for ( declaration expression[opt] ; expression[opt] ) statement
```

whereas later in 6.8.5.3 these two forms are subsumed in a third form by:

```c
for ( clause-1 ; expression-2 ; expression-3 ) statement
```

Obviously the second form above is a typo and doesn't fit within this third
form, the semantic that is given in 6.8.5.3 and to common practice in existing
compilers.

### Suggested Technical Corrigendum

Replace the second form in 6.8.5p1 and A.2.3 by the intended one:

```c
for ( declaration expression[opt] ; expression[opt] ; expression[opt] ) statement
```

---

Comment from WG14 on 2013-04-26:

Oct 2012 meeting

### Proposed Committee Response

> The second form of for-statement is not a typo. The syntax for "declaration", in
> 6.7 paragraph 1, includes an optional init-declarator-list and a trailing
> semicolon.
