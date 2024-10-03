Description: the current specification allows global named-registers to be
initialized:

```c
register REG_A int reg_a = 32;
```

It is however unclear when, and by whom this initialization should be done (one
could imagine that the register storage onto which the variable maps does not
really exist until some device is initialized by some user code).

Proposed solution: disallow initializers on named-register variables.
