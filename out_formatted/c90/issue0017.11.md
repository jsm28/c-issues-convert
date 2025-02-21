## Issue 0017.11: Is `struct t; struct t;` valid?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Clarification of incomplete `struct` declaration

Referring to subclause 6.5.2.3, page 62:

```c
struct t;
 struct t; /* Is this undefined? */
```

People seem to think that the above is undefined.

The problem arises because no rules exist for compatibility of incomplete
structures or unions.

---

Comment from WG14 on 1997-09-23:

### Response

The proposed example is valid. Nothing in the standard prohibits it.

The relevant citation is subclause 6.5.2.3 Semantics, paragraph 2:

> A declaration of the form
>
> ```c
>     struct-or-union  identifier ;
> ```
>
> specifies a structure or union type and declares a tag, both visible only within
> the scope in which the declaration occurs. It specifies a new type distinct from
> any type with the same tag in an enclosing scope (if any).
