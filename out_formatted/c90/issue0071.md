## Issue 0071: Are all enumerated types compatible with a single type?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Cross-references: [0067](../c90/issue0067.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_071.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_071.html)

Item 8 \- enumerated types

The C Standard states (in effect) that an enumerated type is a set of integer
constant values (subclause 6.1.2.5). It also states that an enumerated type must
be compatible with an implementation-defined integer type (subclause 6.5.2.2).
Finally, the integral promotions (subclause 6.2.1.1) convert an enumerated type
to `signed` or `unsigned int`. Consider:

```c
enum foo { foo_A = 0, foo_B = 1, foo_C = 8 };
 enum bar { bar_A = -10, bar_B = 10 };
 enum qux { qux_A = UCHAR_MAX * 4, qux_B };
```

a. If any value between zero and `SCHAR_MAX` (inclusive) is assigned to a
variable of type `enum foo`, and the value of the variable is then converted to
type `int` or `unsigned int`, does the C Standard require the original value to
result; or is the implementation permitted or required to convert it to one of
the three values 0, 1, and 8; or is the result of the assignment undefined?

b. Can a conforming implementation require all enumerated types to be compatible
with a single type?

c. If the answer to (b) is “yes,” and assuming that the value `UCHAR_MAX * 4` is
less than `SHRT_MAX` is the declaration of the type `enum qux` strictly
conforming, or can a conforming implementation require all enumerated types to
be compatible with a single type which is a character type?

d. Can an implementation make the type that `enum bar` is compatible with be an
unsigned type, even though it uses an enumeration constant not representable in
that type?

e. Can an implementation make the type that `enum qux` is compatible with be
either of `signed char` or `unsigned char`, even though it uses an enumeration
constant not representable in that type?

f. If the answer to (d) or (e) is “yes,” what is the effect of making one of the
enumeration constants of an enumerated type outside the range of the compatible
type? What is the effect of assigning the value of that constant to an object of
the enumerated type?

g. Can the type that an enumerated type is compatible with be `signed` or
`unsigned long`? If so, what are the effects of the integral promotions on a
value of that type?

h. If an implementation is allowed to add other types to the list of integer
types (see items 4(b) and (c)), then can the type that an enumerated type is
compatible with be such a type?

---

Comment from WG14 on 1997-09-23:

### Response

a) Every enumerated type is compatible with some integer type (subclause
6.5.2.2). When conversion takes place between compatible types, values are not
altered (subclause 6.2). So for values between 0 and `SCHAR_MAX`, the original
value must result, because no matter what type is chosen, the value can be
expressed in that type.

b) Yes it can.

c-g) It is the intention of the C Standard that all the members of the
enumeration be representable in the enumerated type, and that the compatible
integer type be one which promotes to `int` or `unsigned int`.

h) An implementation is not allowed to add other types to the list. (See reply
to [Defect Report #067](../c90/issue0067.md).)

### Correction

***In subclause 6.5.2.2, page 61, second paragraph of Semantics, change:***

Each enumerated type shall be compatible with an integer type; the choice of
type is implementation-defined.

***to:***

Each enumerated type shall be compatible with an integer type. The choice of
type is implementation-defined, but shall be capable of representing the values
of all the members of the enumeration.
