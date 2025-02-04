## Issue 0017.19: Are macro expansions ambiguous?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Order of evaluation of macros

Refer to subclause 6.8.3, page 89\. In:

```c
#define f(a) a*g
 #define g(a) f(a)
 f(2)(9)
```

it should be defined whether this results in:

1. ```c
   2*f(9)
   ```

   or
2. `2*9*g`

X3J11 previously said, “The behavior in this case could have been specified, but
the Committee has decided more than once not to do so. \[They] do not wish to
promote this sort of macro replacement usage.”

I interpret this as saying, in other words, “If we don't define the behavior
nobody will use it.” Does anybody think this position is unusual?

People seem to agree that the behavior is ambiguous in this case. Should we
specify this case as undefined behavior?

---

Comment from WG14 on 1997-09-23:

### Response

If a fully expanded macro replacement list contains a function-like macro name
as its last preprocessing token, it is unspecified whether this macro name may
be subsequently replaced. If the behavior of the program depends upon this
unspecified behavior, then the behavior is undefined.

For example, given the definitions:

```c
#define f(a) a*g
 #define g(a) f(a)
```

the invocation:

```c
f(2)(9)
```

results in undefined behavior. Among the possible behaviors are the generation
of the preprocessing tokens:

```c
2*f(9)
```

and

```c
2*9*g
```

### Correction

***Add to subclause G.2, page 202:***

\- A fully expanded macro replacement list contains a function-like macro name
as its last preprocessing token (6.8.3).
