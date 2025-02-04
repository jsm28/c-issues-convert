## Issue 0CFP.04: Part 3: Error in function name

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas et al.  
Date: 2016-03-19  
Reference document: [N2029](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2029.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

Page 32: In 12.3, the function name is written as “**scoshdNx**”, instead of
“**coshdNx**” as intended. Although correcting the mistake could be seen as a
substantive change, it is clear from the context that this function is in the
family of **cosh** functions. It is extremely unlikely that any implementer
would not have recognized the mistake and provided the function with the
erroneous name.

### Suggested Technical Corrigendum

Page 32: In 12.3, change “**scoshdNx**” to “**coshdNx**”.

---

Comment from WG14 on 2018-10-18:

Apr 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

Page 32: In 12.3, change “**scoshdNx**” to “**coshdNx**”.
