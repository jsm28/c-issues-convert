ANSI/ISO C Defect Report #rfg27:

Subject: Semantics of assignment to (and initialization of) bit-fields.

a) Is the following program strictly conforming?

b) Must a conforming implementation translate this code into an executable
program which prints `3 3`?

```c
#include <stdio.h>

 struct S { unsigned bit:1; };
 struct S object1 = { 3 };      /* ? */
 struct S object2;

 int main ()
        {
        object2.bit = 3;        /* ? */
        printf ("%d %d\n", object1.bit, object2.bit);
        return 0;
        }
```

Background:

Subclause 6.3.16.1 (**Semantics**):

> In *simple assignment* (`=`), the value of the right operand is converted to the
> type of the assignment expression and replaces the value stored in the object
> designated by the left operand.

Subclause 6.2.1.2 (**Semantics**):

> When a value with integral type is converted to another integral type, if the
> value can be represented by the new type, its value is unchanged.

Unless I'm mistaken, the type of the assignment expression:

> ```c
>         object2.bit = 3;
> ```

in the above example is type `unsigned int`. Thus, according to the rules quoted
here, the value of `3` is converted to an `unsigned int` type value (during this
assignment statement) and it is otherwise unchanged. Then, *that value* of 3
replaces the previous value of `object2.bit`.

I believe that the above examples illustrate the point that the C Standard
currently fails to adequately describe the semantics of assignments to (and/or
initializations of) bit-fields in cases where the value being assigned will not
actually fit into the bit-field object.

In lieu of any description of the special semantics of assignments to bitfields,
it appears to be currently *necessary* for both implementors and users to assume
that the “normal” assignment semantics apply, but as you can see from the above
examples, such assumptions lead to highly counterintuitive expectations (and to
expectations which fly in the face of actual current common practice).

I believe that the Committee should rectify the current unfortunate situation by
adding to subclause 6.3.16.1 (or maybe to subclause 6.2.1.2) some additional new
verbage explicitly describing the special semantics of assignments to
bit-fields.
