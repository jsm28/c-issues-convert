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
> function arguments \[n.b., that should be *parameters*, not *arguments*\]
> (including in prototypes), it is the adjusted type (see 6.7.5.3) that is
> required to be complete.

If the intent is to allow incomplete types, there do not appear to be any
constraints forbidding constructions like:

> ```c
> void func(void parm);
> ```
