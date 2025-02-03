Item 24 \- order of evaluation

Consider the following program:

```c
int g;

 int main (void)
        {
        int x;

 	x = (10, g = 1, 20) + (30, g = 2, 40);	 /* Line A */
 	x = (10, f (1), 20) + (30, f (2), 40);	 /* Line B */
 	x = (g = 1) + (g = 2);			 /* Line C */
        return 0;
        }

 int f (int i)
        {
        g = i;
        return 0;
        }
```

Subclause 6.3 makes the statement:

> Between the previous and the next sequence point an object shall have its stored
> value modified at most once by the evaluation of an expression.

Consider line A. The full expression (the assignment to `x`) assigns two values
(1 and 2\) to `g`. Each such assignment is surrounded by sequence points.
However, there is no sequence point between the two operands of the addition,
and therefore no defined order of evaluation of the two inner assignments. There
are a number of possible interpretations of the C Standard that can be made.

1. Multiple threads of evaluation may take place at one time (or equivalently, the evaluation of various parts of the expression may be interleaved to any level of detail), provided that anything specified to occur before a given sequence point actually takes place before anything specified to occur after the same sequence point. (This is equivalent to the “collateral evaluation” of Algol 68.)

   In this interpretation, the expression is clearly undefined, because the two
   assignments to `g` may take place simultaneously and interfere destructively
   with one another. However, if this model is applied to line B, it yields the
   same result (since the sequence points occur at the same places). This means
   that, in effect, two function calls can be taking place simultaneously, and, if
   they modify the same object, the effect is undefined. This would surprise many
   users of the C Standard.
2. As (1), but assignments are atomic. This means that `g` has the value 1 or 2, though it is unspecified which. When applied to line C, this would also mean that `x` is specified to be assigned the value 3\. This seems counter to the quoted provision of subclause 6.3.
3. Any expression which completely fills the interval between two sequence points, and does not contain any embedded sequence points, is an “atomic sequence.” The operations of any one atomic sequence are carried out together, and cannot be interleaved with any other atomic sequence. The order of the atomic sequences is unspecified, except that if the ending sequence point of one atomic sequence is the same as the starting point of another atomic sequence, they must be executed in that order.

   In line A, there are five atomic sequences:

   (i) evaluate 10

   (ii) assign 1 to `g`

   (iii) evaluate 30

   (iv) assign 2 to `g`

   (v) evaluate 20 and 40, add, and assign to `x`

   (i) must come before (ii), (iii) must come before (iv), (v) must come after (ii)
   and (iv).

   In line A this model has the same effect as (2), but it could differ in more
   complex expressions.
4. Multiple threads of execution can occur within an expression, but all except one are suspended while a function is being executed (this may, of course, spawn off new threads). This interpretation could be viewed as supported by the wording in subclause 6.6: “Except as indicated, statements are executed in sequence.” It would have the effect of leaving line A undefined while line B is conforming (with it being unspecified whether the latter assigns 1 or 2 to `g`).

Which, if any, of these interpretations is correct? If none of them, what is the
correct interpretation to make?
