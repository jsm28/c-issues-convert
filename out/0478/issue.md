### Summary

The text of the standard isn't entirely clear as to whether or not the function
`main` can be used by strictly conforming C programs in hosted environments. The
following passages quote the permissions and requirements that at the same time
suggest that `main` may not be used by such programs, and that there may be more
than the one call to the function made by the implementation at program startup.

§5.1.2.2.2 Program execution says:

> In a hosted environment, a program may use all the functions, macros, type
> definitions, and objects described in the library clause (clause 7).

suggesting that, since `main` is not described in the library clause but rather
in §5.1.2.2.1, it may not be used by a program.

However, §5.1.2.2.3 Program termination, immediately following the section
quoted above, then goes on to state (emphasis added):

> If the return type of the `main` function is a type compatible with `int`, a
> return from the **initial call** to the `main` function is equivalent to calling
> the `exit` function with the value returned by the `main` function as its
> argument; ...

In addition, §7.21.3 Files contains the following sentence (emphasis also
added):

> If the `main` function returns to **its original caller**, all open files are
> closed...

Finally, since the C\+\+ standard explicitly prohibits programs from calling or
otherwise using `main`, one might expect C to do the same. However the
references to `main`'s initial call and its original caller in the latter two
paragraphs suggest otherwise.

The question was raised and discussed on the committee's mailing list starting
with message [(SC22WG14.13780) valid uses of
main](https://www.open-std.org/jtc1/sc22/wg14/13780). In response, members of
the committee who participated in the preparation of the version of the C
standard that introduced the words clarified that the intent was and remains for
C to allow programs to use `main`. In particular, the intent of §5.1.2.2.2
Program execution is to grant permission to programs to use the facilities of
the standard library but not to preclude the uses of `main` or other symbols
defined by them.

However, since the function `main` is special and unlike any other symbol
defined by a program, and since C\+\+ contains a rule to the contrary, we feel
that the intent isn't sufficiently clearly and unambiguously reflected in the
quoted passages or the rest of the standard, and that a clarification is called
for.

### Suggested Technical Corrigendum

In light of the intent of the passages quoted above as made clear by the mailing
list discussion, we offer two proposals to clarify the text of the standard.

#### Proposal 1

Change §5.1.2.2.2 Program execution as follows:

> In a hosted environment, a program may use <u>the function `main` as well as</u>
> all the functions, macros, type definitions, and objects described in the
> library clause (clause 7).

#### Proposal 2

Add a footnote to the end of §5.1.2.2.2 Program execution, with the following
text:

> <u>A program may also use the function `main`.</u>
