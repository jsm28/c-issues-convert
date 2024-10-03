Initialization of unions with unnamed members

Subclause 6.5.7 on page 71, line 39 says: “All unnamed structure or union
members are ignored ...” On page 72, lines 22-23, it says: “... for the first
member of the union.” Subclause 6.5.2.1, page 60, line 40 and Footnote 60 say
that a field with no declarator is a member.

```c
union {
        int  :3;
        float f;} u = {3.4};
```

Should page 72 be changed to refer to the first named member or is the
initialization of a union whose first member is unnamed illegal?

It has been suggested that the situation described above is implicitly
undefined.

I think that it is a straightforward ambiguity that needs resolution one way or
the other.
