## Issue 0317: Function definitions with empty parentheses

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Joseph Myers \<joseph@codesourcery.com\>, UK C Panel  
Date: 2005-03-04  
Reference document: [ISO/IEC WG14 N1105](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1105.htm)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_317.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_317.htm)

### Summary

I believe the intent of C is that old-style function definitions with empty
parentheses do not give the function a type including a prototype for the rest
of the translation unit. For example,

```c
void f(){}
void g(){if(0)f(1);}
```

is valid.

6.9.1#7 specifies that if the declarator in the function definition includes a
parameter type list, it also serves as a prototype for the rest of the
translation unit. It does not specify that nothing else serves as a prototype.
Some readers of the standard interpret 6.7.5.3#14, "An empty list in a function
declarator that is part of a definition of that function specifies that the
function has no parameters.", as specifying that it provides a prototype.

Question 1: Does such a function definition give the function a type including a
prototype for the rest of the translation unit?

Question 2: Is the above translation unit valid?

### Suggested Technical Corrigendum

---

Comment from WG14 on 2006-04-04:

### Committee Response

The grammar states that an empty parens stands for an empty identifier list not
an empty parameter-type-list.

The answer to question #1 is NO, and to question #2 is YES. There are no
constraint violations, however, if the function call were executed it would have
undefined behavior. See 6.5.2.2;p6.
