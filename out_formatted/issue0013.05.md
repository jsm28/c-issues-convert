## Issue 0013.05: When is the `sizeof` an enumeration type known?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0118](issue0118.md), [0165](issue0165.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

Enumeration tag anomaly

Consider the following (bizarre) example:

```c
enum strange1 {
         a = sizeof (enum strange1)      /* line [2] */
 };
 enum strange2 {
         b = sizeof (enum strange2 *)    /* line [5] */
 };
```

The respective tags are visible on lines \[2] and \[5] (according to subclause
6.1.2.1, page 20, lines 39-40, but there is no rule in subclause 6.5.2.3,
**Semantics** (page 62\) that governs their meaning on lines \[2] and \[5].
Footnote 62 on page 62 seems to be written without taking this case into
account.

The first declaration must be illegal. The second declaration should be illegal
for simplicity.

Perhaps these declarations are already illegal, since no rule gives them a
meaning. To clarify matters, I suggest in subclause 6.5.2.3 appending to page
62, line 35:

> A type specifier of the form
>
> ```c
> enum identifier
> ```
>
> shall not occur prior to the end of the `enumerator-list` that defines the
> content.

If this sentence is not appended, something like it should appear as a footnote.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.5.2.3, page 63, another Example:***

An enumeration type is compatible with some integral type. An implementation may
delay the choice of which integral type until all enumeration constants have
been seen. Thus in:

```c
enum f { c = sizeof(enum f) };
```

the behavior is undefined since the size of the respective enumeration type is
not necessarily known when `sizeof`
