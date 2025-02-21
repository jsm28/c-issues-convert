## Issue 0451: Instability of uninitialized automatic variables

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Freek Wiedijk and Robbert Krebbers (Radboud University Nijmegen, The Netherlands)  
Date: 2013-08-30  
Reference document: [N1747](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1747.htm)  
Submitted against: C11 / C17  
Status: Closed  
Cross-references: [0260](../c99/issue0260.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The standard is unclear about the following questions:

1. Can an uninitialized variable with automatic storage duration (of a type that does not have trap values, whose address has been taken so 6.3.2.1p2 does not apply, and which is not volatile) change its value without direct action of the program?
2. If the answer to question 1 is "yes", then how far can this kind of "instability" propagate?
3. If "unstable" values can propagate through function arguments into a called function, can calling a C standard library function exhibit undefined behavior because of this?

Specifically, consider:

```c
unsigned char x[1]; /* intentionally uninitialized */
printf("%d\n", x[0]);
printf("%d\n", x[0]);
```

Does the standard allow an implementation to let this code print two different
values? And if so, if we insert either of the following three statements

```c
x[0] = x[0];
x[0] += 0;
x[0] *= 0;
```

between the declaration and the `printf` statements, is this behavior still
allowed? Or alternatively, can these `printf` statements exhibit undefined
behavior instead of having to print a reasonable number.

#### Motivation and discussion

The standard is unclear about these questions.

On the one hand the committee response to [Defect Report #260](../c99/issue0260.md)
strongly suggests that the committee decided that the standard implies the
answer to question 1 to be "yes". (Although Defect Report #260 applies to the
C99 standard and hence has been superseded by the C11 standard, no modification
to the standard text was deemed necessary at the time, and all relevant text in
the C11 standard is identical to that in the C99 standard.) The relevant quote
from the committee response to Defect Report #260 is:

> In the case of an indeterminate value \[...\] the actual bit-pattern may change
> without direct action of the program.

A subtlety is that Defect Report #260 talks about bit-patterns and not about
values, but for variables of type `unsigned char` there is a one-to-one
correspondence between bit-patterns and values.

Another argument in favor of "instability" of indeterminate values is that
values can "become indeterminate" (e.g. 5.1.2.3p5, 6.2.4p2, and 6.2.4p6). In
these cases the value of an object may also change without an explicit store
(and can keep changing?)

On the other hand, 6.7.9p10 states that the kind of uninitialized variables that
we are discussing get an indeterminate value. From 3.19.2 it follows that if a
type has no trap values, then indeterminate and unspecified values are the same.
And in 3.19.3, it is stated explicitly that an unspecified value is *chosen*.
Which implies that the value \- after having been chosen \- cannot change
anymore.

Another argument against "instability" is that 6.8p3 states that "the values are
stored in the objects (including *storing* an indeterminate value in objects
without an initializer) each time the declaration is reached in the order of
execution", and that 6.2.4p2 states that "An object \[...\] retains its
last-*stored* value throughout its lifetime." The only way that one could read
this in light of Defect Report #260 is if "retaining an indeterminate value" is
read as meaning that the indeterminateness of the value is retained, without the
value having a *specific* value.

It seems attractive to make a distinction between *indeterminate* values that
are allowed to change without direct action of the program in the way that
Defect Report #260 interpreted the standard, and *unspecified* values that do
not have this property. However the current text of 3.19.2 does not allow for
this interpretation. Also, probably some instances of "indeterminate" and
"unspecified" would need to be changed for such an interpretation to make sense.
(For example in 6.2.6.1p6 "the bytes of the object representation that
correspond to any padding bytes take unspecified values." should probably become
"... take indeterminate values.")

The reason for question 3 is that *if* the kind of "instability" that questions
1 and 2 ask for is allowed to propagate maximally, then it becomes impossible to
implement `printf` in C itself. When converting an indeterminate value to a
string of output characters, the value can *keep* changing underneath, and the
code cannot protect itself against this.

On the other hand, if library functions exhibit undefined behavior on these
kinds of "unstable" uninitialized values, then an `fwrite` of a struct with
uninitialized padding bytes would also give undefined behavior. The fact that
one wants to be able to copy uninitialized padding bytes in structs using
`memcpy` without undefined behavior is the reason that using the value of an
uninitialized object is not undefined behavior. This seems to suggest that an
`fwrite` of a struct with uninitialized padding bytes should *not* exhibit
undefined behavior.

### Possible Resolutions

We see three reasonable sets of answers to these questions:

#### Resolution (a)

1. no
2. not applicable
3. not applicable

##### Advantage

Easy to repair the unclarity in the standard. Just add text that explicitly
states that indeterminate values cannot change without direct action from the
program. This will prevent people from invoking the response to Defect Report
#260 from then on.

##### Disadvantage

Restricts the kind of optimizations compilers are allowed to perform.

#### Resolution (b)

1. yes
2. any operation performed on indeterminate values will have an indeterminate value as its result
3. no

Specifically, "unstable" values will also propagate through function calls.
Also, after

```c
x[0] *= 0;
```

the value of `x[0]` *still* will be "unstable" and hence still can be any byte,
and will not necessary be `0`.

##### Advantage

Gives compilers more freedom to perform optimizations.

Is Defect Report #260-compliant (i.e., "the committee did not change its mind").

##### Disadvantage

Needs more modifications to the text of the standard. It will then be necessary
to make an explicit distinction between "indeterminate non-trap value" and
"unspecified value".

#### Resolution (c)

1. yes
2. any operation performed on indeterminate values will have an indeterminate value as its result
3. yes, library functions will exhibit undefined behavior when used on indeterminate values (probably functions like `memcpy` and maybe `fwrite` should be immune from this)

##### Advantage

Restricts program behaviors least, giving compilers even more freedom.

##### Disadvantage

Needs even more modification to the text of the standard.

Needs a decision on what library functions will *not* have undefined behavior
when working on indeterminate values.

This is certainly not compatible with the current version of the standard, as no
undefined behavior of this kind related to library functions is described there.

### Suggested Technical Corrigendum

##### For resolution (a)

In 6.2.4p2, change "An object exists, has a constant address, and retains its
last-stored value throughout its lifetime." to "An object exists and has a
constant address throughout its lifetime. The value of an object is retained,
including the object representation, until some other value is stored into it,
or until the moment when the value becomes indeterminate (at which moment it is
replaced with an indeterminate value, and after which that value is retained
again)."

##### For resolution (b)

In 3.19.2 change "either an unspecified value or a trap representation" to
"either an unspecified value or a trap representation, which can change
arbitrarily without direct action from the program".

In 6.2.4p2, change "An object exists, has a constant address, and retains its
last-stored value throughout its lifetime." to "An object exists, has a constant
address, and retains its last-stored value (provided this value is not
indeterminate), throughout its lifetime."

At the end of 6.5p1 add "If at least one of the operands of an operator is
indeterminate, the result of the operator is also indeterminate."

Some instances of "indeterminate" and "unspecified" (to be determined) should be
replaced by respectively "unspecified" and "indeterminate". See for example the
instance in 6.2.6.1p6 mentioned earlier.

##### For resolution (c)

The changes for resolution (b), and also:

In 7.1.4p1 add: "If a function is called with an indeterminate value, the
behavior is undefined."

In a selection (to be determined) of functions from the library, add text that
counters this general statement added to 7.1.4p1.

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

### Committee Discussion

* The committee asserts that the answer to the first question is "yes", an uninitialized value under the conditions described can appear to change its value.
* Since question 2 is applicable, the answer is that any operation performed on indeterminate values will have an indeterminate value as its result.
* The answer to the applicable question 3 is that indeed library functions will exhibit undefined behavior when used on indeterminate values.
* The committee notes that the problem applies to all types that do not have trap representations as per the implementation.
* Strong sentiment formed, in part based on prior experience in developing Annex L, that a new category of "wobbly" value is needed. The underlying issue is that modern compilers track value propagation, and uninitialized values synthesized for an initial use of an object may be discarded as inconsequential prior to synthesizing a different value for a subsequent use. To require otherwise defeats important compiler optimizations. All uses of "wobbly" values might be deemed undefined behavior.
* The principle of Resolution C is desired.
* This requires careful thought.

Apr 2014 meeting

### Committee Discussion

> The author provided
> [N1793](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1793.pdf) and an
> accompanying presentation
> [N1818](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1818.pdf) in which his
> position changed to believing that "wobbly" values are not actually defined by
> the standard, and after discussion agreed that the following committee response
> would be an acceptable resolution.

### Proposed Committee Response

* The answer to question 1 is "yes", an uninitialized value under the conditions described can appear to change its value.
* The answer to question 2 is that any operation performed on indeterminate values will have an indeterminate value as a result.
* The answer to question 3 is that library functions will exhibit undefined behavior when used on indeterminate values.
* These answers are appropriate for all types that do not have trap representations.
* This viewpoint reaffirms the C99 DR260 position.
* The committee agrees that this area would benefit from a new definition of something akin to a "wobbly" value and that this should be considered in any subsequent revision of this standard.
* The committee also notes that padding bytes within structures are possibly a distinct form of "wobbly" representation.
