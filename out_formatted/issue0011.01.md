## Issue 0011.01: When do the types of multiple external declarations get formed into a composite type?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Rich Peterson, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-008  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0034.01](issue0034.01.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_011.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_011.html)

Merging of declarations for linked identifier

When more than one declaration is present in a program for an externally-linked
identifier, exactly when do the declared types get formed into a composite type?

Certainly, if two declarations have file scope, then after the second, the
effective type for semantic analysis is the composite type of the two
declarations (subclause 6.1.2.6, page 25, lines 19-20). However, if one
declaration is in an inner scope and one is in an outer scope, are their types
formed into a composite type?

In particular, consider the code:

```c
{
 extern int i[];
 {
     /* a different declaration of the same object */
     extern int i[10];
 }
 /* Is the following legal?
    That is, does the outer declaration
    inherit any information from the inner one?  */
 sizeof (i);
 }
```

Similar situations can be constructed with internally linked identifiers. For
instance:

```c
/* File scope */
 static int i[];

 main()
 {
 /* a different declaration of the same object */
 extern int i[10];
 }

 /* Is the following legal?
    That is, does the outer declaration
    inherit any information from the inner one?*/
 int j = sizeof (i);
```

Further variants of this question can be asked:

```c
{
 extern int i[10];
 {
     /* a different declaration of the same object */
     extern int i[];

     /* Is the following legal?
        That is, does the inner declaration
        inherit any information from the outer one? */
      sizeof (i);
 }
 }
```

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.1.2.6, page 25, lines 19-20, change:***

For an identifier with external or internal linkage declared in the same scope
as another declaration for that identifier, the type of the identifier becomes
the composite type.

***to:***

For an identifier with internal or external linkage declared in a scope in which
a prior declaration of that identifier is visible**\***, if the prior
declaration specifies internal or external linkage, the type of the identifier
at the latter declaration becomes the composite type.

\[Footnote \*: As specified in 6.1.2.1, the latter declaration might hide the
prior declaration.\]
