## Issue 0027: May a standard conforming implementation add identifier characters?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Randall Meyers, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-008  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_027.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_027.html)

May a standard conforming implementation make characters in its character set
that are not in the required source character set identifier characters? Can
these additional identifier characters be used in preprocessor identifier tokens
as well as post-processor identifier tokens?

Subclause G.5.2 states:

> Characters other than the underscore `_`, letters, and digits, that are not
> defined in the required source character set (such as the dollar sign `$`, or
> characters in national character sets) may appear in an identifier (subclause
> 6.1.2).

---

Comment from WG14 on 1997-09-23:

### Response

May a standard conforming implementation make characters in its character set
that are not in the required source character set identifier characters?

Answer: Yes.

Can these additional identifier characters be used in preprocessor identifier
tokens as well as post-processor identifier tokens?

Answer: Yes, but the C Standard is currently ambiguous about the parsing of a
definition such as:

```c
#define abc$ x
```

This could either define `abc$` as `x` or `abc` as `$x`. The Correction that
follows resolves the ambiguity.

### Correction

***Add to subclause 6.8, page 86 (Constraints):***

In the definition of an object-like macro, if the first character of a
replacement list is not a character required by subclause 5.2.1, then there
shall be white-space separation between the identifier and the replacement
list.**\***

\[Footnote \*: This allows an implementation to choose to interpret the
directive:

```c
#define THIS$AND$THAT(a, b) ((a) + (b))
```

as defining a function-like macro `THIS$AND$THAT`, rather than an object-like
macro `THIS`. Whichever choice it makes, it must also issue a diagnostic.]
