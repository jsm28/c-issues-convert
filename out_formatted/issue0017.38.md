## Issue 0017.38: What is an iteration control structure or selection control structure?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

What is an iteration control structure or selection control structure?

An “iteration control structure,” a term used in subclause 5.2.4.1 **Translation
limits** on page 13, line 1, is not defined by the standard.

Is it:

1. A `for` loop header excluding its body, e.g. `for (;;)`,

   or
2. A `for` loop header plus its body, e.g. `for (;;) {}`?

Does it make a difference if the compound statement is a simple statement
without the braces?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 5.2.4.1, page 13, lines 1-2, change:***

\- 15 nested levels of compound statements, iteration control structures, and
selection control structures

***to:***

\- 15 nested levels of compound statements, iteration statements, and selection
statements
