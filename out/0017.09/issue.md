Syntax of assignment expression

In subclause 6.3.16.1 on page 53, lines 31-32 there is a typo: “... of the
assignment expression ...” should be “... of the unary expression ...”

In subclause 6.3.16 on page 53, lines 3-5 we have

```c
assignment-expression:
    ...
         unary-expression  assignment-operator  assignment-expression
```

Now the string “*`assignment-expression`*” occurs twice.

The use of “assignment expression” in subclause 6.3.16 on page 53, line 12
refers to the first occurrence (the one to the left of the colon).

We suggest changing the use of “assignment expression” in subclause 6.3.16.1 on
page 53, line 32 in order to prevent confusion. The fact that any qualifier is
kept actually makes more sense, since this qualifier has to take part in any
constraint checking.
