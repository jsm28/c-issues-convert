## Issue 0282: flexible array members \& struct padding

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: J11, Douglas Walls (US)  
Date: 2002-06-11  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_282.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_282.htm)

### Summary

6.7.2.1 Structure and union specifiers, paragraphs 15 and 16 require that any
padding for  
alignment of a structure containing a flexible array member must preceed the
flexible  
array member.  This contradicts existing implementations.  We do not believe
this was the intent of the C99 specification.

### Details

If a struct contains a flexible array member and also requires padding for
alignment, then the current C99 specification requires the implementation to put
this padding **before** the flexible array member.  However, existing
implementations, including at least GNU C, Compaq C, and Sun C, put the padding
**after** the flexible array member.

The layout used by existing implementations can be more efficient. Furthermore,
requiring these existing implementations to change their layout would break
binary backwards compatibility with previous versions.

### Suggested Technical Corrigendum

Change the wording such that it is implementation defined as to whether the
padding is before or after the flexible array member.

---

Comment from WG14 on 2004-03-06:

### Technical Corrigendum

In 6.7.2.1 paragraph 16, replace the second and third sentences ("With two ...
106)" with the following text:.

> In most situations, the flexible array member is ignored. In particular, the
> size of the structure is as if the flexible array member were omitted except
> that it may have more trailing padding than the omission would imply.
>
> replace "Second" with "However" at the start of the following sentence, and
> delete footnote 106\.
>
> Replace the examples (paragraphs 17 to 20\) with:
>
> \[#17\] EXAMPLE After the declaration:
>
> ```c
>             struct s { int n; double d[]; };
> ```
>
> the structure `struct s` has a flexible array member `d`. A typical way to use
> this is:
>
> ```c
>            int m = /* some value */;
>             struct s *p = malloc (sizeof (struct s) + sizeof (double [m]));
> ```
>
> and assuming that the call to `malloc` succeeds, the object pointed to by `p`
> behaves, for most purposes, as if `p` had been declared as:
>
> ```c
>             struct { int n; double d[m]; } *s1;
> ```
>
> (there are circumstances in which this equivalence is broken; in particular, the
> offsets of member `d` might not be the same).
>
> \[#18\] Following the above declaration:
>
> ```c
>             struct s t1 = { 0 };           // valid
>             struct s t2 = { 1, { 4.2 }};   // invalid
>             t1.n = 4;                      // valid
>             t1.d[0] = 4.2;                 // might be undefined behavior
> ```
>
> The initialization of `t2` is invalid (and violates a constraint) because
> `struct s` is treated as if it does not contain member `d`. The assigment to
> `t1.d[0]` is probably undefined behaviour, but it is possible that
>
> ```c
>             sizeof (struct s) >= offsetof (struct s, d) + sizeof (double)
> ```
>
> in which case the assignment would be legitimate. Nevertheless it cannot appear
> in strictly conforming code.
>
> \[#19\] After the further declaration:
>
> ```c
>             struct ss { int n; };
> ```
>
> the expressions:
>
> ```c
>             sizeof (struct s) >= sizeof (struct ss)
>             sizeof (struct s) >= offsetof (struct s, d)
> ```
>
> are always equal to 1\.
>
> \[#20\] If `sizeof (double)` is 8, then after the following code is executed:
>
> ```c
>             struct s *s1;
>             struct s *s2;
>             s1 = malloc(sizeof (struct s) + 64);
>             s2 = malloc(sizeof (struct s) + 46);
> ```
>
> and assuming that the calls to malloc succeed, the objects pointed to by `s1`
> and `s2` behave, for most purposes, as if the identifiers had been declared as:
>
> ```c
>             struct { int n; double d[8]; } *s1;
>             struct { int n; double d[5]; } *s2;
> ```
>
> \[#21\] Following the further successful assignments:
>
> ```c
>             s1 = malloc(sizeof (struct s) + 10);
>             s2 = malloc(sizeof (struct s) +  6);
> ```
>
> they then behave as if the declarations were:
>
> ```c
>             struct { int n; double d[1]; } *s1, *s2;
> ```
>
> and:
>
> ```c
>             double *dp;
>             dp = &(s1->d[0]);       // valid
>             *dp = 42;               // valid
>             dp = &(s2->d[0]);       // valid
>             *dp = 42;               // undefined behavior
> ```
>
> \[#22\] The assignment:
>
> ```c
>             *s1 = *s2;
> ```
>
> only copies the member `n`; if any of the array elements are within the first
> `sizeof (struct s)` bytes of the structure, these might be copied or simply
> overwritten with indeterminate values.
