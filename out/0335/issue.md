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
