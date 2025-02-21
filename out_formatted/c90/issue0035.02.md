## Issue 0035.02: If so, what is the scope of enumeration tags and constants declared in old-style parameter declarations?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-039  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_035.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_035.html)

Also consider:

```c
void g(c)
 enum m{q, r} c;
 {
 }
```

What is the scope of `m`, `q`, and `r`?

Subclause 6.1.2.1 says on page 20, lines 28-29 “... appears outside of any block
or list of parameters, the identifier has *file scope,* ...”

It says on page 20, lines 30-31 “... appears inside a block or within the list
of parameter declarations in a function definition, the identifier has *block
scope,* ...”

Now the above three identifiers appear outside of any block or list of
parameters but they are within the list of parameter declarations.

Who wins?

---

Comment from WG14 on 1997-09-23:

### Response

The scope of `m`, `q`, and `r` ends at the close-brace (block scope). The
operative wording is the more specific statement on page 20, lines 30-31 “...
appears inside a block or within the list of parameter declarations in a
function definition, the identifier has *block scope,* ...”

As an example, in the code fragment:

```c
void g(c)
 enum m{q, r} c;
 {
 }
```

the scope of `m`, `q`, and `r` ends at the closing brace of the function
definition (block scope).
