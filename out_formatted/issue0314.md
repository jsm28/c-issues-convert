## Issue 0314: Cross-translation-unit tagged type compatibility

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Joseph Myers \<joseph@codesourcery.com\>, UK C Panel  
Date: 2005-03-04  
Reference document: [ISO/IEC WG14 N1102](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1102.htm)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_314.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_314.htm)

### Summary

Compatibility of tagged types can be intransitive when there are multiple
translation units:

```c
// TU 1:
struct s;
struct t { struct s *a; };

// TU 2:
struct s { int p; };
struct t { struct s *a; };

// TU 3:
struct s { long q; };
struct t { struct s *a; };
```

where `struct t` in TU 1 is compatible with that in TU 2 and TU 3 but they are
not compatible with each other.

C\+\+ avoids problems with such cases by giving types linkage, meaning that the
incompatible definitions of named struct types yield undefined behavior. In C
types do not have linkage, and such incompatibilities can give rise to several
problems. The requirement of 6.2.7#2 that "All declarations that refer to the
same object or function shall have compatible type; otherwise, the behavior is
undefined." does not seem sufficient to avoid all such problems.

Question 1: Does 6.2.7#2 refer to the types immediately after the declarations,
or the types at any point where the declarations are in scope?

Question 2: If each of the above three translation units started `extern struct
t *x;`, would there be undefined behavior?

Even if the requirement applies to the types anywhere in scope, this may not be
enough. Each translation unit above could have prepended to it

```c
struct t;
static void f(void) { extern struct t *x; }
```

and the incompatible completions are not within the scope of `x`. (`x` might
then be defined in another translation unit that just says `struct t *x;`.)

The above example at least leads to incompatible "ultimate" types for `x` that
the object has at the end of each translation unit, albeit outside the scope of
the declaration. But now consider the following three translation units.

```c
// TU 1:
struct s;
struct t { struct s *a; };
int g1(struct s *);
int g2(struct s *);
int f(struct t *p, int x) { return x ? g1(p->a) : g2(p->a); }

// TU 2:
struct t { int b; };
struct s { int a; struct t *z; };
int g1(struct s *p) { return p->a  + p->z->b; }

// TU 3:
struct t { long c; };
struct s { struct t *z; long a; };
int g2(struct s *p) { return p->a + p->z->c; }
```

Each object and function has a well-defined complete type. But a `struct t` in
TU 1 may contain pointers to two different versions of `struct s`, and each of
these contains pointers to an entirely different `struct t` from that in TU 1\.
This requires very strange gymnastics for an implementation inlining across
translation units to inline `g1` and `g2` into `f`. There is no single
translation unit representing a natural merger of the three above; renaming
static objects with conflicting names does not suffice (indeed, there are no
such objects), and renaming type names used in different names in different
translation units does not help either because there is no single natural
expression of a recursive completion of TU 1's `struct t`.

Question 3: Is an implementation required to accept compiling the three
translation units above together into a program?

This issue arises directly from actual implementation problems implementing
optimizations across multiple translation units in GCC. It is natural for an
implementation to take multiple translation units and convert them into a
language-independent intermediate representation of the whole program which is
then optimized, and in so doing to unify the declarations in different
translation units which refer to the same object or function. But unifying them
involves unifying their types, and so recursively the types involved in the
definitions of those types, and the above translation units, although apparently
valid to link into a single program at present, do not admit of such a
unification.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2008-09-12:

### Committee Discussion (for history only)

2006-10-25, There was not consensus for the *Proposed Committee Response* listed
below. There was no consensus that question 2 is *undefined behavior*. There
does not seem to be specific words in the Standard that make it undefined
behavior, however that may be what the Committee intended.

#### Spring 2007

See [N1237](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1237.htm).

#### Fall 2007

The Standard doesn't seem to specifically allow the compilation/linking of the
three translations units in question, but is does not seem to disallow it
either.

#### Spring 2008

Current response is good. However, is this is an issue that should be addressed
in C1x? Looked again at N1237 (reviewed in Kona).

* publish an answer that C99 is unspecified/undefined, and we will fix it in C1x
* just come up with a fix for C1x

There is consensus that it should be possible for an implementation to combine
the translation units of a program into a single internal representation and
optimize that, unifying structure and union types across translation units where
required to be compatible in the process.

Normally, it is possible to create a single translation unit equivalent to
multiple translation units, after renaming static variables and functions and
structure and union tags. DR314 question 3 is an example where such renaming is
not possible. My proposal is to add a requirement that it is possible.

It was noted that this has been hanging around for several years. Needs someone
to actually come up with the right words.

### Proposed Committee Response

Question 1: Does 6.2.7#2 refer to the types immediately after the declarations,
or the types at any point where the declarations are in scope?

> Subclause 6.2.7 Paragraph 2 makes a statement about *all* declarations of the
> same object or function, regardless of where the declarations that object or
> function are. It requires that all declarations of the same object or function,
> even if those declarations are in different translation units of the program, to
> have compatible type.  
> Note also that if an object with struct or union type is declared with an
> incomplete type, and that type is later completed in the same scope, the type of
> the declaration is the completed type (Subclause 6.2.5, Paragraph 22). Under
> such conditions, the type of the object or function is the completed type, and
> that type must be compatible with any other declarations.

Question 2: If each of the above three translation units started `extern struct
t *x;`, would there be undefined behavior?

> Yes, undefined behavior.

Question 3: Is an implementation required to accept compiling the three
translation units above together into a program?

> It was never the Committees intention that the standard be interpreted this way.  
> This will be addressed in a future revision of the standard. See WG14 N**xxx**.
