Subclause 6.1.8: Preprocessing numbers I note from the rationale document of
November 1988, X3J11 Document Number 88-151, that the following problem has been
observed. I am surprised at the Committee's decision to allow such a loose
description. Under the grammar given for a `pp-number`

```c
0xEE+23     0x7E+macro      0x100E+value-macro
```

are preprocessing numbers and as such a conforming C compiler would be required
to generate an error when it failed to successfully convert them to actual C
language number tokens. The solution is simply to restrict the inclusion of
\[`eE`]\[`+-`] within a *`pp-number`* to situations where the `e` or `E` is the
first *`non-digit`* in the character sequence composing the preprocessing
number. This can be easily implemented in a variety of methods; the informal
description above gives perhaps a better guide to efficient implementation than
the following revised grammar:

```c
pp-number:
         pp-float
         pp-number digit
          pp-number .
         pp-number non-digit  /* A non-digit is a letter or underscore */

 pp-float:
         pp-real
         pp-real E sign         pp-real e sign

 pp-real:
         digit
         .
         pp-real digit
         pp-real .
```

It is unbelievable that a standards committee could so lose sight of its
objective that it would, in full awareness, make simple expressions illegal.

To illustrate the absurdity of the rationale document's claim that the faulty
grammar was felt to be easier to implement, why not adopt the following grammar
for a *`pp-number`* and really make life simple; after all, who wants to have
their preprocessor slowed down by checking whether the `+` or `-` was preceded
by a n `e`or an `E`?

```c
pp-number:
         digit
         .
         pp-number digit
         pp-number .
         pp-number non-digit
         pp-number sign
```
