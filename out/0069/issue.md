Item 6 \- representation of integral types

Subclause 6.1.2.5 refers to the representation of a value in an integral type
being in a “pure binary numeration system,” and defines this further in Footnote
18\. On the other hand, the wording of ISO 2382 is:

> 05.03.15
> 
> **binary (numeration) system**
> 
> The *fixed radix numeration system* that uses the *bits* 0 and 1 and the *radix*
> two.
> 
> Example: In this *numeration system,* the numeral 110,01 represents the number
> "6,25"; that is 1 x 2-2 \+ 1 x 2-1 \+ 1 x 2-2.
> 
> 05.03.11
> 
> **fixed radix (numeration) system**
> 
> **fixed radix notation**
> 
> A *radix numeration system* in which all the *digit places,* except perhaps the
> one with the highest *weight,* have the same *radix.*
> 
> NOTES
> 
> 1\. The weights of successive digit places are successive integral powers of a
> single radix, each multiplied by the same factor. Negative integral powers of
> the radix are used in the representation of factors.
> 
> 2\. A fixed radix numeration system is a particular case of a *mixed radix
> numeration system*; see also Note 2 to 05.03.19.
> 
> 05.03.08
> 
> **radix**
> 
> **base (deprecated in this sense)**
> 
> In a *radix numeration system,* the positive *integer* by which the *weight* of
> any *digit place* is multiplied to obtain the weight of the digit place with the
> next higher weight.
> 
> Example: In the *decimal numeration system* the radix of each digit place is
> 10\.
> 
> NOTE \- The term base is deprecated in this sense because of its mathematical
> use (see definition in 05.02.01).
> 
> 05.03.07
> 
> **radix (numeration) system**
> 
> A *positional representation system* in which the ratio of the *weight* of any
> one *digit place* to the weight of the digit place with the next lower weight is
> a positive *integer.*
> 
> NOTE \- The permissible values of the *character* in any digit place range from
> zero to one less than the *radix* of that digit place.
> 
> 05.03.04
> 
> **weight**
> 
> In a *positional representation system,* the factor by which the value
> represented by a *character* in a *digit place* is multiplied to obtain its
> additive contribution in the representation of a number.
> 
> 05.03.03
> 
> **digit place**
> 
> **digit position**
> 
> In a *positional representation system,* each site that may be occupied by a
> *character* and that may be identified by an ordinal number or by an equivalent
> identifier.
> 
> 05.03.01
> 
> **positional (representation) system**
> 
> **positional notation**
> 
> Any *numeration system* in which a number is represented by an *ordered* set of
> *characters* in such a way that the value contributed by a character depends
> upon its position as well as upon its value.

a. What is the legal force of the footnote, given that it quotes a definition
from a document other than ISO 2382 (see 3)?

b. Is the footnote wording correct, seeing that the ISO 2382 definition does not
appear to allow any of the common representations (note the word “positive” in
05.03.07)?

c. Does the C Standard require that an implementation appear to use only one
representation for each value of a given type?

d. Does the C Standard require that all the bits of the value be significant?

e. Does the C Standard require that all possible bit patterns represent numbers?

f. Do the answers to questions (c), (d), and (e) depend on whether the type is
signed or unsigned, and in the former case, on the sign of the value?

g. If it is permitted for certain bit patterns not to represent values, is
generation of such a value by an application (using bit operators) undefined
behavior, or is use of such a value strictly conforming provided that it is not
used with arithmetic operators?

In particular, are the following five implementations allowed?

h. Unsigned values are pure binary. Signed values are represented using
ones-complement (in other words, positive and negative values with the same
absolute value differ in all bits, and zero has two representations). Positive
numbers have a sign bit of 0, and negative numbers a sign bit of 1\. In both
cases, all bits are significant.

i. Unsigned values are pure binary. Signed values are represented using
sign-and-magnitude with a pure binary magnitude (note that the top bit is not
“additive”). Positive numbers have a sign bit of 0, and negative numbers a sign
bit of 1\. In both cases, all bits are significant.

j. Unsigned values are pure binary, with all bits significant. Signed values
with an MSB (sign bit) of 0 are positive, and the remainder of the bits are
evaluated in pure binary. Signed values with an MSB of 1 are negative, and the
remainder of the bits are evaluated in BCD. If ints are 20 bits, then `INT_MAX`
is 524,287 and `INT_MIN` is -79,999.

k. Signed values are twos-complement using all bits. Unsigned values are pure
binary, but ignoring the MSB (so each number has two representations). In this
implementation, `SCHAR_MAX == UCHAR_MAX`, `SHRT_MAX == USHRT_MAX`, `INT_MAX ==
UINT_MAX`, and `LONG_MAX == ULONG_MAX`.

l. Signed values are twos-complement. Unsigned values are pure binary. In both
cases, the top three bits of the value are ignored (and each number has eight
representations). For signed values, the sign bit is the fourth bit from the
top.

Furthermore:

m. Does the C Standard require that the values of `SCHAR_MAX`, `SHRT_MAX`,
`INT_MAX`, and `LONG_MAX`, defined in `<limits.h>` (subclause 5.2.4.2.1) all be
exactly one less than a power of 2?

n. If the answer to (m) is “yes,” then must the exponent of 2 be exactly one
less than `CHAR_BIT * sizeof (T)`, where `T` is `signed char`, `short`, `int`,
or `long`, respectively?

o. Does the C Standard require that the values of `UCHAR_MAX`, `USHRT_MAX`,
`UINT_MAX`, and `ULONG_MAX`, defined in `<limits.h>` (subclause 5.2.4.2.1) all
be exactly one less than a power of 2?

p. If the answer to (p) is “yes,” then must the exponent of 2 be exactly
`CHAR_BIT * sizeof (T)`, where `T` is `unsigned char`, `unsigned short`,
`unsigned int`, or `unsigned long` respectively?

q. Does the C Standard require that the absolute values of `SCHAR_MIN`,
`SHRT_MIN`, `INT_MIN`, and `LONG_MIN`, defined in `<limits.h>` (subclause
5.2.4.2.1) all be exactly a power of 2 or exactly one less than a power of 2?

r. If the answer to (r) is “yes,” then must the exponent of 2 be exactly one
less than `CHAR_BIT * sizeof (T)`, where `T` is `signed char`, `short`, `int`,
or `long` respectively?

s. If any of the answers to (m), (p), or (r) is “no,” are there any values for
each of these expressions that are permitted by subclause 5.2.4.2 but prohibited
by the C Standard for other reasons, and if so, what are they?

t. Does the C Standard require that the expressions `(SCHAR_MIN + SCHAR_MAX)`,
`(SHRT_MIN + SHRT_MAX)`, `(INT_MIN + INT_MAX)`, and `(LONG_MIN + LONG_MAX)` be
exactly 0 or -1? If not, does it put any restrictions on these expressions?
