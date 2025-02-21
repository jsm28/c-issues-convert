## Issue 0046: May a typedef be redeclared as a parameter outside an old-style function parameter list?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Neal Weidenhofer, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-041  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_046.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_046.html)

In subclause 6.7.1, page 82, line 9, it says, “An identifier declared as a
typedef name shall not be redeclared as a parameter.”

The question I have is: Does that sentence stand by itself absolutely or is it
intended to be read in the context of the paragraph in which it appears?

The beginning of the paragraph says, “If the declarator includes an identifier
list, ...” Function declarators including a parameter type list are dealt with
in the preceding paragraph which says nothing about typedef names.

In other words, is the following valid Standard C?

```c
typedef int foo;
 int bar(int foo) {return foo; }
```

---

Comment from WG14 on 1997-09-23:

### Response

The sentence is a part of the paragraph in which it appears. An identifier
declared as a typedef name may be redeclared as a parameter in a parameter type
list. The example is strictly conforming.
