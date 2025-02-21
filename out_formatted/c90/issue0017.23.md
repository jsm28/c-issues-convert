## Issue 0017.23: How long does `blue paint` persist on macro names?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

How long does blue paint persist?

Consider the following code:

```c
#define a(x) b
 #define b(x) x
 a(a)(a)(a)
```

The macro replacement for `a(a)` results in `b`.

First replacement buffer: `b`

Remaining tokens: `(a)(a)`

Inside the first replacement buffer, no further nested replacements will
recognize the macro name “`a`.” The name “`a`” is painted blue.

The first replacement buffer is rescanned not by itself, but along with the rest
of the source program's tokens. “`b(a)`” also causes macro replacement and
becomes “`a`.”

Second replacement buffer: `a`

Remaining tokens: `(a)`

The second replacement buffer is rescanned not by itself, but along with the
rest of the source program's tokens.

The “`a`” in the second replacement buffer did not come from the first
replacement buffer. It came from three of the remaining tokens which were in the
source file following the first replacement buffer. Is this “`a`” part of a
nested replacement? Is it still painted blue?

Note that there are many “paths” that can be taken for a possible macro name to
travel from a preprocessing token (outside the replacement buffer) to one that
is inside the replacement buffer. When do they stop getting painted blue? If
either too early or too late, they cause very surprising results.

Given the amount of discussion involving macro expansion that uses the concept
of “blue paint,” why doesn't the standard tell the reader about this idea?

Everybody seems to agree that the above is undefined. Does anybody have a set of
words to make this and other cases explicitly undefined?

---

Comment from WG14 on 1997-09-23:

### Response

The reference is to subclause 6.8.3.4, page 91\.

```c
#define a(x) b
 #define b(x) x
 a(a)(a)(a)      /*  may expand as follows: */
 b(a)(a)
 a'(a)   or       a(a)
 a(a)            or       b
 /* a' indicates the symbol a marked for non-replacement */
```

The Committee addressed this issue explicitly in previous deliberations and
decided to say nothing about the situation, understanding that behavior in such
cases would be undefined.

The result, as with other examples, is intentionally left undefined.
