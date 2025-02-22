## Issue 0122: Is the *type* of a bit-field totally independent from its *width*?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0015](../c90/issue0015.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_122.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_122.html)

ANSI/ISO C Defect Report #rfg29:

Subject: Conversion/widening of bit-fields.

Must the following program print `1` or `0`?

```c
#include <stdio.h>

 struct S { unsigned bit:1; } object = { 1 };

 int main ()
        {
        printf ("%d\n", ((object.bit - 2) < 0));
        return 0;
        }
```

(At least one existing implementations prints `1` while another prints `0`.)

Background:

Subclause 6.2.1.1:

> A `char`, a `short int`, or an `int` bit-field, or their signed or unsigned
> varieties, or an enumeration type, may be used in an expression wherever an
> `int` or `unsigned int` may be used. If an `int` can represent all values of the
> original type, the value is converted to an `int`; otherwise it is converted to
> an `unsigned int`.

The key phrase here is “the original type.”

In effect, I am asking if the *type* of a bit-field is totally independent from
its *width* for the purposes of the above rule.

If the answer to that question is “yes,” then the value of `object.bit` must be
considered to be an `unsigned int` (with a value of `1U`). In that case, the
value `2` used in the above example must also be converted to type `unsigned
int` and then the subtraction should be carried out on the two `unsigned int`
values. The subtraction should then itself yield a value of type `unsigned int`
which is itself (by definition) \>\= 0, so it would seem that the C Standard
requires the above program to print `0`.

Is that correct? If so, perhaps the wording of the above paragraph needs to be
improved so as to make the correct interpretation of these rules more apparent
to implementors.

---

Comment from WG14 on 1997-09-23:

### Response

See [Defect Report #015](../c90/issue0015.md). “The original type” applies to both width
and signedness. `object.bit` promotes to `int`, and the program prints `1`.
