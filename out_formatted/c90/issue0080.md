## Issue 0080: Questions on merging of string constants

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_080.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_080.html)

Item 17 \- merging of string constants

Consider the following code:

```c
char *s1 = "abcde" + 2;
 char *s2 = "cde";
```

Can the expression `(s1 == s2)` be non-zero? Is the answer different if the
first string literal is replaced by the two literals `"ab" "cde"` (because then
there are identical string literals)?

---

Comment from WG14 on 1997-09-23:

### Response

When the last paragraph of subclause 6.1.4 refers to “string literals” it is
referring to the static arrays created in translation phase 7 as specified in
the previous paragraph. Although the current wording of the C Standard may imply
that only completely identical arrays need not be distinct, this was not the
Committee's intent.

### Correction

***In subclause 6.1.4, page 31, change the last paragraph of Semantics (before
the Example) from:***

Identical string literals of either form need not be distinct. If the program
attempts to modify a string literal of either form, the behavior is undefined.

***to:***

These arrays need not be distinct provided their elements have the appropriate
values. If the program attempts to modify such an array, the behavior is
undefined.
