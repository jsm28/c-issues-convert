## Issue 0277: declarations within iteration statements

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_277.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_277.htm)

### Problem

Consider the code:

```c
  for (enum fred { jim, sheila = 10 } i = jim; i < sheila; i++)
        // loop body
```

6.8.5#3 reads:

> \[#3\] The declaration part of a `for` statement shall only declare identifiers
> for objects having storage class `auto` or `register`.

Does this wording forbid the declaration of tag `fred` \- since it is not an
object \- or is `fred` not covered by that wording because it is not an object ?

### Suggested Technical Corrigendum

Change 6.8.5#3 to one of:

> \[#3\] The declaration part of a `for` statement shall only declare identifiers
> for objects; any object so declared shall have storage class `auto` or
> `register`.

or:

> \[#3\] Any object whose identifier is declarared in the declaration part of a
> `for` statement shall have storage class `auto` or `register`.

---

Comment from WG14 on 2002-03-07:

### Committee Response

The intent is clear enough; `fred`, `jim`, and `sheila` are all identifiers
which do not denote objects with `auto` or `register` storage classes, and are
not allowed in this context.
