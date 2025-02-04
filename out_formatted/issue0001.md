## Issue 0001: Do functions return values by copying?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Paul Eggert, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-009  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0100](issue0100.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_001.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_001.html)

Do functions return values by copying?

The C Standard is clear (in subclause 6.3.2.2) that function arguments are
copied, but is not clear (in subclause 6.6.6.4) whether a function's returned
value is also copied. This question becomes an issue in the assignment statement
`s=f();` where `f` yields a structure: is the result defined when the structure
`s` overlaps the structure that `f` obtained the returned value from?

I ask this question because the GNU C compiler does not copy the structure in
this case. When I filed the enclosed bug report \[omitted from this document],
Richard Stallman, the author of GNU C, replied that he didn't think that
Standard C required the extra copy. I sympathize with Stallman's desire for
efficient code, and I also would prefer that the C Standard did not require the
extra copy here, but the point should be made clear in the C Standard.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.6.6.4, page 80, lines 30-32, replace:***

If the expression has a type different from that of the function in which it
appears, it is converted as if it were assigned to an object of that type.

***with:***

If the expression has a type different from the return type of the function in
which it appears, the value is converted as if by assignment to an object having
the return type of the function.**\***

\[Footnote \*: The `return` statement is not an assignment. The overlap
restriction in subclause 6.3.16.1 does not apply to the case of function
return.]

***Add to subclause 6.6.6.4, page 80:***

**Example**

In:

```c
struct s {double i;} f(void);
 union {struct {int f1;
                struct s f2;} u1;
        struct {struct s f3;
                int f4;} u2;
       } g;
 struct s f(void)
         {
         return g.u1.f2;
         }
 /* ... */
 g.u2.f3 = f();
```

the behavior is defined.
