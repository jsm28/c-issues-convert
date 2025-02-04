## Issue 0089: When does multiple definitions of a macro require a diagnositc message?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_089.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_089.html)

Item 26 \- multiple definitions of macros

Consider the following code:

```c
#define macro   object_like
 #define macro(argument)        function_like
```

Does this code require a diagnostic?

The wording of subclause 6.8.3 specifies that a macro may be redefined under
certain circumstances (basically identical definitions), but does not actually
forbid any other redefinition. Thus it can be argued that the constraint in
subclause 6.8.3 is not violated, and a diagnostic is not required.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.8.3, page 89, change, in both paragraphs 2 and 3:***

may be redefined by another `#define` preprocessing directive provided that

***to:***

shall not be redefined by another `#define` preprocessing directive unless
