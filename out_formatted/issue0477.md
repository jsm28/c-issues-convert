## Issue 0477: `nan` should take a string argument

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Martin Sebor  
Date: 2015-08-27  
Reference document: [N1957](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1957.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The Description for the `nan(const char *tagp)` function reads as follows:

> The call `nan("`*n-char-sequence*`")` is equivalent to
> `strtod("NAN(`*n-char-sequence*`)", (char**) NULL)`; the call `nan("")` is
> equivalent to `strtod("NAN()", (char**) NULL)`. If `tagp` does not point to an
> *n-char sequence* or an empty string, the call is equivalent to `strtod("NAN",
> (char**) NULL).`

An *n-char sequence* is a string of an implementation-defined form.

§7.1.4, Use of library functions, requires that arguments to library functions
must have valid values. Specifically, pointers must not be null or point outside
the address space of the program. In addition, arguments described as arrays
(including strings) must be such that all address computations and accesses to
objects that would be valid if the pointer argument did point to the first
element of such an array are in fact valid.

Since `tagp` argument is not required to point to a string or array, only the
first condition in §7.1.4 applies: it must not point outside the address space
of the program or be null.

Therefore, in the snippet below, since `tagp` is a valid pointer that does not
point to an *n-char-sequence* or the empty string, the `nan` call is valid and
required to be be equivalent to `strtod("NAN", (char**) NULL).`

```c
    char c = '1';   // not a n-char-sequence (no terminating NUL)
    char *tagp = &c;
    double x = nan (tagp);
```

But for an implementation that recognizes *n-char-sequences* of length greater
than 1 the requirement to determine whether `tagp` points to one is impossible
to implement since to do so `nan` would have to attempt to read past the end of
`c`.

It seems obvious that this is not intended and that the standard text is simply
missing a requirement that the `tagp` argument point to a string.

### Suggested Technical Corrigendum

The solution is to require the argument to the `nan` family of functions to be a
pointer to a string, analogously to all other library functions that operate on
strings.

Change §7.12.11.2 as follows:

> <ins>The `nan`, `nanf`, and `nanl` functions convert the string pointed to by
> `tagp` according to the following rules.</ins> The call
> `nan("`*n-char-sequence*`")` is equivalent to
> `strtod("NAN(`*n-char-sequence*`)", (char**) NULL)`; the call `nan("")` is
> equivalent to `strtod("NAN()", (char**) NULL)`. If `tagp` does not point to an
> *n-char sequence* or an empty string, the call is equivalent to `strtod("NAN",
> (char**) NULL).`

---

Comment from WG14 on 2017-11-03:

Oct 2015 meeting

### Committee Discussion

* The committee agrees with the author and accepts his Suggested Technical Corrigendum as the committee‘s Proposed Technical Corrigendum.
* This issue is likely a defect in the recently published ISO/IEC TS 18661 Floating Point extensions for C \- Part 1, and the author is solicited to submit a DR against FPE-1 to this committee.

### Proposed Technical Corrigendum

To §7.12.11.2 insert as first sentence:

> The `nan`, `nanf`, and `nanl` functions convert the string pointed to by `tagp`
> according to the following rules. The call `nan("`*n-char-sequence*`")` is
> equivalent ...
