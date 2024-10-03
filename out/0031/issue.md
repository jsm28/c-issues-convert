Referring to subclause 6.3, page 38, lines 15-17:

> If an *exception* occurs during the evaluation of an expression (that is, if the
> result is not mathematically defined or not in the range of representable values
> for its type), the behavior is undefined.

and subclause 6.4, page 55, lines 11-12:

> Each constant expression shall evaluate to a constant that is in the range of
> representable values for its type.

What should be the result of the constant expression:

```c
INT_MAX + 2
```

Is this a constraint violation, or it should be mapped onto the set of
representable values?

What should be the result of:

```c
INT_MAX + 2ul
```

How should compilers that do not evaluate the constant expressions at compile
time behave?

What is the result of:

```c
(INT_MAX*4)/4
```

Referring to subclause 6.5.2.2, page 61, lines 29-30:

> The expression that defines the value of an enumeration constant shall be an
> integral constant expression that has a value representable as an `int.`

What is the result of:

```c
enum { a=INT_MAX, b };
```

Does this violate the C Standard?
