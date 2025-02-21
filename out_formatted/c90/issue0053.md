## Issue 0053: Do the aliasing rules cover accesses to different function pointers properly?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1993-03-25  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0168](../c90/issue0168.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_053.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_053.html)

There's been a discussion on `comp.std.c` recently about accessing a pointer to
a function with parameter type information through a pointer to a pointer to a
function without parameter type information. For example:

```c
int f(int);
        int (*fp1)(int);
        int (*fp2)();
        int (**fpp)();

        fp1 = f;
        fp2 = fp1;      /* pointers to compatible types, assignment ok */
        (*fp2)(3);      /* function types are compatible, call is ok */
        fpp = &fp1; /* pointer to compatible types, assignment ok */
        (**fpp)(3);     /* valid? */
```

The final call itself should be valid since the resulting function type is
compatible with the type of the function being called, but there's still a
problem: Subclause 6.3 **Expressions**, page 38, says:

> An object shall have its stored value accessed only by an lvalue expression that
> has one of the following types:**36**
>
> \- the declared type of the object,
>
> \- a qualified version of the declared type of the object,
>
> \- a type that is the signed or unsigned type corresponding to the declared type
> of the object,
>
> \- a type that is the signed or unsigned type corresponding to a qualified
> version of the declared type of the object,
>
> \- an aggregate or union type that includes one of the aforementioned types
> among its members (including, recursively, a member of a subaggregate or
> contained union), or
>
> \- a character type.
>
> \[Footnote 36: The intent of this list is to specify those circumstances in
> which an object may or may not be aliased.\]

This would appear to render the final call undefined since the stored value of
`fp1` is being accessed by an lvalue that does not match its declared type:
`(int (*)())` vs. `(int (*)(int))`.

I think that this example should be valid and that the above limitation is too
strict. I think what we meant to say was “*a type compatible with* the declared
type of the object,” which would allow “reasonable” type mismatches without
allowing aliasing between wildly different types.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.3, page 38, lines 18-21, change:***

An object shall have its stored value accessed only by an lvalue expression that
has one of the following types:**36**

\- the declared type of the object,

\- a qualified version of the declared type of the object,

***to:***

An object shall have its stored value accessed only by an lvalue expression that
has one of the following types:**36**

\- a type compatible with the declared type of the object,

\- a qualified version of a type compatible with the declared type of the
object,
