## Issue 0026: Can one use other than the basic C character set in a strictly conforming program?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Randall Meyers, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-007  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_026.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_026.html)

Example:

```c
#include stdio.h>
 int main()
 {
 puts("@$(etc.)");
 return 0;
 }
```

Is this a strictly conforming program?

---

Comment from WG14 on 1997-09-23:

### Response

Strictly conforming programs cannot depend on unspecified or
implementation-defined behavior (cf. clause 4, page 3, lines 31-32). Note that
`@` and `$` are extended source characters. Source characters are translated to
execution characters in an unspecified manner (cf. subclause 5.2.1). This is in
the `"C"` locale. The `@` character is either a printing character or a control
character, either of which is implementation-defined (subclause 7.3, page 102,
lines 8-11). Therefore, the program is *not* strictly conforming.
