## Issue 0013.02: Is compatible properly defined for recursive types?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

“Compatible” not defined for recursive types

The term “compatible” is not completely defined. Consider the following two
file-scope declarations in *separate* translation units:

```c
extern struct a { struct a *p; } x;
 struct a { struct a *p; } x;
```

Are these two declarations of `x` compatible? Obviously they should be, but
subclause 6.1.2.6 does not say so.

Because subclause 6.1.2.6 does not say how to terminate the recursion in testing
for compatibility of two recursive types, either interpretation is possible. In
other words, it is consistent with the rules in subclause 6.1.2.6 to decide that
the two declarations are compatible; but it is also consistent to decide that
they are incompatible.

We can solve the problem roughly as follows: append the following draft sentence
to the first paragraph of subclause 6.1.2.6 (page 25, line 8):

> If two types declared in separate translation units admit the possibility of
> being either compatible or incompatible, the two types shall be
> compatible.**\*** \[Footnote \*: This case occurs with recursive types.]

This sentence is not satisfactory; perhaps another Committee member can state
this rule better.

---

Comment from WG14 on 1997-09-23:

### Response

We agree that the C Standard can be read in a way that it “loops.” Our intent,
and we feel the only reasonable solution, is that the recursion stops and the
two types are regarded as compatible.
