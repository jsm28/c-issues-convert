## Issue 0042.03: How big is a string object defined by the `str*` functions?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Tom MacDonald, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-001  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_042.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_042.html)

Similar questions arise for the other library string handling functions that
have undefined behavior when copying between overlapping objects. These include
`strcpy`, `strncpy`, `strcat`, `strncat`, `strxfrm`, `mbstowcs`, `wcstombs`,
`strftime`, `vsprintf`, `sscanf`, and `sprintf`. For these functions, however,
the number of bytes referenced through each pointer depends, at least in part,
upon the values stored in the bytes.

Consider a library function for which the number of bytes accessed or modified
is affected by the values of the bytes. Is the object associated with each of
its pointer arguments the smallest contiguous sequence of bytes actually
accessed or modified through that pointer?

In Example 4:

```c
void f4(void) {
        extern char b[2*N];
        strcpy(b+N, b);
        }
```

is the behavior defined if `N >> strlen(b)`?

In Example 5:

```c
void f5(void) {
        extern char c[2*N];
        strcat(c+N, c);
        }
```

is the behavior defined if both `N >> strlen(c)` and `N >> strlen(c) +
strlen(c+N)`?

---

Comment from WG14 on 1997-09-23:

### Response

Length is determined by “various methods.” For strings in which all elements are
accessed, length is inferred by null-byte termination. For `mbstowcs`,
`wcstombs`, `strftime`, `vsprintf`, `sscanf`, `sprintf` and all other similar
functions, it was the intent of the C Standard that the rules in subclause
7.11.1 be applicable by extension (i.e., the objects and lengths are similarly
dynamically determined). The behavior (in Examples 4 and 5\) is defined.
