Item 17 \- merging of string constants

Consider the following code:

```c
char *s1 = "abcde" + 2;
 char *s2 = "cde";
```

Can the expression `(s1 == s2)` be non-zero? Is the answer different if the
first string literal is replaced by the two literals `"ab" "cde"` (because then
there are identical string literals)?
