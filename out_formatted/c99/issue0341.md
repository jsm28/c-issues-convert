## Issue 0341: `[*]` in abstract declarators

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Joseph Myers \<joseph@codesourcery.com\>, Joseph Myers (UK)  
Date: 2007-03-24  
Reference document: [ISO/IEC WG14 N1222](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1222.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_341.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_341.htm)

### Summary

6.7.5.2#4 says that `*` as an array size "can only be used in declarations with
function prototype scope", and paragraph 5 says "If the size is an expression
that is not an integer constant expression: if it occurs in a declaration at
function prototype scope, it is treated as if it were replaced by `*`".

But is a type name in a function prototype a declaration, and does it have
function prototype scope? Scopes are only defined in 6.2.1 for identifiers, and
such type names do not declare identifiers. The presence of `[*]` in the syntax
for abstract declarators suggests that

```c
    void f(int (*)[*]);
```

was intended to be valid and `void f(int (*)[a]);` was intended to be equivalent
to it, but there are no declarations at function prototype scope involved.

Similarly, what is "in" such a declaration? Is the following valid?

```c
    void f(int (*)[sizeof(int (*)[*])]);
```

Although the `[*]` lies within a parameter declaration, it's within an
expression inside it; not one of the declarators involved in declaring the
identifier with function prototype scope.

### Suggested Technical Corrigendum

6.7.5.2 paragraph 4, change "declarations with function prototype scope" to "the
nested sequence of declarators or abstract declarators for a function parameter
in a function declaration that is not a definition"; remove the footnote.
Paragraph 5, change "declaration at function prototype scope" to "the nested
sequence of declarators or abstract declarators for a function parameter in a
function declaration that is not a definition".

---

Comment from WG14 on 2008-07-21:

### Committee Discussion

#### Spring 2007

There was consensus that the first example should be valid, and the second
should be invalid.

Also see [N1238](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1238.htm).

**Fall 2007**

Above reference to N1238 is not relevant.

It appears the issue hinges entirely on the point that a *type-name* is not a
declaration and does not declare an identifier, and because of that it has no
scope. Instead of adding complex wording to avoid using the term "scope" as
suggested in the DR, it seems clearer to modify the definition of Scope such
that it applies to *type-name*, which is described in 6.7.6 as "syntactically a
declaration for a function or an object of that type that omits the identifier".

**Spring 2008**

The Committee does not see a way to avoid this change, it seems to be safe. Not
altogether satisfied with the aesthetics of this change, but this seems to be a
satisfactory way forward.

### Technical Corrigendum

6.2.1, add a new paragraph at the end (following paragraph 7):

> As a special case, a *type-name* (which is not a declaration of an identifier)
> is considered to have a scope that begins just after the place within the
> *type-name* where the omitted identifier would appear were it not omitted.

Also add a forward reference to Type names (6.7.6).

6.7.5.2 paragraph 4, change

> declarations with function prototype scope

to

> declarations or type-names with function prototype scope
