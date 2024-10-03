In subclause 6.4, page 55, line 10, a constraint specifies that a comma operator
may not appear in a constant expression (except within the operand of a `sizeof`
operator).

At the end of the same section, page 56, line 1, it says, “An implementation may
accept other forms of constant expressions.”

Does the later statement give a license to relax the earlier constraint? For
example, may a conforming implementation accept

```c
int i = (1, 2);
```

without issuing a diagnostic?
