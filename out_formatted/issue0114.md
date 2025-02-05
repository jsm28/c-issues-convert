## Issue 0114: Initialization of multi-dimensional `char` array object questions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_114.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_114.html)

ANSI/ISO C Defect Report #rfg21:

Subject: Initialization of multi-dimensional `char` array objects.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
char array2[2][5] = { "defghi" };       /* ? */
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

---

Comment from WG14 on 1997-09-23:

### Response

a) Yes, a diagnostic is required.

b) Yes, this renders the program not strictly conforming.

Note that initialization of an array of character type by a string literal is a
special case, described in subclause 6.5.7.

The phrases “two-dimensional array” and “three-dimensional array” are merely
used for convenience. The **Semantics** section on array declarators (subclause
6.5.4.2) and the syntax specification in the section on declarations (subclause
6.5.4) clearly show that array types must be declared with one index. Thus, an
array which has two indices must be considered an “array of array of type.”

Since this is the case, the **Semantics** description for initializing
aggregates and subaggregates in subclause 6.5.7 applies. This description states

> If the initializer of a subaggregate or the first member of the contained union
> begins with a left brace, the initializers enclosed by that brace and its
> matching right brace initialize the members of the subaggregate or the first
> member of the contained union.

Thus, in the example, the string must be applied only to the first element of
the two-element array (which is an array of 5 characters). Since the initializer
contains 6 characters, it violates the constraint of the same section which
states:

> There shall be no more initializers in an initializer list than there are
> objects to be initialized.
