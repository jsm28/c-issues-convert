## Issue 0017.13: How does `register` affect compatibility of function parameters?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Compatibility of functions with `register` on parameters

Reference subclause 6.5.4.3, page 67\.

```c
f1(int);
 f1(register int a) /* Is this function compatible with the above?  */
 {
 }
```

Subclause 6.5.4.3, page 68, lines 5-7 were presumably intended to make sure that
the `register` storage class got kept in the case of a definition so that the
appropriate constraints applied, i.e., it is not allowed to take its address,
etc. But the further implication of the wording is that the occurrence of
`register` lingers on for other uses \- but there are no other uses.

Suggest a clarification on this point.

---

Comment from WG14 on 1997-09-23:

### Response

The function is compatible. Storage class is not part of the type.

The relevant citation, as given, is subclause 6.5.4.3, page 68, lines 5-7, but
it does not imply any “other uses.”
