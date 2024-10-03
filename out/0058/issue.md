What is the minimum value for the maximum number of digits in a number that can
be processed by the `scanf` family and the `strtod` family?

1. 509
2. 32767
3. something else

Parts of the the C Standard that may help answer the question follow. Subclause
7.9.6.1**The `fprintf` function**, page 134, lines 16-18:

> **Environmental limit**. The minimum value for the maximum number of characters
> produced by any single conversion shall be 509\.

But, note, there is no such environmental limit for `fscanf`.

Subclause 5.2.4.1 **Translation limits**, page 13, line 17:

> \- 509 characters in a logical source line

But, note, there is no execution limit. Subclause 5.2.4.1 **Translation
Limits**, page 13, line 19:

> \- 32767 bytes in an object (in a hosted environment only)

Consider the number 1.0 written as `.00000...00001e32759` that is 32767
characters long (including terminator). There is only one significant digit, the
`1`. It can be stored in an array of 32767 characters, so it should be possible
to pass this string to `atof`, `strtod`, or `sscanf` and get the value 1.0.
Correct?
