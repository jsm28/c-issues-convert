### Summary

### Summary

In 12.5, n is defined to be “the number of digits in the coefficient *c*”, where
the decimal floating-point argument is represented by the triple (*s*, *c*,
*q*). The intention is that *n* is the number of digits in the coefficient of
the particular argument, i.e., the number of significant digits, not the maximum
number of digits in the coefficient for the type. This might be misread,
particularly since 5.2.4.2.2a says

> number of digits in the coefficient
>
> ```c
> DEC32_MANT_DIG                 7
> ```

```c
DEC64_MANT_DIG                 16
```

> ```c
> DEC128_MANT_DIG                34
> ```

This part of 5.2.4.2.2a is in the context of characterizing the type, so clearly
refers to the type and not any particular representation.

### Suggested Technical Corrigendum

In 12.5, change:

> where *n* is the number of digits in the coefficient *c*

to:

>                   where *n* is the number of significant digits in the
> coefficient *c*
