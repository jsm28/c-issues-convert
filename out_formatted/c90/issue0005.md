## Issue 0005: May a conforming implementation define and recognize a pragma which would change the semantics of the language?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Walter J. Murray, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-020  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_005.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_005.html)

According to subclause 6.8.6, a pragma directive “causes the implementation to
behave in an implementation-defined manner.” May a conforming implementation
define and recognize a pragma which would change the semantics of the language?
For example, might a conforming implementation recognize and honor the directive

```c
#pragma UNSIGNED_PRESERVING
```

as a way for a program to request non-standard integral promotions?

I also pose the corollary question. May a strictly conforming program contain a
pragma directive? According to subclause 4, a strictly conforming program “shall
use only those features of the language ... specified in this standard. It shall
not produce output dependent on any unspecified, undefined, or
implementation-defined behavior...”

If there is no constraint on how a conforming implementation may behave when
encountering a pragma directive, would it not follow that a strictly conforming
program may not contain a pragma directive?

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citations are subclause 6.8.6:

> A ... `pragma` ... causes the implementation to behave in an
> implementation-defined manner.

and clause 4:

> A strictly conforming program ... shall not produce output dependent on any ...
> implementation-defined behavior ...

In response to each question:

1. Yes, a conforming implementation may define and recognize a pragma which would change the semantics of the language.
2. Yes, for example, it might honor `UNSIGNED_PRESERVING`.
3. No, a strictly conforming program may not contain a pragma directive.
4. We agree with your conclusion, reasserting answer number 3\.
