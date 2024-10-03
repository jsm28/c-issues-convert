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
