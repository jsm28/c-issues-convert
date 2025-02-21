## Issue 0014.02: How does `fscanf("%n")` behave on end-of-file?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Max K. Goff, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-049  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0167](../c90/issue0167.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_014.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_014.html)

X/Open Reference Number KRT3.159.2

Subclause 7.9.6.2 **The `fscanf` function** states:

> If end-of-file is encountered during input, conversion is terminated. If
> end-of-file occurs before any characters matching the current input directive
> have been read (other than leading white space, where permitted), execution of
> the current directive terminates with input failure; otherwise, unless execution
> of the current directive is terminated with a matching failure, execution of the
> following directive (if any) is terminated with an input failure.

How should an implementation behave when end-of-file terminates an input stream
that satisfies all conversion specifications that consume input but there is a
remaining specification request that consumes no input (e.g. `%n`)? Should the
non-input-consuming directive be evaluated or terminated with an input failure
as described above?

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 7.9.6.2, page 137, line 4 (the*** `n` ***conversion
specifier):***

No argument is converted, but one is consumed. If the conversion specification
with this conversion specifier is not one of `%n`, `%ln`, or `%hn`, the behavior
is undefined.

***Add to subclause 7.9.6.2, page 138, another Example:***

In:

```c
#include <stdio.h>
 /* ... */
 int d1, d2, n1, n2, i;
 i = sscanf("123", "%d%n%n%d",&d1, &n1, &n2, &d2);
```

the value 123 is assigned to `d1` and the value 3 to `n1` . Because `%n` can
never get an input failure the value of 3 is also assigned to `n2`. The value of
`d2` is not affected. The value 3 is assigned to `i`.
