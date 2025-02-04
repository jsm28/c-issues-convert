## Issue 0289: Function prototype with \[restrict]

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: The Open Group, Andrew Josey via Fred Tydeman  
Date: 2003-08-15  
Reference document: [Open Group aardvark 117](http://www.opengroup.org/austin/aardvark/finaltext/xshbug.txt)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_289.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_289.htm)

### Summary

6.7.6 (direct-abstract-declarator) is inconsistent with 6.7.5
(direct-declarator) with respect to omitting an identifier from a declaration to
form a type name.

Here is a specific example that shows the problem.

```c
 int lio_listio(int, struct aiocb *restrict const[restrict]);
```

is invalid and appears to have to be done as:

```c
 int lio_listio(int, struct aiocb *restrict const __FOO[restrict]);
```

6.7.6 Type names, paragraph 2 has:

> In several contexts, it is necessary to specify a type. This is accomplished
> using a type name, which is syntactically a declaration for a function or an
> object of that type that omits the identifier.

So you would think that if

```c
  struct aiocb *restrict const __FOO[restrict]
```

is a valid declaration of the object `__FOO`, then it should follow from the
above statement that

```c
  struct aiocb *restrict const [restrict]
```

must be a valid type name.

---

Comment from WG14 on 2004-03-03:

### Technical Corrigendum

In the syntax rules for *direct-abstract-declarator* in 6.7.6 paragraph 1,
replace

> *direct-abstract-declarator<sub>opt</sub>* `[`
> *assignment-expression<sub>opt</sub>* `]`

with

> *direct-abstract-declarator<sub>opt</sub>* `[`
> *type-qualifier-list<sub>opt</sub> assignment-expression<sub>opt</sub>* `]`
>
> *direct-abstract-declarator<sub>opt</sub>* `[ static`
> *type-qualifier-list<sub>opt</sub> assignment-expression* `]`
>
> *direct-abstract-declarator<sub>opt</sub>* `[` *type-qualifier-list* `static`
> *assignment-expression* `]`
