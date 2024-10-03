ANSI/ISO C Defect Report #rfg23:

Subject: Implicit unary `&` applied to register arrays.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
void example ()
        {
        register int array[5] = 0;

 	array;     /* ? */
 	array[3];  /* ? */
 	array+3;   /* ? */
        }
```

Background:

Subclause 6.5.1 (footnotes):

> The implementation may treat any `register` declaration simply as an `auto`
> declaration. However whether or not addressable storage is actually used, the
> address of any part of an object declared with storage-class specifier
> `register` may not be computed, either explicitly (by use of the unary `&`
> operator as discussed in 6.3.3.2) or implicitly (by converting an array name to
> a pointer as discussed in 6.2.2.1). Thus the only operator that can be applied
> to an array declared with storage-class specifier `register` is `sizeof`.

This footnote, while offering guidance, doesn't really answer the question of
whether or not an implementation is required to issue a diagnostic for the case
where the address of a register array is implicitly taken (as discussed in
subclause 6.2.2.1). Nor does it definitively answer the question of whether such
code should be considered to be strictly conforming or not.

(Reference: CIB #1, [RFI #17, question #6](issue:0017.06).)
