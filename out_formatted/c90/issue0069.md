## Issue 0069: What is the meaning of *pure binary numeration system*?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0171](../c90/issue0171.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_069.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_069.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

Before providing detailed answers, we want to provide some clarified
terminology. For any object type `T`, the underlying bytes of the object can be
copied into an array of `unsigned char`:

```c
#define N sizeof(T)
 union aligned_buf {
         T t;
         unsigned char s[N];
         } buf;
 T object;
 .....
         memcpy(buf.s, (const void *)&object, N);
```

The *object representation* of an object consists of the resulting sequence of
`N` objects of type `unsigned char` in the buffer. The object representation
depends upon several features of the implementation such as byte-ordering
(“big-endian,” “little-endian,” etc.), “holes” (i.e., bits within a scalar
object which do not participate in forming the value of the object), and
“padding” (i.e., bits in a non-scalar object which lie between the component
scalar objects or after the last scalar object).

The *value representation* of an object is a sequence of bits structured in a
specific conventional way. The scalar components are listed in their declaration
sequence. Each scalar component is a sequence of bits (the “participating bits”)
arranged in a conventional ordering. The value representation of floating-point
and pointer types is implementation-defined. The value representation of an
integer type is defined as follows: The least-significant bit (the bit which
represents the integer value 1\) is also called the low-order bit or rightmost
bit; the most-significant bit is also called the high-order bit or leftmost bit.
The sign bit (if any) is the leftmost bit.

If all the bits in a scalar object representation participate in the value
representation (i.e. no holes or padding), then the value representation can be
referred to simply as the *representation.* The bits of the value representation
determine a *value,* which is one discrete element of an implementation-defined
set of values. The conventional depiction of an integer value is as a decimal
integer, optionally signed, such as 128 or -1.

Here is an example. Consider a (possibly hypothetical) ones-complement
implementation whose `int` value representation provides one sign bit and 40
integer bits.

```c
    +-+---------------------+
    | |                     |
    +-+---------------------+
     1         40
```

Its object representation provides one sign bit, a hole containing seven
non-participating bits, and 40 integer bits (issues of byte ordering are
irrelevant here):

```c
    +-+------+---------------------+
    | |      |                     |
    +-+------+---------------------+
     1   7        40
```

The value representation containing 41 zero bits designates the value 0:

```c
    +-+---------------------+
    |0|000     ...       000|
    +-+---------------------+
     1         40
```

Depending upon the implementation, the value representation containing 41 one
bits may designate the same value 0, in which case it is indistinguishable from
the other value representation; or it may designate a distinguishable value,
conventionally depicted as -0, which is arithmetically equal to 0 but
distinguishable by bitwise operations.

```c
    +-+---------------------+
    |1|111     ...       111|
    +-+---------------------+
     1         40
```

Now for detailed replies:

a) Footnotes are not normative. The *legality* of a footnote is beyond the scope
of WG14/X3J11.

b) Yes, the footnote is correct.

c) No, there is no such requirement.

d) In view of the discussion above, we assume you mean the following question:
Does the C Standard require that all bits of the object representation
participate in the value representation? For character types, all bits of the
object representation do contribute. See subclauses 7.9.2 (re binary streams)
and 7.11.1 (re string functions) for (indirect) justification. More precisely,
any bits that do not contribute to the value of a character type must not
contribute to the value of any other object type. (Parity bits are an obvious
example.) For other types, the answer is no.

e) In view of the discussion above, we assume you mean the following question:
Does the C Standard require that all possible bit patterns of the object
representation represent numbers? For the type `unsigned char`, the answer is
yes. (And if all values of the type `char` are non-negative, then the answer is
yes.) Otherwise, the answer is no.

f) No, except for the character types as mentioned above.

g) Not applicable, since it is unclear what are the meanings of “bit pattern”
and “value” in the question; see the answer to part (e).

h) Yes, provided there is no other violation of the C Standard.

i) Yes, provided there is no other violation of the C Standard.

j) No. It is not a pure binary system.

k) Yes, except for `SCHAR_MAX == UCHAR_MAX` (which is specifically disallowed),
provided there is no other violation of the C Standard.

l) Yes, provided there is no other violation of the C Standard.

m) Yes, because subclause 6.1.2.5 states that the positive signed integers have
the same representation as the corresponding unsigned integers, and because
signed integers use a pure binary numeration system. The Committee intended to
permit ones complement, twos complement, and signed magnitude implementation.

n) No. There are architectures on which not all bits can be used.

p) Yes, because subclause 6.1.2.5 requires unsigned integers to behave as if a
result “is reduced modulo the number that is one greater than the largest value
that can represented,” and unsigned integers use a pure binary numeration
system.

q) No. The memory occupied by a value of an integer is allowed to exceed the
number of binary digits used to represent the actual value.

r) Yes. See the answer to part (m).

s) No. See the answer to part (q).

t) Not applicable.

u) Yes, the expression must evaluate to 0 or -1.
