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
