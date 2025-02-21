## Issue 0237: Declarations using `[static]`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14 Convener (J. Benito)  
Date: 2001-04-25  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_237.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_237.htm)

**Summary** Given the following declarations:

```c
  void f(int n, int x[static n]);
   void f(int n, int x[n]) {}
```

An example at the end of 6.7.5.3 (p21) indicates that these declarations are
compatible, but it seems like there should also be something about this in
composite types.

1. If some declarations include "static" and some don't, what is the effect?
2. Does `static` only count if it is on the definition?
3. Does it count if it is on the declaration visible for a given call?

---

Comment from WG14 on 2003-10-23:

### Committee Discussion

The Committee discussed adding a footnote to 6.7.5.3 paragraph 7 along the lines
of item 1\.

### Committee Response

The Committee believe the specification about composite types is clear enough;
the composite type will be based on "qualified pointer to *type*", and the
`static` keyword (and any size values) are not used.

1. The effect is as if all of the declarations had used `static` and the largest size value used by any of them. Each declaration imposes requirements on all calls to the function in the program; the only way to meet all of these requirements is to always provide pointers to as many objects as the largest such value requires.
2. No.
3. Yes. Visibility is not relevant.
