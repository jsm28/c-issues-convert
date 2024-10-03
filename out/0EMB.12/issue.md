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
