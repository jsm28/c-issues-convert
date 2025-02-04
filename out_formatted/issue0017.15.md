## Issue 0017.15: When do array parameters get converted to pointers?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0013.01](issue0013.01.md), [0110](issue0110.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Ordering of conversion of arrays to pointers

In subclause 6.5.4.3 on page 68, line 22 there is a sentence in parentheses.
Does the sentence refer to the whole paragraph or just the preceding sentence?

```c
int f(int a[4]);
 int f(int a[5]);
 int f(int *a);
```

1. It refers to the whole paragraph. This makes all of the above three declarations compatible.
2. It does not refer to the whole paragraph. This makes all three declarations incompatible.

---

Comment from WG14 on 1997-09-23:

### Response

Regarding page 68, line 22: There are *two* sentences in parentheses. They apply
to the entire paragraph. The declarations are all compatible. (See [Defect
Report #013, Question 1](issue0013.01.md) for a clarifying correction in this
area.)
