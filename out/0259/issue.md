### Problem

Consider the code:

```c
   #define m0()  replacement
    #define m1(x) begin x end
    m0() m1()
```

The number of arguments in a macro invocation is defined by 6.10.3#11:

> \[#11] The sequence of preprocessing tokens bounded by the outside-most matching
> parentheses forms the list of arguments for the function-like macro. The
> individual arguments within the list are separated by comma preprocessing
> tokens, but comma preprocessing tokens between matching inner parentheses do not
> separate arguments.

while 6.10.3#4 reads:

> \[#4] If the identifier-list in the macro definition does not end with an
> ellipsis, the number of arguments (including those arguments consisting of no
> preprocessing tokens) in an invocation of a function-like macro shall equal the
> number of parameters in the macro definition. Otherwise, there shall be more
> arguments in the invocation than there are parameters in the macro definition
> (excluding the ...). There shall exist a ) preprocessing token that terminates
> the invocation.

Now:

|  |  |
| --- | --- |
| **EITHER:** | the invocation of `m0` has a single argument, |
| **OR:** | the invocation of `m1` has no arguments, |

and in either case the requirement of 6.10.3#4 is violated.

This is clearly not the intent.

### Suggested Technical Corrigendum

Append to 6.10.3#4:

> If the invocation has no preprocessing tokens between the parentheses, this
> shall count as one argument unless the macro definition has neither an
> identifier list nor an ellipsis, in which case it shall count as no arguments.
