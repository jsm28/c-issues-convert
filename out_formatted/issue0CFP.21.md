## Issue 0CFP.21: P1: printf of one-digit character string

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, C Floating Point Group  
Date: 2018-03-24  
Reference document: [N2224](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2224.pdf)  
Submitted against: Floating-point TS 18661 (C11 version, 2014-2016)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

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

---

Comment from WG14 on 2019-05-03:

Apr 2018 meeting

### Committee Discussion

> The committee, once it understood the three floating values supplied, agreed
> with the proposed change.
>
> Subsequently, the author supplied revised values making such an understanding
> easier. The committee as a whole has yet to see the tweaked values presented
> below as the Proposed Change.

### Proposed Change

Add the following to TS 18661-1 clause 10.2 Conversions to character sequences:

> Add to F.5 Binary-decimal conversion:
>
> NOTE: IEC 60559 specifies that conversion to one-digit character strings using
> roundTiesToEven when both choices are odd, shall produce the value with the
> larger magnitude. This can happen with 9.5e2 whose nearest neighbors are 9.e2
> and 1.e3, both of which are odd.

Oct 2018 meeting

### Committee Discussion

> A new paper [N2283](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2283.htm)
> was presented with revised words from those suggested above in private
> correspondence.
>
> The committee accepts the Suggested Technical Corrigendum from that paper as the
> Proposed Change to resolve this issue.

### Proposed Change

Add the following to TS 18661-1 clause 10.2 Conversions to character sequences:

> At the end of F.5 Binary-decimal conversion, add:
>
> NOTE IEC 60559 specifies that conversion to one-digit character strings using
> roundTiesToEven when both choices have an odd least significant digit, shall
> produce the value with the larger magnitude. For example, this can happen with
> 9.5e2 whose nearest neighbors are 9.e2 and 1.e3, both of which have a single odd
> digit in the significand part.
