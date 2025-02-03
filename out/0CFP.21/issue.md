### Summary

It is possible that a floating-point value, when converted to a one-digit
character string, results in odd numbers no matter which way rounding is done.
For roundTiesToEven, IEC 60559 specifies that the larger magnitude value be
used.

Suggested Technical Corrigendum:

Add the following to TS 18661-1 clause 10.2 Conversions to character sequences:

> Add to F.5 Binary-decimal conversion:
>
> NOTE: IEC 60559 specifies that conversion to one-digit character strings using
> roundTiesToEven when both choices are odd, shall produce the value with the
> larger magnitude. This can happen with 9.5 whose nearest neighbors are 9.e0 and
> 1.e1, both of which are odd.
