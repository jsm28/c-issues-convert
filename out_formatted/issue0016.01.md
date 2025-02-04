## Issue 0016.01: Can a tentative definition have an incomplete type initially?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-052  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_016.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_016.html)

I can find no prohibition of the following translation unit:

```c
struct foo x;
 struct foo { int i; };
```

What I was looking for, but didn't find, was a statement that an implicitly
initialized declaration of an object with static storage duration must have
object type. Is this translation unit legal?

---

Comment from WG14 on 1997-09-23:

### Response

The translation unit cited is valid. It falls into the same category of
construct as

```c
int array[];
 int array[17];
```

Objects may be declared without knowing their size. However, the standard is
clear in what cases such an object may or may not be used, prior to the actual
definition of the object.
