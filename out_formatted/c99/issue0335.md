## Issue 0335: \_Bool bit-fields

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred Tydeman (USA)  
Date: 2006-12-12  
Reference document: [ISO/IEC WG14 N1204](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1204.htm), [ISO/IEC WG14 DR 262](../c99/issue0262.md), [ISO/IEC WG14 DR 315](../c99/issue0315.md)  
Submitted against: C99  
Status: Closed  
Cross-references: [0262](../c99/issue0262.md), [0315](../c99/issue0315.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_335.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_335.htm)

### Summary

What are the constraints on and semantics of \_Bool bit-fields?

```c
  #include <stdbool.h>
  struct bits {
      _Bool    bbf1 : 1;        /* unsigned 1-bit _Bool bit-field */
      _Bool    bbf3 : 3;        /* unsigned 3-bit _Bool bit-field */
  } bits;
  int main(void){
    bits.bbf1 = true;              /* the value 1u */
    bits.bbf1 = ~ bits.bbf1;       /* undefined? 0u? 1u? */
    bits.bbf3 = true;              /* the value 1u */
    bits.bbf3 = ~ bits.bbf3;       /* undefined? 0u? 1u? 6u? */
    return 0;
  }
```

What is the maximum width of a \_Bool bit-field allowed that does not cause a
constraint violation? 1? CHAR\_BIT? Something else? Is bbf3 a constraint
violation?

DR 262 changed 6.7.2.1#3 to require a constraint violation if a bit-field width
is too large.

6.2.5#2 says \_Bool can hold the values 0 and 1\.

6.2.6.2#6 discusses width.

I see nothing that says the width of a \_Bool is 1\.

6.7.2.1#9 has: If the value 0 or 1 is stored into a nonzero-width bit-field of
type \_Bool, the value of the bit-field shall compare equal to the value stored.

So, if a value other than 0 or 1 is stored into a nonzero-width bit-field of
type \_Bool, is that undefined?

The first assignment gives the bit-field the value 1u. The \~ of that value
yields ...1111110u. When that value is then stored into the \_Bool bit-field,
what value is stored?

* 0u since it is a 1-bit unsigned int field.
* 1u since it is a \_Bool (and the value is non-zero).
* 6u since it is a 3-bit unsigned int field.
* Undefined.

6.3.1.2 Boolean type has: When any scalar value is converted to \_Bool, the
result is 0 if the value compares equal to 0; otherwise, the result is 1\.

6.7.2.1#9 has: A bit-field is interpreted as a signed or unsigned integer type
consisting of the specified number of bits.

So, does a \_Bool bit-field have the semantics of a \_Bool (as per 6.3.1.2) or
of an unsigned integer type (as per 6.7.2.1)? DR 315 might be relevant.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2008-07-21:

### Proposed Technical Corrigendum

### Committee Discussion (for history only)

#### Spring 2007

The width of a `_Bool` bit-field is at most the implementation defined width of
the type `_Bool`. A `_Bool` bit-field has the semantics of a `_Bool` (and not an
`unsigned int`).

#### Spring 2008

6.7.2.1 paragraph 3 covers the above Committee discussion. (9899:1999 \+ TC1 \+
TC 2 \+ TC3)

> The expression that specifies the width of a bit-field shall be an integer
> constant expression with a nonnegative value that does not exceed the width of
> an object of the type that would be specified were the colon and expression
> omitted.

Therefore the width of a `_Bool` bit-field is at most the implementation-defined
width of the type `_Bool`.

### Committee Response

6.2.5 paragraph 6 states that

> The type `_Bool` and the unsigned integer types that correspond to the standard
> signed integer types are the standard unsigned integer types.

In other words, `_Bool` is one of the unsigned integer types whether it is used
in a bit-field or not. 6.3.1.2p1 explicitly defines the semantics of `_Bool`,
which are different from other unsigned integer types.

A `_Bool` bit-field has the semantics of a `_Bool` (and not `unsigned int`).

6.7.2.1 paragraph 3 (9899:1999 \+ TC1 \+ TC 2 \+ TC3) states that

> The expression that specifies the width of a bit-field shall be an integer
> constant expression with a nonnegative value that does not exceed the width of
> an object of the type that would be specified were the colon and expression
> omitted.

The width of a `_Bool` bit-field is at most the implementation-defined width of
the type `_Bool`.
