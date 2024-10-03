Clarification of incomplete `struct` declaration

Referring to subclause 6.5.2.3, page 62:

```c
struct t;
 struct t; /* Is this undefined? */
```

People seem to think that the above is undefined.

The problem arises because no rules exist for compatibility of incomplete
structures or unions.
