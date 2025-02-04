## Issue 0035.01: Can one declare an enumeration or struct tag as part of an old-style parameter declaration?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-039  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_035.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_035.html)

```c
void f(a, b)
 int a(enum b {x, y});
 int b;
 {
 }
```

Now this example is perverse because a prototype declaration is used to declare
the parameter of an old-style function declaration. But anyway ...

Is the declaration of the parameter `a` legal or a constraint error?

Now `a(...)` is a declarator.

Subclause 6.7.1 says on page 82, lines 7-8:

> ... each declaration in the declaration list shall have at least one declarator,
> and those declarators shall declare only identifiers from the identifier list.

The identifier list contains `a` and `b`.

The declarator for parameter `a` declares the identifiers `a`, `b`, `x`, and
`y`.

`b` is in the identifier list, so that is okay. But `x` and `y` are not.
Constraint error (methinks so)?

See subclause 6.1.2, page 19 for a definition of an identifier.

---

Comment from WG14 on 1997-09-23:

### Response

There is no constraint violation. The scopes of `b`, `x`, and `y` end at the
right-parenthesis at the end of the `enum`, so there is no violation. It is
difficult to *call* the function `f`, but there is no constraint violation. The
phrase “each declarator declares one identifier” in subclause 6.5.4 refers to
`a`, not to `b`, `x`, or `y`.

As an example, in the conforming definition:

```c
void f(a, b)
 int a(enum b{x, y});
 int b;
 {
 }
```

the scope of `b` (the enum tag), `x`, and `y` ends at the right-parenthesis at
the end of the enum (prototype scope).
