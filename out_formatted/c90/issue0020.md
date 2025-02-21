## Issue 0020: Is the relaxed Ref/Def linkage model conforming?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Bruce Lambert, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-006  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_020.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_020.html)

Is a compiler which allows the Relaxed Ref/Def linkage model to be considered a
conforming compiler? That is, can a compiler that compiles the following code
with no errors or warnings

```c
filea.c:
 #include stdio.h>
 void foo(void);
 int age;
 int main()
 {
 age = 24;
 printf("my age is %d.\n", age);
 foo();
 printf("my age is %d.\n", age);
 return 0;
 }

 fileb.c:
 #include <stdio.h>
 int age;
 void foo()
 {
 age = 25;
 printf("your age is %d.\n", age);
 }
```

and which produces the following output

```c
my age is 24
 your age is 25
 my age is 25
```

be called a standard-compliant compiler?

---

Comment from WG14 on 1997-09-23:

### Response

Yes, a compiler that allows the Relaxed Ref/Def model can be standard
conforming. (In this case, the model permits two tentative definitions for `age`
in two translation units to resolve to a single definition at link time.) See
subclause 6.7, page 81, lines 23-25. The code is conforming but not strictly
conforming. The behavior is undefined.
