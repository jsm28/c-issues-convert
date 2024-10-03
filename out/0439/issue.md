### Summary

I have discovered several issues in 6.8p4, which defines “full expression” and
points out the major implications for an expression that is a full expression.
In this paper I present the issues, along with my recommendations. For the
issues for which it makes sense, I will later submit defect reports.

Here is the text of 6.8p4, with clause numbering added for convenience of
reference:

> 1. A *full expression* is an expression that is not part of another expression or of a declarator.
> 2. Each of the following is a full expression:
>    1. an initializer that is not part of a compound literal;
>    2. the expression in an expression statement;
>    3. the controlling expression of a selection statement (if or switch);
>    4. the controlling expression of a while or do statement;
>    5. each of the (optional) expressions of a for statement;
>    6. the (optional) expression in a return statement.
> 3. There is a sequence point between the evaluation of a full expression and the evaluation of the next full expression to be evaluated.

And here are the issues.

A. The phrase “not part of another expression or of a declarator” (sentence 1\)
is rather difficult to understand. It *probably* means: not part of another
expression, nor part of a declarator. (But DeMorgan's law is hard on the brain.)

I believe this could be fixed as a simple editorial issue.

B. The status of an initializer expression depends on whether the context is a
declaration or a compound literal (clause 2.1). That would seem to imply
different sequencing guarantees in those contexts. As it turns out, it does, but
the implication is quite subtle. Consider 6.7.9p23:

> The evaluations of the initialization list expressions are indeterminately
> sequenced with respect to one another and thus the order in which any side
> effects occur is unspecified.

And consider this example:

```c
#include <stdio.h>



#define ONE_INIT        '0' + i++ % 3

#define INITIALIZERS    [2] = ONE_INIT, [1] = ONE_INIT, [0] = ONE_INIT



int main()

{

        int i = 0;

        char x[4] = { INITIALIZERS }; // case 1

        puts(x);

        puts((char [4]){ INITIALIZERS }); // case 2

        puts((char [4]){ INITIALIZERS } + i % 2); // case 3

}
```

In every use of the `INITIALIZERS` macro, the variable `i` is incremented three
times. In cases 1 and 2, there is no undefined behavior, because the increments
are in expressions that are indeterminately sequenced with respect to one
another, not unsequenced. There is no guarantee in what order the evaluations
are done, so there is no guarantee in what order they will appear, but the
initial values are guaranteed to be `'0'`, `'1'` and `'2'`.

(It's not perfectly clear whether that guarantee was provided by C99, which
instead said:

> The order in which any side effects occur among the initialization list
> expressions is unspecified.

In any event, as a data point, that guarantee was not honored by GCC until
release 4.6, in 2011.)

On the other hand, because case 3 contains an unsequenced evaluation of `i` in
the same full expression, it has undefined behavior.

Considering the number of hours it took me to finally reach this conclusion, I
thought it would be worthwhile to bring it to the full committee to make sure
everyone understands and agrees with it. If so, an addition to the rationale
might be in order.

C. Consider 6.7.6p3 (emphasis added):

> A *full declarator* is a declarator that is not part of another declarator.
> **The end of a full declarator is a sequence point.** …

Also 6.2.4p8:

> A non-lvalue expression with structure or union type, where the structure or
> union contains a member with array type (including, recursively, members of all
> contained structures and unions) refers to an object with automatic storage
> duration and *temporary lifetime*.<sup>36\)</sup> Its lifetime begins when the
> expression is evaluated and its initial value is the value of the expression.
> Its lifetime ends **when the evaluation of the containing full expression or
> full declarator ends**. Any attempt to modify an object with temporary lifetime
> results in undefined behavior.

It is clear from these passages that the sequence of evaluations includes not
only full expressions, but also full declarators – whatever sense it makes to
talk about “evaluating” a full declarator. But sentence 3 does not acknowledge
that reality.

My inclination is to adopt a bit of terminology from Ada, and start talking
about the “elaboration” of a declarator, which, for a variably modified type,
involves the run-time evaluation of array sizes, and then to re-draft sentence 3
and the other paragraphs cited here, to make it clear that sequence points
separate elaborations of full declarators as well as evaluations of full
expressions. In any event, I think there's a problem in sentence 3 that needs to
be fixed.

D. Expressions in abstract declarators are not mentioned at all (compare to
sentence 1). The logical inference is that such an expression is not a full
expression by itself, but part of the containing full expression. But there are
cases where there is no containing full expression. For example:

```c
typedef _Atomic(int (*)[rand()]) T;

_Alignas(int [rand()]) int i;
```

In these examples, not only is there no containing full expression, there isn't
even any containing full declarator, because these expressions appear in the
declaration specifiers, not the declarator.

Probably the simplest approach here would be to disallow variably modified types
with `_Atomic` and `_Alignas`, at least until the next revision of the standard.

E. The list of full expression contexts (sentence 2\) is not logically complete.
According to the definition (sentence 1), an expression appearing in a
constant-expression context is (often) a full expression. Of course there are no
sequencing implications relevant for constant expressions, but it's not clear
that makes it important for a constant expression not to be counted as a full
expression. In any event, it's not clear how the list normatively interacts with
the definition.

I think we should consider moving the list into a note, so it's clear that the
definition is, well, definitive. The note could also point out that sequencing
is irrelevant to constant expressions.
