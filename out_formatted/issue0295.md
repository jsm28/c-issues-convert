## Issue 0295: Incomplete types for function parameters

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Neil Booth, Project Editor (Larry Jones)  
Date: 2004-03-19  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_295.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_295.htm)

### Summary

The standard appears to be contradictory with respect to whether a function
parameter is permitted to have an incomplete type in a prototype other than the
function definition.

6.7.5.3p12 says:

> If the function declarator is not part of a definition of that function,
> parameters may have incomplete type....

But 6.7p7 says:

> If an identifier for an object is declared with no linkage, the type for the
> object shall be complete by the end of its declarator...; in the case of
> function arguments \[n.b., that should be *parameters*, not *arguments*]
> (including in prototypes), it is the adjusted type (see 6.7.5.3) that is
> required to be complete.

If the intent is to allow incomplete types, there do not appear to be any
constraints forbidding constructions like:

> ```c
> void func(void parm);
> ```

---

Comment from WG14 on 2004-09-28:

### Committee Discussion

The Committee agrees that “function arguments” should be “function parameters”.
The cited text from 6.7p7 refers to the declarations of parameters in the
definition of that function; each parameter declares an object whose adjusted
type is required to be complete. Declarations of parameters in prototypes which
are not part of the definition of that function are permitted to declare
incomplete types. Whenever that function is called, arguments are implicitly
converted to the types of the corresponding parameters; see 6.5.2.2p7. The
requirements upon assignment require that the types of the corresponding
parameters are complete types, at the point of calling the function. The
constraint at 6.5.16p2 requires a modifiable lvalue for the left operand of
assignment, and according to 6.3.2.1p1, a modifiable lvalue shall not have
incomplete type.

The Committee agrees that there do not appear to be any constraints forbidding
constructions like

> ```c
> void func(void parm);
> ```

nor are any semantics provided for this construction.

### Technical Corrigendum

Change 6.7p7

> in the case of function arguments (including in prototypes)

to:

> in the case of function parameters (including in prototypes)
