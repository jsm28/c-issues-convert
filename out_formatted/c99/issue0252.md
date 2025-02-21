## Issue 0252: incomplete argument types when calling non-prototyped functions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_252.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_252.htm)

### Problem

Consider the code:

```c
   void jim ();
    void sheila (void);
    // ...   sheila (jim ());   /* Line A */
    jim (sheila ());   /* Line B */
```

Line A violates the constraint of 6.5.2.2#2, that requires the argument to have
a type that can be assigned to the parameter type. But line B doesn't because
that constraint only applies to prototyped functions. 6.5.2.2#4 reads in part:

> \[#4\] An argument may be an expression of any object type.

but this is not a constraint. Should it not be ? After all, the compiler has to
know the type of the argument in order to compile the function call, so it can
check at that point that the argument has a complete object type.

### Suggested Technical Corrigendum

Add a new paragraph #1a following 6.5.2.2#1:

> \[#1a\] Each argument shall have a type which is a completed object type.

---

Comment from WG14 on 2002-03-06:

### Committee Response

> This should not be a constraint.
