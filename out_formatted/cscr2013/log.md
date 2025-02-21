# C Secure Coding Rules TS 17961:2013: issue log

**This issue log has been automatically converted from the original issue lists and some formatting may not have been preserved.**

|Issue|Summary|Status|
|-|-|-|
|[0SCR.01](../cscr2013/log.md#issue0SCR.01)|error in 5.21 example|Fixed in C Secure Coding Rules TS 17961:2013 TC1|
|[0SCR.02](../cscr2013/log.md#issue0SCR.02)|Missing formatted input/output functions in Rule 5.40|Fixed in C Secure Coding Rules TS 17961:202y|

---

<div id="issue0SCR.01">

## Issue 0SCR.01: error in 5.21 example

Authors: WG14, Clive Pygott  
Date: 2014-03-11  
Reference document: [N1801](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1801.htm)  
Status: Fixed  
Fixed in: C Secure Coding Rules TS 17961:2013 TC1  
Converted from: [n2150.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2150.htm)

### Summary

The (cut-down) requirement for rule 5.21 is:

*A call to a standard memory allocation function is presumed to be intended for
type T \* when it appears in any of the following contexts*

* *in the right operand of an assignment to an object of type T \*, or*
* *...*

*A call to a standard memory allocation function taking a size integer argument
n and presumed to be intended for type T \* shall be diagnosed when n \<
sizeof(T).*   

{malloc is identified as a standard memory allocation function}

The example for 5.21 is:

```c
wchar_t *f1(void) {
    const wchar_t *p = L"Hello, World!";
    const size_t n = sizeof(p) * (wcslen(p) + 1);
    wchar_t *q = (wchar_t *)malloc(n); // diagnostic required
    /* ... */
    return q;
}
```

Why is a diagnostic required on the malloc statement? On my machine

* T is wchar\_t
* sizeof(p) \=\= 4
* wcslen(p) \=\= 13
* n \=\= 56
* sizeof(wchar\_t) \=\= 2

56 is not less than 2, so no diagnostic is required.

Indeed, the only values of n that would require a diagnostic are 0 and 1\.

I think the original intent was to make q smaller than 28 (the space required
for 14 wide characters), then copy p to q (buffer overrun), but this rule
doesn’t actually address that and the copy isn’t included in the example. That
is, I think the original example was to be of the form:

```c
wchar_t *f2(void) {
    const wchar_t *p = L"Hello, World!";
    const size_t n =  /*sizeof(p) * */ (wcslen(p) + 1); /* NB  n == 14  */
    wchar_t *q = (wchar_t *)malloc(n);
    wcscpy(q, p);
    return q;
   }
```

This does have an issue \- buffer overrun, but still doesn’t violate 5.21 as
currently stated (14 is still \>\= 2). I think the reason 5.21 got changed was
either:

* buffer overrun is addressed elsewhere \- though I cannot see where that is:
  + Annex C maps CWEs with Buffer Overrun to 5.22 – but that only talks about constructing an invalid pointer by pointer arithmetic or indexing – neither of which apply here
  + wcscpy may be regarded as a restricted sink, with a requirement that the size of the first parameter array \>\= the size of the second, so 5.46 could apply – except that 5.46 only applies to tainted data. The data in this example isn’t tainted
* It was recognised that it’s too difficult to carry the information around that lets you check what use is made of a buffer at an arbitrary point later in the program. The problem in the f2 example is on the line after the allocation, but in general it could be anywhere in the program

### Suggested Technical Corrigendum

Either 5.21 needs a different example, such as :

```c
struct S1 { int x, y, z;};   /*  sizeof(S1)  is 12  */

struct S1 *copyS1(const struct S1 s) {
    struct S1 *q = (struct S1 *)malloc(8); /*  Diagnostic required */
    *q = s;
    return q;
   }
```

or the rule needs to be changed to reflect that the allocated memory is in
effect an array of size n/sizeof(T), and that it shouldn’t be indexed beyond
that size (including by copy functions such as wcscpy etc. \- this caveat may
also need to be added to 5.22)

I'd favour changing the example

---

Comment from WG14 on 2016-10-21:

Apr 2014 meeting

### Committee Discussion

> The words in 5.21 were revised but the example wasn't. A revised example was
> approved as a Proposed Technical Corregendum. A new paper was solicited to
> capture the issue raised by the changed example.

Oct 1014 meeting

### Committee Discussion

> A new paper [N1860](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1860.htm)
> proposing a new rule was submitted and discussed, and it was determined that
> since the original example illustrated an issue, that we could consider this a
> defect after all.
>
> The following Proposed Technical Corrigendum corrects the existing example to
> match the 5.21 rule, and adds a new clause and example to capture the intent of
> the original 5.21 example.
>
> The existing example has an explanation, and the words approved do not, and the
> following have been suggested.
>
> > EXAMPLE 1 In this noncompliant example, a diagnostic is required because `n` is
> > `sizeof(p)`, which is smaller than `sizeof(struct S1)`, so N is 0
> >
> > EXAMPLE 2 In this noncompliant example, a diagnostic is required because `n` is
> > 14 and `sizeof(wchar_t)` is 2, making N equal 7\. `q` is therefore treated as an
> > array of 7 elements, but `wcscpy` attempts to copy `p`, an array with 14
> > elements, into it.

### Proposed Technical Corrigendum

In rule 5.21, Rule section, replace

> A call to a standard memory allocation function taking a size integer argument
> `n` and presumed to be intended for type `T *` shall be diagnosed when `n <
> sizeof(T)`.

with

> A call to a standard memory allocation function taking a size integer argument
> `n` and presumed to be intended for type `T *` shall be regarded as an array of
> `N` elements, where `N = n / sizeof(T)`.
>
> Any allocation where `N == 0` shall be diagnosed (i.e. where `n < sizeof(T)`).
> Also, any attempt to use this array in a manner that causes its array bound to
> be violated shall be diagnosed.

In rule 5.21, replace

> EXAMPLE In this noncompliant example, a diagnostic is required because the value
> of `n` that is used in the `malloc()` call has been possibly miscalculated.
>
> ```c
> wchar_t *f1(void) {
>   const wchar_t *p = L"Hello, World!";
>   const size_t n = sizeof(p) * (wcslen(p) + 1);
>   wchar_t *q = (wchar_t *)malloc(n);  // diagnostic required
>
>   /* ... */
>   return q;
> }
> ```

with

> ```c
> EXAMPLE 1
>
>     struct S1 {
>         unsigned int x;
>         float        y;
>         struct S1   *z;
>     };
>
>
>     struct S1 *f1(void) {
>         struct S1 *p = (struct S1*)malloc(sizeof(p));  // diagnostic required
>         return p;
>     }
>
>
>
>
>
> EXAMPLE 2
>
>     wchar_t *f2(void) {
>         const wchar_t *p = L"Hello, World!";
>         const size_t n = (wcslen(p) + 1);
>         wchar_t *q = (wchar_t *)malloc(n);
>         wcscpy(q, p); // diagnostic required
>         return q;
>     }
> ```


</div>


---

---

<div id="issue0SCR.02">

## Issue 0SCR.02: Missing formatted input/output functions in Rule 5.40

Authors: WG14, Clive Pygott  
Date: 2016-03-01  
Reference document: [N2006](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2006.htm)  
Status: Fixed  
Fixed in: C Secure Coding Rules TS 17961:202y  
Converted from: [n2150.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2150.htm)

### Summary

This suggestion comes from MISRA, as they are adding support for 17961 to their
rules.

Rule 5.40 names a number of functions that can attempt to write beyond the
bounds of the target array, if supplied with tainted input, namely: fscanf,
scanf, vfscanf, vscanf, sscanf, vsscanf and sprintf.

The observation is that vsprintf should be included in this list. Also the \_s
versions of all the above (including vsprintf\_s) should be included, as they
also can write beyond the end of the target array.

It is suggested that this is a defect rather than an enhancement, as from the
rationale for the rule, they should have been included when drafted.

---

Comment from WG14 on 2017-04-07:

Apr 2016 meeting

### Committee Discussion

> The committee agrees with the author.

### Proposed Technical Corrigendum

To 5.40 Rule section first sentence change:

> Calls to the `fscanf`, `scanf`, `vfscanf`, and `vsscanf` functions that pass...

to

> Calls to the `fscanf`, `scanf`, `vfscanf`, and `vsscanf` functions, and their
> Annex K counterparts `fscanf_s`, `scanf_s`, `vfscanf_s`, and `vsscanf_s`, that
> pass...

To 5.40 Rule section second sentence change:

> Calls to the `sscanf` and `vsscanf` functions

to

> Calls to the `sscanf`, `vsscanf`, `sscanf_s`, and `vsscanf_s` functions

To 5.40 Rule section third sentence change:

> Calls to the `sprintf` function that

to

> Calls to the `sprintf`, `vsprintf`, `sprintf_s`, and `vsprintf_s` functions that


</div>


---

