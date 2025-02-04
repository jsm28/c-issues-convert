## Issue 0011.03: Are implicit initializers for tentative array definitions syntactically valid?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Rich Peterson, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-008  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_011.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_011.html)

Initialization of tentative definitions

If the file scope declaration

```c
int i[10];
```

appears in a translation unit, subclause 6.7.2 suggests that it is implicitly
initialized as if

```c
int i[10] = 0;
```

appears at the end of the translation unit. However, this initializer is
invalid, since subclause 6.5.7 prescribes that the initializer for any object of
array type must be brace-enclosed. We believe that the intention of subclause
6.7.2 is that this declaration has an implicit initializer of

```c
int i[10] = {0};
```

Is this true?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.7.2 **External object definitions** contains the following excerpt:

> If a translation unit contains one or more tentative definitions for an
> identifier, and the translation unit contains no external definition for that
> identifier, then the behavior is exactly as if the translation unit contains a
> file scope declaration of that identifier, with the composite type as of the end
> of the translation unit, with an initializer equal to 0\.

This statement describes an effect and not a literal token sequence. Therefore,
this example does not contain an error.
