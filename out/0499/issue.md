### Summary

```c
Given the following code:

union U {
  struct {
    char B1;
    char B2;
    char B3;
    char B4;
  };
  int word;
} u;

Does the storage of B1, B2, B3 and B4 overlap?

According to 6.7.2.1#13, the members should overlap in storage as they become members of 'union U'.
At least one implementation (GCC) seems to NOT consider them to be overlapping.
At least one implementation (IBM's XL LE AIX) considers them to be overlapping as the standard currently states.

Similar code present in example 1 on 6.7.2.1#19.

Suggested TC:
  If the intent is that the members do NOT overlap:
    Append to 6.7.2.1#13:
      Anonymous structures maintain the structure type if they are considered to be members of the containing union.*)
      *) This means the structure members are not considered to occupy the same storage as if they were directly union members.
  If the intent is that the members DO overlap:
    No change, or perhaps add on a comment to 6.7.2.1#19 Example 1:
    ...
    struct { int i, j; }; // anonymous structure, i and j now overlap in storage
    ...
```
