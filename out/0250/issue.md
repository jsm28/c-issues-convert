### Problem

Consider the code:

```c
  #define nothing(x) // Nothing    /* Case 1 */
    nothing (
    #include <stdio.h>
    )
    /* Case 2 */
    nothing (
    #nonstandard
    )
```

6.10.3#11 reads in part:

> If there are sequences of preprocessing tokens within the list of arguments that
> would otherwise act as preprocessing directives, the behavior is undefined.

This clearly covers case 1\. However, it is not clear whether or not case 2 is a
preprocessing directive. It is a "non-directive", but is that also a directive ?
If case 2 is a directive, it is undefined behaviour. If it is not, then case 2
is strictly-conforming and macro-expands to nothing.

Since non-directives are only valid as extensions, it might be more sensible for
them to behave as directives do and make the behaviour undefined in this case.

### Suggested Technical Corrigendum

In 6.10.3#11, change the last sentence to:

> If there are sequences of preprocessing tokens within the list of arguments that
> would otherwise act as preprocessing directives or as non-directives (that is,
> the first pre-processing token on a line is a `#)`, the behavior is undefined.
