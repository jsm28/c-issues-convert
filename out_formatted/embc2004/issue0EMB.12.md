## Issue 0EMB.12: Address space qualifier in specifier-qualifier-list

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [207](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/207)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: in the new text for 6.7.2.1, the TR adds a constraint:

> The *specifier-qualifier-list* in the declaration of a member of a structure or
> union shall not include an address space qualifier.

This is a mistake, because it keeps us from declaring something innocuous like

```c
struct onePointer { _X int *pX; };
```

As written, the constraint would make the member declaration invalid, whereas we
only intended to prohibit declarations such as this:

```c
struct oneInteger { _X int iX; };
```

Proposed solution: change the constraint to be:

> Within a structure or union specifier, the type of a member shall not be
> qualified by an address space qualifier.

---

Comment from WG14 on 2004-11-15:

Problem: The new text for 6.7.2.1, requires that a specifier-qualifier-list in
the declaration of a member of a structure or union shall not include an address
space qualifier. This disallows for instance the type of a member of structure
to be a pointer into a named address space.

Solution: The intention was to disallow members of a single structure/union to
have different address qualifiers.

Change: Modify the constraint for 6.7.2.1 to be: 'Within a structure or union
specifier, the type of a member shall not be qualified by an address space
qualifier.'
