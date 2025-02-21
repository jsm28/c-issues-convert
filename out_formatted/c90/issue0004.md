## Issue 0004: Are multiple definitions of unused identifiers with external linkage permitted?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Paul Eggert, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-012  
Submitted against: C90  
Status: Fixed  
Fixed in: C90  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_004.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_004.html)

Are multiple definitions of unused identifiers with external linkage permitted?

The wording in subclause 6.7 permits multiple definitions of identifiers with
external linkage, so long as the identifiers are never used. For example, the
following program is “strictly conforming” if you read the wording in subclause
6.7 literally:

```c
int F() {return 0;}
 int F() {return 1;}
 int V = 0;
 int V = 1;
 int main() {return 0;}
```

This must be a bug in the wording of subclause 6.7. It cannot have been the
Committee's intent, since it prohibits the most commonly encountered linker
model. For example, most linkers will flatly refuse to link the following
“strictly conforming” program

```c
x.c:
```

> ```c
> int F() {return 0;}
>      int G(int i) {return i;}
> ```

y.c:

> ```c
>     int F() {return 1;}
>      int G(int);
>      int main() {return G(0);}
> ```

because `F` is defined twice.

---

Comment from WG14 on 1997-09-23:

### Response

This Defect Report referred to an earlier draft of the C Standard, and was
corrected prior to the publication of the C Standard.
