## Issue 0342: VLAs and conditional expressions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Joseph Myers \<joseph@codesourcery.com\>, Joseph Myers (UK)  
Date: 2007-03-24  
Reference document: [ISO/IEC WG14 N1223](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1223.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Cross-references: [0340](../c99/issue0340.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_342.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_342.htm)

### Summary

Consider the code:

```c
    int a, b;
    void *p1(void), *p2(void);
    int c1(void);
    int d1(void);
    int z1(void), z2(void);

    int
    h(void)
    {
      int r = (c1()
               ? (z1(), (int (*)[d1()])p1())
               : (z2(), (int (*)[])p2()))[a][b];
      return r;
    }
```

The type of the conditional expression involves the size expression `d1()`
that's only evaluated in one part of the expression, and this information is
needed to evaluate the array reference even when `c1()` returns false.

For a more complicated example and discussion see reflector messages
10731-10754. The validity of that more complicated example depends on the
interpretation of composite type rules as in [DR 340](../c99/issue0340.md), so this
example has been simplified to avoid that problem.

### Suggested Technical Corrigendum

6.7.5.2 paragraph 6 at end add "or one of the size specifiers (including the
case of a single size specifier where the other array type does not include a
size specifier) is not an integer constant expression and is not evaluated
during the flow of execution." with a footnote "This case arises where a
conditional expression involves a cast to variably modified type or a compound
literal of variably modified type."

---

Comment from WG14 on 2008-09-10:

### Committee Discussion (for history only)

#### Spring 2008

The consensus is that the *Note* in the previous version of this DR was not
accurate and should be removed. The DR should be in Review status

#### Fall 2008

The consensus at this meeting is that this defect should be linked with defect
report 340\.

### Proposed Committee Response

See [defect report 340](../c99/issue0340.md)
