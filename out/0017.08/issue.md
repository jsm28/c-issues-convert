Compatibility of pointer to `void` with storage class

Refer to subclause 6.3.9, page 49, lines 24-25. Do these lines make the
following legal?

```c
register void *p;
 char *q;
 if (p==q)  /* legal */
 ...
```

The wording on line 25, “... version of `void`; or” does not talk about the
“`void` type.” This sentence could be taken as simply referring to the
occurrence of a qualified or unqualified occurrence of `void`.

Should the wording on line 25 be changed to “... version of the type `void`; or”
and thus cause the storage class to be ignored, or does the above example fall
outside the scope of the constraint?
