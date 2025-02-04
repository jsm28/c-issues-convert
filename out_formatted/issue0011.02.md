## Issue 0011.02: Does `extern` link to a static declaration that is not visible?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Rich Peterson, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-008  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_011.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_011.html)

Interpretation of `extern`

Consider the code:

```c
/* File scope */
 static int i;           /* declaration 1 */

 main()
 {
 extern int i;           /* declaration 2 */
 {
     extern int i;       /* declaration 3 */
 }
 }
```

A literal reading of subclause 6.1.2.2 says that declarations 1 and 2 have
internal linkage, but that declaration 3 has external linkage (since declaration
1 is not visible, being hidden by declaration 2). (This combination of internal
and external linkage is undefined by subclause 6.1.2.2, page 21, lines 27-28.)

Is this what is intended?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.1.2.2, page 21, change:***

If the declaration of an identifier for an object or a function contains the
storage-class specifier `extern`, the identifier has the same linkage as any
visible declaration of the identifier with file scope. If there is no visible
declaration with file scope, the identifier has external linkage.

***to:***

For an identifier declared with the storage-class specifier `extern` in a scope
in which a prior declaration of that identifier is visible**\***, if the prior
declaration specifies internal or external linkage, the linkage of the
identifier at the latter declaration becomes the linkage specified at the prior
declaration. If no prior declaration is visible, or if the prior declaration
specifies no linkage, then the identifier has external linkage. \[Footnote \*:
As specified in 6.1.2.1, the latter declaration might hide the prior
declaration.]
