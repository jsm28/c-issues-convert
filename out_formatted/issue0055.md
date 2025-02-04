## Issue 0055: Must the `SIG*` macros have distinct values?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Loren Schall, Project Editor (P.J. Plauger)  
Date: 1993-04-14  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_055.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_055.html)

It has been suggested that the six macros `SIGABRT`, `SIGFPE`, `SIGILL`,
`SIGINT`, `SIGSEGV`, and `SIGTERM` must have distinct values. Here is the
relevant portion of subclause 7.7:

> “The macros defined are
>
> ```c
> SIG_DFL
>               SIG_ERR
>               SIG_IGN
> ```
>
> which expand to constant expressions with distinct values that have type
> compatible with the second argument to and the return value of the `signal`
> function, and whose value compares unequal to the address of any declarable
> function; and the following, each of which expands to a positive integral
> constant expression that is the signal number corresponding to the specified
> condition:
>
> ...
>
> An implementation need not generate any of these signals, except as a result of
> explicit calls to the `raise` function.”

On the one hand, the reference to “the signal number corresponding to the
specified condition” might be assumed to imply different numbers for each
signal. On the other hand, the words “distinct values” were explicitly used for
the three `SIG_*` macros and are conspicuously missing for the others.

Also, I think it's worth noting that the standard expects `raise` to work
meaningfully (i.e. to be able to tell them apart).

Summary: must `SIGABRT`, `SIGFPE`, `SIGILL`, `SIGINT`, `SIGSEGV`, and `SIGTERM`
have distinct values?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.7, page 120, lines 14-16, change:***

and the following, each of which expands to a positive integral constant
expression that is the signal number corresponding to the specified condition:

***to:***

and the following, which expand to positive integral constant expressions with
distinct values that are the signal numbers, each corresponding to the specified
condition:
