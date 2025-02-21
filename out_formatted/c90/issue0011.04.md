## Issue 0011.04: Does an incomplete array get completed as a tentative definition?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Rich Peterson, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-008  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_011.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_011.html)

Tentative definition of externally-linked object with incomplete type

If one writes the file-scope declaration

```c
int i[];
```

then subclause 6.7.2 suggests that at the end of the translation unit the
implicit declaration

```c
int i[] = {0};
```

or equivalently

```c
int i[1] = {0};
```

appears. This seems peculiar, since subclause 6.7.2, (page 83, lines 35-36)
specifically forbids this case for internally linked identifiers.

Is this what is intended?

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.7.2, page 84, a second Example:***

If at the end of the translation unit containing

```c
int i[];
```

the array `i` still has incomplete type, the array is assumed to have one
element. This element is initialized to zero on program startup.
