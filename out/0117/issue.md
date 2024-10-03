ANSI/ISO C Defect Report #rfg24:

Subject: Abstract semantics, sequence points, and expression evaluation.

Does the following code involve usage which renders the code itself not strictly
conforming?

```c
int example ()
        {
        int x1 = 2, x2 = 1, x_temp;

        return (x_temp = x1, x_temp) + (x_temp = x2, x_temp);
        }
```

Background:

Subclause 5.1.2.3:

> The semantic descriptions in this International Standard describe the behavior
> of an abstract machine in which issues of optimization are irrelevant.

Subclause 6.3:

> Between the previous and next sequence point an object shall have its stored
> value modified at most once by the evaluation of an expression.

Although it is quite clear that the above quoted “modified at most once” rule
was intended to render certain programs “not strictly conforming,” there is an
unfortunate amount of ambiguity built into the current wording of that rule.

Quite simply, while the “modified at most once” rule is obviously telling us
what a “strictly conforming program” must not do between two particular points
*in time,* it is altogether less than clear what events and/or actions (exactly)
are associated with these two points in time. Additionally, it is also less than
clear (from reading the remainder of the C Standard) what actions and/or events
are allowed (or required) to take place between some pair of sequence points in
cases where both members of the pair are part of some large single expression
whose evaluation order is not completely dictated by the C Standard.

Note that despite the assertion given in subclause 5.1.2.3 (and quoted above)
the C Standard does not *fully* specify the behavior of the “abstract machine,”
especially when it comes to the issue of the ordering of sub-expression
evaluation used by the “abstract machine” model.

This fact makes it inherently impossible to precisely determine even just the
*relative* timings of various events (including the “occurrence” of or the
“execution” of or the “evaluation” of sequence points) which may (or must) occur
sometime during the evaluation of a larger containing expression (except in a
few cases involving `||` or `&&` or `?:` or `,` operators).

To put it more plainly, if some pair of sequence points will be “reached” (or
“evaluated” or “executed”) during the evaluation of any pair of subexpressions
which are themselves operands for some binary operator (other than the operators
`||` or `&&` or `?:` or `,`) then the C Standard's description of the “abstract
machine” semantics are inadequate to enable us to know either which *order*
these two sequence points will occur in, or even which other aspects of the
evaluation of the overall expression may (or must) occur “between” the two
sequence points.

Thus, it seems that it may also be inherently impossible to know whether or not
the prohibition against multiple modifications of a given variable “between” two
consecutive sequence points is (or may be) violated in such contexts.

Here is a simple example of an expression which illustrates these points:

> ```c
>         (x = i, x) + (x = j, x)
> ```

In this expression there are two “comma” sequence points; however, nothing in
the C Standard gives any indication as to which of these two may be (or must be)
“evaluated” or “reached” first. (Indeed, it would seem that on a parallel
machine of some sort, *both* points could perhaps be reached simultaneously.) It
is fairly clear however that each of the references to the stored values of `x`
must not be evaluated until their respective preceding “comma sequence points”
have been “reached” or “evaluated.” Thus, a partial (but very incomplete)
ordering is imposed upon the sequence of events which must occur during the
evaluation of this expression.

For the sake of this example, let us call the leftmost comma in the above
expression “lcomma” and call the rightmost comma “rcomma.” Given this
terminology, it would appear that the C Standard permits the following sequence
of events during evaluation of the above expression:

> ```c
>         eval(i)
>         x=          (leftmost assignment to x)
>         lcomma      <==== sequence point
>         eval(x)     (leftmost reference to stored value of x)
>         eval(j)
>         x=          (rightmost assignment to x)
>         rcomma      <==== sequence point
>         eval(x)     (rightmost reference to stored value of x)
>         +
> ```

Note that in this (very realistic) example, the stored value of `x` is *never*
modified more than once between any pair of sequence points. Given that the
ordering described above is both a perfectly *plausible* and also a perfectly
*permissible* ordering for the evaluation of the expression in question, and
given that this particular permissible ordering of events does not violate the
“modified at most once” rule (quoted earlier) it therefore appears that the
expression in question may in fact be interpreted as being “strictly
conforming,” and that such expressions may appear within “strictly conforming”
programs.

I would like the Committee to either confirm or reject this view, and to provide
some commentary explaining that confirmation or rejection.
