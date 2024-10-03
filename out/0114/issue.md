ANSI/ISO C Defect Report #rfg21:

Subject: Initialization of multi-dimensional `char` array objects.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
char array2[2][5] = { "defghi" };	/* ? */
```

Background:

Subclause 6.5.7 (**Constraints**):

> There shall be no more initializers in an initializer list than there are
> objects to be initialized.

Subclause 6.5.7:

> An array of character type may be initialized by a character string literal,
> optionally enclosed in braces.

Subclause 6.5.7 (examples):

> ... It defines a three-dimensional array object; ...

It appears that many existing compilers seem to feel the the code example shown
above violates the “no more initializers” constraint (quoted above) which is
given in subclause 6.5.7.

Note however that the *entire* two-dimensional array object being initialized
consists of exactly 2\*5 \= 10 individual `char` objects, whereas the
initializer itself only consists of 7 individual `char` values (if one counts
the terminating null byte). Thus, it would appear that these existing
implementations are in fact *wrong* in rejecting the above code, and that such
usage is in fact strictly conforming.

I ask the Committee to unambiguously either confirm or refute that position.
