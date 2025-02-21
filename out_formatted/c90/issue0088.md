## Issue 0088: Are two incomplete structure types with a (lexically) identical tag always compatible?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0139](../c90/issue0139.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_088.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_088.html)

*\[Question was revised in Dec 94\]*

Item 25 \- compatibility of incomplete types

According to subclause 6.1.2.6 **Compatible type and composite type**, an
incomplete structure type is incompatible with everything except “the same
type:”

> Two types *have compatible type* if their types are the same.

The C Standard fails to define when exactly two types are “the same.” It is
intuitively clear in context of basic types and array or pointer derivation, but
becomes vague when genuinely new structure or union types are involved,
especially when they are created as incomplete types first and completed later.

a) Are two incomplete structure types with a (lexically) identical tag always
“the same” in the sense of subclause 6.1.2.6? It would appear not, unless they
are declared in the same scope of the same translation unit.

b) Can two different incomplete structure types be compatible in other ways? If
so, how?

c) Is a structure type before and after completion “the same type” in the sense
of subclause 6.1.2.6? If the answer to (c) is no, then questions (d) to (g)
apply.

d) Are the types before completion and after completion compatible?

Consider the following translation unit (the file `a.c`):

```c
 struct tag;

 int a1 (struct tag * p)
        { a2 (p); }             /* Line A */

 struct tag { int i; } s;

 int main ()
        {
        a1 (&s);
        return 0;
        }

 int a2 (struct tag * p)
        { /* ... */ }
```

e) Is the call to `a2` in line A valid? The parameter and argument types appear
to be incompatible.

f) Suppose that the definition of `a2` were moved to a separate translation
unit, preceded by a definition of `struct tag` which was compatible with the one
in the above translation unit. Would the call in line A then be valid?

g) A constraint in subclause 6.5 demands that:

> All declarations in the same scope that refer to the same object or function
> shall specify compatible types.

Does this mean that:

```c
struct tag;
 extern struct tag* p;          /* Line B */

 struct tag { int x; }
 extern struct tag* p;
```

requires a diagnostic since the two declarations of `p` specify incompatible
types? If not, what is the type `p` is declared as in Line B ?

If the answer to (c) is yes, then question (h) applies.

h) If two types `A` and `B` are compatible, is `A` compatible with all types
that are the same as `B`? For example, is the call in line D below valid? If the
redeclaration in line C is omitted, does undefined behavior result?

```c
 /* First translation unit */

 struct tag;
 int c1 (struct tag * p)
        { /* ... */ }

 struct tag { int i; };         /* Line C */

 /* Second translation unit */

 struct tag { int i; } s;
 int main()
        {
        c1 (&s);            /* Line D */
        return 0;
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

a) No.

b) Yes, see the Response to [Defect Report #139](../c90/issue0139.md).

c) Yes. The C Standard failed to make clear that the type remains the same, but
that is the obvious intent.

d) through (g) not applicable, because of the response to (c).

h) Yes, yes, and no.
