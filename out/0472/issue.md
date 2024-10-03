### Summary

The introduction to complex arithmetic in 7.3.1p3 is wrong on several counts,
all due to CMPLX.

The text in question is:

> Each synopsis specifies a family of functions consisting of a principal function
> with one or more **double complex** parameters and a **double complex** or
> **double** return value; and other functions with the same name but with **f**
> and **l** suffixes which are corresponding functions with **float** and **long
> double** parameters and return values.

The items that are wrong are:

* CMPLX is a macro (not a function).
* CMPLX takes **double** parameters (not **double complex**).
* CMPLX has **F** and **L** suffixes (not **f** and **l**).

### Suggested Technical Corrigendum
