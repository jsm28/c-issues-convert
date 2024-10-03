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
